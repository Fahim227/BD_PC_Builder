
from django.contrib import admin
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bdpcbuilderapi/', include('pc_builder.urls')),
    path('startech/', include('startech.urls')),
     path('techlandbd/', include('techland.urls'))
]
