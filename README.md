# Numerical-Analysis
Simple python algorithms to help solve various linear algebra problems.

IVP_Euler_Method.py is a method of solving initial value problems that have the same setup as outlined here: https://en.wikipedia.org/wiki/Initial_value_problem
This method inputs the function in the form of a lambda expression, and outputs the two variables that were unknown at the beignning of the problem.

LLS.py is the linear least squares method for solving the best fit equation of the line that fits through given data points. The method takes two arrays as input,
an array of x values and an array of their corrisponding y values. The method then prints the resulting equation in the console and returns the resulting lambda expression.

OVS.py is a couple methods to find the solution to one variable equations.
  The Muller mehod uses 3 solution approximations and a lambda expression to find the resulting solution. It is generally faster than the secant method, however
  the Muller method fails when it begins to go into the complex plane. For times when the Muller method fails, the secant method is a good replacement. Generally slower,
  the Secant method is also more reliable at not crashing.
  
General Variables:
  f = the function in question. A lambda function for simplicity sake.
  tol = toleration, the minimum allowed change in the solution before the methods say it has converged at a solution.
  N = the total number of interations the algorithm will go before return failure is there is no convergence.
