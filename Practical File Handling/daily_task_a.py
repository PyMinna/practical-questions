daily_task = ["===Daily Tasks===\n",
           "1.Student Grade Calculation\n",
           "2.Atm Simulator\n"]


file = open("todo.txt", "w")
file.writelines(daily_task)
file.close()

file = open("todo.txt", "a")
file.write("3.Number Guessing Game")
file.close()