import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class ToDoListApp(App):
    def build(self):
        # Create a main layout for the app
        self.main_layout = BoxLayout(orientation='vertical')
        
        # Create a label for the app title
        self.title_label = Label(text='To-Do List', font_size=24)
        self.main_layout.add_widget(self.title_label)
        
        # Create a list of to-do items
        self.todo_items = []
        
        # Create a layout to hold the to-do items
        self.todo_layout = BoxLayout(orientation='vertical')
        self.main_layout.add_widget(self.todo_layout)
        
        # Create a text input and add button for adding new to-do items
        self.add_layout = BoxLayout(orientation='horizontal')
        self.add_text_input = TextInput()
        self.add_button = Button(text='Add')
        self.add_button.bind(on_release=self.add_todo_item)
        self.add_layout.add_widget(self.add_text_input)
        self.add_layout.add_widget(self.add_button)
        self.main_layout.add_widget(self.add_layout)
        
        return self.main_layout
        
    def add_todo_item(self, instance):
        # Create a new label for the to-do item
        todo_item = Label(text=self.add_text_input.text, font_size=16)
        
        # Add the to-do item to the list and layout
        self.todo_items.append(todo_item)
        self.todo_layout.add_widget(todo_item)
        
        # Clear the text input
        self.add_text_input.text = ''

if __name__ == '__main__':
    ToDoListApp().run()
