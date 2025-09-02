import math as m


class Calculation:

    def __init__(self,voltage,current,powerfactor,efficiency):
        self.volt = voltage
        self.amp = current
        self.pf = powerfactor
        self.eff = efficiency

    def real_power_kw (self):
        powerkw = m.sqrt(3) * self.volt * self.amp * self.pf * self.eff
        return powerkw

    def reactive_power_kvar (self):
        sinpf = m.sin (m.acos(self.pf))
        powerkvar = m.sqrt(3) * self.volt * self.amp * sinpf * self.eff
        return powerkvar


