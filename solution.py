import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 5127116142 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    n = len(x)
    t = st.t.ppf(p, 1)
    a1 = np.sqrt(2 * n) / (np.sqrt(2 * n - 3) + t) * 6
    a1 = np.sqrt(a1) if a1 > 0 else 0
    a2 = np.sqrt(2 * n) / (np.sqrt(2 * n - 3) - t) * 6
    a2 = np.sqrt(a2) if a2 > 0 else np.sqrt(6)
    return a1, a2

    
