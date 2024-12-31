from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio),  # Página de inicio

    # Participantes
    path('nuevoParticipante/', views.nuevoParticipante),  # Formulario para agregar participantes
    path('listadoParticipantes/', views.listadoParticipantes),  # Página con el listado de participantes
    path('guardarParticipante/', views.guardarParticipante),  # Guardar participantes
    path('eliminarParticipante/<int:participante_id>', views.eliminarParticipante),  # Eliminar participantes
    path('editarParticipante/<int:participante_id>', views.editarParticipante),  # Editar participante
    path('procesarEdicionParticipantes/', views.procesarEdicionParticipantes),  # Procesar la edición de participante

    # Eventos
    path('nuevoEvento/', views.nuevoEvento),  # Formulario para agregar eventos
    path('listadoEventos/', views.listadoEventos),  # Listado de eventos
    path('guardarEvento/', views.guardarEvento),  # Guardar evento
    path('eliminarEvento/<int:evento_id>', views.eliminarEvento),  # Eliminar evento
    path('editarEvento/<int:evento_id>/', views.editarEvento, name='editarEvento'),
    path('procesarEdicionEvento/', views.procesarEdicionEvento, name='procesarEdicionEvento'),

    # Actividades
    path('nuevaActividad/', views.nuevaActividad),  # Formulario para agregar actividades
    path('listadoActividades/', views.listadoActividades),  # Listado de actividades
    path('guardarActividad/', views.guardarActividad),  # Guardar actividad
    path('eliminarActividad/<int:actividad_id>', views.eliminarActividad),  # Eliminar actividad
    path('editarActividad/<int:actividad_id>/', views.editarActividad, name='editarActividad'),
    path('procesarEdicionActividad/', views.procesarEdicionActividad, name='procesarEdicionActividad'),

    # Inscripciones
    path('nuevaInscripcion/', views.nuevaInscripcion),  # Formulario para inscribir participantes
    path('listadoInscripciones/', views.listadoInscripciones),  # Listado de inscripciones
    path('guardarInscripcion/', views.guardarInscripcion),  # Guardar inscripción
    path('eliminarInscripcion/<int:inscripcion_id>', views.eliminarInscripcion),  # Eliminar inscripción
    path('editarInscripcion/<int:inscripcion_id>/', views.editarInscripcion, name='editarInscripcion'),
    path('procesarEdicionInscripcion/', views.procesarEdicionInscripcion, name='procesarEdicionInscripcion'),

    # Registro de Actividades
    path('nuevoRegistro/', views.nuevoRegistroActividad),  # Formulario para registrar actividad
    path('listadoRegistro/', views.listadoRegistrosActividad),  # Listado de registros de actividad
    path('guardarRegistro/', views.guardarRegistro),  # Guardar registro de actividad
    path('eliminarRegistro/<int:registro_id>', views.eliminarRegistro),  # Eliminar registro de actividad
    path('editarRegistroActividad/<int:registro_id>/', views.editarRegistroActividad, name='editarRegistroActividad'),
    path('procesarEdicionRegistroActividad/', views.procesarEdicionRegistroActividad, name='procesarEdicionRegistroActividad'),
]
