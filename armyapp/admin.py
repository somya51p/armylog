from django.contrib import admin

# Register your models here.
from .models import stock,issueregister,loadchart
admin.site.register(stock)
admin.site.register(issueregister)
admin.site.register(loadchart)
admin.site.site_header = " ADMIN : Army Load Management & Traffic System"