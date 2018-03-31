from django.shortcuts import render
from django.views.generic import TemplateView
from Userdata.forms import InputFormData
import requests
from urllib.request import urlopen
from xml.etree import ElementTree as ET
import logging

LOG_FILENAME = 'output.api.log'
logging.basicConfig(filename=LOG_FILENAME, level=logging.DEBUG, )


# Create your views here.
class HomeView(requests):
    dicti = {'c': 'http://thecatapi.com/api/images/get?format=xml&results_per_page=2',
             'd': 'https://api.thedogapi.co.uk/v2/dog.php?limit=',
             'cn': 'https://api.chucknorris.io/jokes/random?category='}
    msg = ""

    def get(self, request):
        f = InputFormData()

    def post(self, request):
        f = InputFormData(request.POST)
        if f.is_valid():
            num = f.cleaned_data['number']
            name = f.cleaned_data['name']
            cate = f.cleaned_data['category']
            if name == 'c':
                requestURL = 'http://thecatapi.com/api/images/get?format=xml&results_per_page=' + str(num)
                p = urlopen(requestURL)
                msg = p.read() + "\n\n\n\n"
                root = ET.parse(urlopen(requestURL)).getroot()
                caturllist = []
                for i in range(num):
                    imurl = root.find('data').find('images').findall('image')[i].find('url').text
                    caturllist.append(imurl)

            elif name == 'd':
                dogurllist = []
                requestURL = 'https://api.thedogapi.co.uk/v2/dog.php?limit=' + str(num)

                response = requests.get(requestURL)
                res = response.json()
                msg = res + "\n\n\n\n"
                for i in range(num):
                    durl = res['data'][i]['url']
                    dogurllist.append(durl)
            elif name == 'cn':
                if cate == 'no':
                    pass
                else:
                    jokeslist = []
                    url = 'https://api.chucknorris.io/jokes/random?category=' + cate
                    headers = {
                        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
                    for i in range(num):
                        u = requests.get(url=url, headers=headers)
                        res = u.json()
                        msg = res + "\n"
                        jokeslist.append(res['value'])
                    msg = msg + "\n\n\n\n"

    logging.debug(msg)

    con = {'form': 'f', 'clist': 'caturllist', }
    render(requests, 'Userdata/base.html', context=con)
