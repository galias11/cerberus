from django.contrib import admin
from FrontEnd.models import Caso, Documento, EntidadesDoc
from simple_history.admin import SimpleHistoryAdmin

admin.site.register(Caso, SimpleHistoryAdmin)
admin.site.register(Documento, SimpleHistoryAdmin)
admin.site.register(EntidadesDoc, SimpleHistoryAdmin)
