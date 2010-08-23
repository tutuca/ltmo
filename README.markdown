¿Qué es lo que observa?
=============
Nunca hay suficiente redundancia para garantizar la continuidad de la información

Sumamos una herramienta. 

Simple, ante todo. usamos $less  y esas cosas.

Hay un script que publica lo que le pases por stdin y lo trata de mandar, junto 
con todo lo que podamos juntar.
El código es libre y se explica solo.

una vez después de clonar el repo, pueden probar de enviar un post 


$ bin/spill.py -h
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
                        
                        

