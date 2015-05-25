.. title: Usar docker en Debian Jessie
.. slug: usar-docker-en-debian-jessie
.. date: 2015-05-25 07:35:08 UTC-05:00
.. tags:
.. link:
.. description:
.. type: markdown

Hace poco instalé un servidor Debian para producción, entre otras cosas usé docker para facilitar la configuración de algunas cosas,
y para probar algunos contenedores sin tener que instalar todas las dependencias. Docker en el momento que escribo esto, aún no llega a Debian Jessie.

Docker es un proyecto que surgió a partir de LXC (contenedores linux) para automatizar y facilitar el deployment de aplicaciones. Su concepto es crear contenedores de aplicación con todas las dependencias incluidas. Para quien sepa un poco del tema, estos son una especie de microsistemas, un chroot con esteroides, en donde las aplicaciones tienen un entorno ideal para funcionar.

Desde su lanzamiento el proyecto docker ha contado con el entusiasmo de grandes compañias y su proceso de desarrollo es muy acelerado. Incluso se ha creado una distribución Linux sólo para la gestión de contenedores como es CoreOS. Otras distros que intentan automatizar todo mediante docker y de hecho cambiar la manera en que son vistos los sistemas operativos son Red Hat Atomic, y Snappy Ubuntu. El proyecto docker es una de las promesas que promete revolucionar la arquitectura de los sistemas operativos, y tiene muchas ventajas, aunque por ahora sigue en constante desarrollo, y no se ve todavía tanto en la producción. Aunque hay compañias que ya ofrecen servicios relacionados con docker.


Debian Jessie ya es la nueva versión de Debian estable y docker estaba en las repos de Debian en el pasado sólo que el mantenedor del paquete decidió sacarlo ya que el ciclo de desarrollo era muy rápido  por lo que no se podía mantener una versión estable en Debian, es por eso que se planea incluirlo en el repositorio backport de Jessie tan pronto como este disponible.

Por ahora si queremos usar docker en Debian Jessie es fácil, solo hay que seguir las instrucciones que vienen para ubuntu.

```
curl -sSL https://get.docker.com/ | sh

```

Nota: Esto sólo lo probé en Jessie, pero debería de funcionar en Wheezy, si estás usando un kernel superior al 3.13

Con eso debería de bastar para que docker esté instalado en nuestro sistema. Una nota, Debian Jessie por defecto usa Systemd,Ubuntu Trusty usa upstart, así que el manejo de los contenedores en Debian se hace difernete. En mi caso quité systemd y use Sysvinit. Se puede usar Runit para automatizar el lanzamiento de contenedores en Debian.


Pueden seguir el thread sobre docker en Jessie, aquí:

<https://lists.debian.org/debian-release/2015/03/msg00685.html>
