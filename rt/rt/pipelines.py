# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exporters import CsvItemExporter

import pprint
import csv

class RtPipeline(object):

    csv_filename = "testFile.csv"

    def __init__(self):
        self.filename = 'rt_spider.csv'

        writer = csv.writer(open(self.csv_filename, 'a+'))
        writer.writerow(["title", "criticscore", "audiencescore", "rating", "boxoffice", "runtime"])

    def open_spider(self, spider):
        self.csvfile = open(self.filename, 'wb')
        self.exporter = CsvItemExporter(self.csvfile)
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.csvfile.close()

    def process_item(self, item, spider):
        print(pprint.pprint(item));

        new_row = [
            item["title"]
            item["criticscore"],
            item["audiencescore"],
            item["rating"],
            item["boxoffice"],
            item["runtime"],
        ]

        writer = csv.writer(open(self.csv_filename, "a+"))
        writer.writerow(new_row)
       
        return item
