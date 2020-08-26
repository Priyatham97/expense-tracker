import json
from datetime import datetime,timedelta

from django.shortcuts import render
from django.db.models import Count,Sum
from django.core import serializers
from .models import *



# Create your views here.
def home(request):


    try: 
        date_range = [request.GET['from'], request.GET['to']]
    except:
        date_range = [(datetime.today() - timedelta(days=29)).strftime("%Y-%m-%d"), datetime.today().strftime("%Y-%m-%d") ]
    date_filtered = Statement.objects.filter(date__range=date_range)

    cat_stats = date_filtered.values('category').order_by('category').annotate(sum=Sum('debit'),count=Count('category'))
    
    labels = [cat['category'] for cat in cat_stats]
    
    try:
        money_spent = int(Statement.objects.aggregate(spent=Sum('debit'))['spent'])
    except:
        money_spent = 1

    data = [cat['sum']/money_spent for cat in cat_stats]
    statements_count = sum([cat['count'] for cat in cat_stats])
    return render(request,'index.html',{'labels':labels,'data':data,'statements_count':statements_count,'spent':money_spent})

def trends(request):

    # date_filtered = Statement.objects.filter(date__range=date_range)

    return render(request,'trends.html')


def classify(request):
    try: 
        date_range = [request.GET['from'], request.GET['to']]
    except:
        date_range = [(datetime.today() - timedelta(days=29)).strftime("%Y-%m-%d"), datetime.today().strftime("%Y-%m-%d") ]
    date_filtered = Statement.objects.filter(date__range=date_range)

    serialized_data = json.loads(serializers.serialize('json', date_filtered))
    serialized_data = [data['fields'] for data in serialized_data]
    if serialized_data:
        header = [head.upper() for head in list(serialized_data[0].keys())]
    

    return render(request,'statements.html')