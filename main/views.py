from django.shortcuts import render

def show_main(request):
    context = {
        'aplikasi : decathlan',
        'nama: Rayna Balqis',
        'kelas: PBP D'    
    }

    return render(request, "main.html", context)
# Create your views here.
