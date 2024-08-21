from datetime import date, datetime
from pessoa import Endereco, PessoaFisica, PessoaJuridica


def main():
    while True:
        lista_PessoasFisicas : PessoaFisica = []
        lista_PessoasJuridicas = []
        opcao = int(input("Escolha opçao: 1 -Pessoa Fisica / 2 - Pessoa Juridica / 0 - Sair"))

        if opcao == 1:
            while True:
                opcao_Pf = int(input("Escolha uma opçao: 1 - Cadastrar / 2 - Listar Pessoas Fisicas / 3 - Remover cpf / 0 - Voltar menu anterior"))

                if opcao_Pf == 1:
                    novapf = PessoaFisica()
                    novo_endereco_pf = Endereco()

                    novapf.nome = str(input("Digite o nome da pessoa fisica: "))
                    novapf.cpf = str(input("Digite o CPF da pessoa fisica: "))
                    novapf.rendimento = float(input("Digite o rendimento da pessoa fisica: "))
                    
                    data_nascimento = input("Digite a data de nascimento da pessoa fisica: ")
                    novapf.dataNascimento = datetime.strptime(data_nascimento, '%d/%m/%Y').date()

                    idade = (date.today() - novapf.dataNascimento).days // 365

                    if idade < 18:
                        print("A pessoa tem menos de 18 anos. Retornando ao menu")
                        continue
                    
                    endereco_Comercial = input("Este endereço é comercial? S/N: ")
                    novo_endereco_pf.endereco_Comercial = endereco_Comercial.strip().upper() == 'S'
                    novo_endereco_pf.logradouro = input("Digite o logradouro da pessoa fisica: ")
                    novo_endereco_pf.numero = input("Digite o numero da pessoa fisica: ")
                    
                    novapf.endereco = novo_endereco_pf

                    lista_PessoasFisicas.append(novapf)

                    print("Cadastro realizado")
                elif opcao_Pf == 2:
                    if lista_PessoasFisicas:
                        for pessoaFisica in lista_PessoasFisicas:
                            enderecoPessoaFisica = pessoaFisica.endereco

                            print(
                                "Nome:", pessoaFisica.nome, 
                                "CPF:", pessoaFisica.cpf, 
                                "Data de Nascimento:", pessoaFisica.dataNascimento,
                                "Rendimento:", pessoaFisica.rendimento,
                                "Imposto a ser pago:", pessoaFisica.calcular_imposto(pessoaFisica.rendimento),
                                "Logradouro:", enderecoPessoaFisica.logradouro,
                                "Número:", enderecoPessoaFisica.numero
                            )
                    else:
                        print("Lista vazia")
                elif opcao_Pf == 3:
                    cpf_Remover = input("Digite o cpf da pessoa que deseja remover")
                    pessoa_encontrada = False

                    for pessoa_pf in lista_PessoasFisicas:
                        if pessoa_pf.cpf == cpf_Remover:
                            lista_PessoasFisicas.remove(pessoa_pf)
                            pessoa_encontrada = True
                            print("Pessoa removida")
                            break
                            
                        if not pessoa_encontrada:
                            print("Pessoa nao encontrada")

                        elif opcao_Pf == 4:
                            cpf_Atualizar = input("Digite o CPF da pessoa que deseja atualizar: ")
                            pessoa_encontrada = False

                        for pessoa_pf in lista_PessoasFisicas:
                            if pessoa_pf.cpf == cpf_Atualizar:
                                pessoa_encontrada = True
                            print("Atualizando dados da pessoa com CPF: ", pessoa_pf.cpf)

                            pessoa_pf.nome = input(f"Digite o novo nome (atual: {pessoa_pf.nome}): ") or pessoa_pf.nome
                            pessoa_pf.rendimento = float(input(f"Digite o novo rendimento (atual: {pessoa_pf.rendimento})")) or pessoa_pf.rendimento 

                            data_nascimento = input(f"Digite a nova data de nascimento (atual: {pessoa_pf.dataNascimento.strftime('%d/%m/%Y')})")
                            if data_nascimento:
                                pessoa_pf.dataNascimento = datetime.strftime(data_nascimento, '%d/%m/%Y').date()
                            

                            endereco_Comercial = input(f"Este endereco é comercial? (atual: {'S' if pessoa_pf.endereco.endereco_Comercial else 'N'}): ")
                            pessoa_pf.endereco.endereco_Comercial = endereco_Comercial.strip().upper == 'S'
                            pessoa_pf.endereco.logradouro = input(f"Digite o novo logradouro (atual: {pessoa_pf.endereco.logradouro}): ") or pessoa_pf.endereco.logradouro
                            pessoa_pf.endereco.numero = input(f"Digite o novo numero (atual: {pessoa_pf.endereci.numero}): ") or pessoa_pf.endereco.numero

                            print("Dados atualizados")
                            break


                if not pessoa_encontrada:
                    print("Pessoa nao encontrada")     

                elif opcao_Pf == 0:
                    print("Retornando ao menu")
                    break
                else:
                    print("Opção inválida")       
        elif opcao == 2:
            while True:
                opcao_Pj = int(input("Escolha uma opçao: 1 - Cadastrar / 2 - Listar Pessoas Juridica / 3 - Remover / 0 - Voltar menu anterior"))

                if opcao_Pj == 1:
                    novaPJ = PessoaJuridica()
                    novo_endereco_pj = Endereco()

                    novaPJ.nome = str(input("Digite o nome da pessoa juridica: "))
                    novaPJ.cnpj = str(input("Digite o cnpj da pessoa juridica: "))
                    novaPJ.rendimento = float(input("Digite o rendimento da pessoa juridica: "))

                    endereco_Comercial = input("Este endereço é comercial? S/N: ")
                    novo_endereco_pj.endereco_Comercial = endereco_Comercial.strip().upper() == 'S'
                    novo_endereco_pj.logradouro = input("Digite o logradouro da pessoa fisica: ")
                    novo_endereco_pj.numero = input("Digite o numero da pessoa fisica: ")
                    
                    novaPJ.endereco = novo_endereco_pj

                    lista_PessoasJuridicas.append(novaPJ)

                    print("Cadastro realizado")
                elif opcao_Pj == 2:
                    if lista_PessoasJuridicas:
                        for pessoaJuridica in lista_PessoasJuridicas:
                            enderecoPessoaJuridica = pessoaJuridica.endereco

                            print(
                                "Nome:", pessoaJuridica.nome, 
                                "CNPJ:", pessoaJuridica.cnpj, 
                                "Imposto a ser pago:", pessoaJuridica.calcular_imposto(pessoaJuridica.rendimento),
                                "Logradouro:", enderecoPessoaJuridica.logradouro,
                                "Número:", enderecoPessoaJuridica.numero
                            )
                    else:
                        print("Lista vazia")
                elif opcao_Pj == 3:
                    cnpj_Remover = input("Digite o cnpj que deseja remover")
                    pessoa_encontrada = False

                    for pessoa_Pj in lista_PessoasJuridicas:
                        if pessoa_Pj.cnpj == cnpj_Remover:
                            lista_PessoasJuridicas.remove(pessoa_Pj)
                            pessoa_encontrada = True
                            print("Pessoa removida")
                            break

                elif opcao_Pj == 4:
                    cnpj_Atualizar = input("Digite o CNPJ da pessoa que deseja atualizar: ")
                    pessoa_encontrada = False

                    for pessoa_Pj in lista_PessoasJuridicas:
                        if pessoa_Pj.cnpj == cnpj_Atualizar:
                            pessoa_encontrada = True
                            print("Atualizando dados da pessoa com CNPJ:", pessoa_Pj.cnpj)
                            
                            pessoa_Pj.nome = input(f"Digite o novo nome (atual: {pessoa_Pj.nome}): ") or pessoa_Pj.nome
                            pessoa_Pj.rendimento = float(input(f"Digite o novo rendimento (atual: {pessoa_Pj.rendimento}): ") or pessoa_Pj.rendimento)

                            endereco_Comercial = input(f"Este endereço é comercial? (atual: {'S' if pessoa_Pj.endereco.endereco_Comercial else 'N'}): ")
                            pessoa_Pj.endereco.endereco_Comercial = endereco_Comercial.strip().upper() == 'S'
                            pessoa_Pj.endereco.logradouro = input(f"Digite o novo logradouro (atual: {pessoa_Pj.endereco.logradouro}): ") or pessoa_Pj.endereco.logradouro
                            pessoa_Pj.endereco.numero = input(f"Digite o novo número (atual: {pessoa_Pj.endereco.numero}): ") or pessoa_Pj.endereco.numero

                            print("Dados atualizados")
                            break            

                            
                        if not pessoa_encontrada:
                            print("Pessoa nao encontrada")
                elif opcao_Pj == 0:
                    print("Retornando ao menu")
                    break
                else:
                    print("Opçao invalida")
                    break
        elif opcao == 0:
            print("Obrigado por utilizar o nome sistema")
            break
        else: 
            print("Opção inválida, por favor digite uma das opcoes validas")

if __name__ == "__main__":
    main()