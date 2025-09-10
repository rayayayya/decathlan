from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2406400373',
        'nama': 'Rayna Balqis',
        'kelas': 'PBP D'    
    }

    return render(request, "main.html", context)
# Create your views here.
