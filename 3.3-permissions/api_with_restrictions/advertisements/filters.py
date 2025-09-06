from django_filters import rest_framework, DateFromToRangeFilter

from advertisements.models import Advertisement


class AdvertisementFilter(rest_framework.FilterSet):
    """Фильтры для объявлений."""

    date_published = DateFromToRangeFilter(field_name="date_published")
    class Meta:
        model = Advertisement
        fields = ['date_published']
