from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class CalculatorApp(App):
    def build(self):
        self.operand = ""
        self.result = TextInput(font_size=32, readonly=True, halign="right", multiline=False)
        
        layout = BoxLayout(orientation="vertical")
        layout.add_widget(self.result)
        
        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["C", "0", "=", "+"]
        ]
        
        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                button = Button(text=label, font_size=24)
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            layout.add_widget(h_layout)
        
        return layout
    
    def on_button_press(self, instance):
        text = instance.text
        
        if text == "C":
            self.operand = ""
            self.result.text = ""
        elif text == "=":
            try:
                self.result.text = str(eval(self.operand))
            except:
                self.result.text = "Error"
            self.operand = self.result.text
        else:
            self.operand += text
            self.result.text = self.operand

if __name__ == "__main__":
    CalculatorApp().run()
