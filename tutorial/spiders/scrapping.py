import scrapy

from ..items import TutorialItem


class ShortsSpider(scrapy.Spider):
    name = 'shorts'
    start_urls = [
        'https://seamsfriendly.com/collections/shorts'
    ]

    def parse(self, response):
        items = TutorialItem()

        title = response.css('title::text').getall()
        description = response.css('span.boost-pfs-filter-option-title-text::text').getall()
        images = response.css('img').xpath('@src').getall()
        multicolor = response.css('span.boost-pfs-filler-images-swatch::text').getall()

        items['title'] = title
        items['description'] = description
        items['images'] = images
        items['multicolor'] = multicolor

        yield items
