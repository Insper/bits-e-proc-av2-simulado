#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""

import pytest
from myhdl import *
from ula_aux import *

try:
    from telemetry import telemetryMark
    pytestmark = telemetryMark()
except ImportError as err:
    print("Telemetry não importado")

def exe1(a, b, c, q):
    @always_comb
    def comb():
        q.next = 0

    return instances()


def exe2(p, q, r, s):
    @always_comb
    def comb():
        s.next = 0

    return instances()


def exe3(x1, x0, y1, y0, z3, z2, z1, z0):
    @always_comb
    def comb():
        z0.next = 0
        z1.next = 0
        z2.next = 0
        z3.next = 0

    return instances()


def exe4_ula(a, b, inverte_a, inverte_b, c_in, c_out, selecao, zero, resultado):
    @always_comb
    def comb():
        resultado.next = 0

    return instances()
