from bd import obtener_conexion


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

#enviaremos el id del producto para ver todas las compras de ese producto
def obtener_producto_por_id(id):
    conexion = obtener_conexion()
    venta = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT V.id, P.nombre, V.cantidad, U.nombre, V.calificacion FROM venta V JOIN producto P JOIN usuario U ON V.id_producto= %s AND V.id_producto=P.id AND V.id_usuario=U.id", (id,))
        venta = cursor.fetchall()
    conexion.close()
    return venta

#promedio
def promedio_evaluacion(id):
    conexion = obtener_conexion()
    promedio = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT id_producto, AVG(calificacion) FROM venta WHERE id_producto = %s", (id,))
        promedio = cursor.fetchone()
    conexion.close()
    return promedio

#enviaremos el id del producto para ver devolvernos
def obtener_producto_por_id_delvolverme(id):
    conexion = obtener_conexion()
    regreso = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT P.id, P.nombre FROM venta V JOIN proveedor P JOIN producto P1 ON V.id_producto= %s AND P.id=P1.id_proveedor AND V.id_producto= P1.id", (id,))
        regreso = cursor.fetchone()
    conexion.close()
    return regreso