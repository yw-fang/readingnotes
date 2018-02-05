import urlparse
import scrapy

from scrapy.http import Request

class pwc_tax(scrapy.Spider):
    name = "pwc_tax"

    allowed_domains = ["www.pwc.com"]
    start_urls = ["http://www.pwc.com/us/en/tax-services/publications/research-and-insights.html"]

    def parse(self, response):
        for href in response.css('div#all_results h3 a::attr(href)').extract():
            yield Request(
                url=response.urljoin(href),
                callback=self.parse_article
            )

    def parse_article(self, response):
        for href in response.css('div.download_wrapper a[href$=".pdf"]::attr(href)').extract():
            yield Request(
                url=response.urljoin(href),
                callback=self.save_pdf
            )

    def save_pdf(self, response):
        path = response.url.split('/')[-1]
        self.logger.info('Saving PDF %s', path)
        with open(path, 'wb') as f:
            f.write(response.body)
