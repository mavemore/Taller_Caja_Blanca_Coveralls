# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
from clasificacion_clientes import clasificacion_clientes

class Test(unittest.TestCase):

	def test_clasificacion_ID_1(self):
		resultado = clasificacion_clientes(1000,False)
		self.assertEqual(resultado, "Tipo de cliente: no es digno de crédito, Envio de boletin: No" )
	def test_clasificacion_ID_2(self):
		resultado = clasificacion_clientes(31000,True)
		self.assertEqual(resultado, "Tipo de cliente: AAA, Envio de boletin: Si" )
	def test_clasificacion_ID_3(self):
		resultado = clasificacion_clientes(25000,True)
		self.assertEqual(resultado, "Tipo de cliente: AA, Envio de boletin: Si" )
	def test_clasificacion_ID_4(self):
		resultado = clasificacion_clientes(15000,True)
		self.assertEqual(resultado, "Tipo de cliente: A, Envio de boletin: Si" )
	def test_clasificacion_ID_5(self):
		resultado = clasificacion_clientes(10000,True)
		self.assertEqual(resultado, "Tipo de cliente: B, Envio de boletin: Si" )
	def test_clasificacion_ID_6(self):
		resultado = clasificacion_clientes(5000,True)
		self.assertEqual(resultado, "Tipo de cliente: C, Envio de boletin: Si" )

if __name__ == '__main__':
	unittest.main()