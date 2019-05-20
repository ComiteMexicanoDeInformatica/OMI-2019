#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os
import collections

import libkarel
from kareltest import *

class Test(KarelTest):
    def test(self):
        world = self.world

        #Karel inicia en la casilla (1,1) viendo al norte.
        self.assertEqual(1, world.y)
        self.assertEqual(1, world.x)
        self.assertEqual(world.direccion, 'NORTE')

        #Karel tiene infinitos zumbadores en la mochila.
        self.assertEqual(world.mochila, 'INFINITO')

        #Las únicas paredes en el mundo son las que lo delimitan.
        self.assertTightWorldSize()
        self.assertNoInnerWalls()

        #El mundo siempre medirá 100x100
        self.assertEqual(100, world.w)
        self.assertEqual(100, world.h)

        #Solo importa la orientación final de Karel
        self.assertEqual(world.despliega, ['ORIENTACION'])

        beepers = world.lista_zumbadores

        #El número máximo de direcciones es 100
        zumb = 0
        for i in range(1,101):
            if (i, 1) in beepers:
                zumb += 1
            else:
                break

        self.assertTrue(zumb <= 100)

        #Las direcciones en las que sopla el viento son entre 1 y 4
        for i in range(1, zumb + 1):
            self.assertTrue(0 < world.zumbadores(i, 1) <= 4)

        #Las coordenadas de inicio están entre 1 y 100
        self.assertTrue(0 < world.zumbadores(1,2) <= 100)
        self.assertTrue(0 < world.zumbadores(2,2) <= 100)

        #las coordenadas de la meta están entre 1 y 100
        self.assertTrue(0 < world.zumbadores(1,3) <= 100)
        self.assertTrue(0 < world.zumbadores(2,3) <= 100)

        #No hay más zumbadores en el mundo
        self.assertTrue(len(beepers) == (zumb + 4))

Test().run()
