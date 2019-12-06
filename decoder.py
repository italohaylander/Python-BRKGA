import bin as bins
import item
from copy import deepcopy
class Decoder:
	
	def __init__(self,itens,brk,tamPackages):
		self.itens = deepcopy(itens)
		self.brk = deepcopy(brk)
		self.tamPackages = tamPackages


	def geraSolucao(self):
	    
		listaBinAbertos = []
		solucao = []

		while self.brk:
			n_min = min(self.brk)
			n_pos = self.brk.index(n_min) # pega a posição do valor n_min
			self.brk.pop(n_pos)
			#verifica se n possui nenhum bin aberto, caso n possua, cria o primeiro
			if listaBinAbertos == []:
				bin_atual = bins.Bin()                
				aux = self.itens[n_pos]
				self.itens.remove(aux) 
				bin_atual.add_iten(aux.get_id())
				bin_atual.add_peso(aux.get_peso())
				bin_atual.add_conf(aux.get_conflitos())
				listaBinAbertos.append(bin_atual)
			else:
				inseriu = False#flag para verificar se consegui inserir em um bin existente ou se é necessario criar um novo bin
				for j in listaBinAbertos:#verificar se o iten cabe em algum bin que esta aberto    
					#verifica se tem espaço no bin e se nenhum o bin ja n possui conflitos com o item
					binlistaconf = set(j.get_conflitos())
					itenslistaconf = set(self.itens[n_pos].get_conflitos())
					if (int(j.get_pesoT()) + int(self.itens[n_pos].get_peso()) < int(self.tamPackages))  and (self.itens[n_pos].get_id() in j.get_conflitos()):
						aux = self.itens[n_pos]
						self.itens.remove(aux) 
						j.add_iten(aux.get_id())
						j.add_peso(aux.get_peso())
						j.add_conf(aux.get_conflitos()) 
						inseriu = True
						break
					else:
						pass
				if not inseriu: #nao foi possivel inserir em nenhum bin existente entao um novo é criado
					bin_atual = bins.Bin()                
					aux = self.itens[n_pos]
					self.itens.remove(aux)
					bin_atual.add_iten(aux.get_id())
					bin_atual.add_peso(aux.get_peso())
					bin_atual.add_conf(aux.get_conflitos())
					listaBinAbertos.append(bin_atual)           
						
		cont = 0

		return (listaBinAbertos)
	
	def verList(self,item,lista1):
		for i in range(0,len(lista1)):
			if lista1[i] == item:	
				return True
		return False			
	
	def solucao2(self):
		contBin = 0
		binAberto = None

		while self.brk != []:
			n_min = min(self.brk)
			n_pos = self.brk.index(n_min) # pega a posição do valor n_min
			self.brk.pop(n_pos)

			if binAberto == None:
				binAberto = bins.Bin()
				aux = self.itens[n_pos]
				self.itens.remove(aux)
				binAberto.add_iten(aux.get_id())
				binAberto.add_peso(aux.get_peso())
				binAberto.add_conf(aux.get_conflitos())
				contBin += 1
			elif (int(binAberto.get_pesoT()) + int(self.itens[n_pos].get_peso()) < int(self.tamPackages)) and not(self.itens[n_pos].get_id() in binAberto.get_conflitos()) and set(binAberto.getItens()).intersection(set(self.itens[n_pos].get_conflitos()))==set():
				aux = self.itens[n_pos]
				self.itens.remove(aux)
				binAberto.add_iten(aux.get_id())
				binAberto.add_peso(aux.get_peso())
				binAberto.add_conf(aux.get_conflitos())
				
			else:
				binAberto = None
				
				binAberto = bins.Bin()
				
				aux = self.itens[n_pos]
				self.itens.remove(aux)
				binAberto.add_iten(aux.get_id())
				binAberto.add_peso(aux.get_peso())
				binAberto.add_conf(aux.get_conflitos())
				contBin += 1

		return contBin		

				
