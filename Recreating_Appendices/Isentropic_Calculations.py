import math
class Appendices:
    def __init__(self, mymach): # for solving, need to pass values from user to method

        self.mach = mymach
        self.p_0_over_p = None
        self.rho_0_over_rho = None
        self.T_0_over_T = None
        self.A_over_A_start = None
        # start of normal shock wave values for solving users problems :)
        self.p_2_static_over_p_1_static = None
        self.rho_2_static_over_rho_1_static = None
        self.T_2_over_T_1 = None
        self.ptotal_2_over_ptotal_1 = None
        self.mach_downstream = None
        #self.USP = upstream_static_pressure

    def isentropic(self): # don't have to pass mymach argument again to isentropic because the entire class already knows it
        mymach = self.mach
        self.T_0_over_T = 1 + (((1.4 - 1) / 2) * (mymach ** 2))
        self.p_0_over_p = self.T_0_over_T ** (1.4 / 0.4)
        self.rho_0_over_rho = self.T_0_over_T ** (1 / (1.4 - 1))
        #self.A_over_A_start = 1 / mymach * ((1 + (1.4 - 1) / 2 * mymach ** 2) / ((1.4 + 1) / 2)) ** (
                    #(mymach + 1) / (2 * (mymach - 1))) figure out later
    def normal_shcokwave(self):
        #upstream_static_pressure = self.USP
        mymach = self.mach
        self.p_2_static_over_p_1_static = 1 + (((2 * 1.4) / (1.4 + 1)) * ((mymach ** 2) - 1))
        self.rho_2_static_over_rho_1_static = ((1.4 + 1 ) * mymach ** 2) / (2 + ((1.4 - 1 ) * mymach ** 2))
        self.T_2_over_T_1 = (self.p_2_static_over_p_1_static * (self.rho_2_static_over_rho_1_static ** -1))
        self.mach_downstream = math.sqrt((1 + ((1.4 -1)/2) * mymach ** 2) / ((1.4 * mymach ** 2)- ((1.4 - 1)/2)))
        self.ptotal_2_over_ptotal_1 = (((1.4 + 1) * (mymach ** 2)) / (((1.4 - 1) * (mymach ** 2)) + 2)) ** (1.4 / (1.4 - 1)) * ((1.4 + 1) / ((2 * 1.4 * (mymach ** 2)) - (1.4 - 1)))
#(((1.4 + 1) * (mymach ** 2)) / (((1.4 - 1) * (mymach ** 2)) + 2)) ** (1.4 / (1.4 - 1))
        # pressure total relationship and raleigh pitot tube formula left

