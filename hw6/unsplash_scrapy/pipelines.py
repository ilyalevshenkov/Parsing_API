from scrapy.pipelines.images import ImagesPipeline
import scrapy
import csv
import os

class UnsplashPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        yield scrapy.Request(item['image_url'], meta={'title': item['title'], 'category': item['category']})

    def file_path(self, request, response=None, info=None, *, item=None):
        category = request.meta['category'].replace(' ', '_')
        title = request.meta['title'].replace(' ', '_')
        return f'{category}/{title}.jpg'

    def item_completed(self, results, item, info):
        image_path = results[0][1]['path'] if results else None
        with open('all_photos.csv', 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([item['image_url'], image_path, item['title'], item['category']])
        return item
