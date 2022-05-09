#I HAVE CREATED THIS FILE- YASH
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    # abcd= {'name':'Sid','place':'Himachal'}
    return render(request,'index.html')

def removepunc(request):
    print(request.GET.get('text','default'))
    return HttpResponse("removepunc")

# def index(request):
#     f=open("DJ.txt")
#     # return HttpResponse('''\n<a href="http://127.0.0.1:8000/about" > GO to Hackerrank about page</a>''')
#     return HttpResponse(f)

# def about(request):
#     return HttpResponse('''<a href="https://www.hackerrank.com/dashboard"> Hackerrank </a>
#     <a href="http://127.0.0.1:8000/">GO TO HOME </a> ''')