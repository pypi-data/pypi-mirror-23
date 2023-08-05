# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 11:02:23 2016

@author: cpkmanchee

Notes:

Diffraction grating pair
Simulate grating pair
pulse = input pulse object
L = grating separation (m), use (-) L for stretcher, (+) L for 
    compressor geometry
N = lns/mm of gratings
AOI = angle of incidence (deg)

theta = diffraction angle (assumed 1 order, as is standard)
d = groove spacing

EVERYTHING IS FOR 1st order
"""

import numpy as np
from beamtools.constants import h,c

__all__ = ['gdd2len','beta2','dispersion_coefs',
           'diffraction_angle','transverse_beam_size','littrow_angle', 'sym_disp']

def gdd2len(GDD, N, AOI, lambda0):
    '''Calculate separation length from total GDD, for given grating'''
    m = 1
    g = AOI*np.pi/180    #convert AOI into rad
    d = 1E-3/N    #gives grove spacing in m

    w0 = 2*np.pi*c/lambda0
    theta = np.arcsin(m*2*np.pi*c/(w0*d) - np.sin(g))

    L = (np.abs(GDD*(d**2*w0**3*np.cos(theta)**3)
        /(-m**2*2*4*(np.pi**2)*c)))

    L_real = L/np.cos(theta)    
    
    return L, L_real
    
def beta2(N, AOI, lambda0):
    '''Calculate dispersion paramter, beta2, for given grating'''
    m = 1
    g = AOI*np.pi/180    #convert AOI into rad
    d = 1E-3/N    #gives grove spacing in m

    w0 = 2*np.pi*c/lambda0
    theta = np.arcsin(m*2*np.pi*c/(w0*d) - np.sin(g))
    
    beta2 = (-m**2*2*4*(np.pi**2)*c)/(d**2*w0**3*np.cos(theta)**3)

    return beta2
    

def dispersion_coefs(L, N, AOI, lambda0):
    '''Calculate grating dispersion coefficients from grating specs'''
    m = 1
    g = AOI*np.pi/180    #convert AOI into rad
    d = 1E-3/N    #gives grove spacing in m

    w0 = 2*np.pi*c/lambda0
    theta = np.arcsin(m*2*np.pi*c/(w0*d) - np.sin(g))
    
    phi0 = 2*L*w0*np.cos(theta)/c
    phi1 = ((phi0/w0)*(1+(2*np.pi*c*m*np.sin(theta)
            /(w0*d*np.cos(theta)**2))))
    phi2 = ((-m**2*2*4*(np.pi**2)*L*c/(d**2*w0**3))
            *(1/np.cos(theta)**3))
    phi3 = ((-3*phi2/w0)*(1+(2*np.pi*c*m*np.sin(theta)
            /(w0*d*np.cos(theta)**2))))
    phi4 = (((2*phi3)**2/(3*phi2)) 
            + phi2*(2*np.pi*c*m/(w0**2*d*np.cos(theta)**2))**2)
    
    return np.array([phi0,phi1,phi2,phi3,phi4])
    

def diffraction_angle(N, AOI, lambda0):
    '''Calculate angle of diffraction for given grating and AOI'''
    m = 1
    g = AOI*np.pi/180    #convert AOI into rad
    d = 1E-3/N    #gives grove spacing in m

    w0 = 2*np.pi*c/lambda0
    theta = np.arcsin(m*2*np.pi*c/(w0*d) - np.sin(g))
    
    return theta*180/np.pi
    

def transverse_beam_size(GDD, N, AOI, lambda0, dlambda):
    '''Calculate maximum transverse beam size at second grating of pair'''
    L, L_real = gdd2len(GDD, N, AOI, lambda0)
    dth = (np.abs(diffAngle(N, AOI, lambda0 + dlambda/2) 
            - diffAngle(N, AOI, lambda0-dlambda/2)))
    dxMax = 2*L_real*np.arctan(dth*np.pi/(2*180))
    
    return dxMax
    
    
def littrow_angle(N, lambda0):
    '''Calculate Littrow angle for grating'''
    d = 1E-3/N
    a = (180/np.pi)*np.arcsin(lambda0/(2*d))
    
    return a

def sym_disp(L, N, AOI, lambda0):
    m = 1
    g = AOI*np.pi/180    #convert AOI into rad
    d = 1E-3/N    #gives grove spacing in m

    w0 = 2*np.pi*c/lambda0
    #theta = np.arcsin(m*2*np.pi*c/(w0*d) - np.sin(g))
    w = sym.symbols('w')  
    
    orders = 5
    phi = np.zeros(orders)
    
    phi0 = (2*L*w/c)*(1-(m*2*np.pi*c/(w*d) - sym.sin(g))**2)**(1/2)
    
    for i in range(orders):
        phi[i] = sym.diff(phi0,w,i).subs(w,w0)
        
    return phi
    