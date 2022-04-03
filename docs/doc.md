# Mi transporte 

## Requerimientos Base
Fases del proyecto 
Las fases principales son las siguientes:
•	Registro de usuarios que ofrecen el servicio de transporte.
•	Registro de usuarios que adquieren el servicio de transporte. 
•	Registro de información de servicios turísticos  ofrecidos.
•	Realizar lista de servicios que ofrece cada empresa.
•	Registró de reservas.
•	Modalidad de pagos.
•	Geo localización.
•	Desarrollo de sistema de calificación para el servicio turístico.
•	Creación de la base de datos para el sistema de servicios turísticos, validación de datos y utilización de contenidos.
•	Elaboración de Administración de datos del servicio turístico.



Ejemplo 
Mi nombre es Juan Viajero, tengo mi empresa de viajes que ofrece los servicio de turismo a Luribay para catar viñedos,
tambien tengo el servicio de viaje  a excurcion a puno, 

tenemos salidas a luribay  los fines de semana , partimos sabado en la mañana a las 8 am y regresamos domingo a horas 8pm de regreso a  la ciudad de donde se partió el costo es 25 bolivianos, realice su reserva y cancele por medios digitales

Salidas a Puno




Usuario{
    nombre
    apellido
    fecha de nacimiento
    tipo de usuario
}

vehiculo{
    conductor:jonas
    propietario:
    movilidad:minibus
    cantidad:
    placa:
    foto:
}

Lugar {
    nombre:
    ubicacion_gps:
    direccion:
}

servicio turistico{
    nombre_del_viaje:
    origen:
    destino:
    tiempo de viaje:
    caracteristicas:
    costo por persona
}

empresa{
    nombre:
    representant:[]
    Servicio_turisticos:[]
}

viaje{

    tipo: [solo_ida,ida_yuelta]

    fecha y hora de partida
    fecha y hora de llegada al destino

    duracion_del_viaje

    servicion turistico
    transporte

    cantidad maxima
    cupos disponibles
    cupos llenos

    fecha y hora de partida de retorno
    fecha y hora de llegada al origen  
}


Asientos{
    viaje
    transporte
    nro_asiento:    
    usuario
    estado: comprado, reservado,disponible
}


Tipos de Usuarios 
Super-Usuario 
	Validar Usuarios
	Validad la información del servicio turístico.
	Registro de servicios turísticos.
	Habilita la información
	Listar lugares turísticos.
	Actualizar información
Usuario Gerencial
•	Se registra 
•	Sube información sobre el servicio de transporte que ofrece como:
•	tipo de trasporte (aéreo, marítimo y terrestre)
•	sube rutas de destino 
•	sube fotos
•	utiliza geo localización
•	costos
•	lugares turísticos 
•	promociones, paquetes y ofertas
•	horarios de servicios actualizados
•	 duración o tiempo de viaje a distintos lugares
•	Nombre de la empresa a la que pertenece.
•	Publica su información
•	Calificación, comentarios y sugerencias. 

Usuario Cliente 
•	Busca información
•	Escoge lugares
•	Registra sus datos
•	Realiza reservas mediante pagos en línea.
•	Utiliza geo localización
•	Conectarse con la empresa de servicios
•	Calificación, comentarios y sugerencias.

