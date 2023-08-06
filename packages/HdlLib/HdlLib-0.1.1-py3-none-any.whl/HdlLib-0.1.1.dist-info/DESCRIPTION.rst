
HdlLib  
=========

HdlLib is a Python module for dealing with VHDL files :
* Manage a VHDL library,
* Assemble IPs,
* Generate testbenches,
* Parse VHDL entities,
* Generate synoptics of entity interfaces.

***

> This is the README file for the Python project.

***

Installation :
--------------

### From Pypi (recommanded)

```
pip install HdlLib
```

This will setup the commands to be available from a terminal and install the Python package.

HdlLib is only compatible with Python3.x (incompatible with Python2).

Usage :
-------

### By command line
`HdlLib --help` will print the available sub-command options. Currently, these are available :

| Sub-command     | Description                                                                 |
|-----------------|-----------------------------------------------------------------------------|
| addlib          | generate *.xml library file from VHDL sources (interactive).                |
| tbgen           | generate Alstom's tbgen testbench files (VHDL + scenario file) from a VHDL sources (interactive) and a synoptic *.png image of the entity parsed.      |
| synoptic        | generate a synoptic *.png image of the entity parsed from VHDL source file. |
| parseregression | perform regression test of the VHDL parser on every VHDL file found in the given directory (recursively). |

### As a python package

See the documentation.

***

>HdlLib is distributed with a GPLv3 license.
See LICENSE.txt for details.

***

Matthieu PAYET <matthieu.payet@free.fr>

More on Matthieu's website : https://mpayet.net




