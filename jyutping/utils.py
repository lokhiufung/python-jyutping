import requests
from bs4 import BeautifulSoup


def get_jyutping_from_api(char, resource='jyut.net'):
    """
    resources:
    1. jyut.net: https://jyut.net/query
    2. ctext: https://ctext.org/dictionary.pl
    """
    if resource == 'jyut.net':
        jyut = get_jyutping_from_api_1(char)
    elif resource == 'ctext':
        jyut = get_jyutping_from_api_2(char)
    else:
        raise Exception('Invalid resource {}'.format(resource))
    return jyut


def get_jyutping_from_api_1(char):
    base_url = 'https://jyut.net/query'
    data = '?q=' + char
    endpoint = base_url + data
    response = requests.get(endpoint)
    soup = BeautifulSoup(response.content, 'html.parser')
    tag = soup.find('span', class_='jyutping')

    jyut = tag.string if tag is not None else ''
    return jyut


def get_jyutping_from_api_2(char):
    base_url = 'https://ctext.org/dictionary.pl'
    data = '?if=gb&char=' + char
    endpoint = base_url + data
    response = requests.get(endpoint)
    soup = BeautifulSoup(response.content, 'html.parser')
    tag = soup.find('table', class_='info')
    jyut = tag.find_all('tr')[4].find('td').string
    
    if jyut is not None:
        jyut = jyut.split(' ')  # in case more than 1 pronounciation
        if len(jyut) > 1:
            jyut = '/'.join(jyut)
        else:
            jyut = jyut[0]
    else:
        jyut = ''
    return jyut
    