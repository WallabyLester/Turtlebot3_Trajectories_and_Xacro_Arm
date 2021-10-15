"""
Compute the trajectory and its derivatives at a given time and 
Compute the proper control inputs at a given time
"""

import sympy
from sympy import Function, sin, atan2, sqrt, symbols
from sympy.abc import W, H, T, t
from math import pi

def comp_traj (W_input, H_input, T_input):
    # define as functions of time
    v = Function('v')(t)
    x = Function('x')(t)
    y = Function('y')(t)
    theta = Function('theta')(t)

    # define x(t) and y(t)
    x = W/2 * sin(2*pi*t/T)
    y = H/2 * sin(4*pi*t/T)

    xdot = x.diff(t)
    ydot = y.diff(t)
    xddot = xdot.diff(t)
    yddot = ydot.diff(t)

    # xdot = vcos(theta), ydot = vsin(theta)
    v = sqrt(xdot**2 + ydot**2)
    theta = atan2(ydot, xdot)
    thetadot = theta.diff(t)
    omega = thetadot

    '''
    v = v.subs([(W, W_input), (H, H_input), (T, T_input)])
    omega = omega.subs([(W, W_input), (H, H_input), (T, T_input)])
    x = x.subs([(W, W_input), (H, H_input), (T, T_input)])
    xdot = xdot.subs([(W, W_input), (H, H_input), (T, T_input)])
    xddot = xddot.subs([(W, W_input), (H, H_input), (T, T_input)])
    y = y.subs([(W, W_input), (H, H_input), (T, T_input)])
    ydot = ydot.subs([(W, W_input), (H, H_input), (T, T_input)])
    yddot = yddot.subs([(W, W_input), (H, H_input), (T, T_input)])
    '''
   
    list = [v, omega, x, xdot, xddot, y, ydot, yddot]
    values = []
    for i in list:
        i = i.subs([(W, W_input), (H, H_input), (T, T_input)])
        values.append(i)

    v = values[0]
    omega = values[1]
    x = values[2]
    xdot = values[3]
    xddot = values[4]
    y = values[5]
    ydot = values[6]
    yddot = values[7]

    # print(omega) for debugging
    return v, omega, x, xdot, xddot, y, ydot, yddot

class FigureEight():
    def __init__(self, W_input, H_input, T_input):
        self.__x, self.__y, self.__xdot, self.__ydot, self.__xddot, self.__yddot, self.__v, self.__omega = comp_traj(W_input, H_input, T_input)
        self.__t = symbols('t')  # remember separate from function
    
    def get_velocity(self, t):
        """ Function to return the linear and angular velocities 

        """
        x = self.__x.subs(self.__t, t)
        y = self.__y.subs(self.__t, t)
        v = self.__v.subs(self.__t, t)
        w = self.__omega.subs(self.__t,t)

        return x, y, v, w

# comp_traj(5, 5, 5) for debugging
