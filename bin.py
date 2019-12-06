
class Bin:
	def __init__(self):
		self.pesototal = 0
		self.listItens = []
		self.listconf = []

	def add_iten(self,itenid):
		self.listItens.append(itenid)

	def add_peso(self,itenp):
		self.pesototal += itenp
	
	def add_conf(self,itenconf):
		self.listconf.extend(itenconf)

	def getItens(self):
		return self.listItens
	
	def get_pesoT(self):
		return self.pesototal

	def get_itens(self):
		return self.listItens

	def get_conflitos(self):
		return self.listconf

	def mostraBin(self):
		print("Peso total bin: ",self.pesototal)			
		print("intens no bin: ",self.listItens)
		print("conflitos no bin:",self.listconf)	