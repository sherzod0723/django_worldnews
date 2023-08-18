# from django.contrib import admin
# from .models import *
#
#
# admin.site.register([CategoryNewsTitle, NewsTitle, EntertainmentPost, Birthday, HappyDay, Business,
#                      Economy, EconomyNews, TravelNews, BeachNews, CommentNewsTitle])
#
from django.contrib import admin
from .models import *

admin.site.register([CategoryNewsTitle, NewsTitle, EntertainmentPost, BusinessPost, TravelPost, LifeStylePost, CommentNewsTitle])
