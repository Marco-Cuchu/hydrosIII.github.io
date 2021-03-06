.. title: El proyecto Mempo, un Debian más seguro con Gr-security.
.. slug: el-proyecto-mempo-un-debian-mas-seguro-con-gr-security
.. date: 2015-05-25 08:16:49 UTC-06:00
.. tags:
.. link:
.. description:
.. type: text



Recientemente, empezé a preocuparme más por la seguridad de los sistemas ya que, me he dado cuenta de que en general internet es un lugar bastante hostil.
Debido hace poco  a la vulnerabilidad Ghost, me preocupe por el estado del sistema cuando se trata con bugs aún no descubiertos por lo que una cosa
prudente en un servidor abierto a internet es configurar la seguridad preventiva.

Ahora bien, Debian tiene muchas herramientas de seguridad que se pueden instalar facilmente desde los repostiorios oficiales como Selinux o Apparmor, pero
si se quiere algunas cosas no tan oficiales pues es un poco dificil encontrarlas. En este caso yo estaba buscando instalar el Kernel Gr-Security en Debian

Gr-security y Pax son una serie de parches al kernel linux que protegen contra posibles vulnerabilidades en el kernel y que además brindan un sistema parecido a Selinux
o Apparmor. Lo mas interesante del kernel grsecurity es que protege contra los desbordamientos de memoria, que de vez en cuando se encuentran en el kernel. Así protege
que cada uno de los programas no se "salten" a donde no deben, debido a bugs en el código. Lo mejor es que esto es implementado sólo con el hecho de correr el kernel
Gr-security, que además es compatible "out of the box" con casi todas aplicaciones. Digo casi todas por que en realidad Gr-security interfiere con la capacidad del
kernel de usar Apparmor, por lo que si usamos Appramor para securizar Debian, es mejor pensar antes de instalar dicho kernel. Lo positivo es que Gr-security posee su
propia implementación de RBAC, parecida a Apparmor y fácil de usar, por lo que en realidad no se pierde y se gana mucho al instalar este kernel. Ahora bien,
siempre cabe la posibilidad de que algunas cosas fallen debido a la implementación del kernel, sobretodo si son programas que implementan funciones en las cosas que
modifica Gr-security, por lo que si se está corriendo cosas como Docker o linux containers, hay que tener cuidado antes de implementar dicho kernel. Yo no uso ninguna de estas dos tecnologías en los servidores con Gr-security, al menos por ahora, por lo que no sé si son afectadas por los parches Gr-security, pero aconsejo precaución. En cualquier otro caso Gr-security será una capa más en la cebolla de la seguridad.


Hay dos formas de instalar el kernel Gr-security, la primera es bajar el kernel vanilla, parcharlo con los parches disponibles en: http://grsecurity.net/ o en Debian
https://packages.debian.org/wheezy/linux-patch-grsecurity2. Ahora parchar y compilar un kernel no es algo que se puede explicar en un artículo tan corto.
Pero este procedimiento no es tan complicado, tiene sus ventajas y desventajas:

Desventajas:

1. El uso del CPU durante la compilación es mucho, por lo que no es viable compilar el kernel en un servidor en producción. Esto se puede resolver compilando el kernel
en una maquina de escritorio o similar y después subiéndolo aunque se cae en el riesgo de caer en incompatibildades.
2. Podría haber problemas de incompatibildad en los drivers del nuevo kernel y el antiguo, sobretodo si se está compilando una version diferente.
3. Es dificil saber que drivers incluir, la mayoría de los kernels incluyen todos los drivers como módulos cargables, por lo que copiando la configuración por defecto
debería de funcionar, pero requiere de cierta experiencia.
4. Si aparece una vulnerabilidad grave en el kernel y es neceario cambiarlo, habrá que hacer todo el proceso de nuevo, por lo que es más comodo usar un repositorio.


Ventajas:

1. Se puede compilar el kernel sin módulos por seguridad, aunque esto requiere de experiencia y saber para que sirve cada uno, ya que es fácil romper cosas. Por ejemplo
se puede deshabilitar el soporte ipv6, cuando no se use.


Lo más facil somo se vió es usar paquetes precompilados puestos a nuestra disposición por el proyecto Mempo, a traves de sus repositorios.



se puede usar paxtest para probar la protección del kernel, este
en Debian solo esta disponible para i386, yo sólo para probar baje el
paquete 64 bit de arch linux, lo descomprimí ya que es solo un script en
bash y ejecutables compilaodos en c e instale manualmente los ficheros,
usando cp , este seguramente no es muy buen método, pero me fue
imposible construir el paquete Debian de paxtest, creo que es por esto
que no hay versión 64 bits de este. Una vez "instalado" paxtest podemos
hacer las pruebas de protección del kernel.

Hay que tener mucho cuidado con el logueo del kernel gr-security ya que como viene instalado loguea todos los eventos del sistema, abarrotando rapidamente la partición de log del sistema. Esta opción es configurable.

<http://en.wikibooks.org/wiki/Grsecurity/Appendix/Grsecurity_and_PaX_Configuration_Options>

Notas:

No se porque el repo de Mempo esta abajo desde hace un buen rato, por lo que no se si el proyecto continua con vida. Antes se encontraban en essta web. http://deb.mempo.org/

Aún se puede encontrar una página aquí:

<https://rawgit.com/mempo/mempo-websites/master/mempo-main/html/index.html>

Aquí se encuentra la web el proyecto, peor su principal dirección esta caida junto con sus repos. Ahí informa que tiene repos en freenet para evitar este tipo de cosas, pero no me puesto a investigar si realmente sirven. Parece ser que su dominio venció o algo por el estilo pero los repos ya no funcionan.

Se pueden encontrar builds del kernel gr-security aquí:

<http://molly.corsac.net/~corsac/debian/kernel-grsec/packages/>

Espero que el proyecto Mempo no haya muerto y no pase de un nombre de dominio caducado. Entre al IRC y no obtuve respuesta respecto a esto, pero al menos había gente. Si alguién leyendo esto sabe del estado del proyecto, peude dejar un comentario.


Mas info:
<https://wiki.debian.org/grsecurity>
