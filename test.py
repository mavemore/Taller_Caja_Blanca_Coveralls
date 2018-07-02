# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
from clasificacion_clientes import *

class Test(unittest.TestCase):

	def test_clasificacion_ID(self):
		resultado = clasificacion_clientes(2000,False)
		self.assertEqual(resultado, "Tipo de cliente: no es digno de crédito, Envio de boletin: No" )

	def test_clasificacion_AAA(self):
		resultado = clasificacion_clientes(30000,True)
		self.assertEqual(resultado, "Tipo de cliente: AAA, Envio de boletin: Si" )

	def test_clasificacion_AA(self):
		resultado = clasificacion_clientes(20000,True)
		self.assertEqual(resultado, "Tipo de cliente: AA, Envio de boletin: Si" )

	def test_clasificacion_A(self):
		resultado = clasificacion_clientes(15000,True)
		self.assertEqual(resultado, "Tipo de cliente: A, Envio de boletin: Si" )

	def test_clasificacion_B(self):
		resultado = clasificacion_clientes(10000,True)
		self.assertEqual(resultado, "Tipo de cliente: B, Envio de boletin: Si" )

	def test_clasificacion_C(self):
		resultado = clasificacion_clientes(5000,True)
		self.assertEqual(resultado, "Tipo de cliente: C, Envio de boletin: Si" )


if __name__ == '__main__':
	unittest.main()