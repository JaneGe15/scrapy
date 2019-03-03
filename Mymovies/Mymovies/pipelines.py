# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
# import json
# import codecs
import pymysql
from Mymovies import settings
# import logging


class MymoviesPipeline(object):
    def process_item(self, item, spider):
        return item


class DBPipeline(object):
    def __init__(self):
        # 连接数据库
        self.connect = pymysql.connect(
            host=settings.MYSQL_HOST,
            db=settings.MYSQL_DBNAME,
            user=settings.MYSQL_USER,
            password=settings.MYSQL_PASSWORD,
            port=settings.MYSQL_PORT,
            charset='utf8',
            use_unicode=True)

        # 通过cursor执行增删改查
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        try:
            # 插入数据
            self.cursor.execute(
                """insert into t_movie_spider(name, other_name, cover_pic, classification, release_date, area, 
                release_year, director, actors, score, cili_link, torrent_link) 
                value (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                (item['name'],
                 item['other_name'],
                 item['cover_pic'],
                 item['type'],
                 item['show_date'],
                 item['region'],
                 item['show_year'],
                 item['director'],
                 item['actors'],
                 item['douban_score'],
                 item['link1'],
                 item['link2']))
            # 提交sql语句
            self.connect.commit()

        except Exception as error:
            # 出现错误时打印错误信息
            spider.logger.info(error)
            #logging.error(error)
            self.connect.rollback()  # 如果发生错误则回滚

        return item
