# -*- coding: utf-8 -*-
import scrapy
# 导入item模板类
from Tencent.items import TencentItem

# from mySpider.items import MyspiderItem


class TencentSpider(scrapy.Spider):
    name = "tencent"
    allowed_domains = ["tencent.com"]
    start_urls = ["http://hr.tencent.com/position.php"]

    def parse(self, response):

        # 获取所有位置的节点
        node_list = response.xpath("//tr[@class='even']|//tr[@class='odd']")
        print('~~~~~~~~~%s'%len(node_list))
        host = 'http://hr.tencent.com/'

        # 遍历节点列表，抽取数据：
        for node in node_list:

            item = TencentItem()
            item['name'] = node.xpath('./td[1]/a/text()').extract_first()
            item['url'] = host + node.xpath('./td[1]/a/@href').extract_first()
            item['category'] = node.xpath('./td[2]/text()').extract_first()
            item['number'] = node.xpath('./td[3]/text()').extract_first()
            item['address'] = node.xpath('./td[4]/text()').extract_first()
            item['pub_time'] = node.xpath('./td[5]/text()').extract_first()

            yield item

        # 获取下一页url
        next_url = host + response.xpath('//a[@id="next"]/@href').extract_first()

        # 创建新请求，并返回数据给引擎
        yield scrapy.Request(next_url,callback=self.parse)