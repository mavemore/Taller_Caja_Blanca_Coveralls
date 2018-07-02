# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
import clasificacion_clientes as cc

class Test(unittest.TestCase):

	def test_clasificacion_ID1(self):
		resultado = cc.clasificacion_clientes(0, False)
		self.assertEqual(resultado, "Tipo de cliente: no es digno de crédito, Envio de boletin: No")

	def test_clasificacion_ID2(self):
		resultado = cc.clasificacion_clientes(5000, True)
		self.assertEqual(resultado, "Tipo de cliente: C, Envio de boletin: Si")

	def test_clasificacion_ID3(self):
		resultado = cc.clasificacion_clientes(10000, True)
		self.assertEqual(resultado, "Tipo de cliente: B, Envio de boletin: Si")
			
	def test_clasificacion_ID4(self):
		resultado = cc.clasificacion_clientes(15000, True)
		self.assertEqual(resultado, "Tipo de cliente: A, Envio de boletin: Si")
			
	def test_clasificacion_ID5(self):
		resultado = cc.clasificacion_clientes(20000, True)
		self.assertEqual(resultado, "Tipo de cliente: AA, Envio de boletin: Si")
			
	def test_clasificacion_ID6(self):
		resultado = cc.clasificacion_clientes(30000, True)
		self.assertEqual(resultado, "Tipo de cliente: AAA, Envio de boletin: Si")

if __name__ == '__main__':
	unittest.main()