# utils_math.py (local module)
def clamp(x: float, lo: float, hi: float) -> float:
    return max(lo, min(hi, x))
