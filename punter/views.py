from django.shortcuts import render
from django.core.paginator import Paginator
from .models import *
import datetime 

# Create your views here.
def index(request):
    categories =  Category.objects.all()
    predictions = Prediction.objects.all()
    paginator = Paginator(predictions, 1)  # Show 12 predictions per page.
    page_number = request.GET.get("page")
    predictions_obj = paginator.get_page(page_number)
    todays_datetime = datetime.datetime.now() 
    context = {'categories': categories, 'predictions': predictions_obj, 'todays_datetime': todays_datetime}
    return render(request, "index.html",context)
