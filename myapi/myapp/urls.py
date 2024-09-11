from django.urls import path
from .views import Candlestick, Line, Bar, Pie

urlpatterns = [
    path('candlestick-data/', Candlestick.as_view(), name='candlestick-data'),
    path('line-chart-data/', Line.as_view(), name='line-chart-data'),
    path('bar-chart-data/', Bar.as_view(), name='bar-chart-data'),
    path('pie-chart-data/', Pie.as_view(), name='pie-chart-data'),
]
