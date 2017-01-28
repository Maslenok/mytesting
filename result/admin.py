from django.contrib import admin
from .models import Result

class ResultAdmin(admin.ModelAdmin):
    show_change_link = True
    list_display = ("users", "course","resultValue", "dateCreated")
    list_filter = ["users", "course" ]
    fields = ("users", "course","resultValue", "dateCreated","is_complete" )
    readonly_fields = ("users", "course","resultValue", "dateCreated","is_complete" )

admin.site.register(Result,ResultAdmin)

