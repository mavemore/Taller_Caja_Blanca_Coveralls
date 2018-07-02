# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
import clasificacion_clientes

class Test(unittest.TestCase):

	def test_clasificacion_ID_1(self):
		resultado = clasificacion_clientes.clasificacion_clientes(40000, True)
		self.assertEqual(resultado, "Tipo de cliente: AAA, Envio de boletin: Si")

	def test_clasificacion_ID_2(self):
		resultado = clasificacion_clientes.clasificacion_clientes(25000, True)
		self.assertEqual(resultado, "Tipo de cliente: AA, Envio de boletin: Si")

	def test_clasificacion_ID_3(self):
		resultado = clasificacion_clientes.clasificacion_clientes(18000, True)
		self.assertEqual(resultado, "Tipo de cliente: A, Envio de boletin: Si")

	def test_clasificacion_ID_4(self):
		resultado = clasificacion_clientes.clasificacion_clientes(12000, True)
		self.assertEqual(resultado, "Tipo de cliente: B, Envio de boletin: Si")

	def test_clasificacion_ID_5(self):
		resultado = clasificacion_clientes.clasificacion_clientes(7000, True)
		self.assertEqual(resultado, "Tipo de cliente: C, Envio de boletin: Si")

	def test_clasificacion_ID_6(self):
		resultado = clasificacion_clientes.clasificacion_clientes(0, False)
		self.assertEqual(resultado, "Tipo de cliente: no es digno de crédito, Envio de boletin: No")


if __name__ == '__main__':
	unittest.main()