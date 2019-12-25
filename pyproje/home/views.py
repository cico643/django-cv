from django.shortcuts import render,HttpResponse

# Create your views here.
def home_view(request):
    if request.user.is_authenticated:
        context = \
            {
                'isim': 'Muhammet'
            }
    else:
        context = \
            {
                'isim': 'misafir '
            }
    return render(request,'home.html',context)
