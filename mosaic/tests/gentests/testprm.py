from mosaic.utest.testutil import *
import pylab

Fs, dat = readcsv('msaTest1.csv')
print(readparams('msaTest1.prm'))

pylab.plot(dat)
pylab.show()
