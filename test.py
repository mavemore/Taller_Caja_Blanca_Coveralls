
from __future__ import unicode_literals

import unittest
import clasificacion_clientes

class Test(unittest.TestCase):

	def test_clasificacion_ID(self):
		def test_clasificacion_1(self):
			montoDepositado = 60000
			informacionBuro = True
			resultado = clasificacion_clientes.clasificacion_clientes(montoDepositado, informacionBuro)
			self.assertEqual(resultado, "Tipo de cliente: AAA, Envio de boletin: Si")

		def test_clasificacion_2(self):
			montoDepositado = 30000
			informacionBuro = True
			resultado = clasificacion_clientes.clasificacion_clientes(montoDepositado, informacionBuro)
			self.assertEqual(resultado, "Tipo de cliente: A, Envio de boletin: Si")

		def test_clasificacion_3(self):
			montoDepositado = 15000
			informacionBuro = True
			resultado = clasificacion_clientes.clasificacion_clientes(montoDepositado, informacionBuro)
			self.assertEqual(resultado, "Tipo de cliente: A, Envio de boletin: Si")

		def test_clasificacion_4(self):
			montoDepositado = 10000
			informacionBuro = True
			resultado = clasificacion_clientes.clasificacion_clientes(montoDepositado, informacionBuro)
			self.assertEqual(resultado, "Tipo de cliente: B, Envio de boletin: Si")

		def test_clasificacion_5(self):
			montoDepositado = 5000
			informacionBuro = True
			resultado = clasificacion_clientes.clasificacion_clientes(montoDepositado, informacionBuro)
			self.assertEqual(resultado, "Tipo de cliente: C, Envio de boletin: Si")

		def test_clasificacion_6(self):
			montoDepositado = 4000
			informacionBuro = False
			resultado = clasificacion_clientes.clasificacion_clientes(montoDepositado,informacionBuro)
			self.assertEqual(resultado, "Tipo de cliente: no es digno de crédito, Envio de boletin: No")
if __name__ == '__main__':
	unittest.main()