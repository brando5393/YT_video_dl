import downloader
from screen import Screen
from kivy.app import App


class Program(App):
  def build(self):
    # this function returns the "top-level" component of the app all other components must be children
    self.title="YouTube Video Downloader"
    return Screen

if __name__ == "__main__":
  Program().run()