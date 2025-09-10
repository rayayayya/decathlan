from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2406400373',
        'name': 'Rayna Balqis',
        'class': 'PBP D'
    }

    return render(request, "main.html", context)
