from django.core.management.base import BaseCommand
from scraper.scraper.spiders import scraper_spider
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

class Command(BaseCommand):
    help = "Release the spiders"

    def handle(self, *args, **options):
        process = CrawlerProcess(get_project_settings())

        process.crawl(scraper_spider)
        process.start()