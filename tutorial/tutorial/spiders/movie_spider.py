# encoding=utf-8

import scrapy


class MovieSpider(scrapy.Spider):
    name = "movies"

    def start_requests(self):
        urls = [
            'http://www.btgang.com/?PageNo=1',
            'http://www.btgang.com/?PageNo=2',
            'http://www.btgang.com/?PageNo=3',
            'http://www.btgang.com/?PageNo=4',
            'http://www.btgang.com/?PageNo=5'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split('=')[-1]
        filename = 'movie-page-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
