from flask import Flask, render_template, request, redirect, flash, session, url_for
from pymysql import STRING
import controlador_proveedor
import controlador_producto
import controlador_usuario
import controlador_venta
import controlador_evaluacion
from bd import obtener_conexion

app= Flask(__name__)

app.secret_key = 'your secret key'

@app.route("/")
def inicio():
    return render_template("login.html")

@app.route("/agregar_proveedor")
def formulario_agregar_proveedor():
    return render_template("agregar_proveedor.html")

@app.route("/guardar_proveedor", methods=["POST"])
def guardar_proveedor():
    nombre = request.form["nombre"]
    password = request.form["password"]
    controlador_proveedor.insertar_proveedor(nombre, password)
    # De cualquier modo, y si todo fue bien, redireccionar
    return redirect("/proveedor")

#@app.route("/")
@app.route("/proveedor")
def proveedor():
    proveedores = controlador_proveedor.obtener_proveedor()
    return render_template("proveedor.html", proveedores=proveedores)

@app.route("/eliminar_proveedor", methods=["POST"])
def eliminar_proveedor():
    controlador_proveedor.eliminar_proveedor(request.form["id"])
    return redirect("/proveedor")

@app.route("/formulario_editar_proveedor/<int:id>")
def editar_proveedor(id):
    # Obtener el proveedor por ID
    proveedor = controlador_proveedor.obtener_proveedor_por_id(id)
    return render_template("editar_proveedor.html", proveedor=proveedor)

@app.route("/actualizar_proveedor/<id>", methods=["POST"])
def actualizar_proveedor(id):
    id = request.form["id"]
    nombre = request.form["nombre"]
    password = request.form["password"]
    controlador_proveedor.actualizar_proveedor(nombre, password, id)
    productos = controlador_producto.obtener_producto_por_id_proveedor(id)
    proveedor = controlador_producto.obtener_proveedor_producto_id(id)
    return render_template("producto.html", productos=productos, proveedor=proveedor)



#producto

@app.route("/agregar_producto")
def formulario_agregar_producto():
    proveedores = controlador_producto.obtener_proveedor_producto()
    return render_template("agregar_producto.html", proveedores=proveedores)

@app.route("/agregar_producto_id/<id>")
def formulario_agregar_producto_id(id):
    proveedor = controlador_producto.obtener_proveedor_producto_id(id)
    productos = controlador_producto.obtener_producto_por_id_proveedor(id)
    return render_template("agregar_producto.html" , productos=productos,proveedor=proveedor)

@app.route("/guardar_producto", methods=["POST"])
def guardar_producto():
    nombre = request.form["nombre"]
    precio = request.form["precio"]
    id_proveedor = request.form["id_proveedor"]
    controlador_producto.insertar_producto(nombre, precio, id_proveedor)
    # De cualquier modo, y si todo fue bien, redireccionar
    return redirect("/producto")

@app.route("/guardar_producto_id/<id>", methods=["POST"])
def guardar_producto_id(id):
    nombre = request.form["nombre"]
    precio = request.form["precio"]
    id_proveedor = request.form["id_proveedor"]
    controlador_producto.insertar_producto(nombre, precio, id_proveedor)
    proveedor = controlador_producto.obtener_proveedor_producto_id(id)
    productos = controlador_producto.obtener_producto_por_id_proveedor(id)
    # De cualquier modo, y si todo fue bien, redireccionar
    return render_template("producto.html", productos=productos, proveedor=proveedor)

@app.route("/producto_id/<id>")
def producto_id(id):
    proveedor = controlador_producto.obtener_proveedor_producto_id(id)
    productos = controlador_producto.obtener_producto_por_id_proveedor(id)
    promedio = controlador_producto.promedio_evaluacion_producto(id)
    return render_template("producto.html", productos=productos, proveedor=proveedor, promedio=promedio)

@app.route("/eliminar_producto/<id>", methods=["POST"])
def eliminar_producto(id):
    controlador_producto.eliminar_producto(request.form["id"])
    productos = controlador_producto.obtener_producto_por_id_proveedor(id)
    proveedor = controlador_producto.obtener_proveedor_producto_id(id)
    return render_template("producto.html", productos=productos, proveedor=proveedor)

@app.route("/formulario_editar_producto/<int:id>")
def editar_producto(id):
    # Obtener el producto por ID
    proveedor = controlador_producto.obtener_producto_por_id(id)
    productos = controlador_producto.obtener_producto(id)
    return render_template("editar_producto.html", productos=productos, proveedor=proveedor)

@app.route("/actualizar_producto_id/<id_id>", methods=["POST"])
def actualizar_producto_id(id_id):
    id = request.form["id"]
    nombre = request.form["nombre"]
    precio = request.form["precio"]
    id_proveedor = request.form["id_proveedor"]
    controlador_producto.actualizar_producto(nombre, precio, id_proveedor, id)    
    proveedor = controlador_producto.obtener_proveedor_producto_id(id_id)
    productos = controlador_producto.obtener_producto_por_id_proveedor(id_id)  
    return render_template("producto.html", productos=productos, proveedor=proveedor)

#usuario

@app.route("/agregar_usuario")
def formulario_agregar_usuario():
    return render_template("agregar_usuario.html")

@app.route("/guardar_usuario", methods=["POST"])
def guardar_usuario():
    nombre = request.form["nombre"]
    apellido = request.form["apellido"]
    correo = request.form["correo"]
    password = request.form["password"]
    ciudad = request.form["ciudad"]
    controlador_usuario.insertar_usuario(nombre, apellido, correo, password, ciudad)
    # De cualquier modo, y si todo fue bien, redireccionar
    return redirect("/login")

#@app.route("/")
@app.route("/usuario")
def usuario():
    usuarios = controlador_usuario.obtener_usuario()
    return render_template("usuario.html", usuarios=usuarios)

@app.route("/eliminar_usuario", methods=["POST"])
def eliminar_usuario():
    controlador_usuario.eliminar_usuario(request.form["id"])
    return redirect("/usuario")

@app.route("/formulario_editar_usuario/<int:id>")
def editar_usuario(id):
    # Obtener el usuario por ID
    usuario = controlador_usuario.obtener_usuario_por_id(id)
    return render_template("editar_usuario.html", usuario=usuario)

@app.route("/actualizar_usuario/<id>", methods=["POST"])
def actualizar_usuario(id):
    id = request.form["id"]
    nombre = request.form["nombre"]
    apellido = request.form["apellido"]
    correo = request.form["correo"]
    password = request.form["password"]
    ciudad = request.form["ciudad"]
    controlador_usuario.actualizar_usuario(nombre, apellido, correo, password, ciudad, id)
    usuario = controlador_venta.obtener_usuario_por_id(id)
    ventas = controlador_venta.obtener_venta_por_id(id)
    return render_template("venta.html", ventas=ventas, usuario=usuario)

#venta

@app.route("/agregar_venta")
def formulario_agregar_venta():
    productos = controlador_venta.obtener_producto()
    return render_template("agregar_venta.html", productos=productos)

@app.route("/agregar_venta/<id>")
def formulario_agregar_venta_id(id):
    productos = controlador_venta.obtener_producto()
    usuario = controlador_venta.obtener_usuario_por_id(id)
    return render_template("agregar_venta.html", productos=productos, usuario=usuario)

@app.route("/guardar_venta", methods=["POST"])
def guardar_venta():
    id_producto = request.form["id_producto"]
    cantidad = request.form["cantidad"]
    id_usuario = request.form["id_usuario"]
    controlador_venta.insertar_venta(id_producto, cantidad, id_usuario)
    # De cualquier modo, y si todo fue bien, redireccionar
    return redirect("/venta")

@app.route("/guardar_venta_id/<id>", methods=["POST"])
def guardar_venta_id(id):
    id_producto = request.form["id_producto"]
    cantidad = request.form["cantidad"]
    id_usuario = request.form["id_usuario"]
    controlador_venta.insertar_venta(id_producto, cantidad, id_usuario)
    usuario = controlador_venta.obtener_usuario_por_id(id)
    ventas = controlador_venta.obtener_venta_por_id(id)
    # De cualquier modo, y si todo fue bien, redireccionar
    return render_template("venta.html", ventas=ventas, usuario=usuario)

#@app.route("/")
@app.route("/venta")
def venta():
    ventas = controlador_venta.obtener_venta()
    return render_template("venta.html", ventas=ventas)

#@app.route("/")
@app.route("/venta_id/<id>")
def venta_id(id):
    ventas = controlador_venta.obtener_venta_por_id(id)
    usuario = controlador_venta.obtener_usuario_por_id(id)
    return render_template("venta.html", ventas=ventas, usuario=usuario)

@app.route("/eliminar_venta", methods=["POST"])
def eliminar_venta():
    controlador_venta.eliminar_venta(request.form["id"])
    return redirect("/venta")

@app.route("/formulario_editar_venta/<int:id>")
def editar_venta(id):
    # Obtener el venta por ID
    venta = controlador_venta.obtener_venta_por_id_explicito(id)
    
    return render_template("editar_venta.html", venta=venta)

@app.route("/calificar_venta_id/<id_id>", methods=["POST"])
def calificar_venta_id(id_id):
    id = request.form["id"]
    calificacion = request.form["calificacion"]
    controlador_venta.calificar_venta(calificacion, id)
    ventas = controlador_venta.obtener_venta_por_id(id_id)
    usuario = controlador_venta.obtener_usuario_por_id(id_id)
    return render_template("venta.html", ventas=ventas, usuario=usuario)

#login_usuario

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/login", methods=['GET', "POST"])
def login_usuario():
    if request.method == 'POST' and 'correo' in request.form and 'password' in request.form:
        
        correo = request.form['correo']
        password = request.form['password']
        
        cursor = obtener_conexion().cursor()
        cursor.execute('SELECT * FROM usuario WHERE correo = %s AND password = %s', (correo, password,))
        account = cursor.fetchone()
        if account:
            session['loggedin'] = True
            session['id'] = account[0]
            session['username'] = account[1]

            return redirect(url_for('venta_id', id=account[0]))
        else:
            return render_template('agregar_usuario.html')
    

#login_proveedor
@app.route("/login_proveedor")
def login_pro():
    return render_template("login_proveedor.html")

@app.route("/login_proveedor", methods=['GET', "POST"])
def login_proveedor():
    if request.method == 'POST' and 'nombre' in request.form and 'password' in request.form:
        
        nombre = request.form['nombre']
        password = request.form['password']
        
        cursor = obtener_conexion().cursor()
        cursor.execute('SELECT * FROM proveedor WHERE nombre = %s AND password = %s', (nombre, password,))
        account = cursor.fetchone()
        if account:
            session['loggedin'] = True
            session['id'] = account[0]
            session['username'] = account[1]

            #return render_template('proveedor.html')
            return redirect(url_for('producto_id', id=account[0]))
        else:
            return render_template('login.html')

#evaluacion
@app.route("/evaluacion")
def evaluacion():
    evaluaciones = controlador_evaluacion.obtener_producto_por_id()
    return render_template("evaluacion.html", evaluaciones=evaluaciones)

#@app.route("/")
@app.route("/evaluacion_id/<id>")
def evaluacion_id(id):
    venta = controlador_evaluacion.obtener_producto_por_id(id)
    regreso = controlador_evaluacion.obtener_producto_por_id_delvolverme(id)
    promedio = controlador_evaluacion.promedio_evaluacion(id)
    return render_template("evaluacion.html", venta=venta, regreso=regreso, promedio=promedio)



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)