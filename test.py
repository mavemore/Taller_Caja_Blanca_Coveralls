# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
import clasificacion_clientes

class Test(unittest.TestCase):

	def test_clasificacion_cliente_1(self):
		resultado=clasificacion_clientes.clasificacion_clientes(31000,True)
		self.assertEqual(resultado, "Tipo de cliente: AAA, Envio de boletin: Si")
	
	def test_clasificacion_cliente_2(self):
		resultado=clasificacion_clientes.clasificacion_clientes(21000,True)
		self.assertEqual(resultado, "Tipo de cliente: AA, Envio de boletin: Si")
	
	def test_clasificacion_cliente_3(self):
		resultado=clasificacion_clientes.clasificacion_clientes(15000,True)
		self.assertEqual(resultado, "Tipo de cliente: A, Envio de boletin: Si")
	
	def test_clasificacion_cliente_4(self):
		resultado=clasificacion_clientes.clasificacion_clientes(10000,True)
		self.assertEqual(resultado, "Tipo de cliente: B, Envio de boletin: Si")
	
	def test_clasificacion_cliente_5(self):
		resultado=clasificacion_clientes.clasificacion_clientes(5001,True)
		self.assertEqual(resultado, "Tipo de cliente: C, Envio de boletin: Si")
	
	def test_clasificacion_cliente_6(self):
		resultado=clasificacion_clientes.clasificacion_clientes(4999, False)
		self.assertEqual(resultado, "Tipo de cliente: no es digno de crédito, Envio de boletin: No")
if __name__ == '__main__':
	unittest.main()