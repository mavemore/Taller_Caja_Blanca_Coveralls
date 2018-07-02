# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
import clasificacion_clientes

class Test(unittest.TestCase):

	def test_cliente_no_digno(self):
		resultado = clasificacion_clientes.clasificacion_clientes(30000, False)
		self.assertEqual(resultado, "Tipo de cliente: no es digno de crédito, Envio de boletin: No")

	def test_cliente_AAA(self):
		resultado = clasificacion_clientes.clasificacion_clientes(30001, True)
		self.assertEqual(resultado, "Tipo de cliente: AAA, Envio de boletin: Si")

	def test_cliente_AA(self):
		resultado = clasificacion_clientes.clasificacion_clientes(20001, True)
		self.assertEqual(resultado, "Tipo de cliente: AA, Envio de boletin: Si")

	def test_cliente_A(self):
		resultado = clasificacion_clientes.clasificacion_clientes(15001, True)
		self.assertEqual(resultado, "Tipo de cliente: A, Envio de boletin: Si")

	def test_cliente_B(self):
		resultado = clasificacion_clientes.clasificacion_clientes(10001, True)
		self.assertEqual(resultado, "Tipo de cliente: B, Envio de boletin: Si")

	def test_cliente_C(self):
		resultado = clasificacion_clientes.clasificacion_clientes(5001, True)
		self.assertEqual(resultado, "Tipo de cliente: C, Envio de boletin: Si")

if __name__ == '__main__':
	unittest.main()