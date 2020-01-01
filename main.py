import kivy
kivy.require('1.11.1')

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout 
from kivy.uix.button import Button 
from kivy.uix.textinput import TextInput
  




class MyApp(App):

    def build(self):
        self.title = "DnD App"
        layout = GridLayout(cols = 1)
        layout.add_widget(Button(text = 'Hello 1'))
        layout.add_widget(Button(text = 'Hello 1'))
        layout.add_widget(TextInput(text='Hello World', multiline=False))
        layout.add_widget(TextInput(text='Hello World', multiline=False))
        

  
        return layout


if __name__ == '__main__':
    MyApp().run()

