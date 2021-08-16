from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.http import JsonResponse
from app.core.erp.models import Category
from django.views.decorators.csrf import  csrf_exempt , csrf_protect

def category_list(request):
    data = {
        'title': 'Listado de Categorías',
        'categories': Category.objects.all()
    }
    return render(request, 'category/list.html', data)





class CategoryListView(ListView):
    model = Category
    template_name = "category/list.html"


    def get_queryset(self):
        queryset = Category.objects.filter(name__startswith='')
        
        return queryset
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        if request.method == 'GET':
            return redirect('erp:category_list2')

        return super().dispatch(request, *args, **kwargs)
    def post(self,request,*args, **kwargs ):
        data = {'name': 'luis'}
        return  JsonResponse(data)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title']='Listado de Categorias'

        #context['object_list']=Product.objects.all()
        return context
    



