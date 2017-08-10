#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @file  beispiel_py_modul.py
# @date  10 Aug 2017
# @author Aroldo Souza-Leite
"""
short description

long description
long description
"""


# # #  [imports]
import argparse


# # #  [logging]
def _make_slog():
    """
    Diese Funktion benutzt nur die Standardbibliothek.

    Da diese Funktion nur einen ad hoc Logger erstellt,
    importier sie innerhalb der Funktion, sehr untypischerweise.
    Normalerweise sollten die imports modulweit gelten.
    """
    import sys   # non-module-global import: bad Python style!
    import time
    import logging
    logging.basicConfig(
        format = ("\n%(levelname)s:[%(name)s][%(asctime)s]"
                  "[%(module)s.%(funcName)s]\n%(message)1s"),
        stream = sys.stderr)
    _slog = logging.getLogger(__name__ + str(time.time()).replace('.','_'))
    _slog.setLevel(logging.DEBUG)
    return _slog

_slog = _make_slog() # _slog ist Modulweit sichtbar.


# # #  [cli]
def _parse_args(description="Process command line arguments."):
    """
    Handles the script command line arguments.

    Returns an object 'args' with the attributes corresponding
    to the command parameters.
    """
    parser = argparse.ArgumentParser(description = description)
    parser.add_argument(
       # arguments without a name in the command line,
       # also called positional arguments.
       'args_positional',
       # parameter name used only in the help string:
       metavar='P', 
       type=str, 
       # None,one or many parameters are required:
       # 
       nargs='*',
       help='The positional paramenters. (None, one or many)')
    parser.add_argument("--foo", nargs=2, type=str
    # per default, --foo is not a required argument
                        )
    ### the argument -b is required. That is, if you comment out the 
    # parser.add_argument below, the _script will issue an error if
    # the parameter -b is empty. 
    # parser.add_argument("-b","--bar", nargs=1, required=True, 
    #                     type=str, help="alternative usage: --bar=somebar" )
    parser.add_argument(
       # This is an argument without its own parameters:
       '--arg_func', 
       # This is the attribute created by this command line parameter:
       dest='do_something',
       # This is how the parser gets an object to store in the 'dest':
       action='store_const',
       # This the constant object, stored in 'dest' as required by 'action'.
       # In this case, the constant object happens to be a Python function!
       const=lambda x:x, 
       # This the constant object, stored in 'dest' as required by 'action',
       # if the parameter --sum  is absent. In this case also, the constant
       # object to be stored in 'dest' is also a Python function.
       default=lambda x:x,
       help='This attribute contains a function.')
    args = parser.parse_args()
    return  args

_args = _parse_args()


def say_hello(you):
    """
    Says hello to you.
    """
    print('hello', you)
    


# # #  [script]
def _script():
       """
       Intended to be invoked if this module is called as a script.
       """
       # hier können Funktionen des Moduls aufgerufen werden.
       # hier können alle Modul-globale Objekte benutzt werden.
       message = "parsed cli arguments:{}".format(_args)
       _slog.info(message)
       for somebody in _args.args_positional:
           say_hello(somebody)

if __name__=='__main__':
   _script()
del _script
