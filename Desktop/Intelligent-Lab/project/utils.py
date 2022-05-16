from .models import Tag, Project
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def paginateProject(request,projectsList,results):
    page = request.GET.get('page')
    paginator = Paginator(projectsList,results)

    try:
        projectsList = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        projectsList = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        projectsList = paginator.page(page)

    leftIndex = (int(page) - 4)
    if leftIndex < 1 :
        leftIndex = 1
    rightIndex = (int(page) + 5)
    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    custom_range = range(leftIndex,rightIndex)
    return paginator, custom_range, projectsList


def searchProject(request):
    search_query = ''
    
    if request.GET.get('search_query'):
        search_query = request.GET['search_query']

    tags = Tag.objects.filter(name__icontains=search_query)

    projectsList = Project.objects.distinct().filter(
     Q(title__icontains=search_query) |
     Q(description__icontains=search_query) |
     Q(owner__name__icontains=search_query) | 
     Q(tags__in=tags)
    )

    return projectsList , search_query