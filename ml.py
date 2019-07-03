from scipy.io import loadmat
import numpy as np
import scipy.optimize as opt
import pandas as pd

def sigmoid(z):
  return 1/(1+np.exp(-z))

def nnCostFunction(h, y_d):
  temp1 = np.multiply(y_d, np.log(h))
  temp2 = np.multiply(1-y_d, np.log(1-h))
  temp3 = np.sum(temp1 + temp2)
  return np.sum(temp3 / (-m))


def sigmoidGrad(z):
  return np.multiply(sigmoid(z), 1-sigmoid(z))
  
def nnCostFunctionReg(theta1, theta2):
  sum1 = np.sum(np.sum(np.power(theta1[:,1:],2), axis = 1))
  sum2 = np.sum(np.sum(np.power(theta2[:,1:],2), axis = 1))
  return (sum1 + sum2) * lmbda / (2*m)


def nnCostFunc(nn_params, input_layer_size, hidden_layer_size, num_labels, X, y, lmbda):
  theta1 = np.reshape(nn_params[:hidden_layer_size*(input_layer_size+1)], (hidden_layer_size, input_layer_size+1), 'F')
  theta2 = np.reshape(nn_params[hidden_layer_size*(input_layer_size+1):], (num_labels, hidden_layer_size+1), 'F')

  m = len(y)
  ones = np.ones((m,1))
  a1 = np.hstack((ones, X))
  a2 = sigmoid(a1 @ theta1.T)
  a2 = np.hstack((ones, a2))
  h = sigmoid(a2 @ theta2.T)
  
  y_d = pd.get_dummies(y.flatten())
  
  temp1 = np.multiply(y_d, np.log(h))
  temp2 = np.multiply(1-y_d, np.log(1-h))
  temp3 = np.sum(temp1 + temp2)
  
  sum1 = np.sum(np.sum(np.power(theta1[:,1:],2), axis = 1))
  sum2 = np.sum(np.sum(np.power(theta2[:,1:],2), axis = 1))
  
  return np.sum(temp3 / (-m)) + (sum1 + sum2) * lmbda / (2*m)

def randInitializeWeights(L_in, L_out):
  epsilon = 0.12
  return np.random.rand(L_out, L_in+1) * 2 * epsilon - epsilon

def nnGrad(nn_params, input_layer_size, hidden_layer_size, num_labels, X, y, lmbda):
  initial_theta1 = np.reshape(nn_params[:hidden_layer_size*(input_layer_size+1)], (hidden_layer_size, input_layer_size+1), 'F')
  initial_theta2 = np.reshape(nn_params[hidden_layer_size*(input_layer_size+1):], (num_labels, hidden_layer_size+1), 'F')
  y_d = pd.get_dummies(y.flatten())
  delta1 = np.zeros(initial_theta1.shape)
  delta2 = np.zeros(initial_theta2.shape)
  m = len(y)
  
  for i in range(X.shape[0]):
    ones = np.ones(1)
    a1 = np.hstack((ones, X[i]))
    z2 = a1 @ initial_theta1.T
    a2 = np.hstack((ones, sigmoid(z2)))
    z3 = a2 @ initial_theta2.T
    a3 = sigmoid(z3)

    d3 = a3 - y_d.iloc[i,:][np.newaxis,:]
    z2 = np.hstack((ones, z2))
    d2 = np.multiply(initial_theta2.T @ d3.T, sigmoidGrad(z2).T[:,np.newaxis])
    delta1 = delta1 + d2[1:,:] @ a1[np.newaxis,:]
    delta2 = delta2 + d3.T @ a2[np.newaxis,:]
      
  delta1 /= m
  delta2 /= m
  #print(delta1.shape, delta2.shape)
  delta1[:,1:] = delta1[:,1:] + initial_theta1[:,1:] * lmbda / m
  delta2[:,1:] = delta2[:,1:] + initial_theta2[:,1:] * lmbda / m
      
  return np.hstack((delta1.ravel(order='F'), delta2.ravel(order='F')))

def checkGradient(nn_initial_params,nn_backprop_Params,input_layer_size, hidden_layer_size, num_labels,myX,myy,mylambda=0.):
  myeps = 0.0001
  flattened = nn_initial_params
  flattenedDs = nn_backprop_Params
  n_elems = len(flattened) 
  #Pick ten random elements, compute numerical gradient, compare to respective D's
  for i in range(10):
    x = int(np.random.rand()*n_elems)
    epsvec = np.zeros((n_elems,1))
    epsvec[x] = myeps

    cost_high = nnCostFunc(flattened + epsvec.flatten(),input_layer_size, hidden_layer_size, num_labels,myX,myy,mylambda)
    cost_low  = nnCostFunc(flattened - epsvec.flatten(),input_layer_size, hidden_layer_size, num_labels,myX,myy,mylambda)
    mygrad = (cost_high - cost_low) / float(2*myeps)
    print("Element: {0}. Numerical Gradient = {1:.9f}. BackProp Gradient = {2:.9f}.".format(x,mygrad,flattenedDs[x]))

def predict(theta1, theta2, X, y):
  m = len(y)
  ones = np.ones((m,1))
  a1 = np.hstack((ones, X))
  a2 = sigmoid(a1 @ theta1.T)
  a2 = np.hstack((ones, a2))
  h = sigmoid(a2 @ theta2.T)
  return np.argmax(h, axis = 1)

def predictWAV (theta1, theta2, mfcc):
  htot = np.zeros((theta2.shape[0]));
  for i in range (len(mfcc)):
    a1 = np.hstack(([1], mfcc[i]))
    a2 = sigmoid(a1 @ theta1.T)
    a2 = np.hstack(([1], a2))
    h = sigmoid(a2 @ theta2.T)
    htot += h
  return (np.argmax(htot, axis = 0), htot/len(mfcc));
