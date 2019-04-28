from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json, requests
from bs4 import BeautifulSoup as bs
from datetime import datetime
# Create your views here.

SERVER_TIME = datetime.today()

@csrf_exempt
def index(request):
    data = {
        'version' : '2.0',
        'data' : {
            'name' : '안주영',
            'age' : '24',
            'msg' : 'hi'
        }
    }
    data_ = json.dumps(data)
    return HttpResponse(data_, content_type='application/json')

@csrf_exempt
def weather(request):
    print(json.loads(request.body))
    url = 'http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=4311452000'
    r = requests.get(url)
    b_obj = bs(r.text, 'html.parser')
    note = ''
    today_w = {}
    tommorow_w = {}
    d_tommorow_w = {}
    for weather in b_obj.find_all('data'):
        h = weather.find('hour').string
        w = weather.find('wfkor').string
        d = weather.find('day').string
        # 오늘
        if d == '0':
            today_w.update({
                h : w,
            })
        # 내일
        elif d == '1':
            tommorow_w.update({
                h  : w,
            })
        # 모레
        elif d == '2':
            d_tommorow_w.update({
                h : w,
            })

    for w in tommorow_w.keys():
        print(w, tommorow_w[w])
        note += '{0}시 {1} \n'.format(w, tommorow_w[w])
    data = {
        'version' : '2.0',
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": note
                    },
                }
            ]
        }
    }
    return HttpResponse(json.dumps(data), content_type='application/json')
