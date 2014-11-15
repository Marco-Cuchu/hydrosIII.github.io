.. title: Administrando lemonpos con phpmyadmin.
.. slug: administrando-lemonpos-con-phpmyadmin
.. date: 2014-11-13 23:52:35 UTC-06:00
.. tags: lemonpos 
.. link: 
.. description: 
.. type: text

Lemonpos es un buen programa para poner una terminal de punto de venta y 
está hecho con software libre. Sin embargo el administrador squeeze, 
aunque es útil muchas veces no tiene tantas opciones. Una opción para 
superar esta limitación es usar un administrador de base de datos y que 
mejor que phpmyadmin, un administrador de base de datos ligero y muy 
fácil de usar.


Nota: Puedes encontrar el post de instalación de lemonpos :doc:`aquí 
<revision-e-instalacion-de-lemonpos>`.

Nota: Los siguientes comandos se tienen que hacer como root.

Para empezar este tutorial está enfocado a Debian  y derivados ya que en 
otras distros, phpmyadmin requiere un poco de configuración extra. Lo 
primero es instalar apache2 y phpmyadmin. Se pueden instalar otros 
servidores web, pero apache resulta perfecto para el caso ya que 
funciona "out of the box" ::

	apt-get install apache2 phpmyadmin

Ahora se configurara todo y tendremos apache funcionando en el puerto 80 
de nuestra maquina, en un navegador comprobamos que esto sea cierto, 
vamos a la dirección::

	http://127.0.0.1

o::

	http://localhost

ahora debe aparecer algo así como::
	
	It works !


Si no aparece hay que revisar si hubo algún error en a instalación de 
apache.

Una vez configurado, sólo hay que apuntar a apache a phpmyadmin. Yo lo 
hago de manera burda pero eficiente::

	rm -r /var/www
	ln -s /usr/share/phpmyadmin /var/www

y listo. Si nos vamos al navegador otra vez y apuntamos a 127.0.0.1, nos 
encontraremos con phpmyadmin. El usuario para entrar es root y la 
contraseña, la contraseña de administrador de la base de datos, osea la 
que preguntó debian a la hora de instalar mysql.
Una vez dentro de phpmyadmin podemos ver la base de datos de lemonpos. 
Esta se llama lemondb.

¿Para qué sirve esto?
------------------------

Sirve para realizar consultas y operaciones en la base de datos de 
lemonpos. Por ejemplo: una utilización simple pero eficiente es el 
importar listas de productos desde hojas de cálculo, creadas por ejemplo 
en libreoffice o en Ms Excel, en lugar de meter producto por producto. 

Además ofrece tanto bajar como subir respaldos de bases de datos.
Si se tienen conocimientos más avanzados de sql, se pueden generar 
algunos reportes, de manera que pueden exportarse y leerse en 
libreoffice. Por ejemplo de productos agotados.

Espero escribir sobre esto pronto. 





Estos son todos mis posts sobre lemonpos:

.. post-list::
   :tags: lemonpos
