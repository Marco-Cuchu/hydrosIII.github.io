.. title: ¿Cómo se hizo este blog?
.. slug: como-se-hizo-este-blog
.. date: 2014-11-04 22:16:30 UTC-06:00
.. tags: nikola, python 
.. link: 
.. description: 
.. type: text

He tenido la idea de empezar un blog para documentar ciertas cosas, pero 
nunca me he decidido a hacer nada. Claro que ahora parecer me he 
decidido por una técnica mediamente dificil de escribir un blog.

Se me han ocurrido un montón de ideas, desde hostear mi blog en mi 
propio servidor, sobretodo para propósitos didácticos hasta abrir una 
cuenta en wordpress, lo cual ya hice, pero no creo que la utilize. Al 
final me entere de que puedes tener una página en Github. Bueno así no tengo 
cosas en todos lados. Tampoco es que tenga muchas cuentas, pero odio 
estar recordando la contraseña para todas ellas. Y tengo una cuenta en 
gihub, con casi nada de código, lo único que he subido es la plantilla 
latex que utilice para mi tesis, pero al menos así no tengo que recordar 
otra contrseña, y me gustaría aprender a usar git.


Este blog fue hecho usando nikola. 

¿Qué es Nikola?

Pues, no tengo mucha idea, pero digamos que es un wordpress mas geek. Es 
decir que aún hay que editar algunas cosas a la manera antigua cuando 
las páginas aún se hacían en html. Sólo algunas ya que en realidad es muy fácil escribir un post.
La ventaja es que crea páginas web estáticas y no necesita guardar cosas complicadas en una base de datos. Las bases de 
datos son  omnipresentes hoy día y son muy útiles para guardar todos 
los números de tarjeta de crédito de los clientes de un banco y crear un 
sistema que haga busquedas de ellos. Pero si sólo vas a crear un simple 
blog, no creo que sea tan necesaria la base de datos.

En fin. Nikola es un generador de páginas estáticas escrito en Python, un lenguaje de programación popular.

Nikola primeramente genera las páginas en cualquier computador donde 
esté instalado, y luego es posible subirlas a un hosting. La parte 
interesante es que puede ser cualquier cosa que corra un servidor web. 
No es necesario que el hosting soporte X o Y paquetes. Y claro el 
trabajo se realiza en tu computador. La clara desventaja es que si no 
se tiene un computador con Nikola es dificil escribir, pero como ahora 
tengo una computadora portatil de uso habitual, creo que esto no es 
tanto problema.

¿Como instalarlo?

Se necesita tener python instalado el cual está en las distribuciones 
linux. Sin embargo se puede instalar en cualquier sistema operativo. 
Para instalarlo se necesita el instalador de paquetes python pip. 
Primero se instala pip, y pip instala Nikola. 

Los siguientes comandos se necesitan hacer como root

Para logearse como root hay que escribir:

su

En Debian:

apt-get install python-pip

En Arch linux

pacman -S python-pip

En arch linux (la cual uso) también se encuentran en AUR, como hay dos 
paquetes en AUR, uno con python 3 y otro con python 2 esto me confundió
y termine siguiendo la ruta de pip, que me parecio mas simple, aunque no 
me gusta que pip instale cosas en mi sistema, además de que no conozco este programa bien,
pero de que instala cosas fácil, las instala.

Nikola se instala así::

	pip install Nikola

Hay instrucciones que indican que hay que hacer un entorno virtual de 
python, pero al final lo dejé por que lo quería es publicar, ya veré que 
pasa con la suciedad del sistema después.

Las intrucciones de instalación se pueden encontrar en la página web de 
Nikola: http://getnikola.com/handbook.html#installing-nikola

Algo que no detalla en la página, es que una vez hecho esto se debe
salir del usuario root y trabajar como usuario normal para iniciar la 
página web. Si no los permisos de los archivos se hacen un desastre.

asi que podemos escribir::

	exit

luego se puede proseguir con la guia de configuración::

	nikola init mysite

donde mysite es el nombre de la página, se creará una carpeta con este 
nombre conteniendo la página web, en el directorio desde donde se corra 
el anterior comando. Yo me pase buscando algunos minutos para saber donde estaba 
la página. Por ejemplo puedes cambiar mysite por "mi-primer-blog", o 
algo que sea fácil de recordar. Nikola hace algunas preguntas, y la 
verdad es complicado contestarlas, sobretodo si no se tiene idea de 
donde se va a poner la página. Lo único que recuerdo que seleccioné 
los comentarios google groups. Lo demás lo hice un poco al azar. Creo 
que se puede cambiar después::

	cd mysite

Posteriormente podemos iniciar el primer post, con::

	nikola new_post

y luego podemos encontrar el post en el directorio de post dentro del 
directorio de Nikola, este lo podemos editar en cualquier editor de 
texto, para este post yo estoy usando nano. Se puede usar alguna 
sintaxis de markdown, pero por ahora no sé lo que es eso. Asi que esto 
es puro texto.

Una vex que terminamos de escribir el post, damos la orden::

	nikola build

y para ver nuestra pagina:

	nikola serve 

Ahora puedo apuntar mi navegador a 127.0.0.1:8000, y aparecerá la 
nueva página. No parece tan díficil, al menos logré escribir esto y no 
se ve tan mal. El tema por default de Nikola también me gusta, lo que me 
ahorra tener que saber como cambiarlo.

Si se quiere que las páginas se actualizen solas en lugar de reconstruir 
el sitio entero, se puede instalar (de nuevo como root)::

	pip install livereload
	pip install requests

y usar::

	nikola auto

en el directorio de la página.


OJO
--------------------------------------------

Si nikola da errores, se puede instalar desde git para tener lo último, 
para mi fue necesario ya que daba un error al construir la página. 
Obviamente esto no es necesario si todo funciona bien.

Para instalarlo desde git primero se debe desinstalar nikola desde pip

Nos logueamos como root::

	su

Luego desinstalamos nikola::

	pip uninstall nikola

y salimos de root::

	exit

Luego clonamos el repo con git. Hay que instalar git antes desde luego::

	git clone git://github.com/getnikola/nikola.git

y de nuevo como root, instalamos nikola::

	cd nikola
	pip install -r requirements-full.txt
	pip install .


La línea de requerimientos no es necesaria si ya habíamos instalado con 
pip, ya que estos ya se encuentran instalados.

Todo este entrar y salir de root es para que los permisos de archivos 
queden bien.

