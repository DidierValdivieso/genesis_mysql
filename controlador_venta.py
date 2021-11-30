from bd import obtener_conexion


def insertar_venta(id_producto, cantidad, id_usuario):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO venta(id_producto, cantidad, id_usuario) VALUES (%s, %s, %s)",
                       (id_producto, cantidad, id_usuario))
    conexion.commit()
    conexion.close()

def obtener_producto():
    conexion = obtener_conexion()
    productos = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id, nombre, precio FROM producto")
        productos = cursor.fetchall()
    conexion.close()
    return productos

def obtener_usuario_por_id(id):
    conexion = obtener_conexion()
    usuario = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT id,nombre,apellido FROM usuario where id = %s", (id,))
        usuario = cursor.fetchall()
    conexion.close()
    return usuario

def obtener_venta():
    conexion = obtener_conexion()
    ventas = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT V1.id, P1.nombre, V1.cantidad, FORMAT((P1.precio*V1.cantidad), 0) FROM venta V1 JOIN producto P1 JOIN usuario U1 ON V1.id_producto=P1.id and V1.id_usuario = U1.id")
        ventas = cursor.fetchall()
    conexion.close()
    return ventas


def eliminar_venta(id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM venta WHERE id = %s", (id,))
    conexion.commit()
    conexion.close()


def obtener_venta_por_id(id):
    conexion = obtener_conexion()
    venta = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT V1.id, P1.nombre, V1.cantidad, P1.precio*V1.cantidad FROM venta V1 JOIN producto P1 JOIN usuario U1 ON U1.id= %s AND V1.id_producto=P1.id and V1.id_usuario = U1.id", (id,))
        venta = cursor.fetchall()
    conexion.close()
    return venta

def actualizar_venta(id_producto, cantidad, id_usuario, id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE venta SET id_producto = %s, cantidad = %s, id_usuario = %s WHERE id = %s",
                       (id_producto, cantidad, id_usuario, id))
    conexion.commit()
    conexion.close()

def calificar_venta(calificacion, id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE venta SET calificacion = %s WHERE id = %s",
                       (calificacion, id))
    conexion.commit()
    conexion.close()

def obtener_venta_por_id_explicito(id):
    conexion = obtener_conexion()
    venta = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT * FROM venta WHERE id = %s", (id,))
        venta = cursor.fetchone()
    conexion.close()
    return venta

def obtener_usuario_por_id_explicito(id):
    conexion = obtener_conexion()
    usuario = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT id,nombre,apellido FROM usuario where id = %s", (id,))
        usuario = cursor.fetchone()
    conexion.close()
    return usuario

