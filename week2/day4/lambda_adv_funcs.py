import pandas as pd
from functools import reduce

# lambda functions: don't have name and we don't need to call them.
# we create them and excute them on place

#sintax:
to_power = lambda n,power: n ** power

# print(to_power(4,2))

#map() = get another function argument
#filter()
#reduce()

# numbers = [1,2,3,4,5,6,7]

# squared_numbers = map(lambda n: n**2, numbers)

# print(list(squared_numbers))

#IN CONTEXT: APPLYING TO A DATA SET

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [24, 30, 22, 35, 28],
    'Salary': [50000, 60000, 55000, 70000, 48000]
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

#filter

age_filter = list(filter(lambda row: row['Age'] > 25, df.to_dict('records')))

print(pd.DataFrame(age_filter))

#map
salary_increment = list(map(lambda row: {**row, 'Salary': row['Salary'] * 1.10}, df.to_dict('records')))

print(pd.DataFrame(salary_increment))

#reduce
total_salary = reduce(lambda acc, row: acc + row['Salary'], df.to_dict('records'), 0)
print(total_salary)
