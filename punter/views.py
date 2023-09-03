from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    categories =  Category.objects.all()
    predictions = Prediction.objects.all()
    #todays_date = 
    #todays_time = 
    context = {'categories': categories, 'predictions': predictions}
    return render(request, "index.html",context)
