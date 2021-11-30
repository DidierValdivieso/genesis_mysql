from bd import obtener_conexion


def insertar_producto(nombre, precio, id_proveedor):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO producto(nombre, precio, id_proveedor) VALUES (%s, %s, %s)",
                       (nombre, precio, id_proveedor))
    conexion.commit()
    conexion.close()

def obtener_proveedor_producto():
    conexion = obtener_conexion()
    proveedores = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id, nombre FROM proveedor")
        proveedores = cursor.fetchall()
    conexion.close()
    return proveedores

def obtener_proveedor_producto_id(id):
    conexion = obtener_conexion()
    proveedores = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id, nombre FROM proveedor WHERE id = %s", (id,))
        proveedores = cursor.fetchall()
    conexion.close()
    return proveedores

def obtener_producto(id):
    conexion = obtener_conexion()
    productos = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id,nombre,precio FROM producto where id= %s", (id,))
        productos = cursor.fetchone()
    conexion.close()
    return productos


def eliminar_producto(id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM producto WHERE id = %s", (id,))
    conexion.commit()
    conexion.close()


def obtener_producto_por_id(id):
    conexion = obtener_conexion()
    producto = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT E1.id, E1.nombre, E2.id, E2.nombre, E2.precio FROM proveedor E1 JOIN producto E2 ON E2.id= %s AND E2.id_proveedor=E1.id", (id,))
        producto = cursor.fetchall()
    conexion.close()
    return producto

def obtener_producto_por_id_proveedor(id):
    conexion = obtener_conexion()
    productos = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT E2.id, E2.nombre, E2.precio, E1.nombre, E1.id FROM proveedor E1 JOIN producto E2 ON E1.id= %s AND E2.id_proveedor=E1.id", (id,))
        productos = cursor.fetchall()
    conexion.close()
    return productos

def actualizar_producto(nombre, precio, id_proveedor, id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE producto SET nombre = %s, precio = %s, id_proveedor = %s WHERE id = %s",
                       (nombre, precio, id_proveedor, id))
    conexion.commit()
    conexion.close()

#promedio
def promedio_evaluacion_producto(id):
    conexion = obtener_conexion()
    promedio = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT truncate(AVG(V.calificacion),2), P1.nombre FROM venta V JOIN proveedor P JOIN producto P1 ON P.id= %s AND P.id=P1.id_proveedor AND P1.id=V.id_producto GROUP BY P1.id", (id,))
        promedio = cursor.fetchall()
    conexion.close()
    return promedio