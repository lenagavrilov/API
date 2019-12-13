import requests
import xml.etree.ElementTree as ET


list_apis = ["https://reststop.randomhouse.com/resources/authors/3446/"]
             #"https://reststop.randomhouse.com/resources/works/19308/",
             #"https://reststop.randomhouse.com/resources/titles/9781400079148/"]


def read_API(api):
    for each in api:
        response = requests.get(each)
        if response.status_code != 200:
            print('{} was not found.'.format(each))
        else:
            result = response.content
            parse_xml(result)


def parse_xml(xml):
    author_data = {}
    root = ET.fromstring(xml)
    for child in root:
        if child.tag == 'authordisplay':
            author_data['author_name'] = child.text
        if child.tag == 'authorid':
            author_data['id_author'] = int(child.text)
    print(author_data)
    if_dan_brown(author_data)


def if_dan_brown(author_data):
    if author_data['author_name'] == "Dan Brown" and author_data['id_author'] == 3446:
        print("The author is Dan Brown")
    else:
        print("This author is not Dan Brown")




    """for child in root:
        print(child.text)

    for child in root:
        print(child.tag, child.attrib)
    for title in root.iter('isbn'):
        print(title.attrib, title.text)"""










read_API(list_apis)