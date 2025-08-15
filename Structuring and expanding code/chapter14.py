# chapter14.py
# Absolute import from local file in same directory
from utils_math import clamp

def normalized_score(x, lo=0, hi=100):
    return (clamp(x, lo, hi) - lo) / (hi - lo)

if __name__ == "__main__":
    print(normalized_score(120))
