¿Qué es lo que observa?
=============

Este repositorio contiene tanto el código del sitio.

Asumimos una máquina en algún linux corriendo alguna versión reciente de python.
Debería andar en cualquier lado que python sea instalable.

El sitio está hecho en [django](http://djangoproject.com) y tiene muy pocas dependencias, la mejor manera de tener una instancia corriendo es:

### para desarrollo:

    $ virtualenv ltmo
    $ source ltmo/bin/activate
    (ltmo)$ cd /path/to/clone
    (ltmo)$ pip install -r requirements.txt
    (ltmo)$ python setup.py develop
    (ltmo)$ ltmo migrate
    (ltmo)$ ltmo runserver

Una instancia queda corriendo en http://localhost:8000.

### frontend

Usamos un toolchain que consta de [npm](http://npm.io), [grunt](http://grunt.io), [bower](http://bower.io). Se instala más o menos así:

    $ cd /path/to/clone
    $ npm install  # descarga dependencias de desarrollo.
    $ bower install  # descarga bibliotecas para el cliente.
    $ grunt  # observa cambios en una serie de archivos y ejecuta acciones.

Esto resulta en una carpeta `static` en la raíz de tu copia local.

### para producción:

    $ pip install ltmo  # sudo si es necesario.

Vea [[notas de instalación|Deployment]] para saber como instalarlo en un servidor en particular.



## ¿Y qué pasa con el resto?

Todo lo que envíes con spill se manda a ltmo.com.ar ahí vamos a ir agregando cosas a medida que tengamos más tiempo para perder aceite.

No sabemos muy bien de que se trata todo esto pero somos lo que hacemos


[![Bitdeli Badge](https://d2weczhvl823v0.cloudfront.net/tutuca/ltmo/trend.png)](https://bitdeli.com/free "Bitdeli Badge")
