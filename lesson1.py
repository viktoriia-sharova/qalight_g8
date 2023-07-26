#1.
my_list = [6, 7, 8, 9]
total_sum = sum(my_list)

print(my_list)
print(total_sum)

#2
my_list_2 = [6, 7, 8, 9, 7, 8, 7, 8]
unique_sum = sum(set(my_list_2))

print(my_list_2)
print(unique_sum)

#3
employee = {
    "name": "Vika",
    "position": "qa",
    "salary": 2000
}
employee["salary"] *= 1.5

print(employee)