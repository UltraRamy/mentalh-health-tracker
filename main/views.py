from django.shortcuts import render
def show_main(request):
    context = {
        'npm' : '2306210393',
        'name': 'Ramy Ardya Ramadhan',
        'class': 'PBP D'
    }

    return render(request, "main.html", context)