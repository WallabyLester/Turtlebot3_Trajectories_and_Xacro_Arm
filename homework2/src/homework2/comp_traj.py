"""
Compute the trajectory and its derivatives at a given time and 
Compute the proper control inputs at a given time
"""

import sympy
from sympy import Function, atan2, symbols, sqrt, sin, pi
from sympy.abc import W, H, T, t

def comp_traj (W_input, H_input, T_input):

    # define as functions of time
    v = Function('v')(t)
    x = Function('x')(t)
    y = Function('y')(t)
    theta = Function('theta')(t)

    # define x(t) and y(t)
    x = (W/2) * sin((2*pi*t)/T)
    y = (H/2) * sin((4*pi*t)/T)

    xdot = x.diff(t)
    #print(f"xdot = {xdot}")
    ydot = y.diff(t)
    xddot = xdot.diff(t)
    yddot = ydot.diff(t)

    # xdot = vcos(theta), ydot = vsin(theta)
    v = sqrt(xdot**2 + ydot**2)
    theta = atan2(ydot, xdot)
    thetadot = theta.diff(t)
    omega = thetadot
    #print(f"omega = {omega}")

    list = [v, omega, x, xdot, xddot, y, ydot, yddot, theta]
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
    theta = values[8]

    #print(v) # for debugging
    #print(omega) # for debugging
    return v, omega, x, xdot, xddot, y, ydot, yddot

class FigureEight():
    def __init__(self, W_input, H_input, T_input):
        self.v, self.omega, self.x, self.xdot, self.xddot, self.y, self.ydot, self.yddot = comp_traj(W_input, H_input, T_input)
        self.t = symbols('t')  # remember separate from comp_traj function
    
    def get_velocity(self, t):
        """ Function to return the linear and angular velocities 

        """
        x = self.x.subs(self.t, t)
        y = self.y.subs(self.t, t)
        v = self.v.subs(self.t, t)
        omega = self.omega.subs(self.t, t)

        return x, y, v, omega

'''
#comp_traj(5, 5, 5) # for debugging
figure_eight = FigureEight(5,5,5)
#for t in range(10):
t = 10
x,y,v,w = figure_eight.get_velocity(t)
print(f"v = {v}")
print(f"w= {w}")
'''