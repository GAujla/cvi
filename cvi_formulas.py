# -*- coding: utf-8 -*-
"""cvi formulas.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15jl32wbrXNY8I2HaK4hSK3ZrpCw4Zk65
"""
import numpy as np
#thin lens equation

#given the distance of the object from the lens (u) and the distance of the image from the lens (v)
def find_f(u,v):
  f = (1/u) + (1/v)
  print(1/f)
  return 1/f

#given the distance of the object from the lens (u) and the focal length (f)
def find_v(f,u):
  v = (1/f) - (1/u)
  print(1/v)
  return 1/v

#given the distance of the distance of the image from the lens (v) and the focal length (f)
def find_u(f,v):
  u = (1/f) - (1/v)
  print(1/u)
  return 1/u

# 2D and 3D Projection 
def xprime(fprime,z,x):
  xprime = (fprime / z) * x
  print(xprime)
  return xprime

def yprime3D(fprime,z,y):
  yprime = (fprime / z) * y
  print(yprime)
  return yprime

def fprime(xprime,z,x):
  fprime = (z * xprime) / x
  print(fprime)
  return fprime

def x(fprime,z,xprime):
  x = (xprime * z) / fprime
  print(x)
  return x

def z(frime, xprime, x):
  z = (x / xprime) * fprime
  print (z)
  return z

def fprime3D(zprime):
  fprime = zprime
  print(fprime)
  return fprime

#Relating real world coordinates to camera coordinates WHEN PIXEL SIZE IS GIVEN, do it manually

#Relating real world coordinates to camera coordinates WHEN PIXEL SIZE IS NOT GIVEN
#given the coordinates of a point in world reference frame (x,y,z), we can convert it to image reference frame (u,v)
#where (x,y,z) are coordinates in the real world
#a,b (alpha and beta) are magnification factors in x and y direction
#ox, oy are the coordinated of the center point of the camera
def pix_to_cam(x,y,z,a,b,ox,oy):
  (u,v,_) = (1/z) * np.matmul(np.matmul(np.array([[a,0,ox], [0,b,oy], [0,0,1]]), np.array([[1,0,0,0],[0,1,0,0],[0,0,1,0]])), np.array([x,y,z,1]))
  print([u,v,_])
  return [u,v,_]


'''
Nearest Neighbour Interpolation:

  Fill empty value with one of its neighbours (Can choose randomly)

Bilinear Interpolation:

  Take the average of the nearest 2 or 4 pixels from the same colour channel. If
  the color channel is the same as the pixel we are comparing then that we use
  that value and not the average.

Smooth Hue Transition Interpolation

  Interpolation of green pixels. We calculate for Red and Blue. If the pixel
  is red when calculating red, we use that. Otherwise, we multiply the Green 
  channel by its bilinear interpolation.

Nearest Neighbour Interpolation

  For the pixel we're calculating, calculate the horizontal and vertical 
  gradients. Horizontal is absolute difference of the pixel's horizontal 
  neighbours. Vertical is the absolute difference of the pixel's vertical 
  neighbours. 
  If Horizontal < Vertical, add the horizontal neighbour values and divide by 2.
  If Horizontal > Vertical, add the vertical neighbour values and divide by 2.
  If H = V, add the horizontal and vertical neighbour values and divide by 4. 

'''

def rgb2gray(r,g,b):

    r, g, b = rgb[:,:,0], rgb[:,:,1], rgb[:,:,2]
    gray = (r + g + b)/3

    return gray


#CHANGE THE FOLLOWING VALUES:
#R is the rotation matrix
#t is the translation matrix
R = np.array([[1,1,1],[1,1,1],[1,1,1]])
t = np.array([[1],[1],[1]])
zeros = np.zeros((3,1))
zeros_t = np.transpose(zeros)
#(x,y,z) are the coordinates in pixels
def cam_reference_to_world_reference(R, zeros_t, t, x,y,z):
  (X,Y,Z,_) = np.matmul(np.array([R,t],[zeros_t,1]),np.array(x,y,z,1))
  print((X,Y,Z,_))
  return (X,Y,Z,_)

def world_reference_to_cam_reference(R, zeros_t, t, x,y,z):
  R_t = np.transpose(R)
  t = np.matmul(-R_t, t)
  (X,Y,Z,_) = np.matmul(np.array([R_t,t],[zeros_t,1]),np.array(x,y,z,1))
  print((X,Y,Z,_))
  return (X,Y,Z,_)

#point in real world to a point in the image
R = np.array([[1,1,1],[1,1,1],[1,1,1]])
t = np.array([[1],[1],[1]])
zeros = np.zeros((3,1))
zeros_t = np.transpose(zeros)
def world_to_image():
  R_t = np.transpose(R)
  t = np.matmul(-R_t, t)
  [u,v,_] = (1/z) * np.matmul(np.matmul(np.array([[a,0,ox], [0,b,oy], [0,0,1]]), np.array([[1,0,0,0],[0,1,0,0],[0,0,1,0]])), (np.matmul(np.array([R_t,t],[zeros,1]), np.array([x,y,z,1]))))
  print([u,v,_])
  return [u,v,_]
