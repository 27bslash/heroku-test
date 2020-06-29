import os
import requests
from flask import Flask, render_template, request, url_for, redirect
from flask_caching import Cache
from parsel import Selector
import time
from operator import itemgetter
import threading

app = Flask(__name__)
cache = Cache(config={
    'CACHE_TYPE': 'simple'
})
cache.init_app(app)


@app.route('/', methods=['GET'])
def hello():
    return 'hello'


def opendota_call():
    print('test')


if __name__ == '__main__':
    thread1 = threading.Thread(target=opendota_call)
    thread1.start()
    app.run(debug=True)
