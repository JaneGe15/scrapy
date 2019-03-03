# -*- coding: utf-8 -*-
import scrapy
import re
from Mymovies.items import MymoviesItem
from Mymovies import settings


class MovieSpider(scrapy.Spider):
    global page_no
    page_no = 1
    name = "BTmovie"

    start_urls = [
        'http://www.btkat.com/list/index_1.html',
    ]

    def parse(self, response):
        for movie in response.css("div.title"):
            detail_link = "http:" + movie.css("p.tt.cl > a::attr(href)").extract_first()
            if detail_link is not None:
                yield scrapy.Request(detail_link, self.parse_movie)

        global page_no
        page_no = page_no + 1
        if page_no < settings.PAGE_NO:
            next_page_url = 'index_' + str(page_no) + '.html'
            yield scrapy.Request(response.urljoin(next_page_url))

    def parse_movie(self, response):
        item = MymoviesItem()
        link1 = ''
        link2 = ''
        p = re.compile(r'[《](.*?)[》]', re.S)
        movie_detail = response.css("div.ma.cl")
        name = re.findall(p, movie_detail.css("div.title > h1::text").extract_first())[0],
        other_name = movie_detail.css("ul.moviedteail_list > li::text")[0].extract().split(":")[1].strip(),
        type = movie_detail.css("ul.moviedteail_list > li::text")[1].extract().split(":")[1].strip(),
        show_date = movie_detail.css("ul.moviedteail_list > li::text")[2].extract().split(":")[1].strip(),
        region = movie_detail.css("ul.moviedteail_list > li::text")[3].extract().split(":")[1].strip(),
        show_year = movie_detail.css("ul.moviedteail_list > li::text")[4].extract().split(":")[1].strip(),
        director = movie_detail.css("ul.moviedteail_list > li::text")[5].extract().split(":")[1].strip(),
        actors = movie_detail.css("ul.moviedteail_list > li::text")[6].extract().split(":")[1].strip(),
        douban_score = movie_detail.css("p.rt > strong::text").extract_first(),
        cover_pic = movie_detail.css("div.moviedteail_img > a.pic > img::attr(src)").extract_first(),
        if cover_pic[0] == '//image.btkat.com/0200/':
            cover_pic = movie_detail.css("div.moviedteail_img > a.pic > img::attr(onerror)").extract_first().split("=")[2].strip("'"),

        for href in movie_detail.css("div.tinfo > a::attr(href)").extract():
            if href.find("magnet") != -1:
                link1 = link1 + "||" + href
            else:
                link2 = link2 + "||" + href

        item['name'] = name
        item['other_name'] = other_name
        item['cover_pic'] = "http:" + cover_pic[0]
        item['type'] = type
        item['show_date'] = show_date
        item['region'] = region
        item['show_year'] = show_year
        item['director'] = director
        item['actors'] = actors
        item['douban_score'] = douban_score
        item['link1'] = link1.strip("||")
        item['link2'] = link2.strip("||")

        yield item


