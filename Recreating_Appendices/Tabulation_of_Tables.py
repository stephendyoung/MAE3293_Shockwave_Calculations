from Isentropic_Calculations import Appendices
import matplotlib.pyplot as plt

# mach_number = Appendices(mymach=0.02)
#
# while mach_number < 1:
#     mach_number.isentropic()
#     print(f'T0/T = {mach_number.T_0_over_T:.3f}')
#     mach_number += 0.02

data = []
mymach = 0.02
while mymach < 1.02:
    mach_number = Appendices(mymach)
    mach_number.isentropic()
    data.append(f' Mach Number: {mymach:.2f} T0/T = {mach_number.T_0_over_T:.3f} P0/P = {mach_number.p_0_over_p:3f} Rho0/Rho ='
                f' {mach_number.rho_0_over_rho:4f}')
    mymach += 0.02
print(data)

# fig1, ax = plt.subplots()
#
# fig1.patch.set_visible(False)
# ax.set_axis_off()
# table = ax.table(
# plt.show()



#print(data)