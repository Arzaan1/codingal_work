total_homework = 4
completed_count = 0
task_num = 1

print("You have 4 homework tasks today!")

while task_num <= total_homework:

    if task_num == 1:
        task = "Math worksheet"
    elif task_num == 2:
        task = "Science reading"
    elif task_num == 3:
        task = "English writing"
    else:
        task = "Coding practice"

    answer = input("Finished " + task + "? (yes/no): ")

    if answer == "yes":
        completed_count += 1
        task_num += 1
        print("Great job!")
    else:
        print("Finish it and try again!")

    print("Homework remaining:", total_homework - completed_count)

print("ALL HOMEWORK COMPLETE!")
print("Homework completed:", completed_count)
print("Homework remaining:", total_homework - completed_count)