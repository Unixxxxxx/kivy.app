from kivy.app import App
from kivy.uix.label import Label 
from kivy.core.window import Window
Window.clearcolor=(1,1,1,1)

class AmulApp(App):
    def build(self):
        label= Label(text="Hello!", font_size='120sp',bold=True, italic=True,color=(1,0,0,1)) 
        return label   
AmulApp().run()
