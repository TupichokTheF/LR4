from django.contrib import admin

from .models import Incidents, CyberAttack, SourceIncident, StatusIncidents

admin.site.register([Incidents, CyberAttack, SourceIncident, StatusIncidents])
