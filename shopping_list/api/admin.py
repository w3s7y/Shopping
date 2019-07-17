from django.contrib import admin
import api.models


# Register your models here.
admin.site.register(api.models.Item)
admin.site.register(api.models.List)
admin.site.register(api.models.ItemListMap)
admin.site.register(api.models.Favorite)
admin.site.register(api.models.Offer)
admin.site.register(api.models.Shop)
