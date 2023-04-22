----------------------------------- installing -------------------------

pip install django-haystack pysolr

------------------------------------- .env file ------------------------------
SOLR_CORE = 'hv_collection'
SOLR_URL = 'http://127.0.0.1:8983/solr/{}'
------------------------------------settings.py -----------------------------------
INSTALLED_APPS = [
    ...
    'haystack',
    ...
]

SOLR_CORE= str(os.getenv('SOLR_CORE'))
SOLR_URL = str(os.getenv('SOLR_URL')).format(SOLR_CORE)

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.solr_backend.SolrEngine',
        'URL': SOLR_URL,
        'ADMIN_URL': str(os.getenv('SOLR_ADMIN_URL')),
        'INCLUDE_SPELLING': True,
    },
}

HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'
HAYSTACK_DEFAULT_OPERATOR = 'OR'