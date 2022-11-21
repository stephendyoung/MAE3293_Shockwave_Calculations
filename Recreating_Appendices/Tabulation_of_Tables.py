from Isentropic_Calculations import Appendices


# mach_number = Appendices(mymach=0.02)
#
# while mach_number < 1:
#     mach_number.isentropic()
#     print(f'T0/T = {mach_number.T_0_over_T:.3f}')
#     mach_number += 0.02


mymach = 0.02
while mymach < 1.02:
    mach_number = Appendices(mymach)
    mach_number.isentropic()
    print(f"T0/T = {mach_number.T_0_over_T:.3f}")
    mymach += 0.02