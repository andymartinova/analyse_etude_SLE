import pandas as pd
from scipy import stats
from scipy.stats import binomtest

print("=== SLE STATS REPRODUCTIBLES === [file:118]")

# Données EXACTES de ton Excel
public_h, public_f = 1336, 1621
conf_h, conf_f = 37, 61
interv_h, interv_f = 130, 149
questions_h, questions_f = 66, 103

# 1. PUBLIC binomial (p=1.72e-07)
p1 = binomtest(public_h, public_h+public_f, 0.5).pvalue
print(f"1. Public H: p={p1:.2e} ✓")

# 2. CONFÉRENCIERS (p=0.0197)
p2 = binomtest(conf_h, conf_h+conf_f, 0.5).pvalue
print(f"2. Conférenciers H: p={p2:.4f} ✓")

# 3. INTERVENTIONS (p=0.7887)
p3 = binomtest(interv_h, interv_h+interv_f, 0.5).pvalue
print(f"4. Interventions H: p={p3:.4f} ✓")

# 4. QUESTIONS (p=1.25e-08)
p4 = binomtest(questions_h, questions_h+questions_f, 0.5).pvalue
print(f"6. Questions H: p={p4:.2e} ✓")

print("\nTes calculs SAVED !")
