from kivy.app import App
from kivy.uix.label import Label 

class Myapp(App):
    def build(self):
        label= Label(text="Hello!", font_size='120sp',bold=True, italic=True,color=(1,0,0,1)) 
        return label   
Myapp().run()
