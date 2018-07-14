from django.shortcuts import render

# Create your views here.
def index(request):
    ctx = {}
    return render(request, "index.html", ctx)

def detail(requset):
    pass

# def about(request):
#     pass
