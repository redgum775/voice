import win32com.client as wincl

class Sound:
  def __init__(self):
    self.voice = wincl.Dispatch("SAPI.SpVoice")

  def speak(self, text):
    print(f'Speaked: {text} [Volume: {self.voice.Volume}] [Rate: {self.voice.Rate}]')
    self.voice.Speak(text)

  # default volume=100(0~100), rate=0(-10~10)
  def setting(self, volume=None, rate=None):
    if volume is not None:
      if 0 <= volume & volume <= 100:
        self.voice.Volume = volume
        print(f'Voice: Volume changed to {volume}.')
      else:
        print('Voice: Incorrect parameter was specified.')

    if rate is not None:
      if -10 <= rate & rate <= 10:
        self.voice.Rate = rate
        print(f'Voice: Rate changed to {rate}.')
      else:
        print('Rate: Incorrect parameter was specified.')

if __name__ == "__main__":
  sound = Sound()
  sound.setting(100, 2)
  sound.speak("おはよう")