from django.shortcuts import render, redirect
from .models import Stock
from .forms import StockForm
from django.contrib import messages

# pk_b7b18cb494f64dd9943910083541828b

# Create your views here.
def home(request):
    import requests
    import json

    if request.method == "POST":
        ticker = request.POST['ticker']
        
        # create a request and connect with url which calls the api
        api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + str(ticker) + "/quote?token=pk_b7b18cb494f64dd9943910083541828b")

        # error handling
        try:
            # going out to API and getting data
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error..."

        return render(request, 'home.html', {'api': api})

    else:
        return render(request, 'home.html', {'ticker': "Enter a Ticker Symbol Above..."})


def about(request):
    return render(request, 'about.html', {})


def add_stock(request):
    import requests
    import json

    # do stuff with ticker
    if request.method == "POST":
        form = StockForm(request.POST or None)

        if form.is_valid():
            form.save()
            messages.success(request, ("Stock Has Been Added!"))
            return redirect('add_stock')
    else:
        ticker = Stock.objects.all()
        output = []
        for ticker_item in ticker:
            api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + str(ticker_item) + "/quote?token=pk_b7b18cb494f64dd9943910083541828b")
            # error handling
            try:
                # going out to API and getting data
                api = json.loads(api_request.content)
                output.append(api)
            except Exception as e:
                api = "Error..."

        return render(request, 'add_stock.html', {'ticker': ticker, 'output': output})


def delete(request, stock_id):
    # get id number from stock objects
    item = Stock.objects.get(pk=stock_id)
    item.delete()
    messages.success(request, ("Stock Has Been Deleted!"))
    return redirect(delete_stock)


def delete_stock(request):
    ticker = Stock.objects.all()
    return render(request, 'delete_stock.html', {'ticker': ticker})