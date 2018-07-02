# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
from clasificacion_clientes import *

class Test(unittest.TestCase):

	def test_clasificacion_1(self):
		resultado = clasificacion_clientes(30000, True)
		self.assertEqual(resultado, "Tipo de cliente: AAA, Envio de boletin: Si")

	def test_clasificacion_2(self):
		resultado = clasificacion_clientes(20000, True)
		self.assertEqual(resultado, "Tipo de cliente: AA, Envio de boletin: Si")

	def test_clasificacion_3(self):
		resultado = clasificacion_clientes(15000, True)
		self.assertEqual(resultado, "Tipo de cliente: A, Envio de boletin: Si")

	def test_clasificacion_4(self):
		resultado = clasificacion_clientes(10000, True)
		self.assertEqual(resultado, "Tipo de cliente: B, Envio de boletin: Si")

	def test_clasificacion_5(self):
		resultado = clasificacion_clientes(5000, True)
		self.assertEqual(resultado, "Tipo de cliente: C, Envio de boletin: Si")

	def test_clasificacion_6(self):
		resultado = clasificacion_clientes(1000, True)
		self.assertEqual(resultado, "Tipo de cliente: no es digno de crédito, Envio de boletin: Si")

	def test_clasificacion_7(self):
		resultado = clasificacion_clientes(1000, False)
		self.assertEqual(resultado, "Tipo de cliente: no es digno de crédito, Envio de boletin: No")

if __name__ == '__main__':
	unittest.main()