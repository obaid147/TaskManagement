from django.shortcuts import render


def index(request):

    context = {
        'title': 'Manage Tasks',
        'heading': 'Task Management'
    }
    return render(request, 'TaskApp/index.html', context)
