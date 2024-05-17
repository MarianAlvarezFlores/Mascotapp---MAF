from django.urls import path
from .views import home, MascotaList, MascotaDetail, MascotaCreate, MascotaUpdate, MascotaDelete

app_name = "mascota"

urlpatterns = [
    path("", home, name="home"),  # Ruta para la vista home
    path("lista/", MascotaList.as_view(), name="lista_mascotas"),
    path("detalle/<int:pk>/", MascotaDetail.as_view(), name="detalle_mascota"),
    path("crear/", MascotaCreate.as_view(), name="crear_mascota"),
    path("actualizar/<int:pk>/", MascotaUpdate.as_view(), name="actualizar_mascota"),
    path("eliminar/<int:pk>/", MascotaDelete.as_view(), name="eliminar_mascota"),
]
