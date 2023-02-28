from django.urls import reverse
from django.shortcuts import redirect
from urllib.parse import urlencode

def my_view(request):
    # Do some processing...
    params = {'param1': 'value1', 'param2': 'value2'}
    query_string = urlencode(params)
    url = f'{reverse("my_view")}?{query_string}'
    return redirect(url)
