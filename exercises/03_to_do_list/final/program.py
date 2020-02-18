from pathlib import Path
from os import system
import time


def main():
    todo_loc = get_full_pathname("todo")
    todo_list = load_or_create_todo(todo_loc)

    while True:
        system("cls")
        print("-----------To Do list------------")
        print("Current List:")
        print_todo(todo_list)
        print()
        print("What would you like to do?")
        action = int(
            input(
                """1: Add item
2: Delete item
3. Save list
4. Delete list
5. Quit
>> """
            )
        )

        if action == 1:
            new_item = input("what to do should we add to the list? ")
            add_item(todo_list, new_item)

        elif action == 2:
            idx = int(input("which index do you want to delete? "))
            delete_item(todo_list, idx)

        elif action == 3:
            save_todo(todo_list, todo_loc)

        elif action == 4:
            delete_list(todo_loc)
            todo_list = []

        elif action == 5:
            quit()

        else:
            print(f"Error! {action} was not a valid choice, must choose 1 thru 5!")


def load_or_create_todo(loc):
    if not loc.exists():
        loc.touch()
        return []
    return loc.read_text().split("\n")


def get_full_pathname(name="todo"):
    filename = Path(__file__).resolve().parent.joinpath(f"{name}.txt")
    return filename


def add_item(todo_list, item):
    todo_list.append(item)
    print(f"added item {item}")
    time.sleep(1)


def delete_list(loc):
    loc.unlink()
    print(f"Deleted file at {loc}")
    time.sleep(1)


def delete_item(todo_list, idx):
    try:
        removed = todo_list.pop(idx - 1)
        print(f"Deleted todo item {idx}")
    except:
        print(f"Error! Could not find list item number {idx}!")
    time.sleep(1)


def save_todo(todo_list, loc):
    loc.write_text("\n".join(todo_list))
    print(f"Saved to {loc}")
    time.sleep(1)


def print_todo(todo_list):
    for idx, item in enumerate(todo_list):
        print(f"{idx + 1}: {item}")


if __name__ == "__main__":
    main()
