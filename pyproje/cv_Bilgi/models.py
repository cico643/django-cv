from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from ckeditor.fields import RichTextField
evli_CHOICES = (
    ('Evli','EVLİ'),
    ('Bekar', 'BEKAR'),
)

# Create your models here.
class Bilgi(models.Model):
    Name = models.CharField(max_length=120, verbose_name="Adi")
    Surname = models.CharField(max_length=120, verbose_name="Soyadi")
    content = models.TextField(verbose_name="Egitim_Bilgileri")
    experience = models.TextField(verbose_name="Tecrube")
    hobi = RichTextField(verbose_name="Hobi")
    image=models.ImageField(null=True,blank=True)
    job = models.CharField(max_length=120, verbose_name='Meslek')
    language = models.TextField(verbose_name='Dil')
    adress = models.TextField(verbose_name="Adres")
    phone = models.CharField(max_length=11, verbose_name="Telefon")
    email = models.EmailField(verbose_name="Mail")
    date = models.DateField(verbose_name="Dogum_Tarihi")
    dogumyeri = models.CharField(max_length=120, verbose_name="Dogum_Yeri")
    medeni_hali = models.CharField(max_length=6, choices=evli_CHOICES, default='Bekar')



    slug=models.SlugField(unique=True,editable=False,max_length=130)


    def get_abolute_url(self):
        print(reverse('cv_Bilgi:detail',kwargs={'slug':self.slug}))
        return  reverse('cv_Bilgi:detail',kwargs={'slug':self.slug})
        #return '/bilgi/{}'.format(self.id)


    def get_create_url(self):
        return  reverse('cv_Bilgi:create')

    def get_update_url(self):
        return  reverse('cv_Bilgi:update',kwargs={'slug':self.slug})

    def get_delete_url(self):
        return  reverse('cv_Bilgi:delete',kwargs={'slug':self.slug})

    def _get_unique_slug(self):
        slug=slugify(self.Surname.replace('ı','i'))
        unique_slug=slug
        counter=1
        while Bilgi.objects.filter(slug=unique_slug).exists():
            unique_slug='{}-{}'.format(slug,counter)
            counter =1
        return unique_slug


    def save(self,*args,**kwargs):
        self.slug=self._get_unique_slug()
        return super(Bilgi,self).save(*args,**kwargs)

    class Meta:
        ordering=['-id']

    def __str__(self):
        return self.Name+" "+self.Surname


