# mining-data-with-scrapy
To extract data from a website using Scrapy, you need to write a spider, which is a Python class that defines how to crawl and parse the web pages. A spider can have the following components:

name: A unique identifier for the spider.
start_urls: A list of URLs where the spider will begin to crawl from.
parse: A method that will be called to handle the response downloaded for each of the requests made. It can extract data from the response using selectors or BeautifulSoup, and return items or make additional requests.
