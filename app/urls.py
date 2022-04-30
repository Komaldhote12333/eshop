from django.urls import path
from .import views


urlpatterns = [
    path('', views.index, name="index"),
    path('index', views.index, name="home"),
    path('products', views.products, name="products"),
    path('search', views.search, name="search"),
    path('quickview<str:id>', views.quickview, name="quickview"),
    path('login', views.login, name="login"),
    path('registerdone', views.registerdone, name="registerdone"),
    path('logindone', views.logindone, name="logindone"),
    path('logout', views.logout, name="logout"),
    path('contact', views.contact, name="contact"),
    path('contactsavr', views.contactsavr, name="contactsavr"),
    path('checout', views.checout, name="checout"),
    path('ordertaking', views.ordertaking, name="ordertaking"),
    path('ordershow', views.ordershow, name="ordershow"),
    path('update', views.update, name="update"),
    path('about', views.about, name="about"),
    path('delet', views.delet, name="delet"),
   
   
   
   
   
   
   
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',
         views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',
         views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cartdetais',views.cart_detail,name='cart_detail'),   

]