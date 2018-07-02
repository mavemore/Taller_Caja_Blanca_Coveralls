# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
import clasificacion_clientes

class Test(unittest.TestCase):

	def test_clasificacion_ID(self):
		resultado = ""
		self.assertEqual(resultado, "")
	def test_clasificacion_1(self):
		clasificacion = clasificacion_clientes.clasificacion_clientes(25000, False);
		self.assertEqual("Tipo de cliente: no es digno de crédito, Envio de boletin: No",clasificacion);
	def test_clasificacion_2(self):
		clasificacion = clasificacion_clientes.clasificacion_clientes(30000, True);
		self.assertEqual("Tipo de cliente: AAA, Envio de boletin: Si",clasificacion);
		
	def test_clasificacion_3(self):
		clasificacion = clasificacion_clientes.clasificacion_clientes(21000, True);
		self.assertEqual("Tipo de cliente: AA, Envio de boletin: Si",clasificacion);
		
	def test_clasificacion_4(self):
		clasificacion = clasificacion_clientes.clasificacion_clientes(17000, True);
		self.assertEqual("Tipo de cliente: A, Envio de boletin: Si",clasificacion);
		
	def test_clasificacion_5(self):
		clasificacion = clasificacion_clientes.clasificacion_clientes(14000, True);
		self.assertEqual("Tipo de cliente: B, Envio de boletin: Si",clasificacion);
		
	def test_clasificacion_6(self):
		clasificacion = clasificacion_clientes.clasificacion_clientes(7000, True);
		self.assertEqual("Tipo de cliente: C, Envio de boletin: Si",clasificacion);

if __name__ == '__main__':
	unittest.main()