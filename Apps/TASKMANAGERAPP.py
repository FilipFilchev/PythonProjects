
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
class TaskManagerApp(App):
    def build(self):
        # main layout for the app
        self.main_layout = BoxLayout(orientation='vertical')
        
        # label for the app title
        self.title_label = Label(text='Task Manager', font_size=30)
        self.main_layout.add_widget(self.title_label)
        
        # list of task items
        self.task_items = []
        
        # layout to hold the task items
        self.task_layout = BoxLayout(orientation='vertical')
        self.main_layout.add_widget(self.task_layout)
        
        # text input and add button for adding new task items
        self.add_text_input = TextInput()
        self.add_layout = BoxLayout(orientation='horizontal')
        self.add_button = Button(text='Insert Task')
        self.add_button.bind(on_release=self.add_task_item)
        self.add_layout.add_widget(self.add_text_input)
        self.add_layout.add_widget(self.add_button)
        self.main_layout.add_widget(self.add_layout)
        
        return self.main_layout
        
    def add_task_item(self, instance):
        # Create a new label for the task item
        task_item = Label(text=self.add_text_input.text, font_size=20)
        
        # Add the task item to the list and layout
        self.task_items.append(task_item)
        self.task_layout.add_widget(task_item)
        
        # Clear the text input
        self.add_text_input.text = ''

if __name__ == '__main__':
    TaskManagerApp().run()
