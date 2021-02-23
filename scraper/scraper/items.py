# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy_djangoitem import DjangoItem
from pc_builder.models import com_details
# ScraperItem
class com_details_item(DjangoItem):
    django_model = com_details