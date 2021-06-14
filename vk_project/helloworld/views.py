from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
import requests

from .forms import NameForm

def index(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:

            version = '5.131'
            response = requests.get('https://api.vk.com/method/friends.get', params={
                'access_token': form.cleaned_data['token'],
                'v': version,
                'user_id': form.cleaned_data['user_id']
            })

            data = response.json()

            return render(request, 'result.html', {'result': data})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'name.html', {'form': form})