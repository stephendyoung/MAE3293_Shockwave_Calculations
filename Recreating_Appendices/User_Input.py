from Isentropic_Calculations import RecreatingAppendices
# from MAE3293_Shockwave_Calculations.Recreating_Appendices.Isentropic_Calculations import RecreatingAppendices

mach_number = RecreatingAppendices(mymach=float(input("What is your Mach Number ")))
mach_number.isentropic(mach_number)
print(f'T0/T =: {mach_number.T_0_over_T}')
