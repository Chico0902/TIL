from django.shortcuts import render, redirect
from .models import Keyword, Trend
from .forms import KeywordForm, TrendForm
from bs4 import BeautifulSoup, SoupStrainer
from selenium import webdriver
from matplotlib import pyplot as plt
from io import BytesIO
import base64


# Create your views here.
def base(request):
    return render(request, 'base.html')

def keyword(request):
    dongs = Keyword.objects.all()
    if request.method == 'POST':
        form = KeywordForm(request.POST)
        # 유효성 검사 진행
        # 유효성 검사가 통과된 경우
        if form.is_valid():
            keyword = form.save()
            return redirect('trends:keyword',)
    # 요청의 메서드가 POST가 아니라면 (new)
    else:
        form = KeywordForm()
    context = {
        'form': form,
        'dongs':dongs

    }
    return render(request, 'trends/keyword.html', context)

def delete(request, pk):
    keyword = Keyword.objects.get(pk=pk)
    keyword.delete()
    return redirect('trends:keyword')

def keyword_detail():
    return redirect('trends/keyword.html',)


def crawling(request):
    keywords = Keyword.objects.all()
    trends = Trend.objects.all()
    for keys in keywords:
        value = Trend.objects.filter(name = keys.name, search_period = "all")
        if not value.exists():
            url = f"https://www.google.com/search?q={keys.name}"
            driver = webdriver.Chrome()
            driver.get(url)
            html = driver.page_source
            soup = BeautifulSoup(html, "html.parser")
            results = soup.select_one("div #result-stats")
            results = results.contents[0]
            results = results.split("약")[1].strip("개")
            results = int("".join(results.split(",")))
            save_trends = Trend()
            save_trends.name = keys.name
            save_trends.result = results
            save_trends.search_period = "all"
            save_trends.save()
    context = {
        "trends" : trends,
        "keywords" : keywords,
    }
    return render(request, "trends/crawling.html", context)


def crawling_histogram(request):
    trends = Trend.objects.all()
    name = []
    value = []
    for trend in trends:
        name.append(trend.name)
        value.append(trend.result)
    plt.clf()
    plt.title("Technology Trend Analysis")
    plt.bar(name,value)
    plt.grid(True)
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')
    buffer.close()
    context = {
        'chart': f'data:image/png;base64,{image_base64}',
    }
    return render(request, "trends/crawling_histogram.html", context)

def advanced(request):
    keywords = Keyword.objects.all()
    trends = Trend.objects.all()
    for keys in keywords:
        value = Trend.objects.filter(name = keys.name, search_period = "year")
        if not value.exists():
            url = f"https://www.google.com/search?q={keys.name}&tbs=qdr:y"
            driver = webdriver.Chrome()
            driver.get(url)
            html = driver.page_source
            soup = BeautifulSoup(html, "html.parser")
            results = soup.select_one("div #result-stats")
            results = results.contents[0]
            results = results.split("약")[1].strip("개")
            results = int("".join(results.split(",")))
            save_trends = Trend()
            save_trends.name = keys.name
            save_trends.result = results
            save_trends.search_period = "year"
            save_trends.save()
    name = []
    value = []
    for trend in trends:
        if trend.search_period == "year":
            name.append(trend.name)
            value.append(trend.result)
    plt.clf()
    plt.switch_backend('agg')
    plt.title("Technology Trend Analysis")
    plt.bar(name,value)
    plt.grid(True)
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')
    buffer.close()
    context = {
        'chart': f'data:image/png;base64,{image_base64}',
    }
    return render(request, "trends/crawling_advanced.html", context)