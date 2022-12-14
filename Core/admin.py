from django.contrib import admin
from Core.models import Stat, StatHistoryDaily, StatHistoryHourly


# Register your models here.

class StatAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "last_value", "url", "query_selector", "creator")

    def save_model(self, request, obj, form, change):
        obj.creator = request.user
        super().save_model(request, obj, form, change)

    class Meta:
        model = Stat


admin.site.register(Stat, StatAdmin)


class StatHistoryDailyAdmin(admin.ModelAdmin):
    list_display = ("id", "stat", "value", "date")

    class Meta:
        model = StatHistoryDaily


admin.site.register(StatHistoryDaily, StatHistoryDailyAdmin)


class StatHistoryHourlyAdmin(admin.ModelAdmin):
    list_display = ("id", "stat", "value", "hour")

    class Meta:
        model = StatHistoryHourly


admin.site.register(StatHistoryHourly, StatHistoryHourlyAdmin)
