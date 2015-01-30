.. title: Mas vulnerabilidades en Linux: Ghost.
.. slug: mas-vulnerabilidades-en-linux
.. date: 2015-01-30 00:28:54 UTC-06:00
.. tags: seguridad 
.. link: 
.. description: 
.. type: text

Una nueva vulnerabilidad se encontró en la libreria glibc, con la que 
corren la mayoría de las distribuciones Gnu/linux. Esta es sólo una 
pequeña reflexión y no un tutorial de como parchar. Curiosamente aunque 
Debian corre eglibc, también fue afectado.

Un buen tutorial sobre como parchar tu servidor o desktop lo puedes 
encontrar aquí:

http://www.cyberciti.biz/faq/cve-2015-0235-patch-ghost-on-debian-ubuntu-fedora-centos-rhel-linux/

En resumen, actualiza tu sistema desde los repos principales y todo 
estará parchado, a menos que corras algo tan antiguo como Centos 4, en 
cuyo caso, será mejor que te cuestiones por que haces algo como esto, 
más si es un servidor con acceso a internet.


En realidad esta vulnerabilidad se suma a la serie de bugs que se 
encontraron el año pasado en software relacionado con Gnu/linux como es 
heartbleed ( que en realidad afectó a todos los sistemas corriendo 
Openssl), shellshock (Mac y Linux), poodle (de nuevo openssl). A 
Gnu/linux le está lloviendo duro.

Es sorprendente que estas vulnerabilidades son parchadas horas o 
incluso minutos despues de  anunciadas por los expertos en seguridad, 
como es el caso de shellshock, lo que nos habla de una buena gestión de 
la seguridad. Pero también son vulnerabilidades que existían desde hace
hace años, que es lo que tienen en común.
Por lo que en realidad pudieron ser descubiertas por los hackers 
Black Hat, desde hace un buen tiempo, lo que les permitiría controlar 
gran parte de la web. Esto en realidad asusta. No quiero ni pensar lo 
que pasa en sistemas de código cerrado como windows o Mac en donde no se 
publican parches rapidamente y este proceso tarda semanas a veces, o 
incluso con que tarde dias, como hizo Mac al parchar shellshock.

Heartbleed por ejemplo permite tener acceso a todo la memoria de un 
servidor que corra Openssl, esto en realidad hacía que la vulnerabilidad 
hiciera mas inseguro al servidor si corria por ejemplo https, de que si 
corría simple http. La única diferencia es que nadie sabia que estaba 
ahí. Lo mismo con shellshock. Y ahora los investigadores que 
descubrieron Ghost aseguran que crearon un email mediante el cual podían 
obtener privilegios root y una shell!!!!! Paranoid mode enabled.!!!!

Y encima de todo se viene systemd para las distros linux, que he estado 
leyendo tiene algunos fallos de seguridad medio feos, sobretodo 
relacionados con los logs, como este:

http://hackingthesystem4fun.blogspot.mx/2014/12/chicos-systemd-lovers-diganme-alguna.html

¿Que se puede hacer? Yo por lo mientras voy a empezar a aprender algo de 
BSD, ya que aunque no estan flexible como linux, de repente uno tiene la 
sensación de que Gnu/linux es un barco hundiéndose. Por varias cosas.
 
BSD al menos ha esquivado Shellshock y también Ghost. Le empezaré a 
echar un vistazo a OpenBSD el sistema super seguro, ya que en los 
tiempos que corren (NSA vigilante) tener seguridad extra no está demás 
aunque dificulte algo las cosas. Además de que de por si, internet es un 
lugar hostil. Esto lo sé sólo con ver la cuenta de ataques automatizados 
ssh a un servidor.

Lo que menos quiero encontrarme es que mis servidores fueron hackeados 
por una vulnerabildad misteriosa aún no descubierta, y que no se tiene 
ni idea de como un malware entró al sistema.

También sería bueno recalcar que mientras mas simple sea un sistema 
es mas seguro es, por ejemplo debo recalcar que la distribución Alpine 
Linux, se ha salvado de varias. Se salvo de shellshock, y de Ghost. 
Gracias a que usa busybox y ulibc, pero sobretodo a que es un sistema 
más simple.  Tampoco usa systemd y además usa un kernel Grsecurity y 
Pax. Una buena opción, aunque no tan robusta como Debian.

De los bugs de openssl nadie se salvó. Para esta libreria existe como 
alternativa GnuTLS y mas recientemente Libressl.

Por lo mientras a corto plazo voy poniendo PAX en mis sistemas y a largo 
plazo a comenzar con BSD.



