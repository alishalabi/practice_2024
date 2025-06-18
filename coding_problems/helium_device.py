from django.db import models
# from api.models.device import Device
# from api.models.application import Application
# from api.models.tenant import Tenant

class  HeliumDevice(models.Model):
    id = models.CharField(max_length=50, primary_key = True)
    device_eui = models.CharField(max_length=75)
    application_eui = models.CharField(max_length=75)
    # device_uuid = ForeignKey(Device, on_delete=models.SET_NULL)
    # application_uuid = ForeignKey(Application, on_delete=models.SET_NULL)
    # tenant_uuid = ForeignKey(Tenant, on_delete=models.SET_NULL)
    # device_state
    to_update = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    inserted_at = models.DateTimeField()
    deleted_at = models.DateTimeField()
    last_seen = models.DateTimeField()
    last_activity_invoiced = models.DateTimeField()
    last_inactivity_invoiced = models.DateTimeField()
    totaldcs = models.BigIntegerField()
    # TODO: confirm
    # totaldcs_at =
    todaydcs = models.BigIntegerField()
