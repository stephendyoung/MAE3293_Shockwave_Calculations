import math


class Appendices:
    def __init__(self, mymach, upstream_static_pressure):  # for solving, need to pass values from user to method
        self.mach = mymach
        self.p_0_over_p = None
        self.rho_0_over_rho = None
        self.T_0_over_T = None
        self.A_over_A_start = None

        # start of normal shock wave appendix

        self.p_2_static_over_p_1_static = None
        self.rho_2_static_over_rho_1_static = None
        self.T_2_over_T_1 = None
        self.ptotal_2_over_ptotal_1 = None
        self.mach_downstream = None
        self.ptotal_2_over_p_1_static = None

        # start of normal shock waves calculator
        self.given_static_pressure = upstream_static_pressure
        self.downstream_static_pressure = None

        # expansion fan equations
        self.mu = None
        self.nu = None

    def isentropic(self):  # don't have to pass mymach argument again to isentropic because the entire class already
        # knows it

        mymach = self.mach
        self.T_0_over_T = 1 + (((1.4 - 1) / 2) * (mymach ** 2))
        self.p_0_over_p = self.T_0_over_T ** (1.4 / 0.4)
        self.rho_0_over_rho = self.T_0_over_T ** (1 / (1.4 - 1))
        # self.A_over_A_start = 1 / mymach * ((1 + (1.4 - 1) / 2 * mymach ** 2) / ((1.4 + 1) / 2)) ** (
        # (mymach + 1) / (2 * (mymach - 1))) ignore

    def normal_shockwave(self):
        Appendices.isentropic(self)
        mymach = self.mach
        self.p_2_static_over_p_1_static = 1 + (((2 * 1.4) / (1.4 + 1)) * ((mymach ** 2) - 1))
        self.rho_2_static_over_rho_1_static = ((1.4 + 1) * mymach ** 2) / (2 + ((1.4 - 1) * mymach ** 2))
        self.T_2_over_T_1 = (self.p_2_static_over_p_1_static * (self.rho_2_static_over_rho_1_static ** -1))
        self.mach_downstream = math.sqrt((1 + ((1.4 - 1) / 2) * mymach ** 2) / ((1.4 * mymach ** 2) - ((1.4 - 1) / 2)))
        self.ptotal_2_over_ptotal_1 = ((((1.4 + 1) * (mymach ** 2)) / (((1.4 - 1) * (mymach ** 2)) + 2)) ** (
                1.4 / (1.4 - 1))) * ((1.4 + 1) / ((2 * 1.4 * (mymach ** 2)) - (1.4 - 1))) ** (1 / (1.4 - 1))
        self.ptotal_2_over_p_1_static = self.ptotal_2_over_ptotal_1 * self.p_0_over_p

    def expansion_fans(self):
        mymach = self.mach
        self.mu = math.degrees(math.asin(1 / mymach))
        self.nu = math.degrees(math.sqrt((1.4 + 1) / (1.4 - 1)) * math.atan(
            math.sqrt(((1.4 - 1) / (1.4 + 1)) * ((mymach ** 2) - 1))) - math.atan(math.sqrt(mymach ** 2 - 1)))

    def normal_shock_calculations(self):
        upstream_static_pressure = self.given_static_pressure
        self.downstream_static_pressure = upstream_static_pressure * self.p_2_static_over_p_1_static
