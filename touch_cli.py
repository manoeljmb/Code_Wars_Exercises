import json, os, sys
from datetime import datetime

TASKS_FILE = "tasts.json"

def load_tasks():
    # Se o arquivo NÃO existir, retorna lista vazia
    if not os.path.exists(TASKS_FILE):
        return[]
    # Se existir, abre e carrega o JSON
    with open(TASKS_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def save_tasks(tasks):
    with open(TASKS_FILE, "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=2, ensure_ascii=False)


def add_task(description):
    tasks = load_tasks()

    # Define um novo ID (último ID + 1)
    new_id = 1
    if tasks:
        new_id = tasks[-1]["id"] + 1

    now = datetime.now().isoformat()

    task = {
        "id": new_id,
        "description": description,
        "status": "todo",
        "createdAt": now,
        "updatedAt": now,
    }

    tasks.append(task)
    save_tasks(tasks)
    print(f"Tarefa adicionada com sucesso (ID: {new_id})")

def list_tasks(filter_status=None):
    tasks = load_tasks()

    if not tasks:
        print("Nenhuma tarefa encontrada.")
        return
    for task in tasks:
        if filter_status and task["status"] != filter_status:
            continue
        print(f"[{task['id']}] {task['description']} - {task['status']}")


def update_task(task_id, new_description):
    tasks = load_tasks()

    for task in tasks:
        if task["id"] == task_id:
            task["description"] = new_description
            task["updatedAt"] = datetime.now().isoformat()
            save_tasks(tasks)
            print("Tarefa atualizada com sucesso")
            return

    print("Tarefa não encontrada.")

def mark_task(task_id, status):
    tasks = load_tasks()

    for task in tasks:
        if task["id"] == task_id:
            task["status"] = status
            task["updatedAt"] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Tarefa marcada como {status}.")
            return
    print("tarefa não encontrada.")

def delete_task(task_id):
    tasks = load_tasks()
    new_tasks = [task for task in tasks if task["id"] != task_id]

    if len(new_tasks) == len(tasks):
        print("Tarefa não encontrada.")
        return

    print("Tarefa excluída com sucesso")
    save_tasks(new_tasks)


def main():
    if len(sys.argv) < 2:
        print("Uso inválido.")
        return

    command = sys.argv[1]

    if command == "add":
        add_task(sys.argv[2])

    elif command == "list":
        if len(sys.argv) == 3:
            list_tasks(sys.argv[2])
        else:
            list_tasks()
    elif command == "update":
        update_task(sys.argv[2], sys.argv[3])

    elif command == "delete":
        delete_task(int(sys.argv[2]))

    elif command == "mark-in-progress":
        mark_task(int(sys.argv[2]), "in-progress")

    elif command == "mark-done":
        mark_task(int(sys.argv[2]), "done")

    else:
        print("Comando desconhecido.")



if __name__ == "__main__":
    main()


