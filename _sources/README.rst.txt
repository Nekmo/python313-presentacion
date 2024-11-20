.. image:: https://raw.githubusercontent.com/Nekmo/python313-presentacion/master/logo.png
    :width: 100%

|

.. image:: https://img.shields.io/github/actions/workflow/status/Nekmo/python313-presentacion/build.yml?style=flat-square&branch=master
  :target: https://github.com/Nekmo/python313-presentacion/actions?query=workflow%3ABuild
  :alt: Latest CI build status


=================================
¿Qué hay de nuevo en Python 3.13?
=================================
Lo más nuevo de Python se encuentra a la vuelta de la esquina cargadito de novedades, que veremos en una charla amena y
concisa con un repaso muy rápidito. Nuevas mejoras en los mensajes de error (¡mejorando todavía más lo ya iniciado en
versiones anteriores!), un compilador JIT experimental para Python (similar a Numba, con el que podemos lograr más
velocidad), mejoras en el recolector de basura (aunque primero explicaremos de qué va esto), ¡soporte para iOS!
¡¡soporte experimental sin GIL!! (sí sí, como lo oís), cambios y mejoras en los módulos de la biblioteca estándar...
¡No te quedes atrás en lo más nuevo de Python, en esta charla llena de ejemplos de código y mucho humor!

La presentación está `disponible online <https://nekmo.github.io/python313-presentacion/>`_ ya compilada
para su visualización.


Requisitos y contenido
----------------------
Para esta presentación es necesario conocer el lenguaje, pero no las novedades de Python 3.13. Tampoco es necesario un
nivel avanzado de Python, ya que se explicarán los cambios de una forma sencilla y para todos los públicos. La charla
se divide en los siguientes apartados:

* Bienvenida e introducción.
* Comparativa de velocidad.
* Explicación del GIL.
* Compilador JIT.
* Mejoras en la línea de comandos.
* Mejoras en los mensajes de error.
* Mejoras en typing.
* Mejoras en locals().
* Otros cambios.
* Eliminaciones.
* Plataformas soportadas.
* Punto final a la presentación.
* Agradecimientos asociaciones, colaboradores y público.
* Formas de contacto.
* Turno de preguntas.

Motivación
----------
Aprovechando el lanzamiento de Python 3.13, la comunidad de `Python Málaga <https://www.python-malaga.es/>`_ se reúne
para conocer las novedades de la nueva versión del lenguaje, de una forma amena y divertida. Se profundiza en los
puntos más importantes, se explica de forma sencilla las partes más complejas y se resuelven las dudas del público,
todo con ejemplos de código.


Acerca de
---------
Esta charla pertenece a una serie realizada por la asociación Python Málaga, la cual realiza cada año desde Python 3.11
con el fin de conocer las novedades del lenguaje. Las dos charlas anteriores se encuentras disponibles en:

* https://github.com/Nekmo/python312-presentacion
* https://github.com/Nekmo/python311-presentacion

La presente charla ha sido realizada para `Python Málaga <https://www.python-malaga.es/>`_, con fecha de presentación
el 14 de noviembre de 2024 junto con `PyData Málaga <https://www.meetup.com/es/PyData-Malaga/>`_ y en colaboración
con `Plytix <https://www.plytix.com/>`_.

Compilación
-----------
Para compilar desde el código fuente se requiere Python 3 instalado, estando probado sólo bajo Python 3.12. Se
recomienda ejecutar los siguientes pasos en un
`virtualenv <https://nekmo.com/es/blog/python-virtualenvs-y-virtualenvwrapper/>`_::

    # Clonar proyecto
    git clone https://github.com/Nekmo/python313-presentacion.git
    cd python313-presentacion
    # Instalar dependencias
    pip install -r requirements.txt
    # Compilar ficheros de estilos
    sassc _static/theme.scss _static/theme.css
    # Compilar presentación
    make revealjs

Tras la compilación puede verse los ficheros resultantes en el directorio ``_build``.


Copyright
=========
Licencia MIT. Ver fichero ``LICENSE.txt``.

Nekmo 2024.

