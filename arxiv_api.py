import requests
import xml.etree.ElementTree as ET
import uuid


def get_data(keyword, category, sortby, sort_order, max_results, start):

    url = f"http://export.arxiv.org/api/query?search_query=cat:{category}&max_results={max_results}&sort_by={sortby}&sort_order{sort_order}&start={start}"

    response = requests.get(url)

    root = ET.fromstring(response.content)
    data = []
    for entry in root.findall('{http://www.w3.org/2005/Atom}entry'):
        title = entry.find('{http://www.w3.org/2005/Atom}title').text
        summary = entry.find('{http://www.w3.org/2005/Atom}summary').text
        author = entry.find('{http://www.w3.org/2005/Atom}author/{http://www.w3.org/2005/Atom}name').text
        published = entry.find('{http://www.w3.org/2005/Atom}published').text
        link = entry.find('{http://www.w3.org/2005/Atom}link[@type="text/html"]')
        if link is not None:
            link = link.attrib['href']
        
        data.append([uuid.uuid4(), title, summary, author, published, link])
    return data