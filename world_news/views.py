# from django.shortcuts import render
# from .models import *
#
#
# # def home(request):
# #     return render(request, 'front/home.html')
# #
#
# def about(request):
#     return render(request, 'front/about.html')
#
#
# def news_header(request):
#     header_post_objs = NewsTitle.objects.all()[0]
#     category = header_post_objs.category.name
#     title = header_post_objs.title
#     photo = header_post_objs.photo
#     header_items = {
#         "catagory": NewsTitle.objects.all()[:3],
#         "entertiment": EntertainmentPost.objects.all(),
#         "birthday": Birthday.objects.all(),
#         "happyday": HappyDay.objects.all(),
#         "busines": Business.objects.all(),
#         "economy": Economy.objects.all(),
#         "economynews": EconomyNews.objects.all(),
#         "trevelnews": TravelNews.objects.all(),
#         "beachnews": BeachNews.objects.all(),
#         "comment_count": len(CommentNewsTitle.objects.filter(news_title=detail_post.id))
#
#     }
#     return render(request, 'front/home.html', context=header_items)
#

from django.shortcuts import render
from .models import *


# def home(request):
#     return render(request, 'front/home.html')

def about(request):
    return render(request, 'front/about.html')


def news_header(request):
    header_post_objs = NewsTitle.objects.all()[:3]
    entertainment_post_objs = EntertainmentPost.objects.all()
    business_post_objs = BusinessPost.objects.all()
    travel_post_objs = TravelPost.objects.all()
    life_style_post_objs = LifeStylePost.objects.all()
    print(header_post_objs)
    return render(request, "front/home.html", context={'post_title': header_post_objs,
                                                       'entertainment': entertainment_post_objs,
                                                       'business': business_post_objs,
                                                       'travel': travel_post_objs,
                                                       'lifestyle': life_style_post_objs})


def news_header_detail(request, id):
    detail_post = NewsTitle.objects.get(id=id)
    detail_post.views_count += 1
    detail_post.save()
    comment_count = len(CommentNewsTitle.objects.filter(news_title=detail_post.id))
    return render(request, "front/blog-detail-02.html",
                  {"detail_view": detail_post,
                   "comment_count": comment_count})
