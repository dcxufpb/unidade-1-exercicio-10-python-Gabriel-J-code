# coding: utf-8

class Loja:
  
	def __init__(self, nome_loja, logradouro, numero, complemento, bairro, municipio, estado, cep, telefone, observacao, cnpj,inscricao_estadual):
		self.nome_loja = nome_loja
		self.logradouro = logradouro
		self.numero = numero
		self.complemento = complemento
		self.bairro = bairro
		self.municipio = municipio
		self.estado = estado
		self.cep = cep
		self.telefone = telefone
		self.observacao = observacao
		self.cnpj = cnpj
		self.inscricao_estadual = inscricao_estadual

	def dados_loja(self):
		self.validar_campos_obrigatorios()		

		_numero = "s/n" if not self.numero else str(self.numero)

		_complemento = " " + self.complemento if not isEmpty(self.complemento) else ""	

		_bairro = self.bairro + " - " if not isEmpty(self.bairro) else ""

		_cep = "CEP:" + self.cep if not isEmpty(self.cep) else ""

		_telefone = "Tel " + self.telefone if not isEmpty(self.telefone) else ""

		_telefone = " " + _telefone if not isEmpty(self.cep) and not isEmpty(self.telefone) else _telefone

		_observacao = self.observacao if not isEmpty(self.observacao) else ""

		nota = self.nome_loja + "\n"
		nota += "%s, %s%s\n" %(self.logradouro,_numero,_complemento)
		nota += "%s%s - %s\n" % (_bairro,self.municipio,self.estado)
		nota += "%s%s\n" % (_cep,_telefone)
		nota += "%s\n" % (_observacao)
		nota += "CNPJ: %s\n" %(self.cnpj)
		nota += "IE: %s" % (self.inscricao_estadual)

		return nota 

	def validar_campos_obrigatorios(self):
		if isEmpty(self.nome_loja):
			raise Exception("O campo nome da loja é obrigatório")

		if isEmpty(self.logradouro):
			raise Exception("O campo logradouro do endereço é obrigatório")
			
		if isEmpty(self.municipio):
			raise Exception("O campo município do endereço é obrigatório")

		if isEmpty(self.estado):
			raise Exception("O campo estado do endereço é obrigatório")

		if isEmpty(self.cnpj):
			raise Exception("O campo CNPJ da loja é obrigatório")	

		if isEmpty(self.inscricao_estadual):
			raise Exception("O campo inscrição estadual da loja é obrigatório")


def isEmpty(string):
		if (string == None) or (string == ""):
			return True
		return False