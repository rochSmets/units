#! /usr/bin/env python

import numpy as np
import pickle

# open txt file
f = open('dat.txt', 'r+')

# constants :
mu = 4*np.pi*1.0e-7
kb = 1.38e-23
mp = 1.67e-27
qe = 1.6e-19

# read comments in the file
junk = f.readline()
empt = f.readline()
junk = f.readline()
empt = f.readline()

# density
st = f.readline()
txt, colon, vnum = st.strip().split()
n0 = float(vnum)

# magnetic field
st = f.readline()
txt, txt, colon, vnum = st.strip().split()
b0 = float(vnum)

# calculation of alfven velocity, inertial length & gyroperiod
va = b0/np.sqrt(mu*n0*mp)
dp = np.sqrt(mp/(mu*n0*qe*qe))
tc = mp/(qe*b0)
t0 = mp*va*va/kb

s1 = 'alfven velocity    :        {:1.4e}\n'.format(va)
s2 = 'p+ inertial length :        {:1.4e}\n'.format(dp)
s3 = 'p+ gyroperiod      :        {:1.4e}\n'.format(tc)

# read line break
empt = f.readline()

#write the values
f.write(s1)
f.write(s2)
f.write(s3)

# read line break
empt = f.readline()

#remember the position in the file
pf = f.tell()

# e- temperature
st = f.readline()
txt, txt, colon, vnum, junk = st.strip().split()
te = float(vnum)

# p+ temperature
st = f.readline()
txt, txt, colon, vnum, junk = st.strip().split()
tp = float(vnum)

# calculation of e- & p+ temperatures
Te = te/t0
Tp = tp/t0

# set the strings
s1 = 'e- temperature     :        {:1.4e}          {:1.4e}\n'.format(te, Te)
s2 = 'p+ temperature     :        {:1.4e}          {:1.4e}\n'.format(te, Te)

# go to the right position to write
f.seek(pf)

# write the strings
f.write(s1)
f.write(s2)

# read line break
empt = f.readline()

# remember the position in the file
pf = f.tell()

# length
st = f.readline()
txt, colon, vnum, junk = st.strip().split()
lh = float(vnum)

# velocity
st = f.readline()
txt, colon, vnum, junk = st.strip().split()
vy = float(vnum)

# time
st = f.readline()
txt, colon, vnum, junk = st.strip().split()
ti = float(vnum)

# calculation of the dimensionless parameters
Lh = lh/dp
Vy = vy/va
Ti = ti/tc

# set the strings
s1 = 'length             :        {:1.4e}          {:1.4e}\n'.format(lh, Lh)
s2 = 'velocity           :        {:1.4e}          {:1.4e}\n'.format(vy, Vy)
s3 = 'time               :        {:1.4e}          {:1.4e}\n'.format(ti, Ti)

# go to the right position to write
f.seek(pf)

#write the strings
f.write(s1)
f.write(s2)
f.write(s3)

# read line break
empt = f.readline()

# e- beta
Be = 2.0*Te
be = 2.0*mu*n0*kb*te/(b0*b0)

#p+ beta
Bp = 2.0*Tp
bp = 2.0*mu*n0*kb*tp/(b0*b0)

# set the strings
s1 = 'e- beta            :        {:1.4e}          {:1.4e}\n'.format(be, Be)
s2 = 'p+ beta            :        {:1.4e}          {:1.4e}\n'.format(bp, Bp)

#write the strings
f.write(s1)
f.write(s2)

# close the file
f.close()
