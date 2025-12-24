expenditure_data = [
    {'date': '12.03.2025', 'category': 'milk', 'amount': 130},
    {'date': '02.03.2025', 'category': 'fruits', 'amount': 340},
    {'date': '12.09.2025', 'category': 'bread', 'amount': 50},
    {'date': '10.10.2025', 'category': 'meat', 'amount': 400},
    {'date': '12.03.2025', 'category': 'milk', 'amount': 230},
    {'date': '02.03.2025', 'category': 'fruits', 'amount': 140},
    {'date': '12.09.2025', 'category': 'bread', 'amount': 100},
    {'date': '10.10.2025', 'category': 'meat', 'amount': 800},
    {'date': '12.03.2025', 'category': 'milk', 'amount': 490},
    {'date': '02.03.2025', 'category': 'fruits', 'amount': 300},
    {'date': '12.09.2025', 'category': 'bread', 'amount': 150},
    {'date': '10.10.2025', 'category': 'meat', 'amount': 1000},
]

total_amount_by_dates = {}
maximum_amount = 0
maximum_date = ''
number_dates = 0
sum_all_expenses = 0

for expense in expenditure_data:
    if expense['date'] not in total_amount_by_dates:
        total_amount_by_dates[expense['date']] = expense['amount']
    else:
        total_amount_by_dates[expense['date']] += expense['amount']

for date in total_amount_by_dates:
    current_amount = total_amount_by_dates[date]
    if current_amount > maximum_amount:
        maximum_amount = current_amount
        maximum_date = date

    number_dates += 1
    sum_all_expenses += current_amount

print(total_amount_by_dates)
print(f'{maximum_date}: {maximum_amount}')
print(sum_all_expenses / number_dates)
