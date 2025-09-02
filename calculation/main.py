from calculation import *

load_1 = Calculation(400,10,0.8,0.9)

kw_1 = load_1.real_power_kw()
kvar_1 = load_1.reactive_power_kvar()

load_2 = Calculation(400,20,0.8,0.9)
kw_2 = load_2.real_power_kw()
kvar_2 = load_2.reactive_power_kvar()

print(kw_1)
print(kvar_1)
print(kw_2)
print(kvar_2)