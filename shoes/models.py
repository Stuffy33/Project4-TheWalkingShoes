# models for Shoes trading app
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


STATUS = ((0, "Draft"), (1, "Published"))


class Category(models.Model):
    #Shoe Categories
    categories = models.CharField(max_length=20)

    class Meta:
        #Display Trade
        ordering = ("categories",)

    def __str__(self):
        #Display Trade
        return self.categories


class ShoePair(models.Model):
    #model for trading shoes
    shoe_name = models.CharField(
        max_length=50, unique=True, null=False, blank=False)
    trader_name = models.CharField(
        max_length=50, unique=True, null=False, blank=False)
    slug = models.SlugField(
        max_length=50, unique=True, null=False, blank=False)
    trader = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='shoe_pair')
    description = models.TextField()
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, blank=False, null=False)
    shoe_image = CloudinaryField('image', null=False, blank=False)
    shoe_size = models.IntegerField(null=False, blank=False)
    status = models.IntegerField(choices=STATUS, default=0)
    remaining_pairs = models.IntegerField(null=False, blank=False)
    price = models.IntegerField(null=False, blank=False)
    likes = models.ManyToManyField(User, related_name='shoe_likes', blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    amount_of_pairs = models.IntegerField(null=False, blank=False)

    class Meta:
        #display shoes in most recent order
        ordering = ['-created_on']

    def __str__(self):
        #Display Shoe type
        return self.shoe_name

    def number_of_likes(self):
        #Return number of likes per shoes
        return self.likes.count()