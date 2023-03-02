¿Qué es lo que observa?
=============
Nunca hay suficiente redundancia para garantizar la continuidad de la información.

Este es un experimento, una herramienta para evitar perder cosas que en algún momento nos resultaron interesantes.
Hay un [script de linea de comandos](http://github.com/etnalubma/spill) con el que envías cosas a algo que se parece a un blog y está hosteado en http://ltmo.com.ar/

Este repositorio contiene tanto el código del sitio.

El sitio está hecho en [django](http://djangoproject.com) y tiene muy pocas dependencias, la mejor manera de tener una instancia corriendo es con pip

        $ pip install -e .

Ahora sólo debés sincronizar la base de datos y correr el sitio:

        $ ./manage.py syncdb
        $ ./manage.py runserver

¿Y qué pasa con el resto?
---------------

Todo lo que envíes con spill se manda a ltmo.com.ar ahí vamos a ir agregando cosas a medida que tengamos más tiempo para perder aceite.

No sabemos muy bien de que se trata todo esto pero somos lo que hacemos.

