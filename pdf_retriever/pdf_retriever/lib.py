from typing import Union

import bs4
import requests

from pdf_retriever import config


class HtmlScraper:

    def __init__(self, html: str):
        self.__soup: bs4.BeautifulSoup = bs4.BeautifulSoup(html, features='html.parser')
        self.__pdf_anchors = [div.find('a') for div in self.__soup.find_all('div', class_='element_type_107')]

    @property
    def anchors(self) -> list:
        return self.__pdf_anchors


class Retriever:

    def __init__(self, page_url: str = config.access_url, pdf_base_url: str = config.base_url):
        html = requests.get(page_url).text
        self.__anchors = HtmlScraper(html).anchors
        self.__pdf_count = len(self.__anchors)
        self.__pdf_urls = [anchor.get('href') for anchor in self.__anchors]
        self.__pdf_titles = [anchor.get_text() for anchor in self.__anchors]
        self.__information = {ordinal: title for ordinal, title in enumerate(self.__pdf_titles)}
        self.__pdf_base_url = pdf_base_url

    def inform(self):
        return self.__information

    def __ordinal_is_in_range(self, ordinal: int):
        if 0 <= ordinal < self.__pdf_count:
            return True
        else:
            return False

    def __make_ordinal_error_message(self) -> str:
        if self.__pdf_count == 1:
            msg = 'The ordinal is out of range. The enable ordinal is only 0'
        elif self.__pdf_count > 1:
            msg = f'The ordinal is out of range. The range of list is 0 ~ {self.__pdf_count-1}'
        else:
            msg = 'PDF does not exist.'
        return msg

    def retrieve_url(self, ordinal: int) -> str:
        if self.__ordinal_is_in_range(ordinal):
            return self.__pdf_urls[ordinal]
        else:
            return self.__make_ordinal_error_message()

    def retrieve_title(self, ordinal: int) -> str:
        if self.__ordinal_is_in_range(ordinal):
            return self.__pdf_titles[ordinal]
        else:
            return self.__make_ordinal_error_message()

    def retrieve_bytes(self, ordinal: int) -> Union[bytes, str]:
        if self.__ordinal_is_in_range(ordinal):
            response = requests.get(self.__pdf_base_url + self.__pdf_urls[ordinal])
            if response.status_code == 200:
                pass
            else:
                raise requests.exceptions.RequestException(
                    'Status code other than 200 was returned. ({})'.format(response.status_code))
            return response.content
        else:
            return self.__make_ordinal_error_message()
