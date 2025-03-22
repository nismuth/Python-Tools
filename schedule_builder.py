
import os

print("/////////////////////////////////////////")
print("//// Welcome to the Schedule Builder ////")
print("/////////////////////////////////////////")
print("\nInput your tasks for each day (MON-SUN)")

filename = "myschedule"

if os.path.exists(filename):  # Check if the file exists before opening in write mode
    f = open(filename, "w")  # Open in write mode (overwrites existing file)
    print(f"Overwriting existing file: {filename}")
else:
    f = open(filename, "x")

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

schedule = {}  # Dictionary to store tasks for each day

for day in days:
    tasks = input(f"\nWhat tasks do you plan on completing for {day}? (Separate with commas)\n").lower().split(",")

    tasks = [task.strip() for task in tasks]  # Strip spaces from each task

    schedule[day] = tasks  # Store tasks in a dictionary

f.write("\nYour Weekly Schedule:\n")  # Write the final schedule to the file
for day, tasks in schedule.items():
    f.write(f"\n{day}: ")
    f.write("\n".join(tasks) + "\n" if tasks else "No tasks planned.")

f.close()  # Close the file properly
