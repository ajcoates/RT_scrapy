# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exporters import CsvItemExporter

import pprint
import csv
import colors
from termcolor import colored
import os

class RtPipeline(object):

    def __init__(self):
        self.filename = 'rt_spider.csv'
        print(colored("Adding column names to csv", "red"))

        try:
            os.remove(self.filename)
            print("Cleared existing csv file.")
        except OSError:
            print("{} does not exist, creating.".format(self.filename))

        writer = csv.writer(open(self.filename, 'a+'))
        writer.writerow(["title", "criticscore", "audiencescore", "rating", "boxoffice", "runtime"])

        print("Wrote column names to csv.")

    def open_spider(self, spider):
        self.csvfile = open(self.filename, 'wb')
        self.exporter = CsvItemExporter(self.csvfile)
        self.exporter.start_exporting()

        print(colored("Opening spider", "red"))

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.csvfile.close()

        print(colored("Closing spider", "red"))

    def process_item(self, item, spider):

        new_row = [
            item["title"],
            item["criticscore"],
            item["audiencescore"],
            item["rating"],
            item["boxoffice"],
            item["runtime"],
        ]


        print(colored("Adding new row to CSV: '{}'".format(new_row), "red"))

        writer = csv.writer(open(self.filename, "a+"))
        writer.writerow(new_row)
       
        return item
