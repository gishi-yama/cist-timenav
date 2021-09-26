from typing import Union

import bs4
import requests

from pdf_retriever import config


class HtmlScraper:

    def __init__(self, url: str = config.access_url, base_url: str = config.base_url):
        self.__url = url
        html = requests.get(url).text
        soup = bs4.BeautifulSoup(html, features='html.parser')
        href = soup.find('div', class_='element_type_107').find('a').get('href')
        self.__pdf_url = base_url + href

    @property
    def pdf_url(self) -> str:
        return self.__pdf_url


class Retriever:

    @staticmethod
    def retrieve(pdf_url: str) -> Union[bytes, str]:
        response = requests.get(pdf_url)
        if response.status_code == 200:
            pass
        else:
            raise requests.exceptions.RequestException(
                'Status code other than 200 was returned. ({})'.format(response.status_code))
        return response.content

