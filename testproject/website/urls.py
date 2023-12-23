from django.urls import path
from website import views

urlpatterns = [
   
    path('', views.store,name='store'),
    path('showdata', views.index, name = 'showdata'),
    path('edit_product/<int:id>', views.edit_db, name= 'edit_product'),
    path('update_product/<int:id>', views.product_update, name= 'product_update'),
    path('delete_product/<int:id>',views.delete_product, name= 'delete_product'),
    path('task_done/<int:id>', views.task_done, name= 'task_done'),
    path('task_incomplete/<int:id>', views.task_incomplete, name= 'task_incomplete')

]