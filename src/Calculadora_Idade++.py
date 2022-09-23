from calendar import isleap, monthrange
from datetime import date, datetime


# Mostra o dia da semana da data atual ou de uma data especifica! primeiro dia da semana é domingo!
def dia_semana(
    dia=datetime.today().strftime('%d'),
    mes=datetime.today().strftime('%m'),
    ano=datetime.today().strftime('%Y'),
):
    dia_da_semana: int = datetime.strptime(
        f'{ano}-{mes}-{dia}', '%Y-%m-%d'
    ).isoweekday()
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
def leia_int(msg):
    while True:
        try:
            numero: int = int(input(msg))
        except KeyboardInterrupt:
            print(
                '\n\033[1;31mO usuario abartou, preferiu não inserir um valor válido!\033[m'
            )
            break
        except:
            print(
                '\033[1;31mHummm... parece que você não digitou um número inteiro válido!\033[m'
            )
        else:
            return numero


# Perfumaria...
def caixa_dialogo(dialogo):
    print('--' * len(dialogo))
    print(f'| \033[1;30m{dialogo.center(60)}\033[m')
    print('--' * len(dialogo))


def data_correta() -> list():
    # Procura um dia válido!
    while True:
        dia: int = leia_int('Em que DIA você nasceu? ')
        if dia > 31 or dia < 1:
            print(
                f"\033[1;31mDia '{dia}' inexistente, por favor digite um dia válido!\033[m"
            )
        else:
            break

    # Procura um mês válido!
    while True:
        mes: int = leia_int('Em que MÊS você nasceu? ')
        if mes > 12 or mes < 1:
            print(
                f"\033[1;31mMês '{mes}' inexistente, por favor digite um mês válido!\033[m"
            )
        else:
            break

    # Procura um ano válido!
    while True:
        ano_atual: str = int(date.today().strftime('%Y'))
        ano: int = leia_int('Agora digite o ANO em que você nasceu? ')
        if len(str(ano)) == 4 and ano <= ano_atual:
            break
        else:
            print(
                '\033[1;31mFormato inválido! O ano tem que ter 4 digitos e igual ou menor que o ano atual! [Ex: 1900]\033[m'
            )
    return [dia, mes, ano]


# Data Nascimento
dia, mes, ano = data_correta()
dia_atual: int = int(date.today().strftime('%d'))
meses_atual: int = int(date.today().strftime('%m'))
ano_atual: str = int(date.today().strftime('%Y'))    # Busca o ano atual
niver_atual = datetime.strptime(f'{ano_atual}-{mes}-{dia}', '%Y-%m-%d')
data_nasc = datetime.strptime(
    f'{ano}-{mes}-{dia}', '%Y-%m-%d'
)    # Converte "int" para datetime!

# Data Atual
data_atual = (
    datetime.today().date()
)    # Busca a data completa do atual momento!
data_atual_string = datetime.strptime(f'{data_atual}', '%Y-%m-%d')

# Calcula a quantidade de anos bissextos entre duas datas!
num_anos_bissextos: int = 0
for i in range(ano, (ano_atual + 1)):
    bissexto: bool = isleap(i)
    if bissexto:
        num_anos_bissextos += 1

# Realizamos o calculo da quantidade de dias, semanas, meses, ano etc...
q_dias: int = abs(
    (data_atual_string - data_nasc)
).days     # Calcula a quantidade de dias totais, da data de nascimento até a atual, com valor absoluto!
q_anos: int = (
    abs(q_dias - (num_anos_bissextos - 1)) / 365
)      # Acho que eles não consideram o dia em que a pessoa nasceu um ano bissexto(mesmo sendo!)
q_meses: int = int(q_anos * 12)
q_semanas: int = q_dias // 7
q_horas: int = q_dias * 24
q_minutos: int = q_horas * 60
q_segundos: int = q_minutos * 60

lista_meses = list()
contador_meses: int = mes

# Coleta os meses entre o aniversário atual até data de hoje!
if data_atual_string >= niver_atual:
    proximo_niver = datetime.strptime(f'{ano_atual+1}-{mes}-{dia}', '%Y-%m-%d')
    proximo_niver = abs((proximo_niver - data_atual_string).days)
    if meses_atual != mes:
        for iteravel in range(contador_meses, (meses_atual + 1)):
            q_meses_restantes = monthrange(ano_atual, contador_meses)[1]
            lista_meses.append(q_meses_restantes)
            contador_meses += 1
    else:
        q_meses_restantes = monthrange(ano_atual, contador_meses)[1]
        lista_meses.append(q_meses_restantes)
else:
    proximo_niver = abs((niver_atual - data_atual_string).days)
    ano_anterior = ano_atual - 1
    niver_anterior = datetime.strptime(
        f'{ano_anterior}-{mes}-{dia}', '%Y-%m-%d'
    )
    df_niver_restantes: int = abs((data_atual_string - niver_anterior).days)
    while True:
        q_meses_restantes = monthrange(ano_anterior, contador_meses)[1]
        lista_meses.append(q_meses_restantes)
        contador_meses += 1
        if contador_meses == (meses_atual + 1) and ano_anterior == ano_atual:
            break
        if contador_meses == 13:
            contador_meses = 1
            ano_anterior += 1

# Verifica e calcula a quantidade de meses e dias entre duas datas!
q_dias_restantes = q_meses_restantes = 0
if len(lista_meses) > 1:
    ultimo_mes = monthrange(ano_atual, meses_atual)[1]
    lista_meses[0] = abs(lista_meses[0] - dia)
    lista_meses[-1] = abs((lista_meses[-1] - dia_atual) - lista_meses[-1])
    for iteravel_meses in lista_meses:
        if iteravel_meses >= 28 and lista_meses[-1] != ultimo_mes:
            q_meses_restantes += 1
        else:
            q_dias_restantes += iteravel_meses
            if q_dias_restantes >= 30:
                q_meses_restantes += 1
                q_dias_restantes = q_dias_restantes % 30
else:
    if dia_atual == lista_meses[0]:
        q_dias_restantes = lista_meses[0]
        q_meses_restantes = 0
    else:
        q_dias_restantes = abs(dia_atual - dia)
        q_meses_restantes = 0

# Mostra uma mensagem com a quantidade de dias que faltam para o 'niver' ou caso seja o aniversario!
def aniverario():
    if dia == dia_atual and mes == meses_atual:
        return '\nParabéns hoje é seu aniversário!\U0001f973'
    else:
        return f'\nFaltam {proximo_niver} dia(s) para o seu aniversário!'


print('')
caixa_dialogo(f'Alguns dados sobre a data {dia}/{mes}/{ano}!')
print(
    f'\nSua idade: {int(q_anos)} anos | {q_meses_restantes} meses | {q_dias_restantes} dias'
)
print(aniverario())
print(
    f"""\nMAIS DETALHES:\n\nAnos: {int(q_anos)}\nMeses: {q_meses}
Semanas: {q_semanas}\nDias: {q_dias}\nHoras: {q_horas}\nMinutos: {q_minutos}
Segundos: {q_segundos} \nDia da semana: {dia_semana(dia, mes, ano)}"""
)
