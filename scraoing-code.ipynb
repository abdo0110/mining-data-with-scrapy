import scrapy
from scrapy.selector import Selector
from bs4 import BeautifulSoup

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
    ]

    def parse(self, response):
        # create a selector object from the response
        sel = Selector(response)
        # use BeautifulSoup to parse the HTML
        soup = BeautifulSoup(response.text, 'html.parser')
        # find all the quote elements
        quotes = soup.find_all('div', class_='quote')
        # loop through each quote
        for quote in quotes:
            # extract the text, author, and tags using CSS selectors
            text = quote.find('span', class_='text').get_text()
            author = quote.find('small', class_='author').get_text()
            tags = [tag.get_text() for tag in quote.find_all('a', class_='tag')]
            # yield a dictionary with the extracted data
            yield {
                'text': text,
                'author': author,
                'tags': tags,
            }
            scrapy runspider quotes_spider.py -o quotes.json

