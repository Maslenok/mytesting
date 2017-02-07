from django.contrib import admin
from .models import Result

class ResultAdmin(admin.ModelAdmin):
    show_change_link = True
    list_display = ("users", "course","resultValue", "dateCreated","is_complete")
    list_filter = ["users", "course","is_complete" ]
    fields = ("users", "course","resultValue", "dateCreated","is_complete" )
    readonly_fields = ("users", "course","resultValue", "dateCreated","is_complete" )
    list_per_page=10

    def has_add_permission(self, request):

        return False
admin.site.register(Result,ResultAdmin)


