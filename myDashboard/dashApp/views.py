from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

import requests
from bs4 import BeautifulSoup as bs
from bs2json import bs2json
# Create your views here.

def top(request):
    return render(request,"index.html")

def get_aws_rss(request) -> JsonResponse:
    url =  request.GET["url"] if request.GET["url"] else None
    response = requests.get(url)
    soup = bs(response.text,"html.parser")
    converter = bs2json()
    data = converter.convert(soup.channel)
    return JsonResponse(data)
