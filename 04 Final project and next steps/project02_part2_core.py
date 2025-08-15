# project02_part2_core.py
from datetime import date

def next_id(tasks: list[dict]) -> int:
    return (max((t["id"] for t in tasks), default=0) + 1)

def add_task(tasks: list[dict], title: str, due: str | None = None, tags: list[str] | None = None) -> list[dict]:
    title = title.strip()
    if not title:
        raise ValueError("title required")
    tags = tags or []
    new = {
        "id": next_id(tasks),
        "title": title,
        "done": False,
        "due": due,
        "tags": tags,
    }
    return tasks + [new]

def mark_done(tasks: list[dict], task_id: int) -> list[dict]:
    found = False
    out = []
    for t in tasks:
        if t["id"] == task_id:
            t = {**t, "done": True}
            found = True
        out.append(t)
    if not found:
        raise KeyError(f"no task with id {task_id}")
    return out

def delete_task(tasks: list[dict], task_id: int) -> list[dict]:
    new = [t for t in tasks if t["id"] != task_id]
    if len(new) == len(tasks):
        raise KeyError(f"no task with id {task_id}")
    return new

def list_open(tasks: list[dict]) -> list[dict]:
    return [t for t in tasks if not t["done"]]
