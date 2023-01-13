from django.conf import settings
from django_hosts import patterns, host

host_patterns = patterns(
    '',
    host(r'www', 'subdomains_tutorial.frontend_urls', name='www'),
    host(r'(\w+)', settings.ROOT_URLCONF,name='admin'),
    host(r'api', 'subdomains_tutorial.api_urls', name='api'),
    host(r'<str:id>','subdomains_tutorial.api_urls1', name='api1')
)
