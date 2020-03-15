# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# import sqlite3
#
# class RirmscrapyPipeline(object):
#     def __init__(self):
#         self.create_connection()
#         self.create_table()
#
#     def create_connection(self):
#         self.con = sqlite3.connect("rirm.db")
#         self.curr = self.con.cursor()
#
#     def create_table(self):
#         self.curr.execute("""DROP TABLE IF EXISTS rirm_db.db""")
#         self.curr.execute("""create table rirm_tb(urls text)""")
#
#     def process_item(self, item, spider):
#         self.store_db(item)
#         #print("Data came till here" + item['url'][0])
#         return item
#
#     def store_db(self,item):
#         self.curr.execute("""insert into rirm_tb values(?)""",(
#             item['url'][0]))
#         self.con.commit()
