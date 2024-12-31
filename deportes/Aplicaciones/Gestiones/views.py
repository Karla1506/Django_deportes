# Create your views here.
from datetime import timedelta
from django.shortcuts import render, redirect, get_object_or_404
from .models import Participante, Evento, Actividad, Inscripcion, RegistroActividad
from django.contrib import messages

def inicio(request):
    return render(request,'inicio.html')

#---------------------------------------- PARTICIPANTES ----------------------------------------
# Listado de Participantes
def listadoParticipantes(request):
    participantes = Participante.objects.all()
    return render(request, 'listadoParticipantes.html', {'participantes': participantes})

# Crear nuevo Participante
def nuevoParticipante(request):
    return render(request, 'nuevoParticipante.html')

# Guardar Participante
def guardarParticipante(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        email = request.POST['email']
        telefono = request.POST.get('telefono', '')
        fecha_nacimiento = request.POST['fecha_nacimiento']
        direccion = request.POST.get('direccion', '')

        participante = Participante.objects.create(
            nombre=nombre,
            apellido=apellido,
            email=email,
            telefono=telefono,
            fecha_nacimiento=fecha_nacimiento,
            direccion=direccion
        )
        messages.success(request, "Participante guardado exitosamente.")
        return redirect('/listadoParticipantes')
    else:
        messages.error(request, "Error al guardar el participante.")
        return redirect('/nuevoParticipante')

# Eliminar Participante
def eliminarParticipante(request, participante_id):
    participante = get_object_or_404(Participante, id=participante_id)
    participante.delete()
    messages.success(request, "Participante eliminado exitosamente.")
    return redirect('/listadoParticipantes')


# Editar un participante
def editarParticipante(request, participante_id):
    # Buscar el participante por ID
    participante = get_object_or_404(Participante, id=participante_id)
    # Renderizar la plantilla con los datos del participante
    return render(request, 'editarParticipantes.html', {'participante': participante})

# Procesar la edición de un participante
def procesarEdicionParticipantes(request):
    # Obtener el participante por ID
    participante = Participante.objects.get(id=request.POST['id_participante'])

    # Actualizar los campos del participante
    participante.nombre = request.POST['txt_nombre']
    participante.apellido = request.POST['txt_apellido']
    participante.fecha_nacimiento = request.POST['txt_fecha_nacimiento']
    participante.telefono = request.POST['txt_telefono']
    participante.email = request.POST['txt_email']
    participante.direccion = request.POST['txt_direccion']

    # Guardar los cambios en la base de datos
    participante.save()

    # Mostrar mensaje de éxito
    messages.success(request, "Participante actualizado con éxito.")

    # Redirigir al listado de participantes
    return redirect('/listadoParticipantes')


#---------------------------------------- EVENTOS ----------------------------------------
# Listado de Eventos
def listadoEventos(request):
    eventos = Evento.objects.all()
    return render(request, 'listadoEventos.html', {'eventos': eventos})

# Crear nuevo Evento
def nuevoEvento(request):
    return render(request, 'nuevoEvento.html')

# Guardar Evento
def guardarEvento(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        descripcion = request.POST['descripcion']
        fecha_inicio = request.POST['fecha_inicio']
        fecha_fin = request.POST['fecha_fin']
        ubicacion = request.POST['ubicacion']
        organizador = request.POST['organizador']
        cupo_maximo = request.POST['cupo_maximo']

        evento = Evento.objects.create(
            nombre=nombre,
            descripcion=descripcion,
            fecha_inicio=fecha_inicio,
            fecha_fin=fecha_fin,
            ubicacion=ubicacion,
            organizador=organizador,
            cupo_maximo=cupo_maximo
        )
        messages.success(request, "Evento guardado exitosamente.")
        return redirect('/listadoEventos')
    else:
        messages.error(request, "Error al guardar el evento.")
        return redirect('/nuevoEvento')

# Eliminar Evento
def eliminarEvento(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)
    evento.delete()
    messages.success(request, "Evento eliminado exitosamente.")
    return redirect('/listadoEventos')

# Editar un evento
def editarEvento(request, evento_id):
    # Buscar el evento por ID
    evento = get_object_or_404(Evento, id=evento_id)
    
    # Renderizar la plantilla con los datos del evento
    return render(request, 'editarEventos.html', {'evento': evento})

# Procesar la edición de un evento
def procesarEdicionEvento(request):
    # Obtener el evento por ID
    evento = Evento.objects.get(id=request.POST['id_evento'])

    # Actualizar los campos del evento
    evento.nombre = request.POST['txt_nombre']
    evento.descripcion = request.POST['txt_descripcion']
    evento.fecha_inicio = request.POST['txt_fecha_inicio']
    evento.fecha_fin = request.POST['txt_fecha_fin']
    evento.ubicacion = request.POST['txt_ubicacion']
    evento.organizador = request.POST['txt_organizador']
    evento.cupo_maximo = request.POST['txt_cupo_maximo']

    # Guardar los cambios en la base de datos
    evento.save()

    # Mostrar mensaje de éxito
    messages.success(request, "Evento actualizado con éxito.")

    # Redirigir al listado de eventos
    return redirect('/listadoEventos')

#---------------------------------------- ACTIVIDADES ----------------------------------------
# Listado de Actividades
def listadoActividades(request):
    actividades = Actividad.objects.all()
    return render(request, 'listadoActividades.html', {'actividades': actividades})

# Crear nueva Actividad
def nuevaActividad(request):
    eventos = Evento.objects.all()
    return render(request, 'nuevaActividad.html', {'eventos': eventos})

# Guardar Actividad
def guardarActividad(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        descripcion = request.POST['descripcion']
        duracion_str = request.POST['duracion']  # La duración llega como cadena de texto
        evento_id = request.POST['evento']
        nivel_dificultad = request.POST['nivel_dificultad']
        equipo_necesario = request.POST['equipo_necesario']

        # Convertir la duración de cadena a timedelta (suponiendo formato "HH:MM:SS")
        try:
            horas, minutos, segundos = map(int, duracion_str.split(":"))
            duracion = timedelta(hours=horas, minutes=minutos, seconds=segundos)
        except ValueError:
            messages.error(request, "Formato de duración inválido.")
            return redirect('/nuevaActividad')

        evento = get_object_or_404(Evento, id=evento_id)
        actividad = Actividad.objects.create(
            nombre=nombre,
            descripcion=descripcion,
            duracion=duracion,
            evento=evento,
            nivel_dificultad=nivel_dificultad,
            equipo_necesario=equipo_necesario
        )
        messages.success(request, "Actividad guardada exitosamente.")
        return redirect('/listadoActividades')
    else:
        messages.error(request, "Error al guardar la actividad.")
        return redirect('/nuevaActividad')

# Eliminar Actividad
def eliminarActividad(request, actividad_id):
    actividad = get_object_or_404(Actividad, id=actividad_id)
    actividad.delete()
    messages.success(request, "Actividad eliminada exitosamente.")
    return redirect('/listadoActividades')

# Editar Actividad
def editarActividad(request, actividad_id):
    # Buscar la actividad por ID
    actividad = get_object_or_404(Actividad, id=actividad_id)
    
    # Renderizar la plantilla con los datos de la actividad
    return render(request, 'editarActividades.html', {'actividad': actividad})

# Procesar Edición de Actividad
def procesarEdicionActividad(request):
    # Obtener la actividad por ID
    actividad = Actividad.objects.get(id=request.POST['id_actividad'])

    # Actualizar los campos de la actividad
    actividad.nombre = request.POST['txt_nombre']
    actividad.descripcion = request.POST['txt_descripcion']

    # Convertir la duración de cadena a timedelta
    duracion_str = request.POST['txt_duracion']
    try:
        horas, minutos, segundos = map(int, duracion_str.split(":"))
        duracion = timedelta(hours=horas, minutes=minutos, seconds=segundos)
    except ValueError:
        messages.error(request, "Formato de duración inválido.")
        return redirect(f'/editarActividad/{actividad.id}/')

    actividad.duracion = duracion
    actividad.nivel_dificultad = request.POST['txt_nivel_dificultad']
    actividad.equipo_necesario = request.POST['txt_equipo_necesario']

    # Guardar los cambios en la base de datos
    actividad.save()

    # Mostrar mensaje de éxito
    messages.success(request, "Actividad actualizada con éxito.")

    # Redirigir al listado de actividades
    return redirect('/listadoActividades')




#---------------------------------------- INSCRIPCIONES ----------------------------------------
# Listado de Inscripciones
def listadoInscripciones(request):
    inscripciones = Inscripcion.objects.all()
    return render(request, 'listadoInscripciones.html', {'inscripciones': inscripciones})

# Crear nueva Inscripción
def nuevaInscripcion(request):
    participantes = Participante.objects.all()
    eventos = Evento.objects.all()
    return render(request, 'nuevaInscripcion.html', {'participantes': participantes, 'eventos': eventos})

# Guardar Inscripción
def guardarInscripcion(request):
    if request.method == 'POST':
        participante_id = request.POST['participante']
        evento_id = request.POST['evento']
        estado = request.POST['estado']
        comentarios = request.POST.get('comentarios', '')

        participante = get_object_or_404(Participante, id=participante_id)
        evento = get_object_or_404(Evento, id=evento_id)
        
        inscripcion = Inscripcion.objects.create(
            participante=participante,
            evento=evento,
            estado=estado,
            comentarios=comentarios
        )
        messages.success(request, "Inscripción guardada exitosamente.")
        return redirect('/listadoInscripciones')
    else:
        messages.error(request, "Error al guardar la inscripción.")
        return redirect('/nuevaInscripcion')

# Eliminar Inscripción
def eliminarInscripcion(request, inscripcion_id):
    inscripcion = get_object_or_404(Inscripcion, id=inscripcion_id)
    inscripcion.delete()
    messages.success(request, "Inscripción eliminada exitosamente.")
    return redirect('/listadoInscripciones')

# Editar Inscripción
def editarInscripcion(request, inscripcion_id):
    # Buscar la inscripción por ID
    inscripcion = get_object_or_404(Inscripcion, id=inscripcion_id)
    
    # Renderizar la plantilla con los datos de la inscripción
    return render(request, 'editarInscripciones.html', {'inscripcion': inscripcion})

# Procesar Edición de Inscripción
def procesarEdicionInscripcion(request):
    # Obtener la inscripción por ID
    inscripcion = Inscripcion.objects.get(id=request.POST['id_inscripcion'])

    # Actualizar los campos de la inscripción
    inscripcion.estado = request.POST['txt_estado']
    inscripcion.comentarios = request.POST['txt_comentarios']

    # Guardar los cambios en la base de datos
    inscripcion.save()

    # Mostrar mensaje de éxito
    messages.success(request, "Inscripción actualizada con éxito.")

    # Redirigir al listado de inscripciones
    return redirect('/listadoInscripciones')

#---------------------------------------- REGISTRO DE ACTIVIDAD ----------------------------------------
# Listado de Registros de Actividades
def listadoRegistrosActividad(request):
    registros = RegistroActividad.objects.all()
    return render(request, 'listadoRegistro.html', {'registros': registros})

# Crear nuevo Registro de Actividad
def nuevoRegistroActividad(request):
    participantes = Participante.objects.all()
    actividades = Actividad.objects.all()
    return render(request, 'nuevoRegistro.html', {'participantes': participantes, 'actividades': actividades})

# Guardar Registro de Actividad
def guardarRegistro(request):
    if request.method == 'POST':
        participante_id = request.POST['participante']
        actividad_id = request.POST['actividad']
        resultado = request.POST.get('resultado', '')
        puntuacion = request.POST.get('puntuacion', 0.0)
        observaciones = request.POST.get('observaciones', '')
        fecha_realizacion = request.POST['fecha_realizacion']

        participante = get_object_or_404(Participante, id=participante_id)
        actividad = get_object_or_404(Actividad, id=actividad_id)

        registro = RegistroActividad.objects.create(
            participante=participante,
            actividad=actividad,
            resultado=resultado,
            puntuacion=puntuacion,
            observaciones=observaciones,
            fecha_realizacion=fecha_realizacion
        )
        messages.success(request, "Registro de actividad guardado exitosamente.")
        return redirect('/listadoRegistro')
    else:
        messages.error(request, "Error al guardar el registro de actividad.")
        return redirect('/nuevoRegistro')

# Eliminar Registro de Actividad
def eliminarRegistro(request, registro_id):
    registro = get_object_or_404(RegistroActividad, id=registro_id)
    registro.delete()
    messages.success(request, "Registro de actividad eliminado exitosamente.")
    return redirect('/listadoRegistro')

# Editar Registro de Actividad
def editarRegistroActividad(request, registro_id):
    # Buscar el registro de actividad por ID
    registro = get_object_or_404(RegistroActividad, id=registro_id)
    
    # Renderizar la plantilla con los datos del registro de actividad
    return render(request, 'editarRegistro.html', {'registro': registro})

# Procesar Edición de Registro de Actividad
def procesarEdicionRegistroActividad(request):
    # Obtener el registro de actividad por ID
    try:
        registro = RegistroActividad.objects.get(id=request.POST['id_registro'])
    except RegistroActividad.DoesNotExist:
        messages.error(request, "El registro de actividad no existe.")
        return redirect('/listadoRegistro/')
    
    # Actualizar los campos del registro de actividad
    registro.resultado = request.POST['txt_resultado']
    registro.puntuacion = request.POST['txt_puntuacion']
    registro.observaciones = request.POST['txt_observaciones']
    
    # Validar y actualizar la fecha de realización si existe
    fecha_realizacion = request.POST.get('txt_fecha_realizacion', None)
    if fecha_realizacion:
        try:
            registro.fecha_realizacion = fecha_realizacion
        except ValueError:
            messages.error(request, "Formato de fecha de realización inválido.")
            return redirect(f'/editarRegistroActividad/{registro.id}/')

    # Guardar los cambios en la base de datos
    registro.save()

    # Mostrar mensaje de éxito
    messages.success(request, "Registro de actividad actualizado con éxito.")

    # Redirigir al listado de registros de actividad
    return redirect('/listadoRegistro')

