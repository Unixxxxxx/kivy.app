import random
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.animation import Animation
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse

class Token(Widget):
    def __init__(self, color, **kwargs):
        super().__init__(**kwargs)
        self.color = color
        self.position = 0  # Start position (not yet on board)
        with self.canvas:
            Color(*self.get_color())
            self.token = Ellipse(size=(40, 40), pos=self.pos)
    
    def get_color(self):
        colors = {"Red": (1, 0, 0), "Blue": (0, 0, 1), "Green": (0, 1, 0), "Yellow": (1, 1, 0)}
        return colors.get(self.color, (1, 1, 1))
    
    def move(self, new_pos):
        anim = Animation(x=new_pos[0], y=new_pos[1], duration=0.5)
        anim.start(self)

class LudoGame(App):
    def build(self):
        self.players = ["Red", "Blue", "Green", "Yellow"]
        self.tokens = {color: [Token(color) for _ in range(4)] for color in self.players}
        self.current_player_index = 0
        
        self.layout = BoxLayout(orientation='vertical')
        
        self.info_label = Label(text=f"{self.players[self.current_player_index]}'s Turn", font_size=24)
        self.layout.add_widget(self.info_label)
        
        self.dice_label = Label(text="Roll the dice!", font_size=32)
        self.layout.add_widget(self.dice_label)
        
        self.dice_image = Image(source="dice_1.png")
        self.layout.add_widget(self.dice_image)
        
        self.roll_button = Button(text="Roll Dice", font_size=24)
        self.roll_button.bind(on_press=self.roll_dice)
        self.layout.add_widget(self.roll_button)
        
        self.board = GridLayout(cols=8, rows=8)
        for _ in range(64):
            self.board.add_widget(Button(text="", disabled=True))
        self.layout.add_widget(self.board)
        
        return self.layout
    
    def roll_dice(self, instance):
        dice_value = random.randint(1, 6)
        self.dice_label.text = f"{self.players[self.current_player_index]} rolled: {dice_value}"
        self.dice_image.source = f"dice_{dice_value}.png"
        
        Clock.schedule_once(lambda dt: self.move_token(dice_value), 1)
    
    def move_token(self, dice_value):
        player = self.players[self.current_player_index]
        
        for token in self.tokens[player]:
            if token.position + dice_value <= 57:
                old_pos = token.position
                token.position += dice_value
                token.move(self.get_board_position(token.position))
                break
        
        if all(t.position == 57 for t in self.tokens[player]):
            self.info_label.text = f"{player} Wins!"
            self.roll_button.disabled = True
        else:
            self.current_player_index = (self.current_player_index + 1) % 4
            self.info_label.text = f"{self.players[self.current_player_index]}'s Turn"
    
    def get_board_position(self, pos):
        return (pos * 10, pos * 10)  # Placeholder, should map to actual board grid

if __name__ == "__main__":
    LudoGame().run()
