# в рублях
money_capital = 150000
salary = 50000
spend = 75000
# в %
increase = 5
months = 0

budget = money_capital + salary
while budget >= spend:
    months += 1
    budget -= spend
    budget += salary
    spend += spend * increase / 100

print('Месяцев без долгов:', months)