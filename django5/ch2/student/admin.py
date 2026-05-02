from django.contrib import admin
from student.models import Profile, Result

# create simple admin class without any customizations
class ProfileModelClass(admin.ModelAdmin):
    # pass
    list_display = ("id", "name", "age", "email", "city", "roll")
    search_fields = ("name", "email", "city", "roll")
    list_filter = ("age", "city")


admin.site.register(Profile, ProfileModelClass)


@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ("id", "student", "subject", "marks")
    # student__name is used to search by the name of the student in the related Profile model
    search_fields = ("student__name", "subject")
    list_filter = ("subject",)
