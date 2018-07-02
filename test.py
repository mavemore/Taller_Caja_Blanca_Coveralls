# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
import clasificacion_clientes

class Test(unittest.TestCase):

	def test_clasificacion_ID(self):
		resultado = ""
		self.assertEqual(resultado, "")

	def testclasificacion_0(self):
		clasificacion = clasificacion_clientes.clasificacion_clientes(5001, False);
		self.assertEqual("Tipo de cliente: no es digno de crédito, Envio de boletin: No", clasificacion);

	# VALIDACION DE TRUES
	def testclasificacion_1(self):
		clasificacion = clasificacion_clientes.clasificacion_clientes(5001, True);
		self.assertEqual("Tipo de cliente: C, Envio de boletin: Si", clasificacion);

	def testclasificacion2(self):
		clasificacion = clasificacion_clientes.clasificacion_clientes(10001, True);
		self.assertEqual("Tipo de cliente: B, Envio de boletin: Si", clasificacion);

	def testclasificacion3(self):
		clasificacion = clasificacion_clientes.clasificacion_clientes(15001, True);
		self.assertEqual("Tipo de cliente: A, Envio de boletin: Si", clasificacion);

	def testclasificacion4(self):
		clasificacion = clasificacion_clientes.clasificacion_clientes(20001, True);
		self.assertEqual("Tipo de cliente: AA, Envio de boletin: Si", clasificacion);

	def testclasificacion5(self):
		clasificacion = clasificacion_clientes.clasificacion_clientes(30001, True);
		self.assertEqual("Tipo de cliente: AAA, Envio de boletin: Si", clasificacion);


if __name__ == '__main__':
	unittest.main()