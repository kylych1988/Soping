from django.db import models

# Create your models here.
class Setting(models.Model):
    name_site = models.CharField(max_length=200)
    description_site = models.CharField(max_length=150)
    logo_site = models.ImageField(upload_to= 'logo/')
    phone_site = models.CharField(max_length=200)
    instagram_site = models.URLField()
    class Meta:
        verbose_name = 'Настройки'
        verbose_name_plural = 'Настройки'

class Latest(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='image_latest/')
    image1 = models.ImageField(upload_to='image_latest/')
    price = models.CharField(max_length=100)
    class Meta:
        verbose_name = 'Электроника'
        verbose_name_plural = 'Электроника'


class Slid(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to= 'image/')
    descreption = models.CharField(max_length=200)
    name1 = models.CharField(max_length=200)
    image1 = models.ImageField(upload_to= 'image/')
    descreption1 = models.CharField(max_length=200)
    name2 = models.CharField(max_length=200)
    image2 = models.ImageField(upload_to= 'image/')
    descreption2 = models.CharField(max_length=200)


class Ders(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='image_ders/')
    descreption = models.CharField(max_length=200)

class Man(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='image_latest/')
    image1 = models.ImageField(upload_to='image_latest/')
    price = models.CharField(max_length=100)
    class Meta:
        verbose_name = 'Мужской'
        verbose_name_plural = 'Мужской'

class Woman(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='image_latest/')
    image1 = models.ImageField(upload_to='image_latest/')
    price = models.CharField(max_length=100)
    class Meta:
        verbose_name = 'Женский'
        verbose_name_plural = 'Женский'

class Kids(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='image_latest/')
    image1 = models.ImageField(upload_to='image_latest/')
    price = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Детский'
        verbose_name_plural = 'Детский'

class Nues(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='image/')
    price = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Новинка'
        verbose_name_plural = 'Новинка'

class Insta(models.Model):
    image1 = models.ImageField(upload_to='image1/')
    image2 = models.ImageField(upload_to='image2/')
    image3 = models.ImageField(upload_to='image3/')
    image4 = models.ImageField(upload_to='image4/')
    image5 = models.ImageField(upload_to='image5/')

    class Meta:
        verbose_name = 'Инстаграм фото'
        verbose_name_plural = 'Инстаграм фото'

class Closis(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='image/')
    price = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Новый тавар'
        verbose_name_plural = 'Новый '

class Phone(models.Model):
    phone = models.CharField(max_length=100)
    instagram = models.URLField()
    fasebook = models.URLField()
    email = models.EmailField()

    class Mate:
        verbose_name = 'Контакты'
        verbose_name_piural = 'Контакты'


    

    
