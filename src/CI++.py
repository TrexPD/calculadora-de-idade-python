from calendar import isleap, monthrange
from datetime import datetime
from rich import print
from rich.table import Table
from rich import box



# Mostra o dia da semana da data atual ou de uma data especifica! primeiro dia da semana é domingo!
def dia_semana(
    dia: int = datetime.now().day,
    mes: int = datetime.now().month,
    ano: int = datetime.now().year) -> dict:
    dia_da_semana: int = datetime.strptime(f'{ano}-{mes}-{dia}', '%Y-%m-%d').isoweekday()
    semana: dict = {
        1: 'Segunda-Feira',
        2: 'Terça-Feira',
        3: 'Quarta-Feira',
        4: 'Quinta-Feira',
        5: 'Sexta-Feira',
        6: 'Sábado',
        7: 'Domigo',
    }
    return semana[dia_da_semana]


# Função que ler apenas números inteiros!
def leia_int(msg: str) -> str:
    while True:
        try:
            numero: int = int(input(msg))
        except KeyboardInterrupt:
            print('\n[red]O usuario abartou, preferiu não inserir um valor válido![/]')
            break
        except:
            print('\n[yellow]Hummm... parece que você não digitou um número inteiro válido![/]')
        else:
            return numero


def data_correta() -> list:
    # Procura um dia válido!
    while True:
        try:
            while True:
                dia: int = leia_int('Em que dia você nasceu? ')
                if dia > 31 or dia < 1:
                    print(f"\nO [yellow]dia '{dia}'[/] é inexistente, por favor digite um dia válido!")
                else:
                    break

            # Procura um mês válido!
            while True:
                mes: int = leia_int('Em que mês você nasceu? ')
                if mes > 12 or mes < 1:
                    print(f"\nO [yellow]mês '{mes}'[/] é inexistente, por favor digite um mês válido!")
                else:
                    break

            # Procura um ano válido!
            while True:
                ano_atual: int = (datetime.now().year)
                ano: int = leia_int('Agora... digite o ano em que você nasceu? ')
                if len(str(ano)) == 4 and ano <= ano_atual:
                    break
                else:
                    print('\n[yellow]Formato inválido! O ano tem que ter 4 digitos e igual ou menor que o ano atual! (Ex: 1900)[/]')

            # Verifica se a data existe!
            datetime.strptime(f"{dia}/{mes}/{ano}", r"%d/%m/%Y")
        except ValueError: 
            print("[red]Essa data é inexistente! Por favor digite uma data válida![/]")
        else:
            return [dia, mes, ano]


# Calcula a quantidade de anos bissextos entre duas datas!
def ano_bissexto(ano_user: int, ano_atual: int) -> list:
    num_anos_bissextos: list = []
    for anos in range(ano_user, (ano_atual + 1)):
        bissexto: bool = isleap(anos)
        if bissexto:
            num_anos_bissextos.append(anos)
    return num_anos_bissextos



# Mostra uma mensagem com a quantidade de dias que faltam para o 'niver' ou caso seja o aniversario!
def aniversariante(dia_user: int, dia_atual: int, mes_user: int, meses_atual: int, proximo_niver: int) -> str:
    if dia_user == dia_atual and mes_user == meses_atual:
        return '[green]Parabéns hoje é seu aniversário![/] \U0001f973'
    else:
        return f'Faltam [yellow]{proximo_niver} dia(s)[/] para o seu aniversário!'


def main():
    # Data Nascimento
    dia_user, mes_user, ano_user = data_correta()
    dia_atual: str = (datetime.now().day)
    meses_atual: str = (datetime.now().month)
    ano_atual: str = (datetime.now().year)   
    niver_no_atual_ano = datetime.strptime(f'{ano_atual}-{mes_user}-{dia_user}', r'%Y-%m-%d')
    data_nasc = datetime.strptime(f'{ano_user}-{mes_user}-{dia_user}', r'%Y-%m-%d')    # Converte "int" para datetime!

    # Busca a data completa do atual momento!
    data_atual_string = datetime.strptime(f'{ano_atual}-{meses_atual}-{dia_atual}', r'%Y-%m-%d')

    # Realizamos o calculo da quantidade de dias, semanas, meses, ano etc...
    q_dias: int = abs(data_atual_string - data_nasc).days     # Calcula a quantidade de dias totais, da data de nascimento até a atual, com valor absoluto!
    q_anos: int = abs((q_dias - len(ano_bissexto(ano_user, ano_atual)))) / 365
    q_meses: int = int(q_anos * 12)
    q_semanas: int = q_dias // 7
    q_horas: int = q_dias * 24
    q_minutos: int = q_horas * 60
    q_segundos: int = q_minutos * 60


    # Coleta os meses entre o aniversário atual até data de hoje!
    lista_de_meses: list = []
    contador_meses: int = mes_user
    if data_atual_string >= niver_no_atual_ano:
        proximo_niver = datetime.strptime(f'{ano_atual+1}-{mes_user}-{dia_user}', r'%Y-%m-%d')
        proximo_niver: int = abs(proximo_niver - data_atual_string).days
        if meses_atual != mes_user:
            for _ in range(contador_meses, (meses_atual + 1)):
                q_meses_restantes: int = monthrange(ano_atual, contador_meses)[1]
                lista_de_meses.append(q_meses_restantes)
                contador_meses += 1
        else:
            q_meses_restantes: int = monthrange(ano_atual, contador_meses)[1]
            lista_de_meses.append(q_meses_restantes)
    else:
        ano_anterior: int = (ano_atual - 1)
        proximo_niver: int = abs(niver_no_atual_ano - data_atual_string).days
        niver_anterior = datetime.strptime(f'{ano_anterior}-{mes_user}-{dia_user}', r'%Y-%m-%d')
        # df_niver_restantes: int = abs(data_atual_string - niver_anterior).days # Diferença de dias entre o ano passado e o data atual de niver!
        while True:
            q_meses_restantes: int = monthrange(ano_anterior, contador_meses)[1]
            lista_de_meses.append(q_meses_restantes)
            contador_meses += 1
            if contador_meses == (meses_atual + 1) and ano_anterior == ano_atual:
                break
            if contador_meses == 13:
                contador_meses = 1
                ano_anterior += 1

    # Verifica e calcula a quantidade de meses e dias entre duas datas, no mesmo mês!
    q_dias_restantes = q_meses_restantes = 0
    if len(lista_de_meses) > 1:
        ultimo_mes: int = monthrange(ano_atual, meses_atual)[1]
        lista_de_meses[0] = abs(lista_de_meses[0] - dia_user)
        lista_de_meses[-1] = abs((lista_de_meses[-1] - dia_atual) - lista_de_meses[-1])
        for iteravel_meses in lista_de_meses:
            if iteravel_meses >= 28 and lista_de_meses[-1] != ultimo_mes:
                q_meses_restantes += 1
            else:
                q_dias_restantes += iteravel_meses
                if q_dias_restantes >= 30:
                    q_meses_restantes += 1
                    q_dias_restantes = q_dias_restantes % 30
    else:
        if dia_atual == lista_de_meses[0]:
            q_dias_restantes = lista_de_meses[0]
            q_meses_restantes = 0
        else:
            q_dias_restantes = abs(dia_atual - dia_user)
            q_meses_restantes = 0

    print()
    tabela = Table(f'Alguns dados sobre a data [yellow]{dia_user}/{mes_user}/{ano_user}![/]', box=box.MARKDOWN, show_lines=True)
    tabela.add_row(f'Sua idade: [yellow]{int(q_anos)} ano(s)[/] | [yellow]{q_meses_restantes} mese(s)[/] | [yellow]{q_dias_restantes} dia(s)[/]')
    tabela.add_row(aniversariante(dia_user, dia_atual, mes_user, meses_atual, proximo_niver))
    tabela.add_row(f"""
Ano(s):          [blue]{int(q_anos)}[/]
Mes(es):         [blue]{q_meses}[/]
Semana(s):       [blue]{q_semanas}[/]
Dia(s):          [blue]{q_dias}[/]
Hora(s):         [blue]{q_horas}[/]
Minuto(s):       [blue]{q_minutos}[/]
Segundo(s):      [blue]{q_segundos}[/]
Dia da semana:   [blue]{dia_semana(dia_user, mes_user, ano_user)}[/]""")
    print(tabela)


main()

