.. title: Pensamientos sobre systemd
.. slug: pensamientos-sobre-systemd
.. date: 2014-12-20 04:14:56 UTC-06:00
.. tags: linux 
.. link: 
.. description: 
.. type: text

Administro algunos servidores, nada grande, sin embargo leo bastante sobre lo que pasa en el mundo Gnu/linux y me tomó por sorpresa todo lo que se está dando
gracias a systemd. Tengo que admitir que systemd en Arch linux me ha corrido sin problemas, y sus tiempos de booteo son muy pequeños. Sin embargo después de haber
manejado un sistema como Debian en servidores empiezo a entender el por que de esta polémica.

Systemd funciona bien en el escritorio y aunque no  tengo tanta experiencia en la administración de servidores si puedo entender que es demasiado complicado para ser 
una de las partes principales del sistema, el pid 1, con la información que tengo disponible me coloco en la postura antisystemd.

En general systemd debería de ser una opción más, pero de ninguna manera una imposición. Yo encuentro confuso el que este intentando usurpar funciones como las de cron 
¿Que tiene de malo cron? ¿Acaso funciona mal?. También encuentro confuso lo de los logs binarios, he usado esta función dos veces en mi vida a lo mucho, pero mi 
computadura de escritorio se prende y apaga todos los dias, solo corre procesos de escritorio y no la mantengo prendida meses ni dependo de ella para funciones 
cruciales. Mi experiencia con systemd se limita a mi Arch linux. 

Una reflexión, con system V en Debian, nunca me falló nada, de hecho sólo me preocupo de este sistema a la hora del arranque, que en un servidor bien puede ser una vez 
cada año, sin embargo SystemD esta ahí todo el tiempo, con su omnipresencia impuesta. Me parece triste que Gnu/linux y un proyecto comunitario como Debian hayan llegado 
al extremo de una cuasi guerra civil por este programa. Tampoco me parece correcto la imposición de systemd sobre la mayoria de las distros linux.

Tengo un poco de miedo al futuro ya que aposté por Debian para todos mis servidores, no se si hice bien, por ahora seguirán corriendo tranquilos, pero cuando llegue la 
hora de cambiar a Jessie sentiré nervios, espero por el bien de todos que haya Jessie-lts como ya lo hay con squeeze, para tener mucho tiempo.
Una vez en Jessie quizá les ponga systemd, pero si de alguna manera puedo evitarlo no lo haré. Quizá una vez que use systemd en servidores me de cuenta de sus bondades.
Lo único que esperaría es que tenga la opción de elegir. No me queda claro, pero al día de hoy aún existe un paquete de systemV en Jessie, no se 
si se quedará ahí y se pueda evitar systemD. Quizá el proyecto Devuan sea la respuesta, quiza otra distro.

Hasta ahora tengo puesta la vista en Alpine linux que usa Openrc, paquetes binarios (no como Gentoo) y que opta por un diseño minimalista y seguro, este será mi escape 
en caso de emergencia, por lo mientras estoy tranquilo y disfruto la vida, que venga lo que tenga que venir. No se donde se está metiendo Gnu/linux 
cuando sus principales distros empresariales, Red Hat y Suse están usando Systemd. Espero que no empieze la catastrofe. El tiempo lo dirá.
