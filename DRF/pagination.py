
======================================================= helper > utils.py ====================================

from rest_framework.pagination import PageNumberPagination

class CustomPagination(PageNumberPagination):
    

    def __init__(self, default_page_size):
        self.page_size= default_page_size  # default page size

        self.page_size_query_param = 'page_size' # query parameter to specify page size
        self.max_page_size = 100 # maximum allowed page size

    def get_previous_page_number(self):
        if self.page.has_previous():
            return self.page.previous_page_number()

    def get_next_page_number(self):
        if self.page.has_next():
            return self.page.next_page_number()

    def pagination_meta_data(self):
        return {
            'page': self.page.number,
            'total_pages': self.page.paginator.num_pages,
            'total_items': self.page.paginator.count,
            'next_page': self.get_next_page_number(),
            'previous_page': self.get_previous_page_number(),
        }
        
=====================================================  views.py ==================================================

class ProductList(APIView):
    pagination_class = utils.CustomPagination(10)
   
     def get(self, request):
        product_list = self.model.objects.filter(user = request.user).order_by('-id')

        paginator = self.pagination_class
        page = paginator.paginate_queryset(product_list, request)

        
        serializer_data = self.serializer_class(page, many=True).data

        return Response({
            "status":200,
            "conversation_list":serializer_data,
            "pagination_meta_data": paginator.pagination_meta_data(),
        })