from django.shortcuts import render


def index (request):
    context = {
        'yo': request.user
    }
    return render(request, 'base_app.html', context)