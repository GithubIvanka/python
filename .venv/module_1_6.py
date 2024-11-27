home_work_count = 12
hours_spent = 1.5
course_name = "Python"
time_for_one_task = hours_spent / home_work_count

print("Курс: ", course_name, ", Всего задач: ", home_work_count, ", затрачено часов: ", hours_spent, ", среднее время выполнения ", time_for_one_task, sep='')


print(end= "---------------------------------\n\n")

################# Работа со словарями:

my_dict = {"Anton": 2000, "Alex": 2001, "Sasha": 2003}

print(my_dict)
print(my_dict["Anton"])
print(my_dict.get("Nina"))

my_dict["Eva"] = 2000
my_dict.update({"Adam": 2000, "Vova": 2010})
print(my_dict)

print(end= "---------------------------------\n\n")
################# Работа с множествами:

my_set = {0, 0, 1, 2, 2, "one", "one", "zero", "zero", "five"}

print(my_set)

my_set.add("nine")
my_set.add(9)
my_set.remove(2)
print(my_set)