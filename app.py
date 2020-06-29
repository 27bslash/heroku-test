import os
import requests
from flask import Flask, render_template, request, url_for, redirect
from flask_caching import Cache
from parsel import Selector
import time
import random
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


def foo(x, s):
    time.sleep(s)
    print("%s %s %s" % (threading.current_thread(), x, s))


def opendota_call():
    names = []
    out = []
    print('input')
    # for name in names:
    #     pass
    # asyncio.run(pro_request(name, out, 100))
    # asyncio.run(main(get_urls(20, name, name)))

    # time.sleep(60)
    for i in range(5):
        print('second')
    print('end')


threading.Thread(target=opendota_call())
if __name__ == '__main__':
    app.run(debug=True)
