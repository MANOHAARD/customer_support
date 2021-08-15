import django_filters as df
from .models import Order


class OrderFilter(df.FilterSet):

    class Meta:
        model = Order
        # fields = ('product', 'status', 'date_created')
        fields = '__all__'
