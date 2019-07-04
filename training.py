import numpy as np
import scipy.io.wavfile as wav
from scipy.io import savemat
import scipy.optimize as opt
import sys
import os
import glob

import MFCC
import ml

def main():
  folders = os.listdir("wav")
  X = [];
  y = [];
  Xtest = [];
  ytest = [];
  nspeakers = 5;
  #feature extraction
  
  for i in range(nspeakers):
    folder = folders[i];
    files = [f for f in glob.glob("wav/"+folder + "/" + "**/*.wav", recursive=True)]
    
    sztraining = int(len(files)*0.6);
    for fid in range(sztraining):
      sample_rate, signal = wav.read(files[fid])
      mfcc = MFCC.main(signal, sample_rate)
      for j in range (len(mfcc)):
        X.append([])
        for k in range (len(mfcc[j])):
          X[-1].append(mfcc[j][k])
        y.append(i)
    for fid in range(sztraining, len(files)):
      sample_rate, signal = wav.read(files[fid])
      mfcc = MFCC.main(signal, sample_rate)
      for j in range (len(mfcc)):
        Xtest.append([])
        for k in range (len(mfcc[j])):
          Xtest[-1].append(mfcc[j][k])
        ytest.append(i)

  y = np.array(y)
  X = np.array(X)
  ytest = np.array(ytest)
  Xtest = np.array(Xtest)
  input_layer_size = 390
  hidden_layer_size = 200
  num_labels = nspeakers
  
  lmbda = 1
  initial_theta1 = ml.randInitializeWeights(input_layer_size, hidden_layer_size)
  initial_theta2 = ml.randInitializeWeights(hidden_layer_size, num_labels)
  nn_initial_params = np.hstack((initial_theta1.ravel(order='F'), initial_theta2.ravel(order='F')))
  
  print(ml.nnCostFunc(nn_initial_params, input_layer_size, hidden_layer_size, num_labels, X, y, lmbda))
  theta_opt = opt.fmin_cg(maxiter = 50, f = ml.nnCostFunc, x0 = nn_initial_params, fprime = ml.nnGrad, args = (input_layer_size, hidden_layer_size, num_labels, X, y.flatten(), lmbda))
  
  theta1_opt = np.reshape(theta_opt[:hidden_layer_size*(input_layer_size+1)], (hidden_layer_size, input_layer_size+1), 'F')
  theta2_opt = np.reshape(theta_opt[hidden_layer_size*(input_layer_size+1):], (num_labels, hidden_layer_size+1), 'F')
  
  pred = ml.predict(theta1_opt, theta2_opt, Xtest, ytest)
  print(np.mean(pred == ytest.flatten()) * 100)
  savemat('ml.mat', {'theta1' : theta1_opt, 'theta2': theta2_opt});
  
if __name__ == "__main__":
  sys.exit(main())
  
  
  
  
  
  
