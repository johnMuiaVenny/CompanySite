import django_filters
from .models import *


class MyFilter(django_filters.FilterSet):
    class Meta:
         model = BLOG
         fields = ['ABOUT']
     
