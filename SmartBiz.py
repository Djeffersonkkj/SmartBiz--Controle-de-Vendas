'''
SMARTBIZ:
    é um sistema de gerenciamento simples e eficiente que ajuda no controle de produtos e vendas para lojas ou pequenos negócios.
    Trazendo funcionalidades como  pesquisa, edição de produtos e registro de vendas, o sistema é uma solução para pequenos comerciantes
    que precisam organizar seu estoque e acompanhar suas vendas.
'''
import os
def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

produtos = {}
limpar()
    
#MENU
while True:
            print('------------------SMARTBIZ------------------\n')
            print('1 |CADASTRAR')
            print('2 |PESQUISAR')
            print('3 |LISTA')
            print('4 |EDITAR')
            print('5 |VENDER\n')
            print('0 |SAIR')
            op = int(input('SELECIONE UMA OPÇÃO: '))
            
            if op == 1: #CADASTRAR
                limpar()
                for i in range(1):
                    print('--------------CADASTRAR PRODUTO--------------\n')
                    produto_id = int(input('(o id será importante para buscar o produto)\nID DO PRODUTO: '))
                        
                    if produtos.get(produto_id) is None:
                        nome = input('NOME: ')
                        estoque = int(input('EM ESTOQUE: '))
                        valor_compra = float(input('VALOR DE COMPRA: R$'))
                        valor_venda = float(input('VALOR A SER VENDIDO: R$'))
                        produto = {'produto_id': produto_id, 'nome': nome, 'estoque': estoque,
                                    'valor_compra': valor_compra, 'v_compra_total': valor_compra*estoque, 'valor_venda': valor_venda,
                                    'v_compra_total': valor_compra * estoque, 'q_vendas': 0,
                                    't_vendas': 0
                                    }
                        produtos[produto_id] = produto
                        limpar()
                    else:
                        limpar()
                        print('ID JÁ CADASTRADO NO SISTEMA!')
                            
            elif op == 2: #PESQUISAR
                limpar()
                
                if not produtos:
                    print('NENHUM PRODUTO CADASTRADO!')
                else:
                    print('---------------PESQUISAR---------------\n')
                    pesquisa = int(input('DIGITE O ID DO PRODUTO: '))
                    
                    if produtos.get(pesquisa) is None:
                        limpar()
                        print('ID ERRADO OU INEXISTENTE!\n')
                    else:
                        limpar()
                        print(f'-------------------{produtos[pesquisa].get("nome", "nome inexistente").upper()}-------------------\n')
                        print(f'ESTOQUE: {produtos[pesquisa]["estoque"]}x')
                        print(f'VALOR DE COMPRA: R${produtos[pesquisa]["valor_compra"]:.2f} - TOTAL: R$${produtos[pesquisa]["v_compra_total"]:.2f}')
                        print(f'VALOR DE VENDA: R${produtos[pesquisa]["valor_venda"]:.2f} | VENDAS: {produtos[pesquisa]["q_vendas"]} - R${produtos[pesquisa]["t_vendas"]:.2f}')
                        
            elif op == 3: #LISTA
                
                if not produtos:
                    limpar()
                    print('NENHUM PRODUTO CADASTRADO!')
                else:
                    limpar()
                    print('--------------------LISTA--------------------\n')
                    for chave, dados in produtos.items():
                        print(f"NOME: {dados['nome']} ({dados['produto_id']}) | ESTOQUE: {dados['estoque']}x | VALOR DE VENDA: R${dados['valor_venda']:.2f} | \
VENDAS: {dados['q_vendas']}   TOTAL: R${dados['t_vendas']:.2f}")
                        print('---------------------------------------------------------------------')
                            
            elif op == 4: #EDITAR
                
                if not produtos:
                    limpar()
                    print('NENHUM PRODUTO CADASTRADO!')
                else:
                    limpar()
                    print('------------------EDITAR------------------\n')
                    pesquisa = int(input('DIGITE O ID DO PRODUTO: '))
                        
                    if produtos.get(pesquisa) is None:
                        limpar()
                        print('ID ERRADO OU INEXISTENTE!\n')
                    else:
                        while True:
                            limpar()
                            print(f'------------------EDITAR |{produtos[pesquisa].get("nome", "nome inexistente").upper()}------------------\n')
                            print(f'1 |EDITAR - {produtos[pesquisa].get("nome", "nome inexistente")}')
                            print(f'2 |EXCLUIR - {produtos[pesquisa].get("nome", "nome inexistente")}\n')
                            print('0 |VOLTAR')
                            op_3 = int(input('SELECIONE UMA OPÇÃO: '))
                                
                            if op_3 == 1:
                                limpar()
                                print(f'------------------EDITAR |{produtos[pesquisa].get("nome", "nome inexistente").upper()}------------------\n')
                                print(f'--------------------{produtos[pesquisa].get("nome", "nome inexistente").upper()}--------------------\n')
                                print(f'1 |NOME - {produtos[pesquisa].get("nome", "nome inexistente")}')
                                print(f'2 |EM ESTOQUE - {produtos[pesquisa].get("estoque", "estoque inexistente")}')
                                print(f'3 |VALOR DE COMPRA - {produtos[pesquisa].get("valor_compra", "valor de compra inexistente")}')
                                print(f'4 |VALOR DE VENDA - {produtos[pesquisa].get("valor_venda", "valor de venda inexistente")}')
                                print(f'5 |QUANTIDADE DE VENDAS - {produtos[pesquisa].get("q_vendas", "vendas inexistentes")}')
                                print(f'6 |TOTAL DO VALOR DE VENDAS - {produtos[pesquisa].get("t_vendas", "vendas inexistentes")}\n')
                                print('0 |VOLTAR')
                                op_4 = int(input('SELECIONE UMA OPÇÃO: '))

                                if op_4 == 1:
                                    novo_valor = input('NOME: ')
                                    produtos[pesquisa]["nome"] = novo_valor
                                    limpar()
                                elif op_4 == 2:
                                    novo_valor = input('ESTOQUE: ')
                                    produtos[pesquisa]["estoque"] = novo_valor
                                    limpar()
                                elif op_4 == 3:
                                    novo_valor = input('VALOR DE COMPRA: ')
                                    produtos[pesquisa]["valor_compra"] = novo_valor
                                    limpar()
                                elif op_4 == 4:
                                    novo_valor = input('VALOR DE VENDA: ')
                                    produtos[pesquisa]["valor_venda"] = novo_valor
                                    limpar()
                                elif op_4 == 5:
                                    novo_valor = input('QUANTIDADE DE VENDAS: ')
                                    produtos[pesquisa]["q_vendas"] = novo_valor
                                    limpar()
                                elif op_4 == 6:
                                    novo_valor = input('TOTAL DO VALOR DE VENDAS: ')
                                    produtos[pesquisa]["t_vendas"] = novo_valor
                                    limpar()
                                elif op_4 == 0:
                                    limpar()
                                    break
                                else:
                                    limpar()
                                    print('OPÇÃO INVÁLIDA!')
                            elif op_3 == 2:
                                limpar()
                                
                                excluir = input(f'DIGITE "SIM" PARA EXCLUIR {produtos[pesquisa]["nome"].upper()}: ')
                                if excluir in ['SIM', 'Sim', 'sim', 's', 'S']:
                                    limpar()
                                    print(f'{produtos[pesquisa]["nome"].upper()} EXCLUÍDO COM SUCESSO!')
                                    del produtos[pesquisa]
                                    break
                                else:
                                    limpar()
                                    print(f'{produtos[pesquisa]["nome"].upper()} NÃO FOI EXCLUÍDO!')
                                    
                            elif op_3 == 0:
                                limpar()
                                break
                            else:
                                limpar()
                                print('OPÇÃO INVÁLIDA!')
            
            elif op == 5: #VENDER
                
                if not produtos:
                    limpar()
                    print('NENHUM PRODUTO CADASTRADO!')  
                else:
                    limpar()
                    print('------------------VENDER------------------\n')
                    pesquisa = int(input('DIGITE O ID DO PRODUTO: '))
                    
                    if produtos.get(pesquisa) is None:
                        limpar()
                        print('ID ERRADO OU INEXISTENTE!\n')
                    else:
                        limpar()
                        print(f'------------------VENDER |{produtos[pesquisa].get("nome", "nome inexistente").upper()}------------------\n')
                        print(f'NOME: {produtos[pesquisa].get("nome")} |ESTOQUE: {produtos[pesquisa].get("estoque")} |VALOR DE VENDA: R${produtos[pesquisa].get("valor_venda"):.2f}\n')
                        quantidade = int(input(f'DIGITE A QUANTIDADE DE {produtos[pesquisa].get("nome").upper()} A SEREM VENDIDOS: '))
                        
                        if quantidade > produtos[pesquisa].get("estoque"):
                            limpar()
                            print(f'VOCÊ NÃO POSSUÍ {produtos[pesquisa].get("nome").upper()} SUFICIENTES NO SEU ESTOQUE PARA ESSA VENDA.')
                            continue
                        elif quantidade == 0:
                            limpar()
                            print(f'NÃO É POSSÍVEL VENDER 0 (zero) {produtos[pesquisa].get("nome").upper()}.')
                            continue

                        valor_uni = float(input('DIGITE O VALOR QUE O PRODUTO SERÁ VENDIDO (UNIDADE): R$'))
                        valor_total = quantidade * valor_uni
                            
                        limpar()
                        print(f'{quantidade} {produtos[pesquisa].get("nome").upper()} SERÃO VENDIDOS POR {valor_total:.2f}. DESEJA ADICIONAR DESCONTO? ')
                            
                        se_desconto = input('DIGITE "SIM" PARA ADICIONAR DESCONTO: ')
                        if se_desconto in ['SIM', 'Sim', 'sim', 's', 'S']:
                            limpar()
                            
                            while True:
                                v_desconto = int(input('DIGITE A PORCENTAGEM DO DESCONTO: %'))
                                desconto = (v_desconto / 100) * valor_total
                                print(f'{quantidade}x {produtos[pesquisa].get("nome")} com {v_desconto}% de desconto será vendido por {valor_total - desconto:.2f}. DESEJA PROSSEGUIR?\n')
                                confirmar = input('"SIM" para confirmar | "NÃO" para cancelar | "TROCAR" mudar desconto \nDIGITE A OPÇÃO DESEJADA: ')
                                
                                if confirmar in ['SIM', 'Sim', 'sim', 's', 'S']:
                                    limpar()
                                    valor_total = valor_total - desconto 
                                    print('DESCONTO ADICIONADO COM SUCESSO!\n')
                                    break
                                elif confirmar in ['NÃO', 'NAO', 'Não', 'Nao', 'não', 'nao', 'n', 'N']:
                                    limpar()
                                    print('DESCONTO CANCELADO!')
                                    break
                                elif confirmar in ['TROCAR', 'Trocar', 'trocar', 't']:
                                    limpar()
                                    print('TROCAR DESCONTO!\n')
                                else:
                                    limpar()
                                    print('VALOR INVÁLIDO! TROCAR DESCONTO POR PADRÃO.\n')
                            
                        print(f'{quantidade} {produtos[pesquisa].get("nome").upper()} SERÃO VENDIDOS POR R${valor_total:.2f}.')
                        confirmar = input('"SIM" para vender | ')
                        if confirmar in ['SIM', 'Sim', 'sim', 's', 'S']:
                            limpar()
                            produtos[pesquisa]["estoque"] -= quantidade
                            produtos[pesquisa]["q_vendas"] += quantidade
                            produtos[pesquisa]["t_vendas"] += valor_total
                            print('VENDA CONCLUÍDA COM SUCESSO!')        
                        else:
                            print('VENDA CANCELADA!')   
            elif op == 0:
                limpar()
                print("VOCÊ SAIU DO SISTEMA!")
                break
            else:
                limpar()
                print('OPÇÃO INVÁLIDA!')