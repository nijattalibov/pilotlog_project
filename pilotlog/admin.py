from django.contrib import admin
from .models import Aircraft, Flight, Pilot, SettingConfig, Airfield, Imagepic, LimitRules, myQuery, myQueryBuild, Qualification

admin.site.register(Aircraft)
admin.site.register(Flight)
admin.site.register(Pilot)
admin.site.register(SettingConfig)
admin.site.register(Airfield)
admin.site.register(Imagepic)
admin.site.register(LimitRules)
admin.site.register(myQuery)
admin.site.register(myQueryBuild)
admin.site.register(Qualification)
