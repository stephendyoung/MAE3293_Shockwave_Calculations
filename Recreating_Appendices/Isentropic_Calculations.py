class RecreatingAppendices:
    def __init__(self, mymach):
        self.mach = None
        self.p_0_over_p = None
        self.rho_0_over_rho = None
        self.T_0_over_T = None
        self.A_over_A_start = None

    def isentropic(self, mymach):
        self.T_0_over_T = 1 + (1.4 - 1) / 2 * mymach ** 2
        self.p_0_over_p = self.T_0_over_T ** (1.4 / 0.4)
        self.rho_0_over_rho = self.T_0_over_T ** (1 / (1.4 - 1))
        self.A_over_A_start = 1 / mymach * ((1 + (1.4 - 1) / 2 * mymach ** 2) / ((1.4 + 1) / 2)) ** (
                    (mymach + 1) / (2 * (mymach - 1)))
