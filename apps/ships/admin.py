from django.contrib import admin
from apps.ships.models import Ship, ShipOwner, ShipType, ShipAccesories, ShipImage


admin.site.register(Ship)
admin.site.register(ShipOwner)
admin.site.register(ShipType)
admin.site.register(ShipAccesories)
admin.site.register(ShipImage)