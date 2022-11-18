from Isentropic_Calculations import Appendices
# from MAE3293_Shockwave_Calculations.Recreating_Appendices.Isentropic_Calculations import RecreatingAppendices

mach_number = Appendices(mymach=float(input("What is your Mach Number ")))
mach_number.isentropic()  # this calls the isentropic function then the line below calls for each part of the method
print(f'T0/T = {mach_number.T_0_over_T} P0/P = {mach_number.p_0_over_p} Rho0/Rho = {mach_number.rho_0_over_rho}')


""" 
add normal shock wave, prandtl meyer, and plot table for all three (add possible iteration for previous values. 
"""