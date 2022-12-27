from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
import csv



def index(request):
    return redirect(reverse('bus_stations'))

CONTENT = []

with open('data-398-2018-08-30.csv', encoding='UTF-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        CONTENT.append(f'Название станции: {row["Name"]}, Улица: {row["Street"]}, Район: {row["District"]}')

def bus_stations(request):
	page_num = int(request.GET.get("page", 1))
	paginator = Paginator(CONTENT, 10)
	page = paginator.get_page(page_num)

	context = {

		'page': page,
	}

	return render(request, 'stations/index.html', context)

