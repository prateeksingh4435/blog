from django.contrib import admin


# Register your models here.
from Blogging.models import Blog, signupdata ,WriteTechnologyBlog ,WriteBlockchainBlog,WriteRoboticsBlog,WriteWebBlog , BlogByUser

class blogadmin(admin.ModelAdmin):
    list_display = ('firstname','lastname','email','member','query')

class servicesignupdata(admin.ModelAdmin):
    list_display = ('firstname','lastname','email','username','password1')

admin.site.register(Blog,blogadmin)
admin.site.register(signupdata,servicesignupdata)
admin.site.register([WriteTechnologyBlog,WriteWebBlog,WriteRoboticsBlog,WriteBlockchainBlog])
admin.site.register(BlogByUser)
