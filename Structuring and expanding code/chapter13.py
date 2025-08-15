# chapter13.py
from pathlib import Path
import json

DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)
STORE = DATA_DIR / "notes.json"

def read_notes() -> list[dict]:
    if not STORE.exists():
        return []
    text = STORE.read_text(encoding="utf-8")
    return json.loads(text) if text.strip() else []

def write_notes(notes: list[dict]) -> None:
    tmp = STORE.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(notes, ensure_ascii=False, indent=2), encoding="utf-8")
    tmp.replace(STORE)  # atomic-ish write

# Context manager for line-by-line
def copy_text(src: Path, dst: Path):
    with src.open("r", encoding="utf-8") as fin, dst.open("w", encoding="utf-8") as fout:
        for line in fin:
            fout.write(line)
