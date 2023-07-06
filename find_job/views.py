from django.shortcuts import render
import requests
# Create your views here.


def job_listings(request):

    url = "https://storage.googleapis.com/programiz-static/hiring/software/job-listing-page-challenge/data.json"

    response = requests.get(url)

    data = response.json()
    
    return render(request, 'job_listing/job_listings.html', {'job_listings': data})