# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
import clasificacion_clientes

class Test(unittest.TestCase):

	def test_clasificacion_1(self):
		resultado = clasificacion_clientes.clasificacion_clientes(5000, False)
		self.assertEqual(resultado, "Tipo de cliente: no es digno de crédito, Envio de boletin: No")
		
	def test_clasificacion_2(self):
		resultado = clasificacion_clientes.clasificacion_clientes(31000, True)
		self.assertEqual(resultado, "Tipo de cliente: AAA, Envio de boletin: Si")
		
	def test_clasificacion_3(self):
		resultado = clasificacion_clientes.clasificacion_clientes(22000, True)
		self.assertEqual(resultado, "Tipo de cliente: AA, Envio de boletin: Si")
		
	def test_clasificacion_4(self):
		resultado = clasificacion_clientes.clasificacion_clientes(15000, True)
		self.assertEqual(resultado, "Tipo de cliente: A, Envio de boletin: Si")
		
	def test_clasificacion_5(self):
		resultado = clasificacion_clientes.clasificacion_clientes(12000, True)
		self.assertEqual(resultado, "Tipo de cliente: B, Envio de boletin: Si")
	
	def test_clasificacion_6(self):
		resultado = clasificacion_clientes.clasificacion_clientes(7000, True)
		self.assertEqual(resultado, "Tipo de cliente: C, Envio de boletin: Si")

if __name__ == '__main__':
	unittest.main()