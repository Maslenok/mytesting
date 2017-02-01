from django.contrib import admin
from .models import Result, UsersAnswer

class ResultAdmin(admin.ModelAdmin):
    show_change_link = True
    list_display = ("users", "course","resultValue", "dateCreated")
    list_filter = ["users", "course" ]
    fields = ("users", "course","resultValue", "dateCreated","is_complete" )
    readonly_fields = ("users", "course","resultValue", "dateCreated","is_complete" )
    list_per_page=10

    def has_add_permission(self, request):

        return False
admin.site.register(Result,ResultAdmin)

class UserAdmin(admin.ModelAdmin):
    list_display = ("users", "course", "question", "right","result")
    list_filter= ("users", "course", "question", "right","result")


admin.site.register(UsersAnswer, UserAdmin)
