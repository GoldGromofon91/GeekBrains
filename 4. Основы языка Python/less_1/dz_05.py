print('Здравствуйте! Это Программа расчета рентабельности фирмы')
usr_revenue = int(input('Введите доходы фирмы (в $) за последний квартал: '))
usr_costs = int(input('Введите издержки фирмы (в $) за последний квартал: '))
if usr_revenue > usr_costs:
    divergence = usr_revenue - usr_costs
    rent_firm = round((divergence/usr_revenue) * 100)
    print(f'Прибыль вашей фирмы за квартал составила {divergence} $, рентабельность {rent_firm} %')
    staff = int(input('Введите количество сотрудников в штате: '))
    rent_staff = round(divergence/staff,2)
    print(f'Прибыль фирмы на 1 -го сотрудника составляет {rent_staff} $')
else:
    redivergence = usr_costs - usr_revenue
    print(f'Убыток вашей фирмы за квартал составил {redivergence} $')