from django.shortcuts import render, redirect
import ybc_trans
from django.http import HttpResponse
import ybc_weather
import os
import csv
import requests
import json
import ybc_china
from django.contrib.auth.decorators import login_required
from music.get_station import get
import time

# from music.paqu import get
# from my_app.models import search_music

china = ybc_china.provinces()
# Create your views here.


# client_id 为官网获取的AK， client_secret 为官网获取的SK
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=5uutbbr2t7KytYa0GshmFuzf' \
       '&client_secret=eQTzIFk8BhiMRhulYFefWGZ1IXYGfLYE '
response = requests.get(host)
if response:
    access_token = response.json()['access_token']


def trans(request):
    if request.method == 'GET':
        return render(request, 'trans.html')
    else:
        text = request.POST.get('text')
        if text != '' or text is not None:
            try:
                zh = ybc_trans.en2zh(text)
            except TypeError:
                text = ''
                zh = ''
            print(zh)
        else:
            text = ''
            zh = ''
        print(111)
        return render(request, 'trans.html', {'text': text, 'anser': zh})


def OCR(request):
    global access_token
    if request.method == 'GET':
        return render(request, 'OCR.html')
    else:
        obj = request.FILES.get('img')
        if obj == '' or obj is None:
            return HttpResponse('<h1>未选择图片</h1><a href="http://127.0.0.1:7000/index/ocr_text/">返回</a>')
        else:
            filepath = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "\\my_app\\OCR_img",
                                    'my.jpg')
            f = open(filepath, mode='wb')
            for i in obj.chunks():
                f.write(i)
            f.close()
            import base64
            request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic"
            # 二进制方式打开图片文件
            f = open(filepath, 'rb')
            img = base64.b64encode(f.read())
            params = {"image": img}
            request_url = request_url + "?access_token=" + access_token
            headers = {'content-type': 'application/x-www-form-urlencoded'}
            response1 = requests.post(request_url, data=params, headers=headers)
            if response1:
                print(response1.json())
                response1 = response1.json()['words_result']
                t = ''
                for r in response1:
                    text = r['words']
                    t = t + text + '\n'
                print(t)
                return render(request, 'OCR.html', {'text': t})
            else:
                return HttpResponse('出错<a href="http://127.0.0.1:7000/index/ocr_text/">重试</a>')


def weather():
    DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.path.join(os.path.join(DIR, 'my_app'), 'china-city-list.csv')


def statiom(request):
    g = get()
    if request.method == 'GET':
        return render(request, 'station.html')
    else:
        data = request.POST.get('data')
        form = request.POST.get('form')
        to = request.POST.get('to')
        g.isStation()
        station = eval(g.read())
        try:
            form1 = station[form]
            to1 = station[to]
        except KeyError:
            return redirect('/index/station/')
        return render(request, 'station.html', {'station': g.query(data, form1, to1), 't': form, 't1': to, 't2': data})
