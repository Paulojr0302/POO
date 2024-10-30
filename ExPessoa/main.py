import os
os.system('cls')

from pessoa_fisica import PessoaFisica
from pessoa_juridica import PessoaJuridica

pessoa_fisica = PessoaFisica("123.456.789-00", "Paulo", 21)
print(f"Nome: {pessoa_fisica.getNome()}, Idade: {pessoa_fisica.getIdade()}, CPF: {pessoa_fisica.getCPF()}")

pessoa_fisica.setNome("Paulo Junior")
pessoa_fisica.setCPF("987.654.321-00")
print(f"Nome: {pessoa_fisica.getNome()}, CPF: {pessoa_fisica.getCPF()}")

pessoa_juridica = PessoaJuridica("12.345.678/0001-00", "Empresa 1", 10)
print(f"Nome: {pessoa_juridica.getNome()}, CNPJ: {pessoa_juridica.getCNPJ()}")

pessoa_juridica.setNome("Empresa 2")
pessoa_juridica.setCNPJ("98.765.432/0001-99")
print(f"Nome: {pessoa_juridica.getNome()}, CNPJ: {pessoa_juridica.getCNPJ()}")