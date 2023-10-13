from django.shortcuts import render, redirect
from .models import Keyword, Trend
from .forms import KeywordForm, TrendForm


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
    return render(request, 'trends/crawling.html',)
def crawling_histogram(request):
    return render(request, 'trends/crawling_histogram.html',)

def advanced(request):
    return render(request, 'trends/crawling_advanced.html',)