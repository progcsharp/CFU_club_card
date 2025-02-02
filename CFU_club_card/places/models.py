from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Place(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    short_description = models.TextField()
    promotion_image = models.ImageField(upload_to='promotions/', blank=True, null=True)  # Поле для изображения акции
    promotion_text = models.TextField(blank=True, null=True)
    preview_photo = models.ImageField(upload_to='promotions/', blank=True, null=True)
    category = models.ForeignKey(Category, related_name='places', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class PlacePromotionCondition(models.Model):
    place = models.ForeignKey(Place, related_name='promotion_conditions', on_delete=models.CASCADE)
    condition_text = models.CharField(max_length=255)  # Поле для текста условия акции

    def __str__(self):
        return self.condition_text


class PlaceImage(models.Model):
    place = models.ForeignKey(Place, related_name='images', on_delete=models.CASCADE)  # Связь с моделью Place
    image = models.ImageField(upload_to='sliders/', blank=True, null=True)  # Поле для изображения слайдера

    def __str__(self):
        return f"Image for {self.place.name}"


class PlaceAddress(models.Model):
    place = models.ForeignKey(Place, related_name='addresses', on_delete=models.CASCADE)  # Связь с моделью Place
    address = models.CharField(max_length=255)  # Поле для адреса

    def __str__(self):
        return self.address
