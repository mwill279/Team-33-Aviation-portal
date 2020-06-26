from django.contrib import admin
from .models import Jobtype, Jobform
# Register your models here.


admin.site.register(Jobtype)
#admin.site.register(Jobform)

@admin.register(Jobform)
class JobformAdmin(admin.ModelAdmin):
    list_display = ['title','postdate', 'posttime', 'deadlinedate', 'deadlinetime', 'open']



