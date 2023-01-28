-----------------------------------list data display ---------------------------------
@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name")
----------------------------------- use any function ----------------------
@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name", "show_average")

    def show_average(self, obj):
        from django.db.models import Avg
        result = Grade.objects.filter(person=obj).aggregate(Avg("grade"))
        return result["grade__avg"]
      
----------------------------------------- user search -------------------------------
@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    search_fields = ("last_name__startswith", )
    
