# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
import clasificacion_clientes

class Test(unittest.TestCase):

	def test_clasificacion_ID1(self):
		resultado = clasificacion_clientes.clasificacion_clientes(40000,True);
		self.assertEqual(resultado, "Tipo de cliente: AAA, Envio de boletin: Si")
	def test_clasificacion_ID2(self):
		resultado = clasificacion_clientes.clasificacion_clientes(25000,True);
		self.assertEqual(resultado, "Tipo de cliente: AA, Envio de boletin: Si")
	def test_clasificacion_ID3(self):
		resultado = clasificacion_clientes.clasificacion_clientes(15700,True);
		self.assertEqual(resultado, "Tipo de cliente: A, Envio de boletin: Si")
	def test_clasificacion_ID4(self):
		resultado = clasificacion_clientes.clasificacion_clientes(10002,True);
		self.assertEqual(resultado, "Tipo de cliente: B, Envio de boletin: Si")
	def test_clasificacion_ID5(self):
		resultado = clasificacion_clientes.clasificacion_clientes(5010,True);
		self.assertEqual(resultado, "Tipo de cliente: C, Envio de boletin: Si")
	def test_clasificacion_ID6(self):
		resultado = clasificacion_clientes.clasificacion_clientes(5010,False);
		self.assertEqual(resultado, "Tipo de cliente: no es digno de crédito, Envio de boletin: No")
	def test_clasificacion_ID7(self):
		resultado = clasificacion_clientes.clasificacion_clientes(10,True);
		self.assertEqual(resultado, "Tipo de cliente: no es digno de crédito, Envio de boletin: Si")
	
if __name__ == '__main__':
	unittest.main()