from Isentropic_Calculations import Appendices

# from MAE3293_Shockwave_Calculations.Recreating_Appendices.Isentropic_Calculations import RecreatingAppendices
user_selection = input("What appendix are you looking for? \n A) Isentropic Relationship \n B) Normal Schockwave "
                       "Relationship \n C) Prandtl-Meyer Relationship\n Enter A, B, or C: ")

given_values = Appendices(mymach=float(input("\nWhat is your Mach Number ")), upstream_static_pressure=float(input(
    "\nWhat is the upstream static pressure? ")))  # try to add if statement to this here so that it doesn't always ask

""" line above calls the isentropic function then the line below calls for each part of the method. 
error within was dealing with passing the mach number twice but once you assign it, the entire class knows it already. 
Therefore, don't pass it again in class file- comment in there for it. 
"""

if user_selection == "A":
    given_values.isentropic()
    print(
        f'T0/T = {given_values.T_0_over_T:.3f} P0/P = {given_values.p_0_over_p:3f} Rho0/Rho = {given_values.rho_0_over_rho:4f}')
elif user_selection == "B":
    given_values.normal_shockwave()
    given_values.isentropic()

    print(
        f'P_2/P_1 = {given_values.p_2_static_over_p_1_static:.3f} Rho_2/Rho_1 {given_values.rho_2_static_over_rho_1_static:.3f}'
        f' T_2/T_1 = {given_values.T_2_over_T_1:.3f} Ptotal_2/Ptotal_1 {given_values.ptotal_2_over_ptotal_1:.3f}'
        f' Ptotal_2/P_1 = {given_values.ptotal_2_over_p_1_static:.3f} Downstream Mach Number'
        f' {given_values.mach_downstream:.4f}')

    given_values.normal_shock_calculations()
    print(f'\nDownstream Static Pressure (P2) = {given_values.downstream_static_pressure:.3f}')

elif user_selection == "C":
    given_values.expansion_fans()
    print(f'mu = {given_values.mu:.2f}degrees nu = {given_values.nu:.3f}')

""" 
add normal shock wave (done), prandtl meyer (done), and plot table for all three (add possible iteration for previous values.) 
also add what is in notes app Dr. Kara talked about. Can also add try and except to take keyboard interruption/cancel 
key
"""
