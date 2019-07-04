import argparse
import queue
import sys
import matplotlib.pyplot as plt
import numpy as np
import sounddevice as sd
import _thread
from matplotlib.animation import FuncAnimation
from scipy.io.wavfile import write


window = float(200)
interval = float(50)
sample_rate = 16000
downsample = int(10)
channels = [1]
blocksize = 0

mapping = [c - 1 for c in channels] 
q = queue.Queue()

def audio_callback(indata, frames, time, status):
  if status:
    print(status, file=sys.stderr)
  # Fancy indexing with mapping creates a (necessary!) copy:
  q.put(indata[::downsample, mapping])


def update_plot(frame):
  global plotdata, lines
  while True:
    try:
      data = q.get_nowait()
    except queue.Empty:
      break
    shift = len(data)
    plotdata = np.roll(plotdata, -shift, axis=0)
    plotdata[-shift:, :] = data
  for column, line in enumerate(lines):
    line.set_ydata(plotdata[:, column])
  return lines

###############
def plot_audio(thread_name):
  length = int(window * sample_rate / (1000 * downsample))

  global plotdata, lines
  plotdata = np.zeros((length, len(channels)))

  fig, ax = plt.subplots()
  lines = ax.plot(plotdata)

  ax.axis((0, len(plotdata), -1, 1))
  ax.set_yticks([0])
  ax.yaxis.grid(True)
  ax.tick_params(bottom=False, top=False, labelbottom=False, right=False, left=False, labelleft=False)
  fig.tight_layout(pad=0)

  stream = sd.InputStream(device=sd.default.device, channels=max(channels), samplerate=sample_rate, callback=audio_callback)
<<<<<<< HEAD
  print("ky")
  ani = FuncAnimation(fig, update_plot, interval=interval, blit=True)
  print("xk")
  with stream:
    plt.show()
  print("safe")
  stream.close()
  while (not stream.stopped):
    continue
  print("ok")
  return 0
=======
  ani = FuncAnimation(fig, update_plot, interval=interval, blit=True)

  with stream:
    plt.show()

>>>>>>> 82babe8e99bd391de00e4b49ab8d8744df7f7374
def record_audio(seconds):
  print('Vai comecar a gravar o audio')
  eita = sd.rec(int(seconds * sample_rate), samplerate = sample_rate, channels = 1)
  sd.wait()
  write('output.wav', sample_rate, eita)
  print('Terminou de gravar')

def record(seconds):
  _thread.start_new_thread (plot_audio, ("plot_audio_thread", ))
  signal = record_audio(seconds)
  return signal
<<<<<<< HEAD
=======
  
if __name__ == "__main__":
  sys.exit(main()) 
>>>>>>> 82babe8e99bd391de00e4b49ab8d8744df7f7374
