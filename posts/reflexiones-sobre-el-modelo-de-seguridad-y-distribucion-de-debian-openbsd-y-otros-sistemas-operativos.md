<!-- 
.. title: Reflexiones sobre el modelo de seguridad y distribución de Debian, Openbsd y otros sistemas operativos.
.. slug: reflexiones-sobre-el-modelo-de-seguridad-y-distribucion-de-debian-openbsd-y-otros-sistemas-operativos
.. date: 2015-02-04 22:53:03 UTC-06:00
.. tags: Debian, seguridad, openbsd
.. link: 
.. description: 
.. type: text
-->

Anteyer, en la lista de seguridad de Debian se anunció el fin del 
soporte de seguridad para chromium, ya que es imposible construir las 
nuevas versiones de chromium, con los compiladores disponibles en Debian 
Wheezy. Esto es indicador de varias cosas, en primer lugar: Wheezy se 
empieza a quedar viejo, se aproxima el fin de su ciclo de vida. En 
segundo lugar google publica nuevas versiones de chromium demasiado 
pronto sin preocuparse por la compatibilidad reversa.

Para los usuarios que usan chromium, se recomienda dejar de usarlo y 
preferir un navegador como iceweasel, que aún tiene soporte de 
seguridad. Si es posible, desintalarlo del todo del sistema. Ahora bien, 
¿Qué tan peligroso puede ser seguir usando chromium?, la verdad no
mucho, al menos por ahora, sin embargo aunque a nivel personal no 
implique mucho riesgo, si puede implicarlo en una organización con miles 
de computadoras corriendo chromium.

Inmediatamente algunos voluntarios están proponiendo soluciones para ver 
si es posible paliar esto.

Todo esto me lleva a una reflexión más sobre los modelos de seguridad de 
cada uno de los sistemas operativos, y que es lo que esto implica. 

Hace poco acabo de instalar mi primer sistema Openbsd, en una maquina 
vitual, me impresiono la política de distribución que tienen para su 
sistema. Sacan una nueva versión cada seis meses y sólo le dan soporte 
de seguridad a las dos últimas versiones, lo que significa que el soporte 
dura cuando mucho un año. Un año!!!!!, y en el mundo Gnu/linux nos 
quejamos cuando una distribución dura 6 meses, como sería el caso de 
Fedora, mas o menos.

Pero la pregunta es ¿Por que Theo De Raadt y el equipo de OpenBSD decidió esta política de funcionamiento? Según las 
palabras de la página de OpenBSD, pues simplemente por que ellos no 
creen en la compatibilidad binaria reversa. Como un sistema BSD más 
parecido a UNIX, se instala todo desde repositorios oficiales o de plano 
se compila usando el sistema de ports. Los paquetes viejos y no 
mantenidos salen de la distribución, asi como el código fuente 
defectuoso y no compilable. Esto desde luego crea un entorno por si 
mismo hostil hacia el código fuente mal escrito y no mantenido que 
refuerza la seguridad total del sistema. La consecuencia secundaria es 
obvia: fuera aplicaciones viejas de Openbsd, olvidate de usar programas 
precompilados viejos, con vulnerabilidades de seguridad y otras cosas 
peores. Obviamente el software instalable se restringe a software con código fuente libre
y con licencia compatible BSD, lo que vuelve auditable el sistema entero.

Como comparación tenemos distribuciones LTS como Debian que 
implementan unas aplicaciones estables, parches de 
seguridad, además de un cómodo repositorio backports, donde se 
encuentran las aplicaciones nuevas. Es posible hacer funcionar  a veces los programas 
de anteriores versiones de Debian o incluso de Ubuntu. Además de que el soporte extendido permite que estas distribuciones sean 
usadas para servidores y entornos mas estables, ya que no hay que estar 
cambiando tan seguido.

Pero la cuestión es esta: si el modelo de desarrollo más seguro es el de 
OpenBSD, basada más en código fuente. ¿Por que este no es mas 
implementado en servidores?. No es que no se utilize, pero su uso se 
limita más a routers y firewalls. En este 
artículo de blog se argumenta que es más facil gestionar el cambio si 
este es hecho poco a poco, es decir que es mucho más facil actualizar un 
sistema cada 6 meses, y corregir los pocos errores que surjan que 
migrar un sistema de 10 años de antigüedad, como por ejemplo Centos o 
Red Hat. En estas distros su modelo de distribución está basado 
en: (Pensamiento de un sysadmin vago) A ver a quien le toca actualizar esto en 10 años, espero no ser yo.

Ahora, Debian se halla entre esos dos extremos por lo que pienso que su 
modelo de distribucion es ideal para servidores, aunque no tanto para 
escritorios, ya que se mueve muy rápido. Esto partiendo del supuesto de 
que los administradores de servidores son gente que sabe del tema, y que 
les toca gestionar el cambio, mientras que los usuarios "normales", lo 
único que quieren es usar un sistema que sirva. Quizá el modelo  de 
distribución para escritorio sería Centos, Ubuntu LTS o similares.


Según esta premisa de la seguridad planteada por OpenBsd, deberíamos de 
usar en servidores distribuciones de corto soporte. Llevándolo un poco 
al extremo parecería que lo ideal sería usar Arch linux para 
servidores dejando a Centos o Ubuntu LTS, para los desktops y cosas no 
tan "vitales". Siguiendo con esta línea de pensamiento hay una distribución linux
que se ajusta a esta medida, Gentoo, flexible pero robusta, moderna pero estable, mas apegada al pensamiento 
BSD conservador y utilizada en servidores, aunque complicada de configurar y mantener.


Pero a pesar de todos los pensamientos anteriores, la distro de facto en la empresa es Red Hat en servidores,
en el escritorio (ni a distro se llega) es Windows. Windows merece una mención aparte en el tema de la seguridad, ya que en mi opinión
se podria considerar el sistema mas inseguro de los mencionados. Tiene gran compatibilidad binaria reversa, usa programas binarios
sin código fuente auditable por años sin ningún tipo de soporte de seguridad, las actualizaciones de seguridad no actualizan todos los programas, además 
de que necesita antivirus y demás porquerias. Además claro del modelo de software cerrado que promueve, pero es por estas mismas cualidades por las 
que triunfa en la empresa (sobretodo por la compatibilidad reversa de binarios precompilados), además de que poseee un gran tiempo de "soporte". 

En conclusión: Como siempre, es el tema de la seguridad contra la comodidad, por un lado está el sistema operativo super seguro, OpenBSD, con código fuente 
auditable, herramientas de seguridad ultraprobadas, diseño minimalista, y acercamiento a la seguridad activa, pero con corto tiempo de soporte y no amigable 
al usuario sea este el usuario medio de PCs, o un administrador de sistemas. Por otro lado está Windows, un sistema pesado, lleno de binarios que ni sus programadores 
entienden pero que quedaron ahí para conservar la compatibilidad reversa, sin seguridad a nivel de separación de usuarios, sin soporte de seguridad para aplicaciones 
de terceros, que necesita usar antivirus, que promueve el uso de aplicaciones binarias de fuentes no comprobadas, pero eso sí, tiene una interfaz gráfica donde le 
puedes "picar" y creerte experto en computación, además de instalaciones de doble click, y cosas parecidas. Este esquema en el mundo de hoy (que ya no son los 
amigables años 90) es insostenible razón por la cual se le tienen que agregar 30 antivirus y demás cosas. 

Me parece que un justo medio es Debian, amigable para el usuario, cómodo para el administrador y con actualizaciones de seguridad responsables o alguna otra distro 
linux. En fin, final de la reflexión.

Preguntas al aire:

¿Alguién usando windows en servidores por aquí?.
¿Que tan seguro es Red Hat o Centos?
¿Hay que cambiar todos a Gentoo, FreeBSD, OpenBSD?
¿Cuál es el lugar de MacOS en todo esto?


Fuentes:


http://www.openbsd.org/security.html
https://www.debian.org/security/
