#!/usr/bin/python2.7

"""
Claim a freebook without selenium and without opening a browser
"""
import requests

from bs4 import BeautifulSoup, SoupStrainer

__author__ = 'greg'

EMAIL = ''
PASSWORD = ''

baseUrl = 'https://www.packtpub.com/'
freeBookUrl = baseUrl + 'packt/offers/free-learning/'

data = requests.get(freeBookUrl)

text = data.text

loginForm = SoupStrainer(id="packt-user-login-form")
page = BeautifulSoup(text, 'lxml', parse_only=loginForm)

formBuildId = page.find('input', attrs={'name': 'form_build_id'})['value']
formId = page.find('input', attrs={'name': 'form_id'})['value']
op = 'Login'

bookId = BeautifulSoup(text, 'lxml',
                       parse_only=SoupStrainer('a', attrs={'class': 'twelve-days-claim'})).find('a')['href']


def login(session):
    payload = {'email': EMAIL, 'password': PASSWORD, 'form_build_id': formBuildId,
               'form_id': formId, 'op': op}
    return session.post(baseUrl, data=payload)


def getFreeBook(session):
    return session.get(baseUrl + bookId)


# TODO error handling
with requests.session() as session:
    login(session)
    getFreeBook(session)
