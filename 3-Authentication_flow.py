'''
Ruta para iniciar sesión
Lo que obtendremos como resultado al final de este módulo es 
la protección de determinadas rutas de nuestra aplicación 
para las cuales solo se podrá acceder mediante el inicio de 
sesión del usuario. Para esto crearemos una ruta que utilice 
el método POST donde se solicitarán los datos como email y 
contraseña.

Creación y envío de token
Luego de que el usuario ingrese sus datos de sesión correctos 
este obtendrá un token que le servirá para enviarlo al momento 
de hacer una petición a una ruta protegida.

Validación de token
Al momento de que nuestra API reciba la petición del usuario, 
comprobará que este le haya enviado el token y validará si es 
correcto y le pertenece. Finalmente se le dará acceso a la 
ruta que está solicitando.

En la siguiente clase empezaremos con la creación de una 
función que nos va a permitir generar tokens usando la 
librería pyjwt.

* PyJWT: (Python JSON Web Token) es una biblioteca de Python que 
se utiliza para codificar y decodificar tokens JWT 
(JSON Web Token). Un token JWT es un objeto de seguridad que 
se utiliza para autenticar a los usuarios en aplicaciones web 
y móviles. Los tokens JWT se emiten por un servidor de 
autenticación y luego se envían al cliente, que los utiliza 
para demostrar su identidad al acceder a recursos protegidos 
en el servidor
'''