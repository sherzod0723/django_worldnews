# from django.db import models
#
#
#
# class CategoryNewsTitle(models.Model):
#     name = models.CharField(max_length=255, verbose_name="title categoriyasi")
#
#     def __str__(self):
#         return self.name
#
#
# class NewsTitle(models.Model):
#     category = models.ForeignKey('CategoryNewsTitle', on_delete=models.CASCADE, verbose_name="category name")
#     title = models.CharField(max_length=350, verbose_name="sralavha")
#     post_category = models.CharField(max_length=255, verbose_name="Ichki kategoriya", default="GAMe")
#     photo = models.ImageField(upload_to='title/images/')
#     created_at = models.DateTimeField(auto_now=True, null=True)
#     description = models.TextField(verbose_name="yangiliklar matni")
#
#
#     def __str__(self):
#         return self.title
#
#
# class CommentNewsTitle(models.Model):
#     news_title = models.ForeignKey("NewsTitle", on_delete=models.CASCADE)
#     commit = models.TextField()
#
#
#
#
#
# class EntertainmentPost(models.Model):
#     title = models.CharField(max_length=255)
#     photo = models.ImageField(upload_to= "Entertainment/images")
#     in_category = models.CharField(max_length=255)
#     created_at = models.DateTimeField(auto_now=True, null=True)
#     description = models.TextField(verbose_name="Yangiliklar matni")
#
#     def __str__(self):
#         return self.title
#
#
# class Birthday(models.Model):
#     photo = models.ImageField(upload_to='Birthday/images')
#     title = models.CharField(max_length=255)
#     description = models.CharField(max_length=255, verbose_name="Yangili matni")
#     in_category = models.CharField(max_length=255)
#     created_at = models.DateTimeField(auto_now_add=True, null=True)
#
#
# class HappyDay(models.Model):
#     photo = models.ImageField(upload_to='HappyDay/images')
#     title = models.CharField(max_length=255, verbose_name="Yangiliklar")
#     description = models.CharField(max_length=255, verbose_name="Yangili matni")
#     in_category = models.CharField(max_length=255)
#     created_at = models.DateTimeField(auto_now_add=True, null=True)
#
#
# class Business(models.Model):
#     photo = models.ImageField(upload_to='Business/images')
#     title = models.CharField(max_length=255)
#     in_category = models.CharField(max_length=255)
#     created_at = models.DateTimeField(auto_now_add=True, null=True)
#     description = models.CharField(max_length=255, verbose_name="Yangilik matni")
#
# class Economy(models.Model):
#     photo = models.ImageField(upload_to='Economy/images')
#     title = models.CharField(max_length=255)
#     in_category = models.CharField(max_length=255)
#     description = models.CharField(max_length=255, verbose_name="Yangilik matni")
#
#
# class EconomyNews(models.Model):
#     photo = models.ImageField(upload_to='EconomyNews/images')
#     title = models.CharField(max_length=235)
#     description = models.CharField(max_length=250, verbose_name="Yangilik matni")
#     in_category = models.CharField(max_length=255)
#     created_at = models.DateTimeField(auto_now_add=True, null=True)
#
#
# class TravelNews(models.Model):
#     photo = models.ImageField(upload_to='TravelNews/images')
#     title = models.CharField(max_length=235)
#     in_category = models.CharField(max_length=255)
#     created_at = models.DateTimeField(auto_now_add=True, null=True)
#     description = models.CharField(max_length=220, verbose_name="Yangilik matni")
#
#
# class BeachNews(models.Model):
#     photo = models.ImageField(upload_to='BeachNews/images')
#     title = models.CharField(max_length=235)
#     description = models.CharField(max_length=200, verbose_name="Yangilik Matni")
#     in_category = models.CharField(max_length=255)
#     created_at = models.DateTimeField(auto_now_add=True, null=True)
#
#
#
#

from django.db import models
from django.contrib.auth.models import User


class CategoryNewsTitle(models.Model):
    name = models.CharField(max_length=255, verbose_name="Title in the category site")

    def __str__(self):
        return self.name


class NewsTitle(models.Model):
    category = models.ForeignKey(CategoryNewsTitle, on_delete=models.CASCADE, verbose_name="Yangilik turi")
    title = models.CharField(max_length=350, verbose_name="Sarlavha")
    powered_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    post_category = models.CharField(max_length=255, verbose_name="Ichki kategoriya", default="Game")
    photo = models.ImageField(upload_to="title/images")
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    description = models.TextField(verbose_name="Yangilik matni")
    views_count = models.IntegerField(default=0)


class CommentNewsTitle(models.Model):
    news_title = models.ForeignKey(NewsTitle, on_delete=models.CASCADE)
    comment = models.TextField()


class EntertainmentPost(models.Model):
    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to="Entertainment/images")
    inline_category = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    description = models.TextField(verbose_name="Yangilik matni")

    def __str__(self):
        return self.title


class BusinessPost(models.Model):
    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to="Business/images")
    inline_category = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    description = models.TextField(verbose_name="Yangilik matni")

    def __str__(self):
        return self.title


class TravelPost(models.Model):
    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to="Business/images")
    inline_category = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    description = models.TextField(verbose_name="Yangilik matni")

    def __str__(self):
        return self.title


class LifeStylePost(models.Model):
    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to="LifeStyle/images")
    inline_category = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    description = models.TextField(verbose_name="Yangilik matni")

    def __str__(self):
        return self.title
