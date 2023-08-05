ezcurses
========

library to help with curses programming

Installation
------------

From the project root directory::

    $ python setup.py install

Usage::

    from ezcurses import ezscreen

    with ezscreen() as scr:
        w, h = scr.max_size()
        win1 = scr.new_win(orig=(0, 0), size=(10, 10))
        win2 = scr.new_win(orig=(10, 0), size=(10, 10))
        win1.border()
        win2.border()
        win1.background('+', color='red')
        win2.background('.', color=('green', 'blue'))
        win1.draw()
        win2.draw()
        s = win1.getstr(0, 0, echo=True)
        win2.write(s, (0, 0), color=('red', 'black'))
        win2.draw()
        win1.write('Press q to quit', (0, 0), color=('black', 'red'))
        while win1.getkey() != 'q':
            pass


Release Notes
-------------

:0.1.2:
  - Make positional optional and a keyword ``pos`` for the ``getstr`` function
  - Add documentation to API
:0.1.1:
  - Make position optional for ``write`` and default (0, 0) like other funcs
:0.1.0:
  - New features for curses windows
  - get input, string and characters
  - add strings with colors to the window
  - add borders
  - draw lines
  - change background
  - very functional as is
:0.0.1:
  - Project created
