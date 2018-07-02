# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
from clasificacion_clientes import clasificacion_clientes

class Test(unittest.TestCase):

	def test_clasificacion_1(self):
		resultado = clasificacion_clientes(10, False)
		self.assertEqual(resultado, "Tipo de cliente: no es digno de crédito, Envio de boletin: No")
	def test_clasificacion_2(self):
		resultado = clasificacion_clientes(5001, True)
		self.assertEqual(resultado, "Tipo de cliente: C, Envio de boletin: Si")
	def test_clasificacion_3(self):
		resultado = clasificacion_clientes(10001, True)
		self.assertEqual(resultado, "Tipo de cliente: B, Envio de boletin: Si")
	def test_clasificacion_4(self):
		resultado = clasificacion_clientes(15001, True)
		self.assertEqual(resultado, "Tipo de cliente: A, Envio de boletin: Si")
	def test_clasificacion_5(self):
		resultado = clasificacion_clientes(20001, True)
		self.assertEqual(resultado, "Tipo de cliente: AA, Envio de boletin: Si")
	def test_clasificacion_6(self):
		resultado = clasificacion_clientes(30001, True)
		self.assertEqual(resultado, "Tipo de cliente: AAA, Envio de boletin: Si")


if __name__ == '__main__':
	unittest.main()