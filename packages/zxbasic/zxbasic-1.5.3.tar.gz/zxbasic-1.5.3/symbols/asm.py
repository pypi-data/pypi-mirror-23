#!/usr/bin/python
# -*- coding: utf-8 -*-
# vim: ts=4:et:sw=4:

# ----------------------------------------------------------------------
# Copyleft (K), Jose M. Rodriguez-Rosa (a.k.a. Boriel)
#
# This program is Free Software and is released under the terms of
#                    the GNU General License
# ----------------------------------------------------------------------

from .symbol_ import Symbol


class SymbolASM(Symbol):
    ''' Defines an ASM sentence
    '''
    def __init__(self, asm, lineno):
        Symbol.__init__(self)
        self.asm = asm
        self.lineno = lineno
