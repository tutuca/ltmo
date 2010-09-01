¿Qué es lo que observa?
=============
Nunca hay suficiente redundancia para garantizar la continuidad de la información.

Este es un experimento, una herramienta para evitar perder cosas que en algún momento nos resultaron interesantes.
Hay un [script de linea de comandos](http://github.com/tutuca/ltmo/raw/master/bin/spill.py) con el que envías cosas a algo que se parece a un blog y está hosteado en http://ltmo.com.ar/

Este repositorio contiene tanto el código del sitio como el script.

El sitio está hecho en django y tiene muy pocas dependencias que mantenermos con con pip:

        $ pip install -r requirements.txt -E /algun/path/para/un/virtualenv/
        
Si no tenés pip y virtualenv (por qué no???):

        $ sudo easy_install pip
        $ sudo easy_install virtualenv

Ahora podés correr el script así:

        $ cd ltmo/
        $ ./bin/spill.py -h
        Usage: ./spill.py [options]


          /     \                                     
          vvvvvvv  /|__/|                             
              I   /O,O   |                            
              I /_____   |      /|/|                 
             J|/^ ^ ^ \  |    /00  |    _//|          
              |^ ^ ^ ^ |W|   |/^^\ |   /oo |         
               \m___m__|_|    \m_m_|   \mm_|         


        Options:
          -h, --help            show this help message and exit
          -m TEXT, --message=TEXT
                                the message to send to the site, reads from stdin if
                                None
          -t TAG,[TAG,...], --tags=TAG,[TAG,...]
                                tags associated to the message
          -a NAME, --author=NAME
                                author associated to the message, not to be confused
                                with source
          -s NAME, --source=NAME
                                source associated to the message, not to be confused
                                with author
          -r HOST:PORT[/PATH], --remote-server=HOST:PORT[/PATH]
                                destination HOST, PORT and PATH of server, useful for
                                debugging

    Las cucarachas lograron con exito su plan, echando a los pestilentes
    sangre caliente de sus cajas de cemento.  Ahora el hombre es una especie
    errante en el espacio, un vagabundo errante en las estrellas.


¿Y qué pasa con el resto?
---------------

Todo lo que envíes con spill se manda a ltmo.com.ar ahí vamos a ir agregando 
cosas a medida que tengamos más tiempo para perder aceite

El código es libre y se explica solo. Así que no preguntes por ayuda o explicaciones, nosotros tampoco sabemos de que se trata
