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
    with open('json_files/hero_ids.json', 'r') as f:
        data = json.load(f)
        for i in data['heroes']:
            names.append(i['name'])
        # for name in names:
        #     pass
            # asyncio.run(pro_request(name, out, 100))
    with open('json_files/hero_ids.json', 'r') as f:
        data = json.load(f)
        for name in names:
            # asyncio.run(main(get_urls(20, name, name)))
            delete_output()
            # time.sleep(60)
            print('second')
    time.sleep(3)
    print('end')
    
threading.Thread(target=opendota_call())
if __name__ == '__main__':
    app.run(debug=True)
