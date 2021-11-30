from bd import obtener_conexion


def insertar_proveedor(nombre, password):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO proveedor(nombre, password) VALUES (%s, %s)",
                       (nombre, password))
    conexion.commit()
    conexion.close()


def obtener_proveedor():
    conexion = obtener_conexion()
    proveedores = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id, nombre, password FROM proveedor")
        proveedores = cursor.fetchall()
    conexion.close()
    return proveedores


def eliminar_proveedor(id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM proveedor WHERE id = %s", (id,))
    conexion.commit()
    conexion.close()


def obtener_proveedor_por_id(id):
    conexion = obtener_conexion()
    proveedor = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT id, nombre, password FROM proveedor WHERE id = %s", (id,))
        proveedor = cursor.fetchone()
    conexion.close()
    return proveedor


def actualizar_proveedor(nombre, password, id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE proveedor SET nombre = %s, password = %s WHERE id = %s",
                       (nombre, password, id))
    conexion.commit()
    conexion.close()