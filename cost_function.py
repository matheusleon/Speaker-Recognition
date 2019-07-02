import math

def sigmoid(x):
  return 1 / (1 + math.exp(-x))

def cost_function(theta, x, y, lambda):
    h_theta = sigmoid(x * theta)
    