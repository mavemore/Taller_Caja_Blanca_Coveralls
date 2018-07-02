# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
import clasificacion_clientes

from clasificacion_clientes import *


class Test(unittest.TestCase):

	def test_clasificacion_001(self):
		resultado = clasificacion_clientes(1000, False)
		self.assertEqual(resultado, "Tipo de cliente: no es digno de crédito, Envio de boletin: No")

	def test_clasificacion_002(self):
		resultado = clasificacion_clientes(1000, True)
		self.assertEqual(resultado, "Tipo de cliente: no es digno de crédito, Envio de boletin: Si")

	def test_clasificacion_003(self):
		resultado = clasificacion_clientes(30000, True)
		self.assertEqual(resultado, "Tipo de cliente: AAA, Envio de boletin: Si")

	def test_clasificacion_004(self):
		resultado = clasificacion_clientes(20000, True)
		self.assertEqual(resultado, "Tipo de cliente: AA, Envio de boletin: Si")

	def test_clasificacion_005(self):
		resultado = clasificacion_clientes(15000, True)
		self.assertEqual(resultado, "Tipo de cliente: A, Envio de boletin: Si")

	def test_clasificacion_006(self):
		resultado = clasificacion_clientes(10000, True)
		self.assertEqual(resultado, "Tipo de cliente: B, Envio de boletin: Si")

	def test_clasificacion_007(self):
		resultado = clasificacion_clientes(5000, True)
		self.assertEqual(resultado, "Tipo de cliente: C, Envio de boletin: Si")


if __name__ == '__main__':
	unittest.main()
