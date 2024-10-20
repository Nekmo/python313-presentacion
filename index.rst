
.. toctree::
   :glob:
   :hidden:

   *

.. _intro:

#####################################
¿Qué hay de nuevo en **Python 3.13**?
#####################################

.. image:: images/python-logo.*
  :width: 200

.. revealjs-notes::

  Hola a todos.



Sobre mí **Nekmo**
==================

.. revealjs-section::
    :data-transition: concave
    :data-background-color: #2b5b84
    :data-background-gradient: linear-gradient(180deg, rgba(10,59,102,1) 0%, rgba(43,91,132,1) 30%)

+------------------------------------+
|                                    |
| .. image:: images/cara.svg         |
|   :width: 200px                    |
|                                    |
| *Programador Python*               |
|                                    |
+------------------------------------+

.. revealjs-notes::

   Soy Juan José, más conocido en redes como Nekmo, y puede que me conozcáis de charlas anteriores para Python Málaga,
   como...



Charlas anteriores
==================

(imágenes de charlas anteriores)

.. revealjs-notes::

   ¿Qué hay de nuevo en Python 3.11? o ¿Qué hay de nuevo en Python 3.12? Pues bien, hoy no hay sorpresas.



¿Qué hay de nuevo en **Python 3.13**?
=====================================

.. revealjs-notes::

   Vamos a hablar de las novedades de Python 3.13. Y en esta ocasión vamos a hacerlo de la mano de PyData Málaga, con
   Plytix como patrocinador.



Python Málaga + PyData Málaga
=============================

(logos Python Málaga, PyData Málaga y Plytix)

.. revealjs-notes::

   Por lo que no sólo tendremos novedades de Python 3.13, ¡también tendremos muchos datos! Veremos con números cómo de
   rápido es Python 3.13, como seguro que os gustará.



¿Más rápido?
============

.. revealjs-notes::

   Y es que siempre que sale una nueva versión de Python, me encanta hablar de cuááánto más rápido es. Pero en esta
   ocasión es un poco más complicado de comentar...



Python 3.13 retrasado
---------------------

https://www.phoronix.com/news/Python-3.13-rc3-Released

.. revealjs-notes::

   Imaginaros, que Python 3.13 se retrasó en el último minuto, por un problema de rendimiento por su recolector de
   basura, lo cual obligó a retrasarlo una semana.



¿Cuánto más rápido es?
----------------------

.. revealjs-notes::

   Pero finalmente salió el pasado 7 de octubre. Y sí, podemos decir que es más rápido... pero con matices. Aquí tenemos
   los datos del Python 3.13 de serie comparado con Python 3.12, aunque aquí tenemos dos versiones más, una con el
   JIT experimental, sin mucha mejora, y otra con GIL, que es incluso más lenta.



Muerte
======

.. revealjs-notes::

   Espera, ¿cómo que ahora sin GIL es más lento? ¿Pero esto no iba a ser la releche de rápido y nos iba a salvar a
   todos?



Ahora sin GIL
-------------

.. revealjs-notes::

   En realidad no hemos sido muy justos en este test, porque lo hemos probado con un solo hilo, donde el soporte sin
   GIL no es capaz de relucir su potencial. Pero si no sabéis de qué va todo esto vamos a resumirlo.



GIL
---

.. revealjs-notes::

   El GIL, que como su nombre dice es un lock global enooorme a nivel del intérprete, es el responsable de ir cediendo
   el control entre los diferentes hilos de Python. Esto tiene cosas buenas, como que es súper fácil programar con
   concurrencia, porque simplemente no hay una concurrencia real (risas).



Cediendo el control
-------------------

https://miro.medium.com/v2/resize:fit:828/format:webp/1*wd0z1C75VsxD42QdKqCjpA.gif

.. revealjs-notes::

   En resumen, todo se hace en un solo núcleo de tu CPU, y Python va cediendo el control con el GIL, cada vez un
   poquito a cada hilo de Python.



Un solo núcleo
--------------

https://tenor.com/es/view/meme-gif-25244209

.. revealjs-notes::

   Lo malo y evidente de esto, es que sólo trabajamos con un único núcleo de nuestra CPU, y el resto sólo se dedican
   a animar al único que trabaja.



Python sin GIL
--------------

.. revealjs-notes::

   Hacer que el intérprete de Python trabaje con concurrencia es complicado, ya que dificulta su programación, teniendo
   que coordinar los hilos para que no se pisen entre ellos. Esas comprobaciones para que funcione con varios hilos,
   afecta al rendimiento con un solo hilo, aunque por contra es más rápido con varios hilos.



Python 3.13 sin GIL con hilos
-----------------------------

.. revealjs-notes::

   Como podemos ver aquí, ya en esta gráfica con varios hilos, Python 3.13 sin GIL es MUCHO más rápido que cualquier
   otra versión, porque ahora sí se aprovechan todos los núcleos de la CPU. El soporte sin GIL es una característica
   experimental, y requiere que el intérprete sea compilado con soporte para ello.



Nuevo JIT experimental
======================

.. revealjs-notes::

   Lo mismo sucede con el nuevo JIT experimental, el cual requiere compilarse con soporte para ello.



Compilador Just-In-Time
-----------------------

.. revealjs-notes::

   Para quienes no lo conozcáis, un compilador Just-In-Time es un compilador que compila el código bytecode a código
   máquina en tiempo de ejecución, al igual que hacen la máquina virtual de Java o se hace con Numba en Python. Esto
   podría permitir en un futuro que Python sea más rápido, pero de momento la mejora ha sido bastante pequeña. Pero no
   os preocupéis, estamos sólo en el comienzo.



Python 3.13 con JIT experimental
--------------------------------

.. revealjs-notes::

   Recuperando las gráficas de antes y ampliándolas, podéis ver que la mejora de momento es mínima. Pero podéis ir
   probándolo y reportar errores.



Mejoras en la línea de comandos
===============================

.. revealjs-notes::

   Pero no sólo ha habido mejoras de velocidad, ¡también han habido muchos cambios en la línea de comandos!


¡Colores!
---------

.. revealjs-notes::

   Para empezar, ¡ahora tenemos colores! (guauuuu).



Copiar y pegar más fácil
------------------------

F2: Historial
F3: Modo pegar

.. revealjs-notes::

   Y si habéis tenido problemas copiando y pegando de la línea de comandos, ahora es cosa del pasado. Con F2 podéis ver
   todo el histórico sin los prompts, y con F3 podéis activar el modo pegar. También se ha mejorado la edición con
   múltiples líneas cuando se recupera del historial pulsando arriba.


Modo ayuda
----------

F1: Ayuda

.. revealjs-notes::

   Y si necesitáis consultar la documentación, ahora podéis hacerlo pulsando F1, en vez de utilizar help().



Funciones de línea de comandos sin paréntesis
---------------------------------------------

help
exit
quit

.. revealjs-notes::

   Y para más ayuda de los que están empezando, ahora las funciones de línea de comandos se pueden llamar sin
   paréntesis, para que sea aún más fácil.



Mejoras en mensajes de error
============================

.. revealjs-notes::

   No sólo ha cambiado la línea de comandos, sino también los mensajes de error cuando estamos programando.



Nombres de módulo ya en uso
---------------------------

.. revealjs-code-block:: python
    :data-line-numbers:

    $ python random.py
    Traceback (most recent call last):
      File "/home/me/random.py", line 1, in <module>
        import random
      File "/home/me/random.py", line 3, in <module>
        print(random.randint(5))
              ^^^^^^^^^^^^^^
    AttributeError: module 'random' has no attribute 'randint' (consider renaming '/home/me/random.py'
    since it has the same name as the standard library module named 'random' and the import system
    gives it precedence)


.. revealjs-notes::

   Por ejemplo, si llamamos a nuestro módulo como uno ya en uso, por ser del sistema o de un paquete instalado, y
   tenemos un error de importación por ello, nos sugerirá que cambiemos el nombre de nuestro módulo.



Equivocaciones en nombres de parámetros
---------------------------------------

.. revealjs-code-block:: python
    :data-line-numbers:

    >>> "Better error messages!".split(max_split=1)
    Traceback (most recent call last):
      File "<python-input-0>", line 1, in <module>
        "Better error messages!".split(max_split=1)
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^
    TypeError: split() got an unexpected keyword argument 'max_split'. Did you mean 'maxsplit'?

.. revealjs-notes::

   También muy útil, es que si nos equivocamos en el nombre de un parámetro, y hay uno con nombre similar,
   nos sugerirá el correcto.


Mejoras en typing
=================

.. revealjs-notes::

   Y si utilizáis typing, también ha habido varias mejoras.



**PEP 696**: Tipos por defecto en TypeVar, ParamSpec y TypeVarTuple
-------------------------------------------------------------------

.. revealjs-code-block:: python
    :data-line-numbers:

    T = TypeVar("T", default=int)

    @dataclass
    class Box(Generic[T]):
        value: T | None = None

    reveal_type(Box())                      # type is Box[int]
    reveal_type(Box(value="Hello World!"))  # type is Box[str]

.. revealjs-notes::

   Tipos por defecto en TypeVar, ParamSpec y TypeVarTuple. Esto es especialmente útil para quienes usáis los genéricos.
   Si no se define un parámetro en un genérico, ahora se puede definir un tipo por defecto, como en este ejemplo.
   Este caso de uso es común en proyectos como NumPy o TensorFlow.



**PEP 702**: Decorador warnings.deprecated()
--------------------------------------------

.. revealjs-code-block:: python
    :data-line-numbers:

    from warnings import deprecated

    @deprecated("It is pining for the fiords")
    def norwegian_blue(x: int) -> int: ...

    @deprecated("Use Spam instead")
    class Ham: ...

    class Spam:
        @deprecated("There is enough spam in the world")
        def __add__(self, other: object) -> object: ...

.. revealjs-notes::

   El nuevo decorador deprecated() de la librería warnings, nos permite marcar funciones, clases o métodos como
   obsoletos, mostrándose por defecto un mensaje de advertencia cuando se utilizan. Adicionalmente, los validadores de
   tipos como mypy también mostrarán una advertencia.



**PEP 705**: elementos de sólo lectura en TypedDict
---------------------------------------------------

.. revealjs-code-block:: python
    :data-line-numbers:

    from typing import NotRequired, ReadOnly, TypedDict

    class Movie(TypedDict):
        name: ReadOnly[str]
        year: ReadOnly[NotRequired[int | None]]

.. revealjs-notes::

   Esta nueva característica es especialmente útil para quienes utilicéis TypedDict, como es mi caso. Ahora es posible
   marcar ciertas claves como de sólo lectura, en aquellos diccionarios que está previsto que sean modificados. Para
   ello, contamos con el nuevo tipo ReadOnly.



**PEP 742**: TypeIs
-------------------

.. revealjs-code-block:: python
    :data-line-numbers:

    from typing import TypeIs

    def is_int(x: object) -> TypeIs[int]:
        return isinstance(x, int)

.. revealjs-notes::

   Por último, tenemos TypeIs. Este caso es bastante específico, siendo una alternativa a TypeGuard. Es útil en
   funciones que devuelven True o False en función a un tipo. Si el objeto que pasamos a la función es igual al tipo
   que ponemos dentro del TypeIs, será True. Si no, será False. Así de simple.



**PEP 667:** Mejoras en locals()
================================

.. revealjs-code-block:: python
    :data-line-numbers:

    class C:
        x = 1
        sys._getframe().f_locals['x'] = 2
        print(x)  # Print 2

    def f():
        x = 1
        sys._getframe().f_locals['x'] = 2
        print(x)  # Print 1
    f()


.. revealjs-notes::

   Pasando a otro tema, también ha habido cambios importantes en locals(). Hasta ahora, el locals() se obtenía en
   tiempo real, y su modificación podía tener efectos indeseados. No sólo esto, sino que también era bastante lento.
   Ahora se ha cambiado su implementación, haciéndolo más consistente y rápido. Para los usuarios finales no tendrá
   implicaciones, pero para quienes usen la API en C, supone utilizar nuevas llamadas.



Otros cambios
=============

* Nueva excepción ``PythonFinalizationError``, si hay bloquos durante finalización.
* ``argparse`` ahora soporta marcar como obsoleto comandos, argumentos...
* Soporte para codificación z85, usada por ZeroMQ o Git, en el módulo ``base64``.
* ``copy.replace()`` copia y reemplaza del objeto copiado.
* ``dbm.sqlite3`` ahora es el motor por defecto de ``dbm``.
* El módulo ``os`` ahora incluye nuevas funciones *time file descriptors*.
* El módulo ``random`` ahora incluye ***línea de comandos**.

.. revealjs-notes::

   También ha habido otros cambios, los cuales nombraremos rápidamente. (leer).



Eliminaciones
=============

* Eliminación de módulos muertos de stdlib: ``aifc``, ``audioop``, ``cgi``, ``cgitb``, ``chunk``, ``crypt``...
* Eliminado **2to3** y **lib2to3** (obsoleto desde 3.11).
* Eliminado ``tkinter.tix`` (obsoleto desde 3.6).
* Eliminada ``locale.resetlocale()``
* Eliminados ``typing.io`` y ``typing.re``.
* Eliminados los descriptores tipo ``__get__`` y ``__set__`` de ``@classmethod``.



Plataformas soportadas
======================

* **PEP 730:** iOS está oficialmente soportado (tier 3).
* **PEP 738:** Android está oficialmente soportado (tier 3).
* wasm32-wasi pasa a ser tier 2.
* wasm32-emscripten ya no está oficialmente soportado.

.. revealjs-notes::

   También ha habido cambios en las plataformas soportadas. (Leer)



Listado completo de cambios
===========================

https://docs.python.org/3/whatsnew/3.13.html

.. revealjs-notes::

   Y para que no quedase muy larga la presentación, ha habido algunos cambios que he omitido, pero en la página oficial
   tenéis el listado completo.



¿Cuál es vuestra **mejora favorita**?
=====================================

.. revealjs-section::
    :data-background-color: #ffffff
    :data-background-image: _static/grid-bg.png
    :data-background-repeat: repeat-x
    :data-background-position: left top
    :data-background-size: auto
    :data-transition: zoom

.. revealjs-notes::

    Y tras todo esto, ¿cuál ha sido vuestro cambio favorito?



¡Muchas gracias a todos!
========================

.. revealjs-section::
    :data-background-gradient: linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab);

.. revealjs-notes::

    Y ante todo, ¡Muchas gracias a todos!


PyData
======

.. revealjs-notes::

   Y a PyData Málaga por hacer posible esta charla.



Plytix
======

.. revealjs-notes::

   Y a Plytix por su patrocinio.



Pyzzas
======

🍕

.. revealjs-notes::

   Y por las pizzas de después.



Python Málaga
=============

* 🤝 **Meetup:** `Python Málaga <https://www.meetup.com/es-ES/Python-Malaga/>`_.
* 🌐 **Sitio web:** `python-malaga.es <https://www.python-malaga.es/>`_.
* 🐦 **Twitter:** `@PythonMalaga <https://twitter.com/python_malaga>`_.

.. revealjs-notes::

   Para más charlas como esta, tenéis disponible nuestra comunidad de Python Málaga, a la cual podéis uniros en (leer).


QR
==

.. revealjs-notes::

   Y si queréis ver de nuevo esta presentación, la tenéis disponible en el código QR.



**Contactar**
-------------

.. revealjs-section::
    :data-background-color: #ffffff
    :data-background-image: _static/grid-bg.png
    :data-background-repeat: repeat-x
    :data-background-position: left top
    :data-background-size: auto
    :data-transition: zoom

* 🌐 **Sitio web:** `nekmo.com <https://nekmo.com>`_
* 📫 **Email:** `contacto@nekmo.com <mailto:contacto@nekmo.com>`_
* 🐦 **Twitter:** `@nekmocom <https://twitter.com/nekmocom>`_
* 📱 **Telegram:** `@nekmo <https://t.me/nekmo>`_
* 💡 **Jabber:** `nekmo@nekmo.org <xmpp://nekmo@nekmo.org>`_

.. revealjs-notes::

   A cualquier cosa, tenéis mi contacto disponible.
