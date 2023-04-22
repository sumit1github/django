from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.http import JsonResponse


class TerminationCatalogue(View):
    template = app + "/product_catalogue.html"

    def get(self, request,):
        
        product_list=product_termination.get_all_products()

        paginate_product_list=paginate(request, product_list, 50)

        context={
            'product_list':paginate_product_list,
            'data_list':paginate_product_list,
            }
        return render(request, self.template, context)


class ProductSearchAjax(View):
    def get(self, request):

        data= request.GET.dict()
        product_list= product_termination.product_search(data)
        return JsonResponse(product_list, safe=False)