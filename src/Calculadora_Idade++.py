from datetime import date, datetime


# Mostra o dia da semana da data atual ou de uma data especifica! primeiro dia da semana é domingo!
def dia_semana(dia = datetime.today().strftime("%d"), mes = datetime.today().strftime("%m"), ano = datetime.today().strftime("%Y")):
    dia_da_semana: int = datetime.strptime(f"{ano}-{mes}-{dia}", "%Y-%m-%d").isoweekday()
    semana: dict = {                    
    1: "Segunda-Feira",           
    2: "Terça-Feira",
    3: "Quarta-Feira",
    4: "Quinta-Feira",
    5: "Sexta-Feira",
    6: "Sábado",
    7: "Domigo",                  
    } 
    return semana[dia_da_semana]


# Função que ler apenas números inteiros! 
def leiaint(msg):
    while True:
        try:
            numero: int = int(input(msg))
        except KeyboardInterrupt:
            print('\n\033[1;31mO usuario abartou, preferiu não inserir um valor válido!\033[m')
            break
        except:
            print('\033[1;31mHummm... parece que você não digitou um número inteiro válido!\033[m')
        else:
            return numero


# Perfumaria...
def caixadialogo(dialogo):
    print('--' * len(dialogo))
    print(f'| \033[1;30m{dialogo.center(60)}\033[m')
    print('--' * len(dialogo))


def data_correta() -> list():
    # Procura um dia válido!
    while True:
        dia: int = leiaint("Em que DIA você nasceu? ")
        if dia > 31 or dia < 1:
            print(f"\033[1;31mDia '{dia}' inexistente, por favor digite um dia válido!\033[m")
        else:
            break    
    
    # Procura um mês válido!
    while True:
        mes: int = leiaint("Em que MÊS você nasceu? ")
        if mes > 12 or mes < 1:
            print(f"\033[1;31mMês '{mes}' inexistente, por favor digite um mês válido!\033[m")
        else:
            break
    
    # Procura um ano válido!
    while True:
        ano: int = leiaint("Agora digite o ANO em que você nasceu? ")
        if len(str(ano)) == 4:
            break
        else:
            print("\033[1;31mFormato inválido! O ano tem que ter 4 digitos! [Ex: 1900]\033[m")
    return [dia, mes, ano]

# Data Nascimento
dia, mes, ano = data_correta()
ano_atual: str = date.today().strftime("%Y")    # Busca o ano atual
data_nasc = datetime.strptime(f"{ano}-{mes}-{dia}", "%Y-%m-%d")    # Converte "int" para datetime!
proximo_niver = datetime.strptime(f"{ano_atual}-{mes}-{dia}", "%Y-%m-%d")

# Data Atual
data_atual = datetime.today().date()    # Busca a data completa do atual momento!
data_atual_string = datetime.strptime(f"{data_atual}", "%Y-%m-%d")

# Realizamos o calculo da quantidade de dias, semanas, meses, ano etc...
q_meses_restantes: int = abs((proximo_niver - data_atual_string) // 30).days    # Calcula a quantidade de dias, entre a data de "niver" no ano vigente até data atual!
q_dias: int = abs((data_nasc - data_atual_string)).days     # Calcula a quantidade de dias totais, da data de nascimento até a atual, com valor absoluto!
q_anos: int = q_dias // 365
q_meses: int = (q_anos * 12) + q_meses_restantes
q_semanas: int = q_dias // 7
q_horas: int = q_dias * 24
q_minutos: int = q_horas * 60
q_segundos: int = q_minutos * 60

print("")
caixadialogo(f"Alguns dados sobre a data {dia}/{mes}/{ano}!")
print(f"""\nAnos: {q_anos}\nMeses: {q_meses}
Semanas: {q_semanas}\nDias: {q_dias}\nHoras: {q_horas}\nMinutos: {q_minutos}
Segundos: {q_segundos} \nDia da semana: {dia_semana(dia, mes, ano)}""")