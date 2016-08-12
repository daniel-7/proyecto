from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Banco(models.Model):
	nombre_banco  = models.CharField(max_length = 100)
	codigo_banco  = models.CharField(max_length = 100)
	def __unicode__ (self):
		return self.nombre_banco




class Arl(models.Model):
	nombre_arl  		= models.CharField(max_length = 100)
	tipoRiesgo_arl  	= models.CharField(max_length = 100)
	valor_arl  			= models.IntegerField()
	def __unicode__ (self):
		return self.nombre_arl

class Aporte(models.Model):
	numero_plantilla  		= models.CharField(max_length = 100)
	ibc_aporte  			= models.CharField(max_length = 100)
	salud_aporte  			= models.IntegerField()
	pension_aporte		    = models.IntegerField()
	solidaridad_aporte 		= models.IntegerField()
	arl_aporte 				= models.ForeignKey(Arl)
	def __unicode__ (self):
		return self.numero_plantilla



	
class Regional(models.Model):
	codigo 				= models.IntegerField()
	nombre_regional  	= models.CharField(max_length = 100)
	def __unicode__ (self):
		return self.nombre_regional

class Centro(models.Model):
	codigo 				= models.IntegerField()
	nombre_centro  		= models.CharField(max_length = 100)
	regional_centro		= models.ForeignKey(Regional)
	def __unicode__ (self):
		return self.nombre_centro




#modelos contrato

class OrdenadorPago(models.Model):
	nombre 		= models.CharField(max_length = 100)
	apellido 	= models.CharField(max_length = 100)
	telefono	= models.CharField(max_length = 100)
	
	def __unicode__ (self):
		return self.nombre

				
class Supervisor(models.Model):
	nombre 			= models.CharField(max_length = 100)
	apellido 		= models.CharField(max_length = 100)
	correo			= models.CharField(max_length = 100)
	
	def __unicode__ (self):
		return self.nombre


class Contrato(models.Model):
	numero_contrato		= models.CharField(max_length = 100)
	fecha_inicio	= models.DateField(max_length = 100)
	fecha_fin		= models.DateField(max_length = 100)
	valor_total		= models.IntegerField()
	forma_pago		= models.CharField(max_length = 100)
	saldo_anterior	= models.IntegerField()
	saldo_nuevo		= models.IntegerField()
	ordenador_pago 	= models.ForeignKey(OrdenadorPago)
	supervisor 	= models.ForeignKey(Supervisor)
	


	def __unicode__ (self):
		return self.numero_contrato

class Comisiones(models.Model):
	numero_comision =models.CharField(max_length = 200)
	valor_comision	= models.IntegerField()
	valor_retenido	= models.IntegerField()
	total 			= models.IntegerField()
	contrato 		= models.ForeignKey(Contrato)
	def __unicode__ (self):
		return self.numero_comision

class Embargo(models.Model):
	codigo 		=models.CharField(max_length = 200)
	objeto 		=models.CharField(max_length = 200)
	valor 		= models.IntegerField()
	contrato 	= models.ForeignKey(Contrato)

	def __unicode__ (self):
		return self.codigo


class PagoMes(models.Model):
	valor_mes				= models.IntegerField()
	total_dias_liquidacion	= models.IntegerField()
	fecha_inicio			= models.DateField(max_length = 100)
	fecha_fin				= models.DateField(max_length = 100)
	total_pagar				= models.IntegerField()
	numero_pago				= models.CharField(max_length = 100)
	contrato 				= models.ForeignKey(Contrato)
	
	def __unicode__ (self):
		return self.numero_pago


class PagoHora(models.Model):
	numero_horas	= models.IntegerField()
	valor_hora		= models.IntegerField()
	valor_pagar		= models.IntegerField()
	contrato 		= models.ForeignKey(Contrato)
	
	def __unicode__ (self):
		return "valor  Hora "+unicode(self.valor_hora)+"valor  total "+unicode(self.valor_pagar)#+str(self.valor_pagar)


class User(models.Model):
	nickname= models.CharField(max_length = 150)
	password= models.CharField(max_length = 150)
	
	
	def __unicode__ (self):
		return self.nickname


#contratista
class Contratista(models.Model):
	nombre 					= models.CharField(max_length = 100)
	apellido 				= models.CharField(max_length = 100)
	identificacion			= models.CharField(max_length = 100)
	telefono				= models.CharField(max_length = 100)
	correo 					= models.CharField(max_length = 200)
	Clasificacion_persona  	= models.CharField(max_length = 200)
	declarante				= models.CharField(max_length = 100)
	pensionado 				= models.CharField(max_length = 100)
	regimen_iva				= models.CharField(max_length= 100)
	centro 					= models.ForeignKey(Centro)
	aporte 					= models.ForeignKey(Aporte)
	contrato 				= models.OneToOneField(Contrato)
	user 					= models.OneToOneField(User)

	def __unicode__ (self):
		return self.nombre

class Cuenta(models.Model):
	saldo_cuenta  		= models.IntegerField()
	num_cuenta  		= models.IntegerField()
	tipo_cuenta  		= models.CharField(max_length = 100)
	banco_cuenta 		= models.ForeignKey(Banco)
	contratista 		= models.ForeignKey(Contratista)
	def __unicode__ (self):
		return self.num_cuenta


class Actividad(models.Model):
	numero_ficha 			= models.IntegerField()
	descripcion_actividad 	= models.CharField(max_length = 200)
	resultado  				= models.CharField(max_length = 200)
	horas_laboradas			= models.IntegerField()
	valor_hora				= models.IntegerField()
	total  					= models.IntegerField()
	contratista 			= models.ForeignKey(Contratista)
	def __unicode__ (self):
		return self.numero_ficha

class Honorario(models.Model):
	concepto 			=models.CharField(max_length = 200)
	valor_hora			= models.IntegerField()
	valor_retenido		= models.IntegerField()
	total 		  		= models.IntegerField()
	contratista 		= models.ForeignKey(Contratista)
	def __unicode__ (self):
		return self.concepto


