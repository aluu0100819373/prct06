#!/usr/bin/python
#!encoding: UTF-8
pi=3.1415926535897931159979634685441852
def aproximapi(n):
  sumatorio=0.0
  for i in range(1,n+1):
    x=(i-0.5)/float(n)
    #!b=i/float(n)
    #!a=(i-1)/float(n)
    fx=4.0/(1+x**2)
    #!print'Subintervalos[%.3f  %.3f] x_i:%.3f fx_i:%.3f' % (a, b, x,fx)
    sumatorio=sumatorio+fx
    p=(sumatorio/n)
  return p
k=int(raw_input('Nº de veces que desea se ejecute el programa ')) 
s=[]
for t in range(1,k+1):
  n=int(raw_input('Valor de subintervalos: '))
  #!print 'El valor aproximado de pi con 35 decimales es: %.35f' %pi
  print aproximapi(n)
  s=s+[aproximapi(n)]
print s