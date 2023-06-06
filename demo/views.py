import json
from django.http import HttpResponse
from django.core.paginator import Paginator
from rest_framework.views import APIView
import sqlite3
from .ksh import sangshen
from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth import authenticate, login
from CeleryTask.task import start_get_data
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
import pandas as pd

def response_as_json(data):
    json_str = json.dumps(data)
    response = HttpResponse(
        json_str,
        content_type="application/json",
    )
    response["Access-Control-Allow-Origin"] = "*"
    return response


def json_response(data, code=200):
    data = {
        "code": code,
        "msg": "success",
        "data": data,
    }
    return response_as_json(data)


def json_error(error_string="error", code=500, **kwargs):
    data = {
        "code": code,
        "msg": error_string,
        "data": {}
    }
    data.update(kwargs)
    return response_as_json(data)


JsonResponse = json_response
JsonError = json_error



class sankey(APIView):
    def get(self, request, *args, **kwargs):
        return JsonResponse(json.loads(sangshen()))



# 读取json，返回最近数据更新的时间
class update1(APIView):
    def get(self, request, *args, **kwargs):
        with open('./demo/data/UpdateTime.json', 'r', encoding='utf-8') as f:
            data = f.read()
        return JsonResponse(json.loads(data))


@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username= username, password= password)
        if user is not None:
            # 用户名和密码正确，执行任务函数
            response = redirect('/')
            start_get_data().delay
            print("pass")
            return response  # 重定向到原来的页面
        else:
            # 用户名和密码不正确，返回错误信息给用户
            error_message = 'Invalid username or password'
            messages.error(request, error_message)
            return redirect(f'/?error={error_message}')  # 重定向到原来的页面并传递错误信息
    else:
        return render(request, '/')













# 实时热点
class ssrd1(APIView):
    def get(self, request, *args, **kwargs):
        datalist = []
        con = sqlite3.connect("data.db")
        cur = con.cursor()
        sql = "select * from job"
        cur.execute(sql)
        data = cur.fetchall()
        for row in data:
            datalist.append({
                'urlx':row[0],
                'job_name': row[1],
                'company_name': row[2],
                'salary': row[3],
                'address':row[4]
            })
        return  JsonResponse(datalist)


class job_fre1(APIView):
    def get(self, request, *args, **kwargs):
        with open ('./demo/data/job_fre.json','r',encoding='utf-8') as f:
            data = f.read()
        return JsonResponse(json.loads(data))

class lan_fre1(APIView):
    def get(self, request, *args, **kwargs):
        with open('./demo/data/language.json', 'r', encoding='utf-8') as f:
            data = f.read()
        return JsonResponse(json.loads(data))


class avg_salary1(APIView):
    def get(self,request,*args,**kwargs):
        with open('./demo/data/avg_salary.json', 'r', encoding='utf-8') as f:
            data = f.read()
        return JsonResponse(json.loads(data))

class g4(APIView):
    def get(self,request,*args,**kwargs):
        with open('./demo/data/job_category.json', 'r', encoding='utf-8') as f:
            data = f.read()
        return JsonResponse(json.loads(data))

# 主页
class IndexView(APIView):
    def get(self, request, *args, **kwargs):
        return HttpResponse(content=open("./templates/index.html", 'rb').read())


class movieView(APIView):
    def get(self, request, *args, **kwargs):
        con = sqlite3.connect("data.db")
        cur = con.cursor()
        sql = "select * from job"
        data = cur.execute(sql)
        points = []
        for idx, item in enumerate(data):
            if item[9] is not None:  # 判断 jw 列是否为 null
                row =[]
                parts = item[9].split(",")  # 将字符串按逗号分隔
                lng = parts[0]
                lat = parts[1]
                row.append([item[2], item[1], item[4], lng, lat, item[0]])
                points.append(row)
        cur.close()
        con.close()
        return render(request, 'map.html', {'points': json.dumps(points)})


class tempView(APIView):
    def get(self,request):
        return HttpResponse(content=open("./templates/temp.html", 'rb').read())

class scoreView(APIView):
    def get(self,request):
        return HttpResponse(content=open("./templates/graph.html", 'rb').read())
        # return HttpResponse(content=open("./templates/graph.html", 'rb').read())

class wordView(APIView):
    def get(self, request, *args, **kwargs):
        datalist = []
        con = sqlite3.connect("data.db")
        cur = con.cursor()
        sql = "select * from job"
        data = cur.execute(sql)
        for idx,item in enumerate(data):
            row =list(item)
            row.append(idx+1)
            datalist.append(row)
        cur.close()
        con.close()

        paginator = Paginator(datalist, 10)
        page_number = request.GET.get('page')  # 获取当前页码，默认为第1页
        page_obj = paginator.get_page(page_number)  # 获取当前页的数据对象
        return render(request, "word.html", {'page_obj':page_obj} )