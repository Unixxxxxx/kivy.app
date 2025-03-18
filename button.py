from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.image import Image, AsyncImage
from kivy.uix.floatlayout import FloatLayout

class MyApp(App):
    def build(self):
        layout = FloatLayout()

        # Add an Image from URL using AsyncImage
        img1 = AsyncImage(
            source='https://imgs.search.brave.com/NrlZu-RbjGqH--zt6qRLLqua63hgRZuuRQziGS5ua1U/rs:fit:500:0:0:0/g:ce/aHR0cHM6Ly9waXhs/ci5jb20vaW1hZ2Vz/L2luZGV4L2FpLWlt/YWdlLWdlbmVyYXRv/ci1vbmUud2VicA',
            size_hint=(None,None),
            pos_hint={"center_x": 0.5, "center_y": 0.8}  # Position at the top
        )

        # Add a Local Image
        img = Image(
            source="Garden-Sticks.jpg",  # Replace with your image file
            size_hint=(None,None),
            pos_hint={"center_x": 0.5, "center_y": 0.5}  # Center the local image
        )

        # Add a Button
        btn = Button(
            text='Click Me',
            size_hint=(0.2, 0.1),
            pos_hint={"center_x": 0.5, "center_y": 0.2},  # Below the images
            font_size="24sp"
        )
        btn.bind(on_press=self.btn_press, on_release=self.btn_release)

        # Add widgets to layout
        layout.add_widget(img1)  # Add the online image
        layout.add_widget(img)   # Add the local image
        layout.add_widget(btn)   # Add the button

        return layout

    def btn_press(self, btn):
        print("Button pressed")

    def btn_release(self, btn):
        print("Button released")

# Run the application
MyApp().run()
