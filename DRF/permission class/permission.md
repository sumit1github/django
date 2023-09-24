

# helpers > permission.py
    from rest_framework.permissions import BasePermission

    class is_authenticated(BasePermission):
        def has_permission(self, request, view):
            if request.user.is_authenticated:
                return True
            else:
                return False

# views.py 


    from .serializers import is_authenticated

    class YourModelViewSet(viewsets.ModelViewSet):
        queryset = YourModel.objects.all()
        serializer_class = YourModelSerializer
        permission_classes = [is_authenticated,]