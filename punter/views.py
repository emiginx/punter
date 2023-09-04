from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import *
import datetime 

# Create your views here.
def index(request):
    categories =  Category.objects.all()
    predictions = Prediction.objects.all()
    paginator = Paginator(predictions, 12)  # Show 12 predictions per page.
    page_number = request.GET.get("page")
    predictions_obj = paginator.get_page(page_number)
    todays_datetime = datetime.datetime.now() 
    context = {'categories': categories, 'predictions': predictions_obj, 'todays_datetime': todays_datetime}
    return render(request, "index.html",context)

def detail(request, id):
    categories =  Category.objects.all()
    prediction = get_object_or_404(Prediction,id=id)
    todays_datetime = datetime.datetime.now()
    context = { 'prediction': prediction, 'categories': categories,'todays_datetime': todays_datetime}
    return render(request, "detail.html", context)

def category(request, id):
    categories =  Category.objects.all()
    predictions = Prediction.objects.filter(category=id)
    paginator = Paginator(predictions, 12)  # Show 12 predictions per page.
    page_number = request.GET.get("page")
    predictions_obj = paginator.get_page(page_number)
    todays_datetime = datetime.datetime.now() 
    context = {'categories': categories, 'predictions': predictions_obj, 'todays_datetime': todays_datetime}
    return render(request, "category.html",context)
