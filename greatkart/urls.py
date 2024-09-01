
from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # path('jet/', include('jet.urls', 'jet')),
    # path('admin/',include('admin_honeypot.urls',namespace='admin-honeypot')),
    path("loja/", admin.site.urls),
    # path("",views.home, name="home"),
    path("store/", include('store.urls')),
    path('cart/',include('carts.urls')),
    path('account/',include('account.urls')),
   

    # Orders
    path('orders/',include('orders.urls')),
    path('',include('home.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

