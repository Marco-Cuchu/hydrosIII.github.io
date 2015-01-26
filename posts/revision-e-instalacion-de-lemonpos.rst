.. title: Revisión e instalación de LemonPos
.. slug: revision-e-instalacion-de-lemonpos
.. date: 2014-11-07 01:30:04 UTC-06:00
.. tags: lemonpos  
.. link: 
.. description: 
.. type: text


Estoy usando lemonpos para algunas tiendas. Me parece que es un programa 
muy bien hecho, y que al contrario de varios puntos de venta con 
software libre, este es muy simple y muy fácil de usar. Sin 
funcionalidad extra que estorbe. Una de las cosas que más me gusta de 
lemon es su diseño de base de datos, que es en realidad muy simple, lo 
que permite hacer operaciones fáciles como importar productos. Además de 
scripts sencillos en sql para obtener algunos reportes. 

Desde hace tiempo había tenido varios problemas. En primer lugar al contrario de lo recomendando 
no estoy usando kubuntu para probar lemonpos, en lugar de eso estoy 
usando Crunchbag linux. Una distribución ligera derivada de Debian 
Wheezy para correr lemonpos. Esto es obviamente por que me parece que es
inútil gastar recursos para correr el escritorio KDE sólo para correr un 
punto de venta. Las maquinas donde corro lemonpos ya tienen algunos 
años. Y claro una de las cosas que esperas de una máquina de un punto de 
venta es que haga solamente eso. ¿Han visto las terminales de punto de 
venta de los super?. Ni siquiera tienen pantalla, esto claro es un 
beneficio por que se tiene una computadora con mucha seguridad, que no 
tenga virus y que no se use para ver facebook. Al menos desde mi punto 
de vista. 

Otra razón es por que no me gusta ni ubuntu ni las distribuciones 
derivadas.

.. TEASER_END

¿Por que escogí lemonpos?
----------------------------

Antes que nada escogí un programa de punto de venta libre 
por que éste me permite estudiarlo y modificarlo, pero una de las cosas
más importantes es que corre en linux, por lo que hace al sistema mas 
estable en sí. Además, su base de datos es abierta y facil de 
manipular lo cual es algo que considero esencial en este tipo de 
software ya que muchos puntos de venta propietarios ofuscan su base de datos,
por lo que es muy dificil sacar la información de estos sistemas si 
quieres migrar, importar productos, o simplemente crear reportes 
personaizados.

Antes tengo que aclarar que lemonpos es un proyecto que ya no está en 
desarrollo, por lo que antes de pensar si deben o no de instalar 
lemonpos, hay que pensar si vale la pena. Otras opciones son Posper, PHP 
Point of Sale y OpenBravo Pos. Son muy buenas y están mantenidas. Entonces, ¿Porqué escoger 
lemonpos?. Probé todos los puntos de venta anteriores, y no me 
convencieron por varias razones: La mayoria estań dirigidos a 
pantallas táctiles, además de que implementan demasiadas funciones; el
proceso de hacer una simple venta es algo engorroso, cuando en lemonpos 
es simplemente escanear el código de barras del producto y teclear 
enter.

La rapidez del sistema también es una ventaja y con rapidez me 
refiero a que tanto se tarda el sistema entre hacer la venta e imprimir 
el ticket, ya que cuando hay mucha gente comprando en la tienda, es 
dificil de manejar si el sistema tarda algunos segundos. Los atajos del 
teclado son otra cosa muy útil.
 
Ya lo mencione pero el esquema de base de datos que implementa es
una de las mejores cosas de lemon. Usa Mysql, un gestor de 
base de datos que sale sobrado para la tarea de correr una tienda, ya 
que éste se utiliza para manejar gran cantidad de información.
Además su diseño de tablas es claro, lo que indica que el sistema está 
bien hecho.

A pesar de no estar más en desarrollo  es instalable en Debian 
Wheezy, Debian Jessie e inclusive en Arch linux lo que indica que el 
código está bien escrito, y aun se puede portar a sistemas nuevos, ya 
que originalmente estaba desarrollado para Ubuntu 10.04.

Si LemonPos es instalable en una distribución de largo soporte como lo 
es Debian Wheezy o Debian Jessie o Centos 7 esto significa que este 
puede funcionar por más de 10 años sin problemas.


El estado actual de lemonpos
------------------------------------

Escribo todo esto por que parece que es un punto de venta de: haz doble 
click y funciona, quizá fue así hace algunos años pero yo tuve que 
explorar un poco a fondo las opciones que tenía el programa para poder ofrecer 
una instalación estable.

Actualmente existe la paǵina en sourceforge de lemonpos donde se pueden 
conseguir diferentes versiones, también hay dos paǵinas con el código 
fuente de lemonpos, github y gitorious.

1. https://gitorious.org/lemonpos
2. http://sourceforge.net/projects/lemonpos
3. https://github.com/miguelchavez/lemonpos

Estos tres repositorios contienen diferentes cosas. Los repositorios 
github y gitorious casi son iguales, pero el código en github me parece 
que es mas actual. En sourceforge podemos encontrar paquetes .deb algo 
antiguos y código fuente.

Hay dos formas de instalar el código, la primera es compilar, lo cual en 
realidad no es dificil, ya que se puede hacer usando make. La segunda es 
usar los paquetes .deb pero desgraciadamente sólo se pueden usar en una 
distro debian.

¿Que versión escoger?
+++++++++++++++++++++++++++

Como dije lemonpos, ya no está mantenido y hace poco acaba de perder 
la wiki que estaba en sourceforge, además de la documentación en su 
blog, por lo que haré un resumen de mis experiencias con lemonpos por si 
alguién se anima a instalarlo. 

Me parece que lo mejor es escoger una versión más antigua. He aquí mis 
experiencias con las diferentes versiones de lemonpos que he probado:

1.Version 0.9.5 de github: con esta versión me refiero al tag en  
github o gitorious que dice 9.5, es necesario compilarla. 

https://github.com/miguelchavez/lemonpos/archive/v0.9.5.0.zip

No es recomendable ya que tienen un bug que afecta mucho su funcionalidad. No se pueden buscar productos donde dice buscar 
productos ya que el sistema se traba y se tarda demasiado en encontrar 
los productos. Esto sólo lo supe después de tomarme el trabajo de hacer 
un paquete .deb de la misma.

2.Versión 30-abr-2013. Esta versión se encuentra disponible en 
sourceforge. Esta es una versión que corrige el anterior error 
pero que desgraciadamente sólo se encuentra disponible en binario,
no está claro cual es el código fuente exacto de la anterior versión de 
lemonpos, pero estudiando un poco el código me parece que es la rama 
principal de github, o quizá algo un poco anterior. Si se tiene otro 
sistema que no sea un debian o ubuntu instalar esta, no es fácil.

3.Versiones anteriores: No las he probado.Me parece también que aún  
se mantiene una versión "estable" en los repositorios de ubuntu y me 
parece que son versiones algo mas antiguas, quizá sirvan mejor.

4. Version Rc 9.4.8, la probé de forma muy breve y me parece que 
también existe el error de la busqueda de productos.

¿Es acaso una versión mejor que la otra?
______________________________________________

Revisando un poco el código de las diferentes versiones me encontré con 
que después del 2010, lemonpos casi no cambia, básicamente se añaden las 
funcionalidades de: pago con transferencia interna, algunas correciones 
en la base de datos y el intento de inclusión  de las facturas CBB. En 
México éste fue un esquema de facturación que ya no es usado y por lo 
tanto es obsoleto, por lo que ya no sirve esta funcionalidad. También en 
versiones mas recientes se añaden subcategorías.
A mi parecer estas últimas versiones presentes en git solamente, complica demasiado lemon. Así que si te funciona la version 
vieja, no la cambies!!!.
A partir de la versión 9.3 el código de lemonpos se empieza a ensuciar, 
seguro debido a que los desarrolladores no tenían tiempo de seguir con 
el proyecto y tenían varias ideas que no se llegaron a implementar.

A continuación detallaré la instalación de lemonpos en Crunchbag linux 
usando la versión 30-abr-2013 que fue la que al final me funcionó, si 
alguno sabe que son mejores las anteriores versiones, por favor hagamelo 
saber.



Instalación de lemonpos.
------------------------------

EL objetivo es lograr tener un punto de venta estable y ligero. 
Lamentablemente por ahora este tutorial sólo aplica para arquitecturas 
32 bit, osea computadoras viejas, las que deberías usar en un punto de 
venta. :). Ya que la version 30-abr sólo existe en formato binario, he 
buscado la fuente de este y no ha quedado muy claro cual es. Existe 
también la posibilidad de compilar un paquete para computadores de 64 
bit, eso ya lo he probado, pero no he logrado encontrar una versión del 
código estable en github, espero adelantar sobre esto más adelante..

1.Bajas el paquete .deb de aquí.

http://sourceforge.net/projects/lemonpos/files/testing/

Este paquete es compatible con Debian Wheezy.

Antes de instalar el paquete es necesario instalar varias dependencias. 
El paquete original ya trae las dependencias listadas, sin embargo al 
instalarlo me encontré con que faltaban algunas cosas, y sobretodo que 
no se traducía bien el programa al español. Esto me parece que es por 
que  usa ciertos paquetes de KDE para instalar lemonpos, pero correr 
kde acaba con el propósito de lograr un sistema ligero, a base de compilar 
código y hace varias pruebas logré solucionarlo.

Primero nos logueamos como root::

 su

Luego instalamos las dependencias::

	apt-get install kde-runtime libc6 libkdecore5 libgcc1 
	libqt4-dbus libqt4-network libqt4-sql-mysql libqt4-xml libqt4-svg 
	libqt4-core libqt4-gui libstdc++6 mysql-client libkdeui5 
	libkio5

Esto instalará las dependecias de lemonpos básicas, que serán un montón pues es KDE, sin embargo estas no se utilizarán cuando lemon esté corriendo
por lo que el programa sigue siendo ligero y capaz de cargar en computadoras viejas, sólo ocuparán espacio de disco.

Ahora es tiempo de instalar la base de datos::

	apt-get install mysql-server

Durante el proceso de instalación aparecerá un dialogo preguntando por 
la contraseña de root de la base de datos, esta es necesaria anotarla ya 
que la usaremos despúes para el proceso de instalación.

Esta base de datos no necesariamente tiene que estar en la misma 
máquina, de hecho esto hace a lemonpos bastante flexible y puede tener 
varias terminales de punto de venta conectada a la misma base de datos, cuando 
se tiene una tienda un poco mas grande. Espero escribir sobre esto mas 
adelante.

Una vez que todo esto esté instalado es hora de ir al directorio donde 
bajamos el paquete de lemonpos e instalarlo. Lo podemos hacer de manera
gráfica con gdebi o desde la terminal con::

	dpkg -i lemonpos_30-APR-2013-1_i386.deb

Ahora ya estamos casi listos para la implementación de lemonpos. Solo 
falta poblar nuestra base de datos. Escondidos dentro del paquete de 
lemonpos están los scripts necesarios para crear esta base de datos, los 
puedes encontrar en el directorio::

	/usr/share/kde4/apps/lemon

aquí se encuentran una serie de scripts, que crearán la base de datos y 
algunos que están ahí para migrar de versiones anteriores de lemonpos. 

Primeramente creamos la base de datos con::

	cat lemon_mysql.sql | mysql -u root -p

Aquí preguntará el password que pusimos al instalar la base de datos, 
por lo que es importante anotarlo.

Luego aplicamos el siguiente script::
	
	cat fix_roles.sql | mysql -u root -p

Nuevamente pregunta el password y ya, podemos ignorar los demás archivos 
presentes en esta carpeta.

Ahora podemos iniciar lemonpos, primeramente hay que salir de root con::

	exit

y escribir::
	
	lemon

para iniciar el programa. El programa de administrador es "squeeze", si 
escribes esto en una terminal aparecerá. El usuario por defecto es 
"admin" y la contraseña "linux".

Conclusión
-----------

No es nada fácil instalar lemon hoy día, el estado en el que se 
encuentra el proyecto es de abandono, sin embargo sigue siendo un 
programa muy bajado en sourceforge y francamente es un programa bueno y 
bien diseñado, por lo que vale la pena su instalación y configuración, 
ademas es software mexicano. La caída de la wiki y otros recursos esta 
haciendo más dificil el acercamiento a este programa. Es una lástima, 
por lo menos yo espero seguirlo usando los siguientes años.

Espero escribir otro post, sobre como configurar lemonpos, importar 
productos desde una lista de excel y como tener un setup multicaja,
asi de como conectarse remotamente con lemon, para actualziar el inventario
desde lejos, es decir desde otra máquina, además de producir algunos reportes.


Actualizacion importante:
-----------------------------

Actualmente está lista una versión estable para lemonpos, en donde los
errores de la última versión que se consigue en sourceforge están
corregidos. Además de los que están en este artículo.

Los cambios importantes con los siguientes:

1. Las traducciones al español funcionan bien, he adicionado traducciones que faltaban.
2. Quité la funcionalidad de facturas CBB ya que estas no se usan más en 
México.

En realidad nada nuevo, pero corregí algunos detalles.

Pasen por mi página en github para descargar el nuevo código fuente.
Usen la rama estable.

