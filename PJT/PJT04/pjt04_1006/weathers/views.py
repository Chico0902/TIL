from django.shortcuts import render
import matplotlib.pyplot as plt
import pandas as pd
from io import BytesIO
import base64
csv_path = 'weathers/data/austin_weather.csv'
plt.switch_backend("Agg")


# Create your views here.
def problem1(request):
    df = pd.read_csv(csv_path)
    context = {
        'df': df,
    }
    return render(request, 'weathers/problem1.html', context)

def problem2(request):
    columns = ['Date', 'TempHighF', 'TempAvgF', 'TempLowF']
    df = pd.read_csv(csv_path, usecols=columns)
    df['Date'] = pd.to_datetime(df['Date'])

    plt.clf()

    # 그래프 먼저 3개 그려주기
    plt.plot(df.Date, df.TempHighF, label='High Temperature')
    plt.plot(df.Date, df.TempAvgF, label='Average Temperature')
    plt.plot(df.Date, df.TempLowF, label='Low Temperature')

    plt.title('Temperature Variation')  # 제목
    plt.ylabel('Temperature (Fahrenheit)')  
    plt.xlabel('Date')
    # plt.xticks(rotation=45)
    plt.grid(True)  # 격자추가
    plt.legend(loc='lower center')  # 범례설정

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    img_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')
    buffer.close()
    context = {
        'chart_image' : f'data:image/png;base64,{img_base64}',
    }
    return render(request, 'weathers/problem2.html', context)


def problem3(request):
    columns = ['Date', 'TempHighF', 'TempAvgF', 'TempLowF']
    df = pd.read_csv(csv_path, usecols=columns)
    df['Date'] = pd.to_datetime(df['Date'])
    mean_df_H = df.groupby(pd.Grouper(key='Date', freq = 'M'))['TempHighF'].mean().reset_index()
    mean_df_A = df.groupby(pd.Grouper(key='Date', freq = 'M'))['TempAvgF'].mean().reset_index()
    mean_df_L = df.groupby(pd.Grouper(key='Date', freq = 'M'))['TempLowF'].mean().reset_index()        
    
    plt.clf()

    # 그래프 먼저 3개 그려주기
    plt.plot(mean_df_H.Date, mean_df_H.TempHighF, label='High Temperature')
    plt.plot(mean_df_A.Date, mean_df_A.TempAvgF, label='Average Temperature')
    plt.plot(mean_df_L.Date, mean_df_L.TempLowF, label='Low Temperature')

    plt.title('Temperature Variation')  # 제목
    plt.ylabel('Temperature (Fahrenheit)')  
    plt.xlabel('Date')
    # plt.xticks(rotation=45)
    plt.grid(True)  # 격자추가
    plt.legend(loc='lower right')  # 범례설정

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    img_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')
    buffer.close()
    context = {
        'chart_image' : f'data:image/png;base64,{img_base64}',
    }
    return render(request, 'weathers/problem3.html',context)


def problem4(request):
    # columns = ['Events']
    
    # 필요한 값 추출
    df = pd.read_csv(csv_path)
    df = df.replace({'Events' : ' '}, 'No Events') 
    
    # "Event" 열의 값을 분리하여 새로운 열에 저장
    df['Event_Separated'] = df['Events'].str.split(' , ')

    # 분리된 값들을 개별적으로 카운트
    event_counts = df['Event_Separated'].explode().value_counts()



    plt.bar(event_counts.index, event_counts.values)
    plt.title('Events Counts')
    plt.xlabel('Events')
    plt.ylabel('Count')
    plt.grid(True)
    plt.show()


    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    img_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')
    buffer.close()
    context = {
        'chart_image' : f'data:image/png;base64,{img_base64}',
    }

    return render(request, 'weathers/problem4.html',context)
