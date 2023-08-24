from django.shortcuts import render


def custom404view(request, exception):
    return render(request, '404.html', status=404)