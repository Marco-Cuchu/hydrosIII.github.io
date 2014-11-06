.. title: Actualizar openerp, moviendo la instalación de launchpad a github.
.. slug: actualizar-openerp-moviendo-la-instalacion-de-launchpad-a-github
.. date: 2014-11-05 00:24:19 UTC-06:00
.. tags: draft, openerp, python, git
.. link: 
.. description: 
.. type: text

Hace poco Openerp, mudó su plataforma donde es construido de launchpad a
github. Esto me parece que fue una decisión positiva ya que git me
parece mejor que bzr, pero en realidad no conozco ninguno de los dos, es
sólo una opinión a la ligera.

Lo que si hizo es cambiar muchas cosas, en primer lugar su nombre pues
ahora se llama odoo, lo que significo el movimiento de todas las
páginas web, y yo no me había enterado muy bien hasta que entre a
reportar un problema.

Ahora todo el desarrollo esta en github, dejando a muchas comunidades de
openerp sin migrar y en launchpad incluyendo la de México. Bueno, fue un
relajo.

Entre las cosas que rompió fue una clara vía de actualización para mi
servidor openerp, ya que fue instalado desde fuentes usando bzr, desde
la rama ocb de openerp. La rama ocb, es una rama que hace un backport
más rápido de los bugs que la rama principal de openerp, por lo que
decidí instalarla en mi servidor.

Pasaron seis meses desde que instale openerp y un día me decidí a
actualizar el servidor, para  beneficiarme de los últimos parches, pero
me encontré con que todo era diferente, y el desarrollo se había
detenido en launchpad.

Antes en launchpad se tenían tres ramas de addons de openerp, la web, la principal y la base.
Estos los instale en tres capetas diferentes.
