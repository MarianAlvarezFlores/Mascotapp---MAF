from django.urls import path
from .views import home, MascotaList, MascotaDetail, MascotaCreate, MascotaUpdate, MascotaDelete

app_name = "mascota"

urlpatterns = [
    path("", home, name="home"),  # Agregamos la ruta para la vista home
    path("mascota/lista/", MascotaList.as_view(), name="lista_mascotas"),
    path("mascota/detalle/<int:pk>/", MascotaDetail.as_view(), name="detalle_mascota"),
    path("mascota/crear/", MascotaCreate.as_view(), name="crear_mascota"),
    path("mascota/actualizar/<int:pk>/", MascotaUpdate.as_view(), name="actualizar_mascota"),
    path("mascota/eliminar/<int:pk>/", MascotaDelete.as_view(), name="eliminar_mascota"),
]
