# Использование %:
team1_num = 5
team2_num = 6

print("В комоде Мастера кода участников: %d !" % team1_num)
print("Итого сегодня в командах участников: %s и %s !" % (team1_num, team2_num))


# Использование .format():
score_2 = 42
team1_time = 18015.2

print("Команда Волшебники данных решила задач: {score} !".format(score=score_2))
print("Волшебники данных решили задачи за {} c !".format(team1_time))


# Использование f-строк:
score_1 = 40
challenge_result = "Мастера кода"
tasks_total = 82
time_avg = 350.4

print(f"Команды решили {score_1} и {score_2} задач.")
print(f"Результат битвы: победа команды {challenge_result}!")
print(
    f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!"
)
