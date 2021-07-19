from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import re
import requests
from bs4 import BeautifulSoup as bs
from bs2json import bs2json
# Create your views here.

def top(request):
    return render(request,"index.html")

def get_aws_rss(request) -> JsonResponse:
    url =  request.GET["url"] if request.GET["url"] else None
    if url is None:
        response = requests.get(url)
        if response.status_code == 200:
            soup = bs(response.text,"html.parser")
            converter = bs2json()
            data = converter.convert(soup.channel)
            data["status"] = "success"
        else:
            data = {"status":"error","log":"Incorrect URL","status code":response.status_code}
    else:
        data = {"status":"error","log":"no URL"}
    return JsonResponse(data)

def get_downdetector(request) -> JsonResponse:
    link = "https://downdetector.jp/archive"
    response = requests.get(link)
    if response.status_code == 200:
            soup = bs(response.text,"html.parser")
            data = {"status":"success","table":[]}
            for item in soup.select("#page table tr.border"):
                jdata = {}
                item_data = item.select("td")
                jdata["name"] = re.sub("\s","",item_data[0].text)
                jdata["link"] = item_data[0].find("a").get("href")
                jdata["date"] = re.sub("\s","",item_data[1].text)
                jdata["time"] = re.sub("\s","",item_data[2].text)
                data["table"].append(jdata)
    else:
        data = {"status":"error","log":"Incorrect URL","status code":response.status_code}
    return JsonResponse(data)
