from django.http import JsonResponse
from rest_framework.decorators import api_view
import random
import csv
import numpy as np
import pandas as pd




# def file_open_by_numpy():
#     # np.loadtxt(구분자 = ',', 데이터 타입: string)
#     np_arr = np.loadtxt('data/test_data.CSV', delimiter=",", encoding='cp949', dtype=str)
#     return np_arr

# arr = file_open_by_numpy()
# print(arr)

# df = pd.DataFrame(arr)
# df
@api_view(['GET'])
def file_open_by_pandas(request):
    df = pd.read_csv('data/test_data.CSV', encoding='cp949')
    data = df.to_dict('records')
    return JsonResponse({'dat':data})

@api_view(['GET'])
def file_open_by_pandas_with_null(request):
    df = pd.read_csv('data/test_data_has_null.CSV', encoding='cp949')
    # df['나이'].fillna(-1, inplace=True)
    df['성별'].fillna('NULL', inplace=True)
    df['직업'].fillna('NULL', inplace=True)
    df['사는곳'].fillna('NULL', inplace=True)
    data = df.to_dict('records')
    return JsonResponse({'dat':data})


@api_view(['GET'])
def file_open_by_pandas_with_null_meanage(request):
    df = pd.read_csv('data/test_data_has_null.CSV', encoding='cp949')
    # df['나이'].fillna(-1, inplace=True)
    df['성별'].fillna('NULL', inplace=True)
    df['직업'].fillna('NULL', inplace=True)
    df['사는곳'].fillna('NULL', inplace=True)
    pyung = df['나이'].mean(numeric_only=True)
    df['diff'] = (pyung-df['나이']).abs()
    df = df.sort_values('diff')[:10]
    data = df.to_dict('records')
    
    return JsonResponse({'dat':data})
    # return JsonResponse({'dat':data})



array_length = 1000
random_range = 5000

@api_view(['GET'])
def bubble_sort(request):
    li = []
    for i in range(array_length):
        li.append(random.choice(range(1, random_range)))
    for i in range(len(li) - 1, 0, -1):
        for j in range(i):
            if li[j] < li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]
    context = {
      'top': li[0]
    }
    return JsonResponse(context)

@api_view(['GET'])
def normal_sort(request):
    li = []
    for i in range(array_length):
        li.append(random.choice(range(1, random_range)))
    li.sort(reverse=True)
    context = {
        'top': li[0]
    }
    return JsonResponse(context)

from queue import PriorityQueue

@api_view(['GET'])
def priority_queue(request):
    pq = PriorityQueue()
    for i in range(array_length):
        pq.put(-random.choice(range(1, random_range)))
    context = {
        'top': -pq.get()
    }
    return JsonResponse(context)
