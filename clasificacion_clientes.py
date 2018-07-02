# -*- coding: utf-8 -*-
from __future__ import unicode_literals

def clasificacion_clientes(montoDepositado, informacionBuro):
	enviarBoletinInformativo = "No"
	clasificacionCliente = "no es digno de crédito"
	if informacionBuro:  # True: digno de credito, False: no es digno de credito
		if montoDepositado >= 30000:
			clasificacionCliente = "AAA"
		elif montoDepositado >= 20000 and montoDepositado < 30000:
			clasificacionCliente = "AA"
		elif montoDepositado >= 15000 and montoDepositado < 20000:
			clasificacionCliente = "A"
		elif montoDepositado >= 10000 and montoDepositado < 15000:
			clasificacionCliente = "B"
		elif montoDepositado >= 5000 and montoDepositado < 10000:
			clasificacionCliente = "C"
		enviarBoletinInformativo = "Si"
	return "Tipo de cliente: %s, Envio de boletin: %s" % (clasificacionCliente, enviarBoletinInformativo)