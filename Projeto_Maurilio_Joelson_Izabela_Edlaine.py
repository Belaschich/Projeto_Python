'''INFORMAÇÕES GERAIS DO PROJETO
tema: Loja de Informática
linguagem de comunição: imperativa
Convenção de nomenclatura = snake_case
Principais recursos de programação = listas | cadeias estáticas if else / Loops de repetição / Funções
Principais Métodos de controle de recursos (lógica) = relacionamentos de index / indices das listas
'''

# BIBLIOTECAS ----------------------------------------------------------------------
from datetime import datetime

horas = datetime.now().hour

# FUNÇÕES ----------------------------------------------------------------------
def periodo_do_dia():
    periodo = ""

    if horas in range(6, 12):
        periodo = "BOM DIA"

    elif horas in range(12, 18):
        periodo = "BOA TARDE"

    elif horas in range(18, 24) or horas in range(0, 6):
        periodo = "BOA NOITE"

    return periodo

def calcula_total(lista_precos_total):
    soma = 0

    for i in range(len(lista_precos_total)):
        soma += lista_precos_total[i]

    # RETORNA A SOMA DE TODOS OS PREÇOS QUE ESTÃO NA LISTA PRINCIPAL
    return soma

def duvidas_frequentes():
    print(f"1 - POSSO ADICIONAR OUTROS PRODUTOS NO CARRINHO AO FINALIZAR A COMPRA?"
          f"\nNão."
          f"\nApós finalizada, a compra não poderá ser alterada. Para adquirir outro produto, você deverá iniciar uma "
          f"\nnova Compra."

          f"\n\n2 - POSSO FAZER MINHA COMPRA NO SITE E RETIRAR OS PRODUTOS NA LOJA FÍSICA?"
          f"\nSim!"
          f"\nNeste momento, estamos trabalhamos somente com retiradas na loja física. Estamos adaptando nossos processos"
          f"\npara que futuramente nossos clientes possam receber seus produtos em casa. Dúvidas entre em contato conosco!"

          f"\n\n3 - EXISTE UM VALOR MINÍMO DE PEDIDO?"
          f"\nNão."
          f"\nVocê pode aproveitar nossas ofertas quantas vezes desejar."

          f"\n\n4 - POSSO RETOMAR UM CARRINHO DE COMPRAS?"
          f"\nSim!"
          f"\nDesde que os produtos nele indicados ainda estejam disponíveis em estoque, será possível recuperar o "
          f"\ncarrinho de compras e finalizar a Compra."

          f"\n\n5 - QUAIS SÃO OS MEIOS DE PAGAMENTOS DISPONÍVEIS?"
          f"\nAtualmente trabalhamos somente com dinheiro e cartão."

          f"\n\n6 - QUAIS SÃO OS PRAZOS PARA ESTORNO DE VALORES PAGOS COM CARTÃO?"
          f"\nA loja pedirá o estorno à administradora de cartões dentro de 72 (setenta e duas) horas. No entanto, "
          f"\nvocê deverá aguardar o estorno na fatura. O estorno poderá acontecer em até duas faturas, de acordo com "
          f"\na política de cancelamento da administradora do cartão de crédito."

          f"\n\n7 - POSSO CANCELAR MINHA COMPRA?"
          f"\nSim!"
          f"\nSe quiser cancelar uma compra já efetivada, você deve dirigir-se pessoalmente a uma de nossas lojas "
          f"\nfísicas ou entrar nem contato conosco pelo telefone (11) 98111-1111 ou pelos outros meios de contato "
          f"\ndisponibilizados. Nos dois casos, nossos atendentes orientarão você com relação ao processo por completo."

          f"\n\n8 - COMO POSSO ENTRAR EM CONTATO?"
          f"\nVocê pode entrar em contato conosco por meio do endereço de email suporte_cliente@g5stars.com, enviar "
          f"uma mensagem ou realizar uma ligação para o número de telefone (Whatsapp/ Telegram): +55 (11) 98111-1111."
          )

def ver_carrinho(carrinho_usuario, lista_precos_total, nome_usuario, email_usuario, agendamento):
    print(f"\nCHECKOUT:"
          f"\n\nOBS.: CASO TENHA UTILIZADO SOMENTE O SERVIÇO DE AGENDAMENTO, ESCOLHA QUALQUER CONDIÇÃO DE PAGAMENTO!"
          f"\nO SERVIÇO DE AGENDAMENTO NÃO POSSUI CUSTOS."
          f"\n\n- Cliente: {nome_usuario}"
          f"\n- Email: {email_usuario}"
          f"\n- Serviços: {agendamento}"
          f"\n- Total parcial: R$ {calcula_total(lista_precos_total)}"
          f"\n\n- Produtos no carrinho:")

    for i in range(len(carrinho_usuario)):
        print(f"--- {carrinho_usuario[i]} | R$ {lista_precos_total[i]}")

def sumariza_cartao(metodo_pagamento, precos_total, valor_total_com_desconto):
    print(f"\n{metodo_pagamento.upper()} SELECIONADO:"
          f"\n- Total (sem descontos) = R$ {precos_total}"
          f"\n- Total (com acréscimo) = R$ {valor_total_com_desconto}")

    print(f"\n- Valor a pagar: R$ {valor_total_com_desconto}")

def sumariza_metodo_pagamento(nome_loja, nome_usuario, email_usuario, metodo_pagamento, condicao_pagamento,
                              precos_total, valor_total_com_desconto):
    print(f"\n-- NOME DA LOJA = {nome_loja} --"
          f"\n\n- Cliente = {nome_usuario}"
          f"\n- Email = {email_usuario}"
          f"\n- Método de pagamento = {metodo_pagamento}"
          f"\n- Condição = {condicao_pagamento}"
          f"\n- Total (sem descontos) = R$ {precos_total}"
          f"\n- Total (com descontos/ acréscimos) = R$ {valor_total_com_desconto}")

    if precos_total >= valor_total_com_desconto or precos_total == valor_total_com_desconto:
        print(f"\n- Valor a ser pago: R$ {valor_total_com_desconto}")

# INICIO ---------------------------------------------------------------------
nome_loja = "5 STARS"

# VARIÁVEIS DE CONTROLE E VARIÁVEIS/LISTAS PRINCIPAIS ---------------------------------------------------------------------
'''AS VARIÁVEIS/ FLAGS DE CONTROLE SÃO USADAS PARA DIRECIONAR O USUÁRIO PARA QUALQUER PARTE DO PROGRAMA'''
flag_controle_1 = 1
flag_controle_2 = 2

carrinho_usuario = []
lista_precos_total = []
nome_usuario = ""
email_usuario = ""
agendamento = 0
cancelamento = ""

# NECESSÁRIO DECLARAR ESSAS VARIAVEIS PARA CONTROLE DE SAÍDA / RETORNO DO CÓDIGO
menu_1, menu_2, menu_21, menu_22, menu_221, menu_23, menu_24 = None, None, None, None, None, None, None
perifericos = None

'''LAÇO PRINCIPAL DO PROGRAMA'''
while True:
    print(f"\n- - - - - - LOJA DE INFORMÁTICA {nome_loja} - - - - - -\n" + "-" * 100 +
          f"\nNOSSOS MEIOS DE CONTATO:"
          f"\nEmail: suporte_ao_cliente@g5stars.com"
          f"\nTelefone (Whatsapp/ Telegram): +55 (11) 98111-1111\n")

    # BLOCO 1 (INICIO) ---------------------------------------------------------------------
    '''REQUISITO 1
        Criar um programa que simule um software de acordo com o segmento que foi definido para a sua equipe. 
        O software deverá seguir as especificações abaixo:
        Ao executar o algoritmo, deverá aparecer duas opções:
        A - Para acessar o programa ou 
        F - Para finalizar o programa'''

    if flag_controle_1 == 1:
        nome_usuario = str.capitalize(input(f"{periodo_do_dia()}!"
                                            f"\nPARA MELHOR EXPERIÊNCIA EM NOSSO AMBIENTE, INFORME:\n"
                                            f"\nNOME: "))

        email_usuario = str.lower(input("EMAIL: "))

        print("\n" + "-" * 100)

        if nome_usuario == "" and email_usuario == "":
            nome_usuario = "Visitante"
            email_usuario = "A Nota Fiscal será impressa ao final da operação!"

        elif nome_usuario == "":
            nome_usuario = "Visitante"

        elif email_usuario == "":
            email_usuario = "A Nota Fiscal será impressa ao final da operação!"

        while True:
            try:
                menu_1 = str.lower(input(f"\nSEJA BEM VINDO {nome_usuario}! DESEJA INICIAR O SISTEMA?\n"
                                         "\nS - Sim"
                                         "\nN - Não"
                                         "\n\nDigite sua escolha: "))

                if menu_1 == "s" or menu_1 == "n":
                    break

                else:
                    print("-" * 100 + "\nHum... Vocẽ digitou um valor inválido. Comece Novamente!\n" + "-" * 100)
                    continue

            except:
                print("-" * 100 + "\nHum... Vocẽ digitou um valor inválido. Comece Novamente!\n" + "-" * 100)
                continue

    if menu_1 == "s":
        flag_controle_2 = 2

    elif menu_1 == "n":
        flag_controle_1 = 1
        print("-" * 100 + "\nObrigado por usar o nosso sistema! Volte sempre!\n" + "-" * 100)
        continue

    else:
        flag_controle_1 = 1
        continue

    # BLOCO 2 (ESCOLHE SERVIÇO E PRODUTOS) ---------------------------------------------------------------------
    '''REQUISITO 2
        A cada produto ou serviço selecionado, deverá aumentar o valor a ser pago na conta , igualmente num caixa 
        de supermercado convencional . considerando que o cliente pode levar mais de uma quantidade do mesmo produto/
        serviço (ex : 2 caixas de leite , 2 trocas de pneus ) . (LISTAS)'''

    print("\n" + "-" * 100)

    # SESSÃO DE CATEGORIAS
    if menu_1 == "s" and flag_controle_1 == 1 or flag_controle_2 == 2:
        lista_servicos = ['Produtos', 'Gift Card Digital', 'Agendamento online (Entrega\ Retirada\ Orçamento)',
                          'Esclarecer dúvidas frequentes (FAQ)', 'Voltar ao início']

        while True:
            try:
                menu_2 = int(input(f"\nO QUE VOCÊ PROCURA HOJE?\n"
                                   f"\n1 - {lista_servicos[0]}"  # Produtos
                                   f"\n2 - {lista_servicos[1]}"  # Gift Card
                                   f"\n3 - {lista_servicos[2]}"  # Agendamento orçamento online
                                   f"\n4 - {lista_servicos[3]}"  # Dúvidas Frequentes
                                   f"\n0 ** {lista_servicos[4]}"  # Voltar ao inicio
                                   f"\n\nDigite sua escolha: "))

                if menu_2 == 0 or menu_2 == 1 or menu_2 == 2 or menu_2 == 3 or menu_2 == 4:
                    break

                else:
                    print("-" * 100 + "\nHum... Vocẽ digitou um valor inválido. Comece Novamente!\n" + "-" * 100)
                    continue

            except:
                print("-" * 100 + "\nHum... Vocẽ digitou um valor inválido. Comece Novamente!\n" + "-" * 100)
                continue

        # SESSÃO DE PRODUTOS
        if menu_2 == 1:
            print("\n" + "-" * 100)

            computadores, monitores, perifericos, redes = 0, 0, 0, 0

            lista_categorias = ['Computadores', 'Monitores', 'Periféricos', 'Redes', 'Voltar ao início']

            lista_produtos_computadores = ['Desktop Dell Vostro 3681 ', 'Notebook Lenovo G-4080',
                                           'Tablet Samsung Galaxy Note S7', 'Voltar ao início']
            lista_produtos_monitores = ["Monitor Dell SE2216H 21'", "Monitor Lenovo Y25 21'",
                                        "Monitor Samsung Odyssey 49'", 'Voltar ao início']
            lista_produtos_perifericos = ['Mouse Wireless Dell WM126', 'Webcam Lenovo 300',
                                          'Teclado Samsung KBD10000 Retroiluminado', 'Voltar ao início']
            lista_produtos_redes = ['Placa de rede Intel Gb-Ex930', 'Roteador Wireless TP-Link AC1350',
                                    'Voltar ao início']

            lista_precos_produtos_computadores = [3000, 2000, 5000]
            lista_precos_produtos_monitores = [1500, 2000, 10000]
            lista_precos_produtos_perifericos = [100, 300, 250]
            lista_precos_produtos_redes = [300, 400]

            while True:
                try:
                    menu_21 = int(input(f"\nBEM VINDO A SESSÃO DE {lista_servicos[0].upper()}! ESCOLHA A CATEGORIA!\n"
                                        f"\n1 - {lista_categorias[0]}"  # Computadores
                                        f"\n2 - {lista_categorias[1]}"  # Monitores
                                        f"\n3 - {lista_categorias[2]}"  # Periféricos
                                        f"\n4 - {lista_categorias[3]}"  # Redes
                                        f"\n0 ** {lista_categorias[4]}"  # Voltar ao início
                                        "\n\nDigite sua escolha: "))

                    if menu_21 == 0 or menu_21 == 1 or menu_21 == 2 or menu_21 == 3 or menu_21 == 4:
                        break

                    else:
                        print("-" * 100 + "\nHum... Vocẽ digitou um valor inválido. Comece Novamente!\n" + "-" * 100)
                        continue

                except:
                    print("-" * 100 + "\nHum... Vocẽ digitou um valor inválido. Comece Novamente!\n" + "-" * 100)
                    continue

            # SE COMPUTADORES
            if menu_21 == 1:
                print("\n" + "-" * 100)

                while True:
                    try:
                        computadores = int(input(f"\nCATEGORIA {lista_categorias[0].upper()}! ESCOLHA UMA DAS OPÇÕES!\n"
                                                 f"\n1 - {lista_produtos_computadores[0]} | R$ {lista_precos_produtos_computadores[0]}"
                                                 f"\n2 - {lista_produtos_computadores[1]} | R$ {lista_precos_produtos_computadores[1]}"
                                                 f"\n3 - {lista_produtos_computadores[2]} | R$ {lista_precos_produtos_computadores[2]}"
                                                 f"\n0 ** {lista_produtos_monitores[3]}"
                                                 f"\n\nDigite sua escolha: "))

                        if computadores == 0 or computadores == 1 or computadores == 2 or computadores == 3:
                            break

                        else:
                            print(
                                "-" * 100 + "\nHum... Vocẽ digitou um valor inválido. Comece Novamente!\n" + "-" * 100)
                            continue

                    except:
                        print("-" * 100 + "\nHum... Vocẽ digitou um valor inválido. Comece Novamente!\n" + "-" * 100)
                        continue

                if computadores == 1:
                    carrinho_usuario.append(lista_produtos_computadores[0])
                    lista_precos_total.append(lista_precos_produtos_computadores[0])

                elif computadores == 2:
                    carrinho_usuario.append(lista_produtos_computadores[1])
                    lista_precos_total.append(lista_precos_produtos_computadores[1])

                elif computadores == 3:
                    carrinho_usuario.append(lista_produtos_computadores[2])
                    lista_precos_total.append(lista_precos_produtos_computadores[2])

            # MONITORES
            elif menu_21 == 2:
                print("\n" + "-" * 100)

                while True:
                    try:
                        monitores = int(input(f"\nCATEGORIA {lista_categorias[1].upper()}! ESCOLHA UMA DAS OPÇÕES!\n"
                                              f"\n1 - {lista_produtos_monitores[0]} | R$ {lista_precos_produtos_monitores[0]}"
                                              f"\n2 - {lista_produtos_monitores[1]} | R$ {lista_precos_produtos_monitores[1]}"
                                              f"\n3 - {lista_produtos_monitores[2]} | R$ {lista_precos_produtos_monitores[2]}"
                                              f"\n0 ** {lista_produtos_monitores[3]}"
                                              f"\n\nDigite sua escolha: "))

                        if monitores == 0 or monitores == 1 or monitores == 2 or monitores == 3:
                            break

                        else:
                            print(
                                "-" * 100 + "\nHum... Vocẽ digitou um valor inválido. Comece Novamente!\n" + "-" * 100)
                            continue

                    except:
                        print("-" * 100 + "\nHum... Vocẽ digitou um valor inválido. Comece Novamente!\n" + "-" * 100)
                        continue

                if monitores == 1:
                    carrinho_usuario.append(lista_produtos_monitores[0])
                    lista_precos_total.append(lista_precos_produtos_monitores[0])

                elif monitores == 2:
                    carrinho_usuario.append(lista_produtos_monitores[1])
                    lista_precos_total.append(lista_precos_produtos_monitores[1])

                elif monitores == 3:
                    carrinho_usuario.append(lista_produtos_monitores[2])
                    lista_precos_total.append(lista_precos_produtos_monitores[2])

            # PERIFÉRICOS
            elif menu_21 == 3:
                print("\n" + "-" * 100)

                while True:
                    try:
                        perifericos = int(input(f"\nCATEGORIA {lista_categorias[2].upper()}! ESCOLHA UMA DAS OPÇÕES!\n"
                                                f"\n1 - {lista_produtos_perifericos[0]} | R$ {lista_precos_produtos_perifericos[0]}"
                                                f"\n2 - {lista_produtos_perifericos[1]} | R$ {lista_precos_produtos_perifericos[1]}"
                                                f"\n3 - {lista_produtos_perifericos[2]} | R$ {lista_precos_produtos_perifericos[2]}"
                                                f"\n0 ** {lista_produtos_perifericos[3]}"
                                                f"\n\nDigite sua escolha: "))

                        if perifericos == 0 or perifericos == 1 or perifericos == 2 or perifericos == 3:
                            break

                        else:
                            print(
                                "-" * 100 + "\nHum... Vocẽ digitou um valor inválido. Comece Novamente!\n" + "-" * 100)
                            continue

                    except:
                        print("-" * 100 + "\nHum... Vocẽ digitou um valor inválido. Comece Novamente!\n" + "-" * 100)
                        continue

                if perifericos == 1:
                    carrinho_usuario.append(lista_produtos_perifericos[0])
                    lista_precos_total.append(lista_precos_produtos_perifericos[0])

                elif perifericos == 2:
                    carrinho_usuario.append(lista_produtos_perifericos[1])
                    lista_precos_total.append(lista_precos_produtos_perifericos[1])

                elif perifericos == 3:
                    carrinho_usuario.append(lista_produtos_perifericos[2])
                    lista_precos_total.append(lista_precos_produtos_perifericos[2])

            # REDES
            elif menu_21 == 4:
                print("\n" + "-" * 100)

                while True:
                    try:
                        redes = int(input(f"\nCATEGORIA {lista_categorias[3].upper()}! ESCOLHA UMA DAS OPÇÕES!\n"
                                          f"\n1 - {lista_produtos_redes[0]} | R$ {lista_precos_produtos_redes[0]:}"
                                          f"\n2 - {lista_produtos_redes[1]} | R$ {lista_precos_produtos_redes[1]}"
                                          f"\n0 ** {lista_produtos_redes[2]}"
                                          f"\n\nDigite sua escolha: "))

                        if redes == 0 or redes == 1 or redes == 2:
                            break

                        else:
                            print(
                                "-" * 100 + "\nHum... Vocẽ digitou um valor inválido. Comece Novamente!\n" + "-" * 100)
                            continue

                    except:
                        print("-" * 100 + "\nHum... Vocẽ digitou um valor inválido. Comece Novamente!\n" + "-" * 100)
                        continue

                if redes == 1:
                    carrinho_usuario.append(lista_produtos_redes[0])
                    lista_precos_total.append(lista_precos_produtos_redes[0])

                elif redes == 2:
                    carrinho_usuario.append(lista_produtos_redes[1])
                    lista_precos_total.append(lista_precos_produtos_redes[1])

            elif menu_21 or computadores or monitores or perifericos or redes == 0:
                menu_1 = "s"
                flag_controle_1 = 0
                flag_controle_2 = 2

                print("-" * 100 + "\nAguarde! Voltando ao inicio...\n" + "-" * 100)

                continue

        # SESSÃO DE GIFT CARD
        elif menu_2 == 2:
            print("\n" + "-" * 100)

            lista_gifts_card = ['Gift Card Amazon', 'Gift Card Apple Store', 'Gift Card Play Store', 'Voltar ao início']
            lista_precos_gift_card = [20, 50, 100, 200, 'Voltar ao inicio']

            while True:
                try:
                    menu_22 = int(input(f"\nBEM VINDO A SESSÃO DE {lista_servicos[1].upper()}! ESCOLHA UM ACESSO!\n"
                                        f"\n1 - {lista_gifts_card[0]}"  # Amazon
                                        f"\n2 - {lista_gifts_card[1]}"  # Apple Store
                                        f"\n3 - {lista_gifts_card[2]}"  # Play Store              
                                        f"\n0 ** {lista_gifts_card[3]}"  # Voltar ao início
                                        f"\n\nDigite sua escolha: "))

                    if menu_22 == 0 or menu_22 == 1 or menu_22 == 2 or menu_22 == 3:
                        break

                    else:
                        print("-" * 100 + "\nHum... Vocẽ digitou um valor inválido. Comece Novamente!\n" + "-" * 100)
                        continue

                except:
                    print("-" * 100 + "\nHum... Vocẽ digitou um valor inválido. Comece Novamente!\n" + "-" * 100)
                    continue

            # ADICIONA O PRODUTO NO CARRINHO DO USUÁRIO
            if menu_22 == 1:
                carrinho_usuario.append(lista_gifts_card[0])

            if menu_22 == 2:
                carrinho_usuario.append(lista_gifts_card[1])

            if menu_22 == 3:
                carrinho_usuario.append(lista_gifts_card[2])

            elif menu_22 == 0:
                flag_controle_1 = 0
                flag_controle_2 = 2
                print("-" * 100 + "\nAguarde! Voltando ao inicio...\n" + "-" * 100)
                continue

            print("\n" + "-" * 100)

            while True:
                try:
                    menu_221 = int(input("\nESCOLHA O PREÇO DO GIFT CARD!\n"
                                         f"\n1 - para R$ {lista_precos_gift_card[0]}"  # 15
                                         f"\n2 - para R$ {lista_precos_gift_card[1]}"  # 20
                                         f"\n3 - para R$ {lista_precos_gift_card[2]}"  # 50
                                         f"\n4 - para R$ {lista_precos_gift_card[3]}"  # 100
                                         f"\n0 ** {lista_precos_gift_card[4]}"  # Voltar ao inicio
                                         f"\n\nDigite sua escolha: "))

                    if menu_221 == 0 or menu_221 == 1 or menu_221 == 2 or menu_221 == 3 or menu_221 == 4:
                        break

                    else:
                        print("-" * 100 + "\nHum... Vocẽ digitou um valor inválido. Comece Novamente!\n" + "-" * 100)
                        continue

                except:
                    print("-" * 100 + "\nHum... Vocẽ digitou um valor inválido. Comece Novamente!\n" + "-" * 100)
                    continue

            # ADICIONA O PREÇO DO PRODUTO
            if menu_221 == 1:
                lista_precos_total.append(lista_precos_gift_card[0])

            elif menu_221 == 2:
                lista_precos_total.append(lista_precos_gift_card[1])

            elif menu_221 == 3:
                lista_precos_total.append(lista_precos_gift_card[2])

            elif menu_221 == 4:
                lista_precos_total.append(lista_precos_gift_card[3])

            elif menu_221 == 0:
                menu_1 = "s"
                flag_controle_1 = 0
                flag_controle_2 = 2
                print("-" * 100 + "\nAguarde! Voltando ao inicio...\n" + "-" * 100)
                continue

        # SESSÃO DE AGENDAMENTO ONLINE DE ORÇAMENTO
        elif menu_2 == 3:
            print("\n" + "-" * 100)

            while True:
                try:
                    menu_23 = int(input(f"\nBEM VINDO A SESSÃO {lista_servicos[2].upper()}!\n\n" +
                                        "-" * 60 + f"\nINFORMAMOS QUE OS SERVIÇOS RELACIONADOS AO AGENDAMENTO SÃO REALIZADOS EM DIAS DA SEMANA E "
                                                   f"\nHORARIOS ESPECÍFICOS."
                                                   "\n\nOBS.: PARA VERIFICAR A DISPONIBILIDADE DE OUTROS DIAS DA SEMANA E HORÁRIOS, FAVOR ENTRE CONTATO POR MEIO "
                                                   f"\nDOS NOSSOS CANAIS DE ATENDIMENTO!\n" + "-" * 60 +
                                        f"\n\n1 - Consultar datas e horários"
                                        f"\n0 ** Voltar ao inicio"
                                        f"\n\nDigite sua escolha: "))

                    if menu_23 == 0 or menu_23 == 1:
                        break

                    else:
                        print("-" * 100 + "\nHum... Vocẽ digitou um valor inválido. Comece Novamente!\n" + "-" * 100)
                        continue

                except:
                    print("-" * 100 + "\nHum... Vocẽ digitou um valor inválido. Comece Novamente!\n" + "-" * 100)
                    continue

            if menu_23 == 1:
                print("\n" + "-" * 100)

            if menu_23 == 0:
                menu_1 = "s"
                flag_controle_1 = 0
                flag_controle_2 = 2

                print("-" * 100 + "\nAguarde! Voltando ao inicio...\n" + "-" * 100)

                continue

            lista_agendamento = ['Agendamento: Segunda Feira | 8:00 ás 12:00',
                                 'Agendamento: Terça Feira | 8:00 ás 15:00',
                                 'Agendamento: Sábado | 9:00 ás 18:00',
                                 'Voltar ao inicio do programa']

            while True:
                try:
                    agendamento = int(input("\nFAÇA SUA ESCOLHA DE ACORDO COM A LISTA DE CONSULTA ABAIXO:"
                                            f"\n\n1 - {lista_agendamento[0]}"  # Segunda
                                            f"\n2 - {lista_agendamento[1]}"  # Terça
                                            f"\n3 - {lista_agendamento[2]}"  # Sabádo
                                            f"\n0 **  {lista_agendamento[3]}"
                                            "\n\nDigite sua escolha: "))

                    if agendamento == 0 or agendamento == 1 or agendamento == 2 or agendamento == 3:
                        break

                    else:
                        print("-" * 100 + "\nHum... Vocẽ digitou um valor inválido. Comece Novamente!\n" + "-" * 100)
                        continue

                except:
                    print("-" * 100 + "\nHum... Vocẽ digitou um valor inválido. Comece Novamente!\n" + "-" * 100)
                    continue

            if agendamento == 1:
                print("\nAgendamento realizado com sucesso!"
                      "\nEsse serviço não possui custos!")

                carrinho_usuario.append(lista_agendamento[0])
                lista_precos_total.append(0)
                agendamento = lista_agendamento[0]

            elif agendamento == 2:
                print("\nAgendamento realizado com sucesso!"
                      "\nEsse serviço não possui custos!")

                carrinho_usuario.append(lista_agendamento[1])
                lista_precos_total.append(0)
                agendamento = lista_agendamento[1]

            elif agendamento == 3:
                print("\nAgendamento realizado com sucesso!"
                      "\nEsse serviço possui tem custos!")

                carrinho_usuario.append(lista_agendamento[2])
                lista_precos_total.append(0)
                agendamento = lista_agendamento[2]

            elif agendamento == 0:
                menu_1 = "s"
                flag_controle_1 = 0
                flag_controle_2 = 2

                print("-" * 100 + "\nAguarde! Voltando ao inicio...\n" + "-" * 100)

                continue

        # SESSÃO DÚVIDAS FREQUENTES (FAQ)
        elif menu_2 == 4:
            print("\n" + "-" * 100)

            print(f"\nBEM VINDO A SESSÃO {lista_servicos[3].upper()}!\n")

            while True:
                # FUNÇÃO QUE EXIBE TEXTO COM AS INFORMAÇÕES
                duvidas_frequentes()

                try:
                    menu_24 = int(
                        input(f"\n" + ("-" * 100) + "\n\nSUAS DÚVIDAS FORAM ESCLARECIDAS? O QUE DESEJA FAZER AGORA?\n"
                                                    f"\n1 - Visualizar novamente as informações"
                                                    f"\n0 ** Voltar ao início"
                                                    f"\n\nDigite sua escolha: "))

                    if menu_24 == 1:
                        print("\n" + "-" * 100 + "\n")
                        continue

                    elif menu_24 == 0:
                        break

                    else:
                        print("-" * 100 + "\nHum... Vocẽ digitou um valor inválido. Comece Novamente!\n" + "-" * 100)
                        continue

                except:
                    print("-" * 100 + "\nHum... Vocẽ digitou um valor inválido. Comece Novamente!\n" + "-" * 100)
                    continue

            if menu_24 == 0:
                menu_1 = "s"
                flag_controle_1 = 0
                flag_controle_2 = 2
                carrinho_usuario = [].clear()
                lista_precos_total = [].clear()

                print("-" * 100 + "\nAguarde! Voltando ao inicio...\n" + "-" * 100)
                continue

        elif menu_2 == 0:
            menu_1 = "s"
            flag_controle_1 = 0
            flag_controle_2 = 2

            print("-" * 100 + "\nAguarde! Voltando ao inicio...\n" + "-" * 100)

            continue

    # BLOCO 3 (CHECKOUT / EXIBIÇÃO DOS DADOS) ---------------------------------------------------------------------
    '''REQUISITO 3
        Ao fechar/concluir o processo de seleção de produtos/serviços deve exibir ao cliente o total de valor a ser 
        pago e pedir para que o cliente selecione a forma de pagamento , obrigatoriamente deve existir a forma de pagamento 
        em dinheiro que gere troco , caso o troco seja gerado deve-se informar o valor do troco e quantas cedulas vão ser 
        dadas para o cliente, sempre considere a menor quantidade de cédulas possíveis . 
        (LISTA, IF, EXIBIR SOMA, **EXCLUIR ITEM)'''

    # CASO O USUÁRIO QUEIRA ADD MAIS PRODUTOS NO CARRINHO
    print("\n" + "-" * 100)

    checkout = ""

    while True:
        try:
            checkout = str.lower(input("\nDESEJA ADICIONAR MAIS PRODUTOS AO CARRINHO?\n"
                                       "\nS - Sim"
                                       "\nN - Não (Você será direcionado(a) a sessão de pagamento)"
                                       "\n\nv - Ver carrinho"
                                       "\nx ** Finalizar sessão (zera o carrinho e inicia uma nova sessão)"
                                       "\n\nDigite sua escolha: "))

            if checkout == "s" or checkout == "x":
                break

            elif checkout == "n":
                if len(lista_precos_total) > 0:
                    break

                else:
                    print(
                        "-" * 100 + f"\nSeu carrinho está vazio! Não há pagamentos a serem processados!\n" + "-" * 100)
                    continue

            elif checkout == "v":
                if len(lista_precos_total) > 0:
                    ver_carrinho(carrinho_usuario, lista_precos_total, nome_usuario, email_usuario, agendamento)

                else:
                    print(
                        "-" * 100 + f"\nSeu carrinho está vazio! Não há produtos e/ou pagamentos a serem exibidos!\n" + "-" * 100)
                    continue

            else:
                print("-" * 100 + "\nHum... Vocẽ digitou um valor inválido. Comece Novamente!\n" + "-" * 100)
                continue

        except:
            print("-" * 100 + "\nHum... Vocẽ digitou um valor inválido. Comece Novamente!\n" + "-" * 100)
            continue

    if checkout == "s":
        menu_1 = "s"
        flag_controle_1 = 0
        flag_controle_2 = 2
        continue

    elif checkout == "x":
        flag_controle_1 = 1
        print("-" * 100 + "\nSua sessão foi finalizada!"
                          "\nObrigado por usar nosso sistema! Volte sempre!\n" + "-" * 100)

        carrinho_usuario.clear()
        lista_precos_total.clear()

        continue

    elif checkout == "n":
        pass

    # PASSA DADOS PARA A FUNÇÃO E IMPRIME A LISTA DE PRODUTOS DO CARRINHO E OS PREÇOS DOS RESPECTIVOS PRODUTOS
    print("\n" + "-" * 100)

    ver_carrinho(carrinho_usuario, lista_precos_total, nome_usuario, email_usuario, agendamento)

    # FECHAMENTO
    '''REQUISITO 4
        As cédulas disponíveis são : 50 , 20 , 10 , 5 ,2 e 1 real . Pode descartar valores de centavos 
        (USAR VALORES EXATOS)'''
    print("\n" + "-" * 100)

    desconto_dinheiro = 0.10
    desconto_cartao = 0.05
    acrescimo_cartao = 0.10
    valor_total_com_desconto = 0
    condicao_pagamento = ""

    lista_metodo_pagamento = ['Dinheiro', 'Cartão', 'Voltar ao inicio']
    lista_condicao_pagamento = ['10% de desconto | Troco: Notas de R$ 50, R$ 20, R$ 10, R$ 5, R$ 2 | Moedas de R$ 1',
                                '5% no débito | à vista',
                                '2x no crédito | sem desconto',
                                '3x no crédito | acréscimo de 10% de juros', 'Espécie']

    # PASSA A LISTA DE PREÇO TOTAL PARA A FUNÇÃO COM TODOS OS PREÇOS DO CARRINHO E RECEBE O VALOR TOTAL CALCULADO
    metodo_pagamento = 0

    precos_total = calcula_total(lista_precos_total)

    while True:
        try:
            metodo_pagamento = int(input("\nESCOLHA A CONDIÇÃO DE PAGAMENTO:\n"
                                         f"\n1 - {lista_metodo_pagamento[0]} ({lista_condicao_pagamento[0]})"
                                         f"\n2 - {lista_metodo_pagamento[1]} ({lista_condicao_pagamento[1]})"
                                         f"\n3 - {lista_metodo_pagamento[1]} ({lista_condicao_pagamento[2]})"
                                         f"\n4 - {lista_metodo_pagamento[1]} ({lista_condicao_pagamento[3]})"
                                         f"\n\n0 ** {lista_metodo_pagamento[2]}"
                                         f"\n5 ** Cancelar compras (zera o carrinho e inicia uma nova sessão)"
                                         f"\n\nDigite sua escolha: "))

            if metodo_pagamento == 0 or metodo_pagamento == 1 or metodo_pagamento == 2 or \
                    metodo_pagamento == 3 or metodo_pagamento == 4 or metodo_pagamento == 5:
                break

            else:
                print("-" * 100 + "\nHum... Vocẽ digitou um valor inválido. Comece Novamente!\n" + "-" * 100)
                continue

        except:
            print("-" * 100 + "\nHum... Vocẽ digitou um valor inválido. Comece Novamente!\n" + "-" * 100)
            continue

    # PAGAMENTO NO DINHEIRO
    if metodo_pagamento == 1:
        metodo_pagamento = lista_metodo_pagamento[0].capitalize()
        condicao_pagamento = lista_condicao_pagamento[4]

        valor_total_com_desconto = precos_total - (precos_total * desconto_dinheiro)

        print("\n" + "-" * 100)

        sumariza_metodo_pagamento(nome_loja, nome_usuario, email_usuario, metodo_pagamento, condicao_pagamento,
                                  precos_total, valor_total_com_desconto)

        # VALOR QUE O CLIENTE IRÁ PAGAR
        notas = 0

        while True:
            try:
                notas = float(input(f"\nInsira em notas (cédulas) o valor a ser pago: R$ "))

                if notas < valor_total_com_desconto:
                    print("-" * 60 + f"\nVocê inseriu um valor insuficientes! Por favor, insira em notas (cédulas) "
                                     f"o valor a ser pago!\n" + "-" * 60)
                    continue

                elif notas >= valor_total_com_desconto:
                    break

                else:
                    print("-" * 60 + f"\nVocê inseriu um valor insuficientes! Por favor, insira em notas (cédulas) "
                                     f"o valor a ser pago!\n" + "-" * 60)
                    continue

            except:
                print("-" * 100 + "\nHum... Vocẽ digitou um valor inválido. Comece Novamente!\n" + "-" * 100)
                continue

        # SE NECESSÁRIO TROCO
        if notas > valor_total_com_desconto:
            troco = notas - valor_total_com_desconto
            cedulas = [50, 20, 10, 5, 2]

            print("\n" + "-" * 100 + "\n\nAPÓS CONFIRMAÇÃO DO PAGAMENTO, VOCÊ RECEBERÁ:")

            print(f"\n- Valor do troco: R$ {troco}")
            calculo_cedulas = [troco // 50, (troco % 50) // 20, ((troco % 50) % 20) // 10,
                               (((troco % 50) % 20) % 10) // 5, ((((troco % 50) % 20) % 10) % 5) // 2,
                               (((((troco % 50) % 20) % 10) % 5) % 2) // 1]

            for i in range(len(calculo_cedulas)):
                if calculo_cedulas[i] > 0:
                    print(f"- {calculo_cedulas[i]} cédulas de R$ {cedulas[i]}")

        elif notas == valor_total_com_desconto:
            print(
                "-" * 100 + "\nNão há troco a ser calculado! O processo de finalização seguirá normalmente\n" + "-" * 100)

    elif metodo_pagamento == 0:
        menu_1 = "s"
        flag_controle_1 = 0
        flag_controle_2 = 2

        print("-" * 100 + "\nAguarde! Voltando ao inicio...\n" + "-" * 100)

        continue

    while metodo_pagamento == 5:
        print("\n" + "-" * 100)

        try:
            cancelamento = str.lower(input(f"\nDESEJA REALMENTE CANCELAR SUAS COMPRAS?\n"
                                           f"\nS - Sim"
                                           f"\nN - Não"
                                           f"\n\nDigite sua escolha: "))

            if cancelamento == "s" or cancelamento == "n":
                break

            else:
                print("-" * 100 + "\nHum... Vocẽ digitou um valor inválido. Comece Novamente!\n" + "-" * 100)
                continue

        except:
            print("-" * 100 + "\nHum... Vocẽ digitou um valor inválido. Comece Novamente!\n" + "-" * 100)
            continue

    # CANCELAMENTO
    if cancelamento == "s":
        flag_controle_1 = 1

        carrinho_usuario.clear()
        lista_precos_total.clear()

        print("-" * 100 + "\nSua compra foi cancelada e sua sessão finalizada!"
                          "\nObrigado por usar nosso sistema! Volte sempre!\n" + "-" * 100)

        continue

    elif cancelamento == "n":
        print("\n" + "-" * 100)

        ver_carrinho(carrinho_usuario, lista_precos_total, nome_usuario, email_usuario, agendamento)
        pass

    else:
        # A VISTA NO CARTÃO
        if metodo_pagamento == 2:
            metodo_pagamento = lista_metodo_pagamento[1].capitalize()
            condicao_pagamento = lista_condicao_pagamento[1]

            valor_total_com_desconto = (precos_total - (precos_total * desconto_cartao))

            print("\n" + "-" * 100)

            sumariza_cartao(metodo_pagamento, precos_total, valor_total_com_desconto)

        # 2x NO CARTÃO
        elif metodo_pagamento == 3:
            metodo_pagamento = lista_metodo_pagamento[1].capitalize()
            condicao_pagamento = f"{lista_condicao_pagamento[2]} | R$ {precos_total / 2:.2f}"

            valor_total_com_desconto = precos_total

            sumariza_cartao(metodo_pagamento, precos_total, valor_total_com_desconto)

        # 3x NO CARTÃO
        elif metodo_pagamento == 4:
            metodo_pagamento = lista_metodo_pagamento[1].capitalize()
            condicao_pagamento = f"{lista_condicao_pagamento[3]} | R$ {precos_total / 3:.2f} am"

            valor_total_com_desconto = (((precos_total * acrescimo_cartao)) + precos_total)

            sumariza_cartao(metodo_pagamento, precos_total, valor_total_com_desconto)

        elif metodo_pagamento == 0:
            flag_controle_1 = 1
            carrinho_usuario = [].clear()
            lista_precos_total = [].clear()

            print("-" * 100 + "\nAguarde! Voltando ao inicio...\n" + "-" * 100)

            continue

        print("\n" + "-" * 100)

        sumariza_metodo_pagamento(nome_loja, nome_usuario, email_usuario, metodo_pagamento, condicao_pagamento,
                                  precos_total, valor_total_com_desconto)

    '''REQUISITO 5
        No processo de finalização da compra deve existir uma opção para o cliente desistir da compra , 
        em caso positivo deve ser perguntado a confirmação da desistência (informando os produtos/serviços que o 
        cliente está desistindo) (IF)'''
    print("\n" + "-" * 100)

    confirmacao = ""

    while True:
        try:
            confirmacao = str.lower(input("\nVOCÊ CONFIRMA OS DADOS ACIMA?\n"
                                          "\nS - Sim"
                                          "\nN - Não (volta ao início)"
                                          "\n\nx - Finalizar sessão (zera o carrinho e inicia uma nova sessão)"
                                          "\n\nDigite sua escolha: "))

            if confirmacao == "s" or confirmacao == "n" or confirmacao == "x":
                break

            else:
                print("-" * 100 + "\nHum... Vocẽ digitou um valor inválido. Comece Novamente!\n" + "-" * 100)
                continue

        except:
            print("-" * 100 + "\nHum... Vocẽ digitou um valor inválido. Comece Novamente!\n" + "-" * 100)
            continue

    if confirmacao == "s":
        print("\n" + "-" * 100)

        print(f"Uma Nota Fisca Eletronica (NF-E) foi encaminnhada para: {email_usuario}")

        print("-" * 100 + "\nObrigado por usar nosso sistema! Volte sempre!\n" + "-" * 100)

    elif confirmacao == "n":
        menu_1 = "s"
        flag_controle_1 = 0
        flag_controle_2 = 2
        carrinho_usuario.clear()
        lista_precos_total.clear()

        print("-" * 100 + "\nAguarde! Voltando ao inicio...\n" + "-" * 100)

        continue

    elif confirmacao == "x":
        flag_controle_1 = 1

        carrinho_usuario.clear()
        lista_precos_total.clear()

        print("-" * 100 + "\nSua sessão foi finalizada!"
                          "\nObrigado por usar nosso sistema! Volte sempre!\n" + "-" * 100)

        continue

    # FIM ---------------------------------------------------------------------
    '''REQUISITO 6  
        Ao finalizar a compra deve-se voltar a tela inicial Acessar programa / finalizar programa . 
        Quando finalizar deve-se exibir uma mensagem agradecendo a visita, informando o que foi comprado e o valor 
        gasto no estabelecimento (RESPOSTA 1º WHILE)'''
    saida = 0

    while True:
        try:
            saida = int(input("\nO QUE DESEJA FAZER AGORA?\n"
                              "\n1 - Sair do programa"
                              "\n0 ** Voltar ao menu inicial (zera o carrinho e inicia uma nova sessão)"
                              "\n\nDigite sua escolha: "))

            if saida == 0 or saida == 1:
                break

            else:
                print("-" * 100 + "\nHum... Vocẽ digitou um valor inválido. Comece Novamente!\n" + "-" * 100)
                continue

        except:
            print("-" * 100 + "\nHum... Vocẽ digitou um valor inválido. Comece Novamente!\n" + "-" * 100)
            continue

    if saida == 1:
        print("-" * 100 + "\nObrigado por usar nosso sistema! Volte sempre!\n" + "-" * 100)
        exit(0)
        break

    elif saida == 0:
        menu_1 = "s"
        flag_controle_1 = 0
        flag_controle_2 = 2

        carrinho_usuario.clear()
        lista_precos_total.clear()

        print("-" * 100 + "\nAguarde! Voltando ao inicio...\n" + "-" * 100)

    continue
