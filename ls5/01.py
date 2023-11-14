from collections import namedtuple


def incomecalc():
    v = 'Company'
    count_company = int(input('Введите количесво компний: '))
    companies = namedtuple(v, 'name q1 q2 q3 q4')
    income_aver = {}
    for i in range(count_company):
        company = companies(
            name=input(f'Введите название компании номер {i + 1}: '),
            q1=int(input('Введите прибыль за первый квартал: ')),
            q2=int(input('Введите прибыль за второй квартал: ')),
            q3=int(input('Введите прибыль за третий квартал: ')),
            q4=int(input('Введите прибыль за четвёртый квартал: '))
        )
        income_aver[company.name] = (company.q1 + company.q2 + company.q3 + company.q4) / 4

    total_ever = 0

    for value in income_aver.values():
        total_ever += value
    total_ever = total_ever / count_company

    for key, value in income_aver.items():
        if value > total_ever:
            print(f'У комании {key} прибыль выше средней')
        elif value < total_ever:
            print(f'У комании {key} прибыль ниже средней')
        else:
            print(f'У комании {key} прибыль ровна средней')


incomecalc()
