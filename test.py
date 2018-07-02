# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
import clasificacion_clientes

class Test(unittest.TestCase):

	def test_clasificacion_ID(self):
		resultado = clasificacion_clientes.clasificacion_clientes(30000, True)
		mensaje = "Tipo de cliente: AAA, Envio de boletin: Si"
		self.assertEqual(resultado, mensaje)

if __name__ == '__main__':
	unittest.main()
