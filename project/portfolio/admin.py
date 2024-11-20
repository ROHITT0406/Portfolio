from django.contrib import admin
from  portfolio.models import *
# Register your models here.
admin.site.register(Contact)
admin.site.register(Blog)

class InternshipAdmin(admin.ModelAdmin):
    list_display=('fullname',
                'usn',
                'email',
                'college_name',
                'offer_status',
                'start_date',
                'end_date',
                'proj_report',
                'timestamp')
    search_fields=('fullname','usn','email',)
admin.site.register(Internship,InternshipAdmin)