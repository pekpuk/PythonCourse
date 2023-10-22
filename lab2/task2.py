# в рублях
money_capital = 0
salary = 50000
spend = 75000
# в %
increase = 3
goal_months = 10

for _ in range(goal_months):
    money_capital += spend - salary
    spend += spend * increase / 100

print('Подушка безопасности на', goal_months, 'месяцев', round(money_capital, 2), 'рублей')

