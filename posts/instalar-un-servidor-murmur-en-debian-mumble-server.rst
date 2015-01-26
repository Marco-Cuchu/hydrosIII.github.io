.. title: Instalar un servidor murmur en Debian (mumble-server)
.. slug: instalar-un-servidor-murmur-en-debian-mumble-server
.. date: 2015-01-25 01:18:48 UTC-06:00
.. tags: Debian
.. link: 
.. description: 
.. type: text



Este es un minitutorial sobre como instalar un servidor murmur en 
Debian.
Para quien no lo sepa, murmur es el servidor de mumble, un programa que 
puede sustituir a skype, para hablar con gente de lejos. Mumble fue 
pensado originalmente para los videojuegos y esta diseñado par trabajar 
con anchos de banda pobres, por lo que lo hace muy eficiente en cuanto a 
la transmisión de audio, mucho mejor que skype.


Pero la principal ventaja que yo le veo, es la seguridad que obtenemos 
al correr todo esto en un servidor propio, y saltarnos la vigilancia de 
compañias como google o skype. Se puede instalar en una vieja maquina 
con Debian, cualquier cacharro de los 90 funciona para correr este 
servidor. Igualmente una raspberry pi, o inclusive existe una version 
para los routers con Openwrt. Los routers de marca linksys. 

.. TEASER_END

Para instalarlo en una red casera, hay que configurar un servicio de DNS 
dinámico y estar seguros que nuestro proveedor de internet sale 
directamente a la red, y tenemos control sobre nuestra ip pública. Lo 
cual puede complicar un poco, pero no imposibilitar la configuración de 
mumble-server.

Sin embargo, compré un pequeño VPS para este tipo de cosas. La 
configuración en internet facilita mucho las cosas, y se puede abirir un 
servidor para platicar con tus amigos sin tener que gastar en teléfono. 
O con los miembros de tu familia. Además cuenta con clientes para 
Android y Iphone, lo cual lo hace ideal para llamadas a traves de 3g, 
que además superan cualquier intento de escucha por parte de la compañia 
teléfonica ya que toda la información va cifrada.

Bueno, después de toda esta larga charla. Les muestro como correr 
murmur, que en Debian esta empaquetado como mumble-server.

Nos logueamos como root en nuestro servidor y escribimos::

	apt-get install mumble-server --no-install-recommends

Es bueno instalarlo sin las recomendaciones, ya que jala muchas 
dependencias innecesarias si tenemos un servidor web, además de que usa 
avahi. Posteriormente a la instalación hay que asegurarse de tener avahi 
desactivado si se está instalando en un servidor abierto al internet, ya que este crea una vulnerabilidad de 
seguridad. También hay que asegurarse de tener el puerto 64738 abierto a 
las conexiones entrantes.

Después, de instalarlo, es recomendable mover algo las configuraciones 
en ::

	/etc/default/mumble-server

en donde modificamos el número de procesos que puede abrir mumble-server 
a un límite razonable, de acuerdo al uso que se le vaya a dar y los 
recursos del sistema::

	MURMUR_LIMIT_NOFILE=20


Por último movemos otro archivo de configuración localizado en::

	/etc/mumble-server.ini

Yo recomendaría la siguiente línea::

	certrequired=True

por seguridad, pero igualmente hay varias configuraciones, explicadas 
con comentarios en el archivo. Ahora si sólo hay que reiniciar el 
mumble-server para que acepte las nuevas configuraciones::

	 service mumble-server restart

Y ya nos podemos loguear desde mumble en nuestra pc a nuestro nuevo 
servidor murmur.

Es posible además instalar el paquete mumble-django para agregar una 
interfaz web de configuración al servidor. Disfruten su nuevo servidor 
murmur.
