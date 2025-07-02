from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
from pandas.io import json
from .models import Data
def hello(request):
    if (request.method == 'POST'):
        previous_data = Data.objects.all()
        previous_data.delete()
        file = request.FILES['file']
        df = pd.read_csv(file)
        json_record = df.reset_index().to_json(orient='records')
        data = []
        data = json.ujson_loads(json_record)
        #saving data in database.Populating the DB
        for d in data:
            name = d['property_name']
            price = d['property_price']
            rent = d['property_rent']
            emi = d['emi']
            tax = d['tax']
            exp = d['other_exp']
            expense_monthly = emi+tax+exp
            income_monthly = rent-expense_monthly
            dt = Data(name=name,price=price,rent=rent,emi=emi,tax=tax,exp=exp,expense_monthly=expense_monthly,income_monthly=income_monthly)
            dt.save()
        #Data is saved and DB is created. Now access it and display in the HTML page
        data_objects = Data.objects.all()
        #print(data_objects[0].expense_monthly)
        return render(request, template_name='myapp/index.html', context={'data_objects': data_objects})
    else:
        print("This is a get method")
    return render(request,'myapp/index.html')


