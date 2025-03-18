from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

Window.clearcolor=(1,0,0,1)
Window.size=(330,520)

class MyButton(App):
    def build(self):
        layout = BoxLayout(orientation="vertical",spacing=20,padding=50)
        btn = Button(text='Click_me')
        btn1 = Button(text='Click_me1')
        layout.add_widget(btn)
        layout.add_widget(btn1)
        return layout
MyButton().run()