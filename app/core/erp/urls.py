from django.urls import path


from app.core.erp.views.category.views import CategoryListView, category_list

app_name = 'erp'

urlpatterns = [
    path('category/list/', CategoryListView.as_view(), name='category_list'),
    path('category/list2/', category_list, name='category_list2')
]
