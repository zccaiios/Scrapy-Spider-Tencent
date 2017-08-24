# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs

class TencentPipeline(object):

    # 创建存储数据的文件
    def __init__(self):
        self.file = open('tencent.json','w')

    # 处理数据
    def process_item(self, item, spider):
        data = json.dumps(dict(item),ensure_ascii=False) + ',\n'
        # 写入文件
        self.file.write(data)
        return item

    def close_spider(self, spider):
        self.file.close()
