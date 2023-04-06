import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 5127116142 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    n = len(x)
    sd1 = np.std(x)
    t = st.t.ppf(p,n-1)
    return sd1 * math.sqrt(2*n) / (math.sqrt(2*n-3) + t), sd1 * math.sqrt(2*n) / (math.sqrt(2*n-3) - t)
    
