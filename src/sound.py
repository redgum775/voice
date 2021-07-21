import win32com.client as wincl

voice = wincl.Dispatch("SAPI.SpVoice")

def speak(text):
  voice.Speak(text)
  print('Speaked: ' + text)

def setting(volume, rate):
  if 0 <= volume & volume <= 100:
    voice.Volume = volume
  elif volume == None:
    print('Voice: No parameter specified.')
  else:
    print('Voice: Incorrect parameter was specified.')

  if -10 <= rate & rate <= 10:
    voice.Rate = rate
  elif rate == None:
    print('Rate: No parameter specified.')
  else:
    print('Rate: Incorrect parameter was specified.')

