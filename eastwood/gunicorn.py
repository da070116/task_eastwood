from multiprocessing import cpu_count
from os import environ

def max_workers():
    return cpu_count()


bind = '127.0.0.1:' + environ.get('PORT', '8000')
max_requests = 1000
worker_class = 'gevent'
workers = max_workers()

env = {
    'DJANGO_SETTINGS_MODULE': 'eastwood.settings'
}

reload = True
name = 'Eastwood  test app'