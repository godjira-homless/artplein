import django_filters
from .models import Technic

class TechnicFilter(django_filters.FilterSet):

    class Meta:
        model = Technic
        fields = {
            'name': ['icontains'],
                  }


