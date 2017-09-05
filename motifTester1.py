'''
FUNC:A_1a4s_1_2_1_8
PDB:1a4s
EC:1.2.1.8
RESI:asn,glu,cys
LOCI:a-166,263,297;
'''
import motifFunctions as cmd
import time as t

A_1a4s_1_2_1_8 = {}
matrices = {}

glu = ['CB', 'CG', 'CD', 'OE1', 'OE2', 'O', 'C', 'CA', 'N']
cys = ['CB', 'SG', 'O', 'C', 'CA', 'N']
asn = ['CB', 'CG', 'OD1', 'ND2', 'O', 'C', 'CA', 'N']

cmd.select(A_1a4s_1_2_1_8, matrices, 'n. CB&r. cys w. %s of n. CB&r. glu'%(d*8.79))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. CB&r. cys w. %s of n. CG&r. glu'%(d*9.87))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. CB&r. cys w. %s of n. CD&r. glu'%(d*9.67))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. CB&r. cys w. %s of n. OE1&r. glu'%(d*8.65))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. CB&r. cys w. %s of n. OE2&r. glu'%(d*10.70))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. CB&r. cys w. %s of n. O&r. glu'%(d*8.10))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. CB&r. cys w. %s of n. C&r. glu'%(d*8.26))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. CB&r. cys w. %s of n. CA&r. glu'%(d*9.12))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. CB&r. cys w. %s of n. N&r. glu'%(d*10.47))

cmd.select(A_1a4s_1_2_1_8, matrices, 'n. SG&r. cys w. %s of n. CB&r. glu'%(d*8.47))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. SG&r. cys w. %s of n. CG&r. glu'%(d*9.28))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. SG&r. cys w. %s of n. CD&r. glu'%(d*8.88))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. SG&r. cys w. %s of n. OE1&r. glu'%(d*7.89))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. SG&r. cys w. %s of n. OE2&r. glu'%(d*9.76))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. SG&r. cys w. %s of n. O&r. glu'%(d*8.52))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. SG&r. cys w. %s of n. C&r. glu'%(d*8.61))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. SG&r. cys w. %s of n. CA&r. glu'%(d*9.13))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. SG&r. cys w. %s of n. N&r. glu'%(d*10.51))

cmd.select(A_1a4s_1_2_1_8, matrices, 'n. O&r. cys w. %s of n. CB&r. glu'%(d*11.14))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. O&r. cys w. %s of n. CG&r. glu'%(d*12.15))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. O&r. cys w. %s of n. CD&r. glu'%(d*11.72))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. O&r. cys w. %s of n. OE1&r. glu'%(d*10.52))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. O&r. cys w. %s of n. OE2&r. glu'%(d*12.68))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. O&r. cys w. %s of n. O&r. glu'%(d*10.37))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. O&r. cys w. %s of n. C&r. glu'%(d*10.24))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. O&r. cys w. %s of n. CA&r. glu'%(d*11.13))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. O&r. cys w. %s of n. N&r. glu'%(d*12.51))

cmd.select(A_1a4s_1_2_1_8, matrices, 'n. C&r. cys w. %s of n. CB&r. glu'%(d*10.74))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. C&r. cys w. %s of n. CG&r. glu'%(d*11.71))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. C&r. cys w. %s of n. CD&r. glu'%(d*11.25))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. C&r. cys w. %s of n. OE1&r. glu'%(d*10.08))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. C&r. cys w. %s of n. OE2&r. glu'%(d*12.18))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. C&r. cys w. %s of n. O&r. glu'%(d*10.17))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. C&r. cys w. %s of n. C&r. glu'%(d*10.12))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. C&r. cys w. %s of n. CA&r. glu'%(d*10.93))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. C&r. cys w. %s of n. N&r. glu'%(d*12.33))

cmd.select(A_1a4s_1_2_1_8, matrices, 'n. CA&r. cys w. %s of n. CB&r. glu'%(d*10.30))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. CA&r. cys w. %s of n. CG&r. glu'%(d*11.37))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. CA&r. cys w. %s of n. CD&r. glu'%(d*11.11))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. CA&r. cys w. %s of n. OE1&r. glu'%(d*10.03))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. CA&r. cys w. %s of n. OE2&r. glu'%(d*12.10))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. CA&r. cys w. %s of n. O&r. glu'%(d*9.49))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. CA&r. cys w. %s of n. C&r. glu'%(d*9.64))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. CA&r. cys w. %s of n. CA&r. glu'%(d*10.56))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. CA&r. cys w. %s of n. N&r. glu'%(d*11.90))

cmd.select(A_1a4s_1_2_1_8, matrices, 'n. N&r. cys w. %s of n. CB&r. glu'%(d*11.10))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. N&r. cys w. %s of n. CG&r. glu'%(d*12.11))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. N&r. cys w. %s of n. CD&r. glu'%(d*11.85))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. N&r. cys w. %s of n. OE1&r. glu'%(d*10.84))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. N&r. cys w. %s of n. OE2&r. glu'%(d*12.79))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. N&r. cys w. %s of n. O&r. glu'%(d*10.39))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. N&r. cys w. %s of n. C&r. glu'%(d*10.67))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. N&r. cys w. %s of n. CA&r. glu'%(d*11.53))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. N&r. cys w. %s of n. N&r. glu'%(d*12.86))

cmd.select(A_1a4s_1_2_1_8, matrices, 'n. CB&r. cys w. %s of n. CB&r. asn'%(d*9.29))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. CB&r. cys w. %s of n. CG&r. asn'%(d*8.02))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. CB&r. cys w. %s of n. OD1&r. asn'%(d*8.20))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. CB&r. cys w. %s of n. ND2&r. asn'%(d*6.93))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. CB&r. cys w. %s of n. O&r. asn'%(d*11.33))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. CB&r. cys w. %s of n. C&r. asn'%(d*10.89))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. CB&r. cys w. %s of n. CA&r. asn'%(d*10.55))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. CB&r. cys w. %s of n. N&r. asn'%(d*10.82))

cmd.select(A_1a4s_1_2_1_8, matrices, 'n. SG&r. cys w. %s of n. CB&r. asn'%(d*9.35))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. SG&r. cys w. %s of n. CG&r. asn'%(d*7.99))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. SG&r. cys w. %s of n. OD1&r. asn'%(d*8.06))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. SG&r. cys w. %s of n. ND2&r. asn'%(d*6.98))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. SG&r. cys w. %s of n. O&r. asn'%(d*10.87))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. SG&r. cys w. %s of n. C&r. asn'%(d*10.49))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. SG&r. cys w. %s of n. CA&r. asn'%(d*10.44))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. SG&r. cys w. %s of n. N&r. asn'%(d*10.80))

cmd.select(A_1a4s_1_2_1_8, matrices, 'n. O&r. cys w. %s of n. CB&r. asn'%(d*11.57))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. O&r. cys w. %s of n. CG&r. asn'%(d*10.57))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. O&r. cys w. %s of n. OD1&r. asn'%(d*11.04))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. O&r. cys w. %s of n. ND2&r. asn'%(d*9.32))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. O&r. cys w. %s of n. O&r. asn'%(d*13.61))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. O&r. cys w. %s of n. C&r. asn'%(d*13.40))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. O&r. cys w. %s of n. CA&r. asn'%(d*12.99))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. O&r. cys w. %s of n. N&r. asn'%(d*13.46))

cmd.select(A_1a4s_1_2_1_8, matrices, 'n. C&r. cys w. %s of n. CB&r. asn'%(d*10.64))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. C&r. cys w. %s of n. CG&r. asn'%(d*9.60))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. C&r. cys w. %s of n. OD1&r. asn'%(d*10.06))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. C&r. cys w. %s of n. ND2&r. asn'%(d*8.33))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. C&r. cys w. %s of n. O&r. asn'%(d*12.53))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. C&r. cys w. %s of n. C&r. asn'%(d*12.33))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. C&r. cys w. %s of n. CA&r. asn'%(d*12.02))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. C&r. cys w. %s of n. N&r. asn'%(d*12.54))

cmd.select(A_1a4s_1_2_1_8, matrices, 'n. CA&r. cys w. %s of n. CB&r. asn'%(d*9.28))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. CA&r. cys w. %s of n. CG&r. asn'%(d*8.22))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. CA&r. cys w. %s of n. OD1&r. asn'%(d*8.67))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. CA&r. cys w. %s of n. ND2&r. asn'%(d*6.98))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. CA&r. cys w. %s of n. O&r. asn'%(d*11.35))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. CA&r. cys w. %s of n. C&r. asn'%(d*11.07))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. CA&r. cys w. %s of n. CA&r. asn'%(d*10.67))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. CA&r. cys w. %s of n. N&r. asn'%(d*11.12))

cmd.select(A_1a4s_1_2_1_8, matrices, 'n. N&r. cys w. %s of n. CB&r. asn'%(d*8.19))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. N&r. cys w. %s of n. CG&r. asn'%(d*7.24))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. N&r. cys w. %s of n. OD1&r. asn'%(d*7.87))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. N&r. cys w. %s of n. ND2&r. asn'%(d*5.94))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. N&r. cys w. %s of n. O&r. asn'%(d*10.09))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. N&r. cys w. %s of n. C&r. asn'%(d*9.93))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. N&r. cys w. %s of n. CA&r. asn'%(d*9.59))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. N&r. cys w. %s of n. N&r. asn'%(d*10.22))

cmd.select(A_1a4s_1_2_1_8, matrices, 'n. CB&r. glu w. %s of n. CB&r. asn'%(d*13.49))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. CB&r. glu w. %s of n. CG&r. asn'%(d*12.01))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. CB&r. glu w. %s of n. OD1&r. asn'%(d*11.27))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. CB&r. glu w. %s of n. ND2&r. asn'%(d*11.70))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. CB&r. glu w. %s of n. O&r. asn'%(d*15.05))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. CB&r. glu w. %s of n. C&r. asn'%(d*14.17))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. CB&r. glu w. %s of n. CA&r. asn'%(d*14.06))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. CB&r. glu w. %s of n. N&r. asn'%(d*13.61))

cmd.select(A_1a4s_1_2_1_8, matrices, 'n. CG&r. glu w. %s of n. CB&r. asn'%(d*14.47))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. CG&r. glu w. %s of n. CG&r. asn'%(d*12.97))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. CG&r. glu w. %s of n. OD1&r. asn'%(d*12.19))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. CG&r. glu w. %s of n. ND2&r. asn'%(d*12.69))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. CG&r. glu w. %s of n. O&r. asn'%(d*15.76))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. CG&r. glu w. %s of n. C&r. asn'%(d*14.91))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. CG&r. glu w. %s of n. CA&r. asn'%(d*14.95))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. CG&r. glu w. %s of n. N&r. asn'%(d*14.53))

cmd.select(A_1a4s_1_2_1_8, matrices, 'n. CD&r. glu w. %s of n. CB&r. asn'%(d*14.74))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. CD&r. glu w. %s of n. CG&r. asn'%(d*13.23))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. CD&r. glu w. %s of n. OD1&r. asn'%(d*12.55))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. CD&r. glu w. %s of n. ND2&r. asn'%(d*12.82))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. CD&r. glu w. %s of n. O&r. asn'%(d*15.89))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. CD&r. glu w. %s of n. C&r. asn'%(d*15.16))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. CD&r. glu w. %s of n. CA&r. asn'%(d*15.29))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. CD&r. glu w. %s of n. N&r. asn'%(d*15.03))

cmd.select(A_1a4s_1_2_1_8, matrices, 'n. OE1&r. glu w. %s of n. CB&r. asn'%(d*14.23))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. OE1&r. glu w. %s of n. CG&r. asn'%(d*12.72))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. OE1&r. glu w. %s of n. OD1&r. asn'%(d*12.15))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. OE1&r. glu w. %s of n. ND2&r. asn'%(d*12.18))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. OE1&r. glu w. %s of n. O&r. asn'%(d*15.49))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. OE1&r. glu w. %s of n. C&r. asn'%(d*14.81))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. OE1&r. glu w. %s of n. CA&r. asn'%(d*14.90))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. OE1&r. glu w. %s of n. N&r. asn'%(d*14.74))

cmd.select(A_1a4s_1_2_1_8, matrices, 'n. OE2&r. glu w. %s of n. CB&r. asn'%(d*15.59))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. OE2&r. glu w. %s of n. CG&r. asn'%(d*14.09))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. OE2&r. glu w. %s of n. OD1&r. asn'%(d*13.39))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. OE2&r. glu w. %s of n. ND2&r. asn'%(d*13.71))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. OE2&r. glu w. %s of n. O&r. asn'%(d*16.53))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. OE2&r. glu w. %s of n. C&r. asn'%(d*15.83))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. OE2&r. glu w. %s of n. CA&r. asn'%(d*16.07))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. OE2&r. glu w. %s of n. N&r. asn'%(d*15.84))

cmd.select(A_1a4s_1_2_1_8, matrices, 'n. O&r. glu w. %s of n. CB&r. asn'%(d*12.55))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. O&r. glu w. %s of n. CG&r. asn'%(d*11.17))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. O&r. glu w. %s of n. OD1&r. asn'%(d*10.52))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. O&r. glu w. %s of n. ND2&r. asn'%(d*10.88))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. O&r. glu w. %s of n. O&r. asn'%(d*14.67))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. O&r. glu w. %s of n. C&r. asn'%(d*13.71))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. O&r. glu w. %s of n. CA&r. asn'%(d*13.25))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. O&r. glu w. %s of n. N&r. asn'%(d*12.67))

cmd.select(A_1a4s_1_2_1_8, matrices, 'n. C&r. glu w. %s of n. CB&r. asn'%(d*13.44))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. C&r. glu w. %s of n. CG&r. asn'%(d*12.02))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. C&r. glu w. %s of n. OD1&r. asn'%(d*11.42))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. C&r. glu w. %s of n. ND2&r. asn'%(d*11.61))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. C&r. glu w. %s of n. O&r. asn'%(d*15.49))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. C&r. glu w. %s of n. C&r. asn'%(d*14.58))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. C&r. glu w. %s of n. CA&r. asn'%(d*14.19))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. C&r. glu w. %s of n. N&r. asn'%(d*13.70))

cmd.select(A_1a4s_1_2_1_8, matrices, 'n. CA&r. glu w. %s of n. CB&r. asn'%(d*14.25))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. CA&r. glu w. %s of n. CG&r. asn'%(d*12.79))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. CA&r. glu w. %s of n. OD1&r. asn'%(d*12.11))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. CA&r. glu w. %s of n. ND2&r. asn'%(d*12.43))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. CA&r. glu w. %s of n. O&r. asn'%(d*16.06))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. CA&r. glu w. %s of n. C&r. asn'%(d*15.16))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. CA&r. glu w. %s of n. CA&r. asn'%(d*14.91))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. CA&r. glu w. %s of n. N&r. asn'%(d*14.43))

cmd.select(A_1a4s_1_2_1_8, matrices, 'n. N&r. glu w. %s of n. CB&r. asn'%(d*15.15))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. N&r. glu w. %s of n. CG&r. asn'%(d*13.72))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. N&r. glu w. %s of n. OD1&r. asn'%(d*12.96))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. N&r. glu w. %s of n. ND2&r. asn'%(d*13.47))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. N&r. glu w. %s of n. O&r. asn'%(d*16.96))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. N&r. glu w. %s of n. C&r. asn'%(d*15.99))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. N&r. glu w. %s of n. CA&r. asn'%(d*15.71))
cmd.select(A_1a4s_1_2_1_8, matrices, 'n. N&r. glu w. %s of n. N&r. asn'%(d*15.10))

# print "Matches:", A_1a4s_1_2_1_8, "\n"
# print "Matrix", matrices

# Sizes
# print "Size:", len(A_1a4s_1_2_1_8[("CYS", "GLU")][0]), len(A_1a4s_1_2_1_8[("CYS", "GLU")][1]), len(A_1a4s_1_2_1_8[("CYS", "GLU")][2])
# print "Size:", len(matrices[("CYS", "GLU")][0]), len(matrices[("CYS", "GLU")][1]), len(matrices[("CYS", "GLU")][2])

# First row
# print "element:", A_1a4s_1_2_1_8[("CYS", "GLU")][0]
# print "element:", matrices[("CYS", "GLU")][0]


temp = {}
for pair in matrices:
    print pair
    temp[pair] = cmd.pca(matrices[pair])