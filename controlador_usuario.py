from bd import obtener_conexion


def insertar_usuario(nombre, apellido, correo, password, ciudad):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO usuario(nombre, apellido, correo, password, ciudad) VALUES (%s, %s, %s, %s, %s)",
                       (nombre, apellido, correo, password, ciudad))
    conexion.commit()
    conexion.close()

def obtener_usuario():
    conexion = obtener_conexion()
    usuarios = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT * FROM usuario")
        usuarios = cursor.fetchall()
    conexion.close()
    return usuarios


def eliminar_usuario(id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM usuario WHERE id = %s", (id,))
    conexion.commit()
    conexion.close()


def obtener_usuario_por_id(id):
    conexion = obtener_conexion()
    usuario = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT * FROM usuario WHERE id = %s", (id,))
        usuario = cursor.fetchone()
    conexion.close()
    return usuario


def actualizar_usuario(nombre, apellido, correo, password, ciudad, id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE usuario SET nombre = %s, apellido = %s, correo = %s, password = %s, ciudad = %s WHERE id = %s",
                       (nombre, apellido, correo, password, ciudad, id))
    conexion.commit()
    conexion.close()