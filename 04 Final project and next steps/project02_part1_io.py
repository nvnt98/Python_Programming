# project02_part1_io.py
from pathlib import Path
import json, os

APP_DIR = Path(os.path.expanduser("~")) / ".todo"
APP_DIR.mkdir(exist_ok=True)
DB = APP_DIR / "todo.json"

def load_tasks() -> list[dict]:
    if not DB.exists():
        return []
    text = DB.read_text(encoding="utf-8")
    return json.loads(text) if text.strip() else []

def save_tasks(tasks: list[dict]) -> None:
    tmp = DB.with_suffix(".tmp")
    tmp.write_text(json.dumps(tasks, ensure_ascii=False, indent=2), encoding="utf-8")
    tmp.replace(DB)
