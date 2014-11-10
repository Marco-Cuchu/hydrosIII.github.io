.. title: Arch linux en PC Duino.
.. slug: arch-linux-en-pc-duino
.. date: 2014-11-10 16:35:53 UTC-06:00
.. tags: Pcduino
.. link: 
.. description: 
.. type: text

Tiene tiempo que compré una Pcduino para experimentar. Es una 
microcomputadora similar a la Raspberrypi pero con un poco más de 
capacidad de computo.

El objetivo era usarla como computadora de punto de venta para lograr 
una computadora que fuera portátil y ahorrara luz.
Es posible compilar lemonpos para aquitectura ARM lo cuál 
me decía que podía ser una buena idea. Desgraciadamente una vez que 
compré PCduino me di cuenta muy tarde de que no hay drivers de impresora de 
tickets para arquitectura ARM. Las que uso con las Epson TMT.

Esto y otras cosas  detuvieron los planes de construir una caja 
con PCduino, ya que aunque lemonpos puede imprimir texto plano, usabámos 
las 
computadoras para imprimir algunos archivos de libreoffice de cuentas. 
Además esta PC sólo cuenta con una salida de video HDMI, lo cual implica comprar un 
monitor moderno, o comprar un cable convertidor, y ninguna de las dos 
resultó una opción.


Problemas con la PC Duino.
----------------------------

La PC en sí fue cara, pues aunque estas PC's se anuncian como muy 
baratas, por los impuestos de importación de Estados Unidos y por 
que son un artículo raro, no se consiguen a un precio accesible en el 
país. El convertidor de HDMI a VGA también era más caro que la compu. 
Esto acabó con la utilidad de la computadora y la relegó al fondo del 
cajón durante un tiempo. Ya que computadoras viejas arquitectura X86 se 
consiguen baratas y por montones.

Otro punto en contra es que si bien es más potente 
que la Raspberrypi, es menos flexible, viene con Lubuntu instalado, no se puede 
instalar Raspbian (al menos ahora, pero puede ser que la version 8 de 
debian tenga soporte para esta computadora) y no se puede encontrar 
documentación.

El lubuntu que trae por defecto corre muy lento y tarda bastante hasta 
en instalar un programa, esto se debe al parecer a la lentitud de 
escritura de la memoria NAND que trae integrada.


Buscando la utilidad.
-----------------------

Decidido a no malgastar el dinero, hace poco me puse a investigar como 
darle una utilidad y vi que lo mejor era utilizarlo como un pequeño 
sevidor. He decidido usarlo para servir una micro págia web, su 
capacidad es la suficiente para esta tarea, con la ventaja de que si se 
queda prendida todo el día el consumo de luz es mínimo. Para lo anterior 
decidí cambiar ubuntu por Arch linux, ya que es el otro sistema linux 
que soporta además de Android. uso arch linux a diario y me es familiar 
y me resulta cómodo.

Se necesita una tarjeta microSD, yo usé una de un celular viejo con 2GB 
de capacidad. Y las instrucciones se pueden encontrar aquí.

http://archlinuxarm.org/platforms/armv7/allwinner/pcduino

Desgraciadamente las instrucciones no están completas. 

Para instalar Arch linux ARM en PC duino se necesita otra computadora 
con linux, ganas de aprender y paciencia. Me parece que 
también sirve en Mac el tutorial mientras se tenga dd y tar.

1.Primero se hacen dos particiones en la tarjeta SD. Se pueden hacer 
usando fdisk o cfdisk. La primera de 16MB y la segunda de lo que sobre. 
A la primer partición se le da formato vfat y la segunda ext4. El 
problema  que  no se indica en la página es que la primer partición
necesita empezar a partir del sector 2048 de la tarjeta. Es decir que 
hay que dejar espacio suficiente al inicio del disco para que se instale el 
cargador de arranque. Así que esto hay que tenerlo en cuenta cuando se 
hagan las particiones.

2. A partir de aquí se pueden seguir las instrucciones del link 
anterior. Se baja el tarball del cargador de arranque desde aquí:

http://archlinuxarm.org/os/sunxi/pcduino-bootloader.tar.gz

Se descomprime usando tar, y se copia mediante dd al la tarjeta SD::

	wget http://archlinuxarm.org/os/sunxi/pcduino-bootloader.tar.gz 
	tar xzf pcduino-bootloader.tar.gz 
	dd if=pcduino/sunxi-spl.bin of=/dev/mmcblkX bs=1024 seek=8 
	dd if=pcduino/u-boot.bin of=/dev/mmcblkX bs=1024 seek=32

La tarjeta SD en el anterior código mmcblkX, en mi caso me parecio como 
/dev/sdb. Se puede saber como apareció la tarjeta SD en nuestro sistema 
usando fdisk -l. En este caso se tiene que usar el disco SD entero, no 
las particiones, es decir no usar /dev/sdb1 sino /dev/sdb. Si se usa alguna de las 
particiones en lugar del disco entero habrá que empezar todo de nuevo.

3. Se baja el tarball del sistema Arch Linux ARM;, se descomprime y 
copia a la tarjeta SD::

	mkdir /tmp/boot mkdir /tmp/arch mount /dev/mmcblkXp1 /tmp/boot 
	mount /dev/mmcblkXp2 /tmp/arch wget 
	http://archlinuxarm.org/os/ArchLinuxARM-sun4i-latest.tar.gz 
	bsdtar -xpf ArchLinuxARM-sun4i-latest.tar.gz -C /tmp/arch 
	cp /tmp/arch/boot/uImage /tmp/boot/uImage

Se montan las particiones en las capetas creadas en /tmp, luego se 
extrae la imagen del sistema a la futura partición raiz y copia
el kernel a la partición de boot. Aquí si se tiene que usar el número de 
partición.


4. Luego hay que copiar unos archivos especiales a la partición boot. 
Estos están también dentro del primer tarball que bajamos::

	cp pcduino/pcDuino.bin /tmp/boot/ cp pcduino/uEnv.txt 
	/tmp/boot/uEnv.txt

5. Sacamos la tarjeta SD con seguridad::
	
	sync
	umount /dev/mmcblkX*

Todo esto se tiene que hacer como root


Bien ahora sólo se inserta la tarjeta SD en la PcDuino y se le conecta 
el cable de corriente. 

Yo estuve esperando a que booteará un buen rato, frente a mi monitor 
HDMI, esperando a que diera señal pero ... nunca hubo señal. 
¿Qué esta pasando? ¿Acaso me equivoqué? ¿Dónde esta el fallo?. Resulta 
que Arch linux ARM, viene sin nada, totalmente simple, tan simple que no
manda señal al HDMI, aunque si corre. ¿Pero que estaba pensando quien 
hizo esto?

Para mi en realidad fue conveniente ya que pensaba usar PCduino como 
servidor Web. Resulta que aunque no tiene salida HDMI, la imagen de Arch 
linux ARM, viene con ssh y dhcp configurados, por lo que para tener 
acceso al dispositivo hay que conectarlo por cable ethernet a un router. 
Cualquier router casero maneja dhcp, por lo que es un paso fácil. Una 
vez hecho esto, se conecta la compu y desde otra compu con linux vamos a 
entrar emdiante ssh.

Lo primero es saber que dirección ip adquirió la PCduino. Para esto yo 
use nmap. Este programa esta en todas las distribuciones. El comando 
sería::

 nmap 192.168.1.1-254

Lo que escanea toda la red doméstica o interna en busca de puertos 
abietos, esto se tiene que adaptar hay que sustituir 192.168.1.1 por tu 
subred, pero en la mayoría de los routers caseros este comando 
funcionará copiando y pegando. Debe salir algo como esto::

	Nmap scan report for 192.168.2.1
	Host is up (0.065s latency).
	Not shown: 998 closed ports
	PORT     STATE    SERVICE
	22/tcp   open     ssh

Lo que indica que hay una computadora con un puerto ssh abierto, por lo 
que desde mi máquina linuz hago::

	ssh root@192.168.1.1

la contraseña por defecto es "root" no olviden cambiarla después. El 
sistema por defecto trae el hostname de alarm. Dentro de 
Arch Linux en PCduino un buen primer comando para ejecutar sería::
	
	pacman -Syu

Fuente:

http://archlinuxarm.org/forum/viewtopic.php?f=9&t=5334
y experimentos propios.
