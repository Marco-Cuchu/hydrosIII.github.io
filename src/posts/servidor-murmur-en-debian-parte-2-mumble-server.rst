.. title: Servidor murmur en Debian parte 2 (mumble-server)
.. slug: servidor-murmur-en-debian-parte-2-mumble-server
.. date: 2015-01-26 00:29:53 UTC-06:00
.. tags: Debian
.. link: 
.. description: 
.. type: text

Esta es la segunda parte del tutorial para correr el un servidor murmur 
en Debian.  Aunque el tutorial anterior delineaba lo básico. Cuando 
intenté cambiar algunas configuraciones empezé a tener problemas, por lo 
que escribo esto a manera de notas, y por si alguien lo necesita 
consultar. Trata sobre la configuración de los certificados SSL para que 
nuestro servidor sea reconocido como seguro.

Nota: En este artículo se utilizará mumble-server y murmurd como 
sinónimos ya que son lo mismo pero por la convención de los nombres de 
Debian tienen dos nombres diferentes, espero que esto no cause 
confusión.

.. TEASER_END

Antes que nada este tutorial es para lograr que murmur funcione con un 
certificado SSL oficial proveido por una autoridad certificadora, este 
es solo necesario si vamos a abrir nuestro servidor a otros usuarios mas 
que nuestro grupo de amigos, y estos desconfian del letrero que aparece 
diciendo que el certificado no es de confianza. Si esta no es tu 
situación lo mejor es quedarse con la configuración del artículo 
anterior.

En primer lugar hay que configurar un poco más nuestro servidor murmur, 
por lo que en Debian una vez instalado, escribimos::

	dpkg-reconfigure mumble-server

Con lo que aparecerán algunas opciones, elige como te sea conveniente, 
lo interesante es que viene la opción de definir una contraseña para el 
superusuario del servidor. Con esta cuenta se pueden manejar algunas 
cosas dentro del server, con respecto a los demás usuarios.

Despues de esto, pasamos a la configuración de los certificados SSL. 
Primero que nada es necesario comprar u obtener uno de un proveedor de 
certificados. Hasta ahora el único que conozco que otorga certificados 
gratuitos es StartSSL, para un único dominio. Una vez obtenidos 
uno de estos, se debe colocar su dirección en el archivo de configuración /etc/mumble-server.ini quedando este 
mas o menos así ::

	
	sslCert=/etc/ssl/private/mi-certificado.crt
	sslKey=/etc/ssl/private/millave.key


El problema viene un poco después ya que el proceso tiene varios bugs, 
en primer lugar, el usuario en el que se inicia el servidor murmurd, es 
el usuario murmur-server que no tiene permisos para leer esta carpeta. 
Una solucion fácil sería cambiar los permisos de los certificados a 777. 
Desde luego esto es muy inseguro. Por suerte este es un bug reportado: 

https://bugs.launchpad.net/ubuntu/+source/mumble/+bug/1017301

Según el anterior post, la solución pasa por poner la línea::


	user=root

en el archivo /etc/default/murmur-server. Esto hará que en un principio, 
el servidor murmur, pueda leer los certificados y luego cambie al 
usuario murmur-server, descrito en el murmur-server.ini. Si esto no se 
hace así murmur-server crea unos certificados autofirmados que pueden 
dar el típico mensaje de error.

El siguiente paso está descrito en la wiki de murmur, por alguna razón 
el servidor murmur, transmite el certificado imcompleto lo que hace que 
los clientes mumble se niegen a conectarse al servidor. La solución 
nuevamente pasa por buscar un poco. Consta en unir el certificado 
del proveedor con el certificado de tu dominio. Esto también se recomienda
para cualquier página web con el fin de evitar errores con varios 
navegadores. He aqui las instrucciones tomadas de la wiki de mumble::

	wget --no-check-certificate http://www.startssl.com/certs/ca.pem
	cat ca.pem >> mi-certificado.crt
	rm ca.pem

Obteniendo un certificado concatenado, en mi caso yo lo renombré a 
micertificado-concatenado.crt, por cuestión de orden, pero si lo haces 
tendrás que modificar el archivo de configuración nuevamente.

Al parecer ya casi esta listo, todo, ¿no? Pues no ahora resulta que 
es necesario borrar, todos los certificados autofirmados que mumble-server 
creó cuando se inició por primera vez. Para esto hay que reiniciar el 
servidor murmur haciendo que olvide los certificados anteriores, primero 
vamos a detener el servidor murmur con::

	service mumble-server stop

Para luego correr como root el siguiente comando::

	murmurd -wipessl --ini /etc/mumble-server.ini

Lo que quitará los certificados anteriores de la base de datos. Antes de 
iniciar el servidor en forma, vamos a matar ese proceso con::

	killall murmurd

Para después iniciarlo correctamente con::

	service mumble-server start

Ahora ya no debería de haber problemas con el certificado SSL.
Si continua habiendo problemas, se puede modificar el script init, para 
que siempre use la opción -wipessl, pero espero que esto no sea 
necesario.


En conclusión me parece demasiado engorroso este proceso, no entiendo 
por que no ha sido arreglado el bug reportado en Ubuntu. Debian 
empaqueta mumble-server de manera extraña y no lo hace de manera clara, 
ya que la mayoría de sus paquetes es sólo instalar y usar. Lo bueno es
que hay bastante documentación en la wiki de mumble, pero esto debería
de ser más claro.Quizá compilar el servidor desde fuentes, de menor errores,
quien sabe.

Finalmente, a disfrutar de mumble.



Fuentes:

http://wiki.mumble.info/wiki/Obtaining_a_StartCom_Murmur_Certificate
https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=529413
https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-mumble-server-murmur-on-ubuntu-14-04
https://bugs.launchpad.net/ubuntu/+source/mumble/+bug/1017301

