# 3) Рост дочерей 175, 167, 154, 174, 178, 148, 160, 167, 169, 170
# Рост матерей  178, 165, 165, 173, 168, 155, 160, 164, 178, 175
# Используя эти данные построить 95% доверительный интервал для разности 
# среднего роста родителей и детей.

import numpy as np
import scipy.stats as stats

D = np.array([175, 167, 154, 174, 178, 148, 160, 167, 169, 170])
mean_D = D.mean()
M = np.array([178, 165, 165, 173, 168, 155, 160, 164, 178, 175])
mean_M = M.mean()

delta = mean_M - mean_D

D1 = np.var(M, ddof=1)
D2 = np.var(D, ddof=1)
D = (D1+D2)/2
SE = np.sqrt(D/10 + D/10)
t = stats.t.ppf(0.975, 18)

L = delta - t*SE
U = delta + t*SE

print (L, U)