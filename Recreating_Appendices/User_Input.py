from Isentropic_Calculations import Appendices
# from MAE3293_Shockwave_Calculations.Recreating_Appendices.Isentropic_Calculations import RecreatingAppendices
user_selection = input("What appendix are you looking for? \n A) Isentropic Relationship \n B) Normal Schockwave "
                       "Relationship \n C) Prandtl-Meyer Relationship\n Enter A, B, or C: ")

mach_number = Appendices(mymach=float(input("\nWhat is your Mach Number ")))

""" line above calls the isentropic function then the line below calls for each part of the method. 
error within was dealing with passing the mach number twice but once you assign it, the entire class knows it already. 
Therefore, don't pass it again in class file- comment in there for it. 
"""

if user_selection == "A":
    mach_number.isentropic()
    print(f'T0/T = {mach_number.T_0_over_T:.3f} P0/P = {mach_number.p_0_over_p:3f} Rho0/Rho = {mach_number.rho_0_over_rho:4f}')
elif user_selection == "B":
    mach_number.normal_shcokwave()
    mach_number.isentropic()

    print(f'P_2/P_1 = {mach_number.p_2_static_over_p_1_static:.3f} Rho_2/Rho_1 {mach_number.rho_2_static_over_rho_1_static:.3f}'
          f' T_2/T_1 = {mach_number.T_2_over_T_1:.3f} Ptotal_2/Ptotal_1 {mach_number.ptotal_2_over_ptotal_1:.3f}'
          f' Ptotal_2/P_1 = {mach_number.ptotal_2_over_p_1_static:.3f} Downstream Mach Number'
          f' {mach_number.mach_downstream:.4f}')




elif user_selection == "C":
    mach_number.expansion_fans()
    print(f'mu = {mach_number.mu:.2f}degrees nu = {mach_number.nu:.3f}')

""" 
add normal shock wave (done), prandtl meyer, and plot table for all three (add possible iteration for previous values.) 
also add what is in notes app Dr. Kara talked about. Can also add try and except to take keyboard interruption/cancel 
key
"""