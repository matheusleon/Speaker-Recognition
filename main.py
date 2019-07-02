import matplotlib.pyplot as plt
import numpy
import scipy.io.wavfile as wav
import sys

import MFCC
#import cost_function

def printa(signal, figure_name):
  plt.figure(1)
  plt.title(figure_name)
  plt.plot(signal)
  plt.show()

def main():
  sample_rate, signal = wav.read('00001.wav')
  signal = signal[0:int(2 * sample_rate)]

  mfcc = MFCC.main(signal, sample_rate)

  #printa(mfcc, "MFCC")


if __name__ == "__main__":
  sys.exit(main())