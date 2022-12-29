from django.shortcuts import render

# Create your views here.
def jinja_print(request):
    d={'name':'yogi'}
    return render(request,'jinja_print.html',context=d)
