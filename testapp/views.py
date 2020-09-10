from django.shortcuts import render
from testapp.models import FilterModel

# Create your views here.
def index_views(request):
    return render(request,'testapp/index.html')

def upper_views(request):
    data_list = FilterModel.objects.all()
    return render(request,'testapp/upper.html',{'data_list':data_list})

def lower_views(request):
    data_list = FilterModel.objects.all()
    return render(request,'testapp/lower.html',{'data_list':data_list})

def truncate_view(request):
    data_list = FilterModel.objects.all()
    return render(request,'testapp/truncate.html',{'data_list':data_list})

def title_view(request):
    data_list = FilterModel.objects.all()
    return render(request,'testapp/title.html',{'data_list':data_list})
