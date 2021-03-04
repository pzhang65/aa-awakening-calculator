# /config.py

class Production(object):
    SECRET_KEY = '11122233344'

app_config = {
    'development': Development,
    'production': Production,
    'testing': Testing
}
