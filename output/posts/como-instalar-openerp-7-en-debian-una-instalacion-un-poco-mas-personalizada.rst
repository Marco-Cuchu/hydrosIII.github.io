.. title: ¿Como instalar openerp 7 en Debian? Una instalación un poco mas personalizada.
.. slug: como-instalar-openerp-7-en-debian-una-instalacion-un-poco-mas-personalizada
.. date: 2014-11-05 00:47:48 UTC-06:00
.. tags: openerp, python, debian, draft
.. link: 
.. description: 
.. type: text

Openerp es un buen ERP y es de código abierto.

Aquí hay unas instrucciones para instalarlo en Debian wheezy desde launchpad. Aunque es posible instalarlo
desde launchpad, lo mejor es hacerlo desde github, sin membargo aún hay muchos tutoriales de como hacerlo así 
y posteo esto sobretodo para recordar como lo hice yo. 

Em primer lugar se necesita entrar como el usuario root::

	su

a partir de aquí hay que tene cuidado con lo que se escribe por que ya me ha pasado haber borrado sistemas enteros por un mal comando.

hay que instalar las dependecias usando el gestor de paquetes::

	apt-get install python postgresql-client python-dateutil \
	python-docutils python-feedparser python-gdata python-imaging \
	python-jinja2 python-ldap python-libxslt1 python-lxml python-mako \
	python-mock python-openid python-psutil python-psycopg2 python-pybabel \
	python-pychart python-pydot python-pyparsing python-reportlab \
	python-simplejson python-tz python-unittest2 python-vatnumber \
	python-vobject python-webdav python-werkzeug python-xlwt python-yaml \
	python-zsi graphviz ghostscript python-matplotlib poppler-utils

estas son las dependencias básicas ahora hay que instalar algunas más para funcionalidad extra::

	apt-get install python-dev bzr python-setuptools python-babel \
	python-feedparser python-reportlab-accel python-zsi python-openssl \
	python-egenix-mxdatetime python-jinja2 python-unittest2 python-mock \
	python-docutils lptools make python-psutil python-paramiko poppler-utils \
	python-pdftools antiword

La dependecia de bzr se necesita para bajar el código fuente.

Hay que instalar el gestor de bases de datos; este en una instalación simple puede estar en el mismo servidor que openerp, en instalaciones mas complejas y/o grandes se 
utiliza una maquina independiente para instalar el gestor ya que es el que realiza todas las operaciones que mueven a openerp y usa mucho poder de computo::

	apt-get install postgresql

Luego creamos un usuario dentro de postgres para openerp, este usuario es un usuario dentro del gestor de bases de datos, no hay que confundirlo con el usuario del 
sistema linux. Este es definido por seguridad y para separar. Pero se puede usar el usuario root de postgres si es una instalación simple o para pruebas.
Así se crea el usuario y una base de datos del mismo nombre sobre la que tiene privilegios::

	postgres -c "createuser --createdb --username openerp --no-createrole --no-superuser --pwprompt"

Ahora se crea el usuario de linux, que va a usar openerp. Esto se hace por seguridad, ya que los servicios en linux deben correr con el mínimo de privilegios posibles.
Por lo que se crea un usuario limitado, para que openerp corra::

	adduser openerp --system --home=/opt/openerp --shell=/bin/false --disabled-login
	chown -R openerp /opt/openerp

Se añade el usuario con directorio home en /opt/openerp y no puede loguerse. Para que todo salga bien se cambian los permisos de usuario del directorio home de este último, me parece que este paso es superfluo, pero lo hago para asegurarme.

Se va a usar la rama ocb-backports de openerp que introduce parches para los bugs de openerp antes de la rama principal, por lo que es mas estable, además de ser 
compatible con la rama principal.


Desde Launchpad.
------------------------------------
Este método ya no debe ser usado, por que ya no hay codigo en launchpad, pero lo posteo aquí por que fue lo que originalmente hice y seguramente muchos también. Escribí 
una guía de migración.

Desde Github.
------------------------------------
