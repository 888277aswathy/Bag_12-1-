from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from django.contrib import admin
from .views import add_category, add_to_cart,ship_order,deliver_order, checkout,orders,all_orders,ordered_items,aordered_items, confirm_purchase,alogout_view,login_view,forgot_password,forgot1,password_new,myprofile,edit_profile, product_detail, register_request, logout_view, home, add_product, edit_product, delete_product,product_list,index_home, remove_from_cart, thank_you_page,view_cart,first

urlpatterns = [
    path('', first, name='first'),
    path('products/', product_list, name='product_list'),
    path('admin/', admin.site.urls),
    path('login/', login_view, name='login'), 
    path('logout/', logout_view, name='logout'),
    path('alogout/', alogout_view, name='adminlogout'),
    path('home/', home, name='home'),
    path('add-product/', add_product, name='add_product'),
    path('edit-product/<int:id>/', edit_product, name='edit_product'),
    path('delete-product/<int:id>/', delete_product, name='delete_product'),
    path("register", register_request, name="register"),
    path("forgot", forgot_password, name="forgot"),
    path("forgot1",forgot1),
    path('password_new',password_new),
    path('myprofile',myprofile,name='view_profile'),
    path('edit_profile',edit_profile,name='edit_profile'),
    path('cart/', view_cart, name='view_cart'),
    path('orders',orders,name='orders'),
    path('all_orders',all_orders,name='all_orders'),
    path('ordered_items/<str:id>',ordered_items,name='ordered_items'),
    path('aordered_items/<str:id>',aordered_items,name='aordered_items'),
    path('ship_order/<str:id>',ship_order,name='ship_order'),
    path('deliver_order/<str:id>',deliver_order,name='deliver_order'),

    path('add/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('remove/<int:item_id>/',remove_from_cart, name='remove_from_cart'),
    path('index/', index_home, name='index'),
    path('checkout/', checkout, name='checkout'),
    path('confirm-purchase/', confirm_purchase, name='confirm_purchase'),
    path('add_category/', add_category, name='add_category'),
    path('confirm-purchase/', confirm_purchase, name='confirm_purchase'),
    path('thank-you/', thank_you_page, name='thank_you_page'),
    path('product/<int:product_id>/', product_detail, name='product_detail'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
