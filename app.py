import MFCC
import audio
import numpy as np
import scipy.io.wavfile as wav
from scipy.io import loadmat
import sounddevice as sd
import threading
import ml
import os
import sys
import glob

def main():
  theta1 = loadmat('ml.mat')['theta1'];
  theta2 = loadmat('ml.mat')['theta2'];

<<<<<<< HEAD
  """Xtest = [];
  ytest = [];
=======

"""
theta1 = loadmat('ml.mat')['theta1'];
theta2 = loadmat('ml.mat')['theta2'];
>>>>>>> 82babe8e99bd391de00e4b49ab8d8744df7f7374

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
  """

<<<<<<< HEAD
  signal = []
  sample_rate = 16000

  th = threading.Thread(target = audio.plot_audio, args = (1,));
  th.start();
  while True:
    cmd = input("Digite um comando");
    print("CMDZAO = " + str(cmd))
    if cmd == "record":
      seconds = 5
      print("recording...")
      print('AQUI\n')
      signal = sd.rec(int(seconds * sample_rate), samplerate = sample_rate, channels = 1)
      sd.wait()
      print('safe')
    elif cmd == "who":
      if not len(signal):
        print("no signal")
        continue
      sd.play(signal, sample_rate)
      
      signal = signal[0:int(2 * sample_rate)]
      mfcc = MFCC.main(signal, sample_rate)
      
      mlres = ml.predictWAV(theta1, theta2, mfcc)
      
      print("user id: {}".format(mlres[0]))
    elif cmd == "exit":
      break
    else:
      print("not found.")
  th.join()
  return 0
if __name__ == "__main__":
  sys.exit(main()) 
=======
pred = [];
for i in range(len(Xtest)):
  pred.append(ml.predictWAV(theta1, theta2, Xtest[i])[0])
print(np.mean(pred == ytest.flatten()) * 100)
"""

signal = []
sample_rate = 16000
while True:
  cmd = input("Digite um comando");
  print("CMDZAO = " + str(cmd))
  if cmd == "record":
    seconds = 14
    print("recording...")
    #_thread.start_new_thread (record_audio, ("plot_audio_thread", ))
    #print('AQUI\n')
    #signal = record_audio(seconds)
    #signal = sd.rec(int(seconds * sample_rate), samplerate = sample_rate, channels = 1)
    #sd.wait()
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
  
  
>>>>>>> 82babe8e99bd391de00e4b49ab8d8744df7f7374
