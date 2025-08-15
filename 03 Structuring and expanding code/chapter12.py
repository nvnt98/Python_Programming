# chapter12.py
class TodoError(Exception): ...
class TaskNotFound(TodoError): ...
class InvalidTask(TodoError): ...

def parse_int(s: str) -> int:
    try:
        return int(s.strip())
    except ValueError as e:
        raise InvalidTask(f"not an integer: {s!r}") from e

def get_item(xs, idx):
    try:
        return xs[idx]
    except IndexError as e:
        raise TaskNotFound(f"index out of range: {idx}") from e

# try/except/else/finally
def read_file(path):
    f = None
    try:
        f = open(path, "r", encoding="utf-8")
        data = f.read()
    except FileNotFoundError:
        return ""
    else:
        return data
    finally:
        if f:
            f.close()
