from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.home,name='home'),
    path('home/',views.home,name='home'),
    path('add-product/',views.add_product,name='add_product'),
    path('bidding/',views.bidding,name='bidding'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)