#? name: CrossRef
#? www: http://www.crossref.org/
#? urls: http://crossref.org/ http://dx.doi.org/


import json
import re
import socket
import urllib

import urllib2
from lxml import etree


api_key = 'API_KEY'

def fetch(doi):
    url = 'http://dx.doi.org/{0}'.format(doi)
    headers = { 'Accept': 'application/unixref+xml' }
    request = urllib2.Request(url, None, headers)
    return urllib2.urlopen(request, timeout=10).read()

def resolve(doi):
    citation = {}
    identifiers = {'doi': doi}
    links = []

    try:
        response = fetch(doi)
    except urllib2.HTTPError as e:
        if getattr(e, 'code') in (404, 406):
            return citation
        else:
            raise

    citation['raw_crossref_unixref'] = response
    dom = etree.fromstring(response)

    # Find as much metadata as possible from this crossref record

    # Authors of the article
    persons = dom.findall('doi_record/crossref/journal/journal_article/contributors/person_name[@contributor_role="author"]')
    if len(persons) > 0:
        citation['authors'] = [(etree.tostring(person.find('surname'), with_tail=False, method='text', encoding=unicode) + ', ' + \
                                etree.tostring(person.find('given_name'), with_tail=False, method='text', encoding=unicode)) for person in persons]

    # Favour electronic ISSN FIXME should this print one even be used?
    issn = dom.findtext('doi_record/crossref/journal/journal_metadata/issn[@media_type="electronic"]')
    if issn is None:
        issn = dom.findtext('doi_record/crossref/journal/journal_metadata/issn')
    if issn is not None:
        if len(issn) == 8:
            issn = '{0}-{1}'.format(issn[:4], issn[-4:])
        citation['publication-issn'] = issn

    def findtext(xpath, field):
        valueelem = dom.find(xpath)
        if valueelem is not None:
            value = etree.tostring(valueelem, method="text", encoding=unicode, with_tail=False)
            if value is not None:
                citation[field] = re.sub(r'\s+', ' ', value)

    findtext('doi_record/crossref/journal/journal_metadata/full_title', 'publication-title')
    findtext('doi_record/crossref/journal/journal_issue/publication_date/year', 'year')
    findtext('doi_record/crossref/journal/journal_issue/journal_volume/volume', 'volume')
    findtext('doi_record/crossref/journal/journal_issue/issue', 'issue')
    findtext('doi_record/crossref/journal/journal_article/titles/title', 'title')
    findtext('doi_record/crossref/journal/journal_article/pages/first_page', 'first_page')
    findtext('doi_record/crossref/journal/journal_article/pages/last_page', 'last_page')

    rename = {'pmid': 'pubmed', 'pmcid': 'pmc', 'arxivid': 'arxiv'}
    for idelem in dom.xpath('doi_record/crossref/journal/journal_article/publisher_item/identifier'):
        key = idelem.get('id_type')
        value = idelem.text
        identifiers[rename.get(key, key)] = value

    links.append({
        'url': 'http://dx.doi.org/{0}'.format(doi),
        'mime': 'text/html',
        'type': 'article',
        'title': "Show on publisher's website",
        })

    pages = u'-'.join((p for p in (citation.get('first_page'), citation.get('last_page')) if p is not None))
    if len(pages) > 0:
        citation['pages'] = pages

    if len(identifiers) > 0:
        citation['identifiers'] = identifiers
    if len(links) > 0:
        citation['links'] = links

    return citation

def search(title):
    citations = []
    url = 'http://search.crossref.org/dois?{0}'.format(urllib.urlencode({
        'version': '1',
        'access': api_key,
        'format': 'json',
        'op': 'OR',
        'q': title.encode('utf8'),
    }))
    response = urllib2.urlopen(url, timeout=12).read()
    data = json.loads(response)
    for item in data:
        citation = {
            'title': item['title'],
            'year': item['year'],
            'identifiers': { 'doi': item['doi'] },
        }
        citations.append(citation)
    return citations

def freeform_search(freeform):
    url = 'https://api.crossref.org/reverse'
    request = urllib2.Request(url, headers={
        'Content-Type': 'application/json',
    }, data=json.dumps(freeform))
    response = urllib2.urlopen(request, timeout=12).read()
    data = json.loads(response)
    if isinstance(data, dict) and data.get('status', '') == 'ok':
        message = data.get('message')
        if message is not None:
            citation = {}
            for old_key, new_key in {'DOI': 'doi'}.items():
                citation.setdefault('identifiers', {})
                if old_key in message:
                    citation['identifiers'][new_key] = message[old_key]
                    if new_key == 'doi':
                       citation["links"]=[{
                           "type": 'article',
                           "url": 'http://dx.doi.org/{}'.format(citation['identifiers'][new_key]),
                           "mime": "text/html",
                           "title": "Show on publisher's website"
                       }]
            citation['score'] = float(message.get('score', 0))
            authors = []
            for author in message.get('author', []):
                name = author.get('family', 'Unknown')
                if 'given' in author:
                    name += u', {}'.format(author.get('given', 'Unknown'))
                authors.append(name)
            if len(authors) > 0:
                citation['authors'] = authors
            issued = message.get('published-print', {}).get('date-parts', [])
            if len(issued) == 0:
                issued = message.get('issued', {}).get('date-parts', [])
            if len(issued) > 0:
                year, month, day = (issued[0] + [0, 0, 0])[:3]
                if yeah is not None and year > 0:
                    citation['year'] = u'{}'.format(year)
            page = message.get('page')
            if page is not None:
                match = re.match('(\w+)(?:[-\u2010\u2011\u2012\u2013\u2014\u2015](\w+))?', page)
                if match is not None:
                    page_from, page_to = match.groups((1, 2))
                    if page_from is not None:
                        citation['page-from'] = page_from
                    if page_to is not None:
                        citation['page-to'] = page_to
            for old_key, new_key in {'title[]': 'title',
                                     'subtitle[]': 'subtitle',
                                     'container-title[]': 'publication-title',
                                     'volume': 'volume',
                                     'issue': 'issue',
                                     'publisher': 'publisher',
                                     'ISSN[]': 'publication-issn',
                                     'ISBN[]': 'publication-isbn'}.items():
                if old_key[-2:] == '[]':
                    old_key = old_key[:-2]
                    if old_key in message and len(message[old_key]) > 0:
                        citation[new_key] = message[old_key][0]
                elif old_key in message:
                    citation[new_key] = message[old_key]
            if 'doi' in citation.get('identifiers', {}):
                return citation
    return None
