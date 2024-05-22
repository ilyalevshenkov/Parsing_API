BOT_NAME = 'unsplash_scraper'

SPIDER_MODULES = ['unsplash_scraper.spiders']
NEWSPIDER_MODULE = 'unsplash_scraper.spiders'

ROBOTSTXT_OBEY = True

# Pipeline settings
ITEM_PIPELINES = {
    'unsplash_scraper.pipelines.UnsplashPipeline': 1,
}

IMAGES_STORE = 'images'


# settings.py

CLOSESPIDER_ITEMCOUNT = 10
