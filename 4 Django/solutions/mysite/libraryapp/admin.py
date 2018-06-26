from django.contrib import admin

from .models import AuthorMTO, BookMTO, AuthorMTM, BookMTM


admin.site.register(AuthorMTO)
admin.site.register(BookMTO)

admin.site.register(AuthorMTM)
admin.site.register(BookMTM)

