import sys
print("Здравствуйте! Это Консольная программа расчета ЗП сотрудника!")
time = sys.argv[1]
money_for_time = sys.argv[2]
prize = sys.argv[3]
cash = int(time) * int(money_for_time)+int(prize)
print('Количество часов работника: ', time)
print('Ставка работника за час: ', money_for_time)
print('Премия работника: ', prize)
print('ЗП сотрудника: ', cash)
