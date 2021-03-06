"""
Computes the trajectory and its derivatives at a given time and gives the proper control inputs

"""

import sympy
from sympy import Function, atan2, symbols, sqrt, sin, pi
from sympy.abc import W, H, T, t

def comp_traj (W_input, H_input, T_input):
    """ Function to compute the trajectory 

    Calculates the trajectory for a given shape 

    Args:
        W_input : width of the figure eight 
        H_input : height of the figure eight 
        T_input : period of the figure eight 

    Returns: 
        v, omega, x, xdot, xddot, y, ydot, yddot, theta 
        Symbolic values for the trajectory, velocites and derivatives
    """
    # define as functions of time
    v = Function('v')(t)
    x = Function('x')(t)
    y = Function('y')(t)
    theta = Function('theta')(t)

    # define x(t) and y(t)
    x = (W/2) * sin((2*pi*t)/T)
    y = (H/2) * sin((4*pi*t)/T)

    xdot = x.diff(t)
    ydot = y.diff(t)
    xddot = xdot.diff(t)
    yddot = ydot.diff(t)

    # given that xdot = vcos(theta), ydot = vsin(theta)
    v = sqrt(xdot**2 + ydot**2)
    theta = atan2(ydot, xdot)
    thetadot = theta.diff(t)
    omega = thetadot

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

    return v, omega, x, xdot, xddot, y, ydot, yddot, theta

class FigureEight():
    """ Computes the linear and angular velocity at a given time
    """
    def __init__(self, W_input, H_input, T_input):
        self.v, self.omega, self.x, self.xdot, self.xddot, self.y, self.ydot, self.yddot, self.theta = comp_traj(W_input, H_input, T_input)
        self.t = symbols('t')  # remember separate from comp_traj function
    
    def get_velocity(self, t):
        """ Function to return the linear and angular velocities 

        Calculates the numeric solution to the symbolic solutions from comp_traj

        Args:
            t (time) : given time from ros functions 

        Returns: 
            x, y, v, omega
            Values for the x and y position and linear and angular velocities 
        """
        x = self.x.subs(self.t, t)
        y = self.y.subs(self.t, t)
        v = self.v.subs(self.t, t)
        omega = self.omega.subs(self.t, t)

        return x, y, v, omega

    def theta0(self, t):
        """ Function to return theta value 

        Calculates the theta value at time 0 

        Args: 
            t (time) : given time (0 in this instance)

        Returns: 
            theta, angle for initial position of the turtle/robot
        """
        theta = self.theta.subs(self.t, t)

        return theta

    def test(self, t):
        """ Function for testing the python package calculations

        Calculates all positional values 

        Args:
            t (time) : given time from test function 

        Returns: 
            x, y, xdot, ydot, xddot, yddot, v, omega
            Values for use in testing 
        """
        x = self.x.subs(self.t, t)
        y = self.y.subs(self.t, t)
        xdot = self.xdot.subs(self.t, t)
        ydot = self.ydot.subs(self.t, t)
        xddot = self.xddot.subs(self.t, t)
        yddot = self.yddot.subs(self.t, t)
        v = self.v.subs(self.t, t)
        omega = self.omega.subs(self.t, t)

        return x, y, xdot, ydot, xddot, yddot, v, omega

# for testing calculations 
'''
figure_eight = FigureEight(5,5,5)
#for t in range(10):
t = 10
x,y,v,w = figure_eight.get_velocity(t)
print(f"v = {v}")
print(f"w= {w}")
'''
# for finding test cases 
'''
figure_eight = FigureEight(4,2,6)
t = 3
x, y, xdot, ydot, xddot, yddot, v, omega = figure_eight.test(t)
print(f"{x}, {y}, {xdot}, {ydot}, {xddot}, {yddot}, {v}, {omega}")
'''