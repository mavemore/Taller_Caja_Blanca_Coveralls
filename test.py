# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
import clasificacion_clientes

class Test(unittest.TestCase):

	def test_clasificacion_0(self):
		resultado = clasificacion_clientes.clasificacion_clientes(4000, False)
		self.assertEqual(resultado, "Tipo de cliente: no es digno de crédito, Envio de boletin: No")
	
	def test_clasificacion_1(self):
		resultado = clasificacion_clientes.clasificacion_clientes(6000, False)
		self.assertEqual(resultado, "Tipo de cliente: no es digno de crédito, Envio de boletin: No")
		
	def test_clasificacion_2(self):
		resultado = clasificacion_clientes.clasificacion_clientes(32000, True)
		self.assertEqual(resultado, "Tipo de cliente: AAA, Envio de boletin: Si")
		
	def test_clasificacion_3(self):
		resultado = clasificacion_clientes.clasificacion_clientes(23000, True)
		self.assertEqual(resultado, "Tipo de cliente: AA, Envio de boletin: Si")
		
	def test_clasificacion_4(self):
		resultado = clasificacion_clientes.clasificacion_clientes(16000, True)
		self.assertEqual(resultado, "Tipo de cliente: A, Envio de boletin: Si")
		
	def test_clasificacion_5(self):
		resultado = clasificacion_clientes.clasificacion_clientes(11000, True)
		self.assertEqual(resultado, "Tipo de cliente: B, Envio de boletin: Si")
	
	def test_clasificacion_6(self):
		resultado = clasificacion_clientes.clasificacion_clientes(6500, True)
		self.assertEqual(resultado, "Tipo de cliente: C, Envio de boletin: Si")
		
	def test_clasificacion_7(self):
		resultado = clasificacion_clientes.clasificacion_clientes(3000, True)
		
		self.assertEqual(resultado, "Tipo de cliente: no es digno de crédito, Envio de boletin: Si")

if __name__ == '__main__':
	unittest.main()
