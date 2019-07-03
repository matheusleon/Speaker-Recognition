import MFCC
import numpy as np
import scipy.io.wavfile as wav
from scipy.io import loadmat
import sounddevice as sd
import ml
import os
import glob


theta1 = loadmat('ml.mat')['theta1'];
theta2 = loadmat('ml.mat')['theta2'];

Xtest = [];
ytest = [];

nspeakers = theta2.shape[0];
folders = os.listdir("wav")
for i in range(5):
  folder = folders[i];
  print(folder)
  files = [f for f in glob.glob("wav/"+folder + "/" + "**/*.wav", recursive=True)]
  sztraining = int(len(files)*0.6);
  for fid in range(sztraining, len(files)):
    sample_rate, signal = wav.read(files[fid])
    signal = signal[0:int(2 * sample_rate)]
    mfcc = MFCC.main(signal, sample_rate)
    Xtest.append(mfcc)
    ytest.append(i)
    
ytest = np.array(ytest)
Xtest = np.array(Xtest)

pred = [];
for i in range(len(Xtest)):
  pred.append(ml.predictWAV(theta1, theta2, Xtest[i])[0])
print(np.mean(pred == ytest.flatten()) * 100)


signal = []
sample_rate = 16000
while True:
  cmd = input();
  if cmd == "record":
    seconds = 14
    print("recording...")
    signal = sd.rec(int(seconds * sample_rate), samplerate = sample_rate, channels = 1)
    sd.wait()
  elif cmd == "who":
    if not len(signal):
      print("no signal")
      continue
    sd.play(signal, sample_rate)
    
    signal = signal[0:int(2 * sample_rate)]
    mfcc = MFCC.main(signal, sample_rate)
    
    mlres = ml.predictWAV(theta1, theta2, mfcc)
    
    print("user id: {}".format(mlres[0]))
  else:
    print("not found.")
  
  
