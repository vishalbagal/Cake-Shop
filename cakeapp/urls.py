from django.urls import path
from cakeapp import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('',views.home),
    path('register',views.register),
    path('login',views.user_login),
    path("logout",views.user_logout),
    path("about",views.about_us),
    path("contact",views.contact_us),
    path("detail/<pid>",views.product_detail),
    path("catfilter/<cv>",views.catfilter),
    path("range",views.range),
    path("addtocart/<pid>",views.addtocart),
    path("cart",views.cart),
    path("updateqty/<qv>/<cid>",views.updateqty),
    path("placeorder",views.placeorder),
    path("makepayment",views.makepayment),
    path('menu',views.menucard),



]


if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)