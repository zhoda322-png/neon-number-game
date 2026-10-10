from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from random import randint

class NeonGame(App):
    def build(self):
        self.target = randint(1, 20)
        self.tries = 0

        layout = BoxLayout(
            orientation="vertical",
            padding=20,
            spacing=15
        )

        layout.add_widget(Label(
            text="[b]NEON NUMBER[/b]",
            markup=True,
            font_size="30sp",
            color=(0, 1, 1, 1)
        ))

        self.info = Label(
            text="Guess a number from 1 to 20",
            font_size="20sp"
        )
        layout.add_widget(self.info)

        self.entry = TextInput(
            hint_text="Type a number",
            input_filter="int",
            multiline=False,
            font_size="24sp",
            size_hint_y=0.7
        )
        layout.add_widget(self.entry)

        guess = Button(
            text="GUESS",
            font_size="22sp",
            background_color=(0, 0.6, 0.8, 1)
        )
        guess.bind(on_press=self.check_guess)
        layout.add_widget(guess)

        self.status = Label(text="Good luck!")
        layout.add_widget(self.status)

        reset = Button(
            text="NEW GAME",
            font_size="18sp"
        )
        reset.bind(on_press=self.reset_game)
        layout.add_widget(reset)

        return layout

    def check_guess(self, button):
        if not self.entry.text:
            self.status.text = "Enter a number!"
            return

        number = int(self.entry.text)
        self.tries += 1

        if number < self.target:
            self.info.text = "Too low! Try higher."
        elif number > self.target:
            self.info.text = "Too high! Try lower."
        else:
            self.info.text = "YOU WON! Number: " + str(self.target)

        self.status.text = "Tries: " + str(self.tries)
        self.entry.text = ""

    def reset_game(self, button):
        self.target = randint(1, 20)
        self.tries = 0
        self.info.text = "Guess a number from 1 to 20"
        self.status.text = "New game!"
        self.entry.text = ""

NeonGame().run()