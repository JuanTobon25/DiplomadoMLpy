# -*- coding: utf-8 -*-
"""Metnum.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1w-nfnnkXluCj-rJcvvgF8jZMB4Ixflji
"""

import numpy as np

def newtonrap(f, df, p0, tol):
  error=10
  while error > tol:
    if f(p0)==0:
      raiz = p0
    else:
      p=p0-f(p0)/df(p0)
      error = abs(p-p0)
      p0=p
  raiz = p
  return raiz

def biseccion(f, a, b, tol):
    error = 10
    while error>tol:
        p1=(a+b)/2
        fa=f(a)
        fp1=f(p1)
        if f(p1)==0: 
            raiz=p1
            break
        elif fa*fp1<0:
            b=p1
        else:
            a=p1
        raiz=p1
        error=abs(fp1)
    return raiz

def puntofijo(g, p0, tol):
    error = 10
    while error > tol:
        p=g(p0)
        error=abs(p-p0)
        p0=p
        print(p0)
    return p0

def secante(f, p0, p1, tol):
    error = 10
    while error > tol:
        pn = p1 - (f(p1)*(p1-p0))/(f(p1)-f(p0))
        p0=p1
        p1=pn
        error = abs(p1-p0)
        print("Raiz: ", p1)
        print("error: ", error)
    return p1

#Derivada centrada a 5 puntos
def derivada5puntos(f,x0,h):
    dev=(-f(x0+2*h)+8*f(x0+h)-8*f(x0-h)+f(x0-2*h))/(12*h)
    return dev

#Segunda derivada
def segundaderivada(f,x0,h):
    sdev=(f(x0+h)-2*f(x0)+f(x0-h))/(h**2)
    return sdev

def trapeciomulti(a,b,f,n=10000):
  h = (b-a)/n
  xs = np.arange(a,b+h,h)
  integral = 0
  for i in range(n+1):
    if i == 0 or i == n:
      integral += f(xs[i])
    else:
      integral += 2*f(xs[i])
  integral = (h/2)*(integral)
  return integral

