import pyssdb


# For standalone use.
DUPEFILTER_KEY = 'dupefilter:%(timestamp)s'

PIPELINE_KEY = '%(spider)s:items'

SSDB_CLS = pyssdb.Client
SSDB_ENCODING = 'utf-8'
# Sane connection defaults.
SSDB_PARAMS = {
    'socket_timeout': 30,
    # 'encoding': SSDB_ENCODING,
}

SCHEDULER_QUEUE_KEY = '%(spider)s:requests'
SCHEDULER_QUEUE_CLASS = 'scrapy_ssdb.queue.FifoQueue'
SCHEDULER_DUPEFILTER_KEY = '%(spider)s:dupefilter'
SCHEDULER_DUPEFILTER_CLASS = 'scrapy_ssdb.dupefilter.RFPDupeFilter'

START_URLS_KEY = '%(name)s:start_urls'
