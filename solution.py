import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 5127116142 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 1 - p
    n = len(x)
    sd1 = np.std(x)
    return sd1 * math.sqrt(n-1) / math.sqrt(st.chi2.ppf(1-alpha/2,n-1)), sd1 * math.sqrt(n-1) / math.sqrt(st.chi2.ppf(alpha / 2, n-1))
    
