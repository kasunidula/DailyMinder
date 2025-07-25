import pyttsx3
import datetime
import pickle
import os
import random

# ✅ Proper speak() function with fresh engine every time
def speak(text):
    """Speaks the given text using pyttsx3 with fresh engine every time."""
    try:
        engine = pyttsx3.init()
        engine.setProperty('rate', 165)
        engine.setProperty('volume', 1.0)
        engine.say(text)
        engine.runAndWait()
        engine.stop()
    except Exception as e:
        print(f"(Voice error) {e}")

# Load tasks if the file exists
if os.path.exists("tasks.pkl"):
    with open("tasks.pkl", "rb") as f:
        tasks = pickle.load(f)
else:
    tasks = []

def add_task(task):
    tasks.append({"task": task, "date": datetime.date.today().strftime("%Y-%m-%d")})
    with open("tasks.pkl", "wb") as f:
        pickle.dump(tasks, f)
    print("Task added:", task)
    speak(f"Task added: {task}")

def show_tasks():
    today = datetime.date.today().strftime("%Y-%m-%d")
    today_tasks = [task["task"] for task in tasks if task["date"] == today]

    if today_tasks:
        print("\nToday's tasks:")
        speak(f"You have {len(today_tasks)} tasks for today.")
        for i, task in enumerate(today_tasks, 1):
            print(f"{i}. {task}")
    else:
        print("\nNo tasks for today.")
        speak("No tasks for today.")

def show_all_tasks():
    if tasks:
        print("\nAll Tasks:")
        speak("Here are all your tasks.")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task['task']} (Added on: {task['date']})")
    else:
        print("\nNo tasks found.")
        speak("No tasks found.")

def delete_task():
    if not tasks:
        print("\nNo tasks to delete.")
        speak("No tasks to delete.")
        return

    show_all_tasks()
    try:
        task_num = int(input("Enter the task number to delete: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            with open("tasks.pkl", "wb") as f:
                pickle.dump(tasks, f)
            print(f"Task deleted: {removed_task['task']}")
            speak(f"Task deleted: {removed_task['task']}")
        else:
            print("Invalid task number.")
            speak("Invalid task number. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        speak("Invalid input. Please enter a valid number.")

def clear_tasks():
    global tasks
    tasks = []
    with open("tasks.pkl", "wb") as f:
        pickle.dump(tasks, f)
    print("\nAll tasks have been cleared.")
    speak("All tasks have been cleared.")

def inspire_me():
    quotes = [
        "Believe in yourself. Every day is a new opportunity.",
        "You are stronger than you think.",
        "Success is not final, failure is not fatal: It is the courage to continue that counts.",
        "Keep pushing forward. You’ve got this!"
    ]
    quote = random.choice(quotes)
    print("\nMotivation:", quote)
    speak("Here is your motivational quote.")
    speak(quote)

def main():
    speak("Hello! I am your daily task assistant.")
    while True:
        print("\n===== Daily Task Assistant =====")
        print("1. Add a Task")
        print("2. Show Today's Tasks")
        print("3. Show All Tasks")
        print("4. Delete a Task")
        print("5. Clear All Tasks")
        print("6. Inspire Me")
        print("7. Exit")
        print("================================")

        try:
            choice = int(input("Enter your choice (1-7): "))

            if choice == 1:
                task = input("What task would you like to add? ")
                add_task(task)

            elif choice == 2:
                show_tasks()

            elif choice == 3:
                show_all_tasks()

            elif choice == 4:
                delete_task()

            elif choice == 5:
                clear_tasks()

            elif choice == 6:
                inspire_me()

            elif choice == 7:
                speak("Goodbye! Have a productive day.")
                print("Goodbye!")
                break

            else:
                print("Invalid choice, please try again.")
                speak("Invalid choice, please try again.")

        except ValueError:
            print("Invalid input. Please enter a number between 1 and 7.")
            speak("Invalid input. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()
