from django.contrib import admin


from .models import *

from .models import Image

admin.site.register(Image)

admin.site.register(Jobs)
admin.site.register(JobApplication)
admin.site.register(Enquiry)
admin.site.register(Bussiness)
