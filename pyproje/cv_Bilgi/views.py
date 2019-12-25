from django.shortcuts import render,HttpResponse,get_object_or_404,HttpResponseRedirect,redirect,Http404
from .models import Bilgi
from .forms import BilgiForm #Kullanıcıya servis edilecek olan form import  ediyoruz
from django.contrib import messages
from django.utils.text import slugify
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from  django.db.models import Q #arama

# Create your views here.

def bilgi_index(request):
    bilgi_list=Bilgi.objects.all()
    query=request.GET.get('q')
    if query:
        bilgi_list=bilgi_list.filter(Q(Name__icontains=query ) |
                                     Q(Surname__icontains=query )|
                                     Q(content__icontains=query ))

    paginator = Paginator(bilgi_list,3)  # Show 25 contacts per page

    page = request.GET.get('sayfa')
    try:
        bilgiler = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        bilgiler = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        bilgiler = paginator.page(paginator.num_pages)


    return render(request,'cv_bilgi/index.html',{'bilgiler':bilgiler})



def bilgi_create(request):
    if not request.user.is_authenticated:
        return Http404()



    # if reguest.method=="POST":
    #   print(reguest.POST)
    #  name=reguest.POST.get('Name')
    #  surname=reguest.POST.get('Surname')
    # content=reguest.POST.get('content')
    # birthyear=reguest.POST.get('Birthyear')
    #  Bilgi.objects.create(Name=name,Surname=surname,content=content,Birthyear=birthyear)
    #if reguest.method == "POST":
       # form = BilgiForm(reguest.POST)
      #  if form.is_valid():
     #       form.save()
    #else:
    #    form = BilgiForm()

    form = BilgiForm(request.POST or None,request.FILES or None) #fıles resmi getiriyort post metinsel ifadeler
    if form.is_valid():
        bilgi=form.save()

        messages.success(request,'Başarılı Birşekilde oluşturuldu')
        return HttpResponseRedirect(bilgi.get_abolute_url())

    contex = {
        'form': form
    }


    return render(request,'cv_bilgi/form.html',contex)


def bilgi_detail(request,slug):
    bilgi =get_object_or_404(Bilgi,slug=slug)
    context={
        'bilgi':bilgi,
    }
    return render(request, 'cv_bilgi/detail.html', {'bilgi': bilgi})



def bilgi_update(request,slug):
    if not request.user.is_authenticated:
        return Http404()
    bilgi = get_object_or_404(Bilgi, slug=slug)
    form = BilgiForm(request.POST or None,request.FILES or None,instance=bilgi)
    if form.is_valid():
        form.save()
        messages.success(request,'Başarılı Birşekilde Düzenlendi',extra_tags='mesaj-basarili')

        return HttpResponseRedirect(bilgi.get_abolute_url())
    contex = {
        'form': form
    }

    return render(request,'cv_bilgi/form.html',contex)


def bilgi_delete(request,slug):
    if not request.user.is_authenticated:
        return Http404()
    bilgi = get_object_or_404(Bilgi, slug=slug)
    bilgi.delete()
    return redirect('cv_Bilgi:index')

