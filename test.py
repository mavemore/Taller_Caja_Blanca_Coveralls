# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
from clasificacion_clientes import *

class Test(unittest.TestCase):

	def test_clasificacion_ID(self):
		resultado = clasificacion_clientes(2000,False)
		self.assertEqual(resultado, "Tipo de cliente: no es digno de crédito, Envio de boletin: No" )

	def test_clasificacion_AAA(self):
		resultado = clasificacion_clientes(30000,False)
		self.assertEqual(resultado, "Tipo de cliente: AAA, Envio de boletin: Si" )


if __name__ == '__main__':
	unittest.main()