# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
import clasificacion_clientes

class Test(unittest.TestCase):

	def test_clasificacion_1(self):
		resultado = clasificacion_clientes.clasificacion_clientes(30000, True)
		mensaje = "Tipo de cliente: AAA, Envio de boletin: Si"
		self.assertEqual(resultado, mensaje)

	def test_clasificacion_2(self):
		resultado = clasificacion_clientes.clasificacion_clientes(25000, True)
		mensaje = "Tipo de cliente: AA, Envio de boletin: Si"
		self.assertEqual(resultado, mensaje)

	def test_clasificacion_3(self):
		resultado = clasificacion_clientes.clasificacion_clientes(18000, True)
		mensaje = "Tipo de cliente: A, Envio de boletin: Si"
		self.assertEqual(resultado, mensaje)

	def test_clasificacion_4(self):
		resultado = clasificacion_clientes.clasificacion_clientes(13000, True)
		mensaje = "Tipo de cliente: B, Envio de boletin: Si"
		self.assertEqual(resultado, mensaje)

	def test_clasificacion_5(self):
		resultado = clasificacion_clientes.clasificacion_clientes(6000, True)
		mensaje = "Tipo de cliente: C, Envio de boletin: Si"
		self.assertEqual(resultado, mensaje)

if __name__ == '__main__':
	unittest.main()
