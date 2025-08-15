# project02_part3_cli.py
import argparse, sys, json
from project02_part1_io import load_tasks, save_tasks
from project02_part2_core import add_task, mark_done, delete_task, list_open

def cmd_add(args):
    tasks = load_tasks()
    tasks = add_task(tasks, args.title, args.due, args.tags)
    save_tasks(tasks)
    print(f"Added: {args.title}")

def cmd_list(args):
    tasks = load_tasks()
    data = tasks if args.all else list_open(tasks)
    for t in data:
        status = "✓" if t["done"] else " "
        print(f"[{status}] {t['id']:3}  {t['title']}")
        if t.get("due"):
            print(f"     due: {t['due']}")
        if t.get("tags"):
            print(f"     tags: {', '.join(t['tags'])}")

def cmd_done(args):
    tasks = load_tasks()
    try:
        tasks = mark_done(tasks, args.id)
    except KeyError as e:
        print(e, file=sys.stderr); return 1
    save_tasks(tasks); print(f"Done: {args.id}")

def cmd_delete(args):
    tasks = load_tasks()
    try:
        tasks = delete_task(tasks, args.id)
    except KeyError as e:
        print(e, file=sys.stderr); return 1
    save_tasks(tasks); print(f"Deleted: {args.id}")

def build_parser():
    p = argparse.ArgumentParser(prog="todo", description="Simple To-Do CLI")
    sub = p.add_subparsers(dest="cmd", required=True)

    a = sub.add_parser("add", help="Add a new task")
    a.add_argument("title")
    a.add_argument("--due")
    a.add_argument("--tags", nargs="*", default=[])
    a.set_defaults(func=cmd_add)

    l = sub.add_parser("list", help="List tasks")
    l.add_argument("--all", action="store_true")
    l.set_defaults(func=cmd_list)

    d = sub.add_parser("done", help="Mark task done")
    d.add_argument("id", type=int)
    d.set_defaults(func=cmd_done)

    r = sub.add_parser("delete", help="Delete task")
    r.add_argument("id", type=int)
    r.set_defaults(func=cmd_delete)
    return p

def main(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)
    rc = args.func(args)
    sys.exit(rc or 0)

if __name__ == "__main__":
    main()
