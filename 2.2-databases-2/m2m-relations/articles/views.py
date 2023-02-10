from django.shortcuts import render

from articles.models import Article


def articles_list(request):
    template = 'articles/news.html'
    articles = Article.objects.all().order_by(ordering)
    context = {'object_list': articles}

    return render(request, template, context)
