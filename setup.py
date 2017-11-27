# -*- coding: utf-8 -*-

import sys
from distutils.core import setup

kwargs = {}
if 'py2exe' in sys.argv:
    import py2exe
    kwargs = {
        'console' : [{
            'script'         : '__init__.py',
            'description'    : 'Cuatro en linea.',
            'icon_resources' : [(0, 'ejecutar.ico')]
            }],
        'zipfile' : None,
        'options' : { 'py2exe' : {
            'dll_excludes'   : ['w9xpopen.exe'],
            'bundle_files'   : 1,
            'compressed'     : True,
            'optimize'       : 2
            }},
         }

setup(
    name='Cuatro en Linea',
    author='Ernesto Rojas',
    author_email='ernesto20145@gmail.com',
    **kwargs)