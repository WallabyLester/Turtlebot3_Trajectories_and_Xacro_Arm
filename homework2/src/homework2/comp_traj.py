"""
Compute the trajectory and its derivatives at a given time and 
Compute the proper control inputs at a given time
"""

import sympy as sym
from sympy import Function, sin, cos, atan2, sqrt
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
    thetadot = theta.diff(t)

    # xdot = vcos(theta), ydot = vsin(theta)
    v = sqrt(xdot**2 + ydot**2)
    theta = atan2(ydot, xdot)
    omega = thetadot

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

    return x, y, xdot, ydot, xddot, yddot, v, omega

comp_traj(10.0, 5.0, 20.0)