from kivy.app import App
from kivy.uix.button import Button 

class buttonApp(App):
    def build(self):
        # btn = Button(text='Clickme')
        return Button(text='Click Me', size_hint=(0.3,0.4,),pos_hint={"center_x":0.5,"center_y":0.5})
buttonApp().run()