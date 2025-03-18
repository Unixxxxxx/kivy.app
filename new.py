from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.popup import Popup
import shutil
import os

UPLOAD_FOLDER = "uploads"
ADMIN_PASSWORD = "admin123"

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

class DocumentUploadPage(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        self.add_widget(Label(text="Upload a Document", font_size=24))
        
        self.file_chooser = FileChooserIconView()
        self.add_widget(self.file_chooser)
        
        self.upload_button = Button(text="Upload File", font_size=20)
        self.upload_button.bind(on_press=self.upload_file)
        self.add_widget(self.upload_button)
        
        self.admin_panel_button = Button(text="Admin Panel", font_size=20)
        self.admin_panel_button.bind(on_press=self.open_admin_panel)
        self.add_widget(self.admin_panel_button)
    
    def upload_file(self, instance):
        selected_file = self.file_chooser.selection
        if selected_file:
            dest_path = os.path.join(UPLOAD_FOLDER, os.path.basename(selected_file[0]))
            shutil.copy(selected_file[0], dest_path)
            self.show_popup("Success", "File uploaded successfully!")
        else:
            self.show_popup("Error", "No file selected.")
    
    def open_admin_panel(self, instance):
        self.admin_popup = AdminLoginPopup()
        self.admin_popup.open()
    
    def show_popup(self, title, message):
        popup = Popup(title=title, content=Label(text=message), size_hint=(0.5, 0.5))
        popup.open()

class AdminLoginPopup(Popup):
    def __init__(self, **kwargs):
        super().__init__(title="Admin Login", size_hint=(0.5, 0.5), **kwargs)
        layout = BoxLayout(orientation='vertical')
        self.label = Label(text="Enter Admin Password:")
        self.password_input = Button(text="Login", font_size=20)
        self.password_input.bind(on_press=self.check_password)
        layout.add_widget(self.label)
        layout.add_widget(self.password_input)
        self.content = layout
    
    def check_password(self, instance):
        self.dismiss()
        self.admin_panel = AdminPanel()
        self.admin_panel.open()

class AdminPanel(Popup):
    def __init__(self, **kwargs):
        super().__init__(title="Admin Panel", size_hint=(0.7, 0.7), **kwargs)
        self.layout = BoxLayout(orientation='vertical')
        self.file_list = FileChooserIconView(path=UPLOAD_FOLDER)
        self.layout.add_widget(self.file_list)
        
        self.delete_button = Button(text="Delete Selected", font_size=20)
        self.delete_button.bind(on_press=self.delete_selected)
        self.layout.add_widget(self.delete_button)
        
        self.content = self.layout
    
    def delete_selected(self, instance):
        selected_files = self.file_list.selection
        for file in selected_files:
            os.remove(file)
        self.file_list._update_files()

class DocumentManagerApp(App):
    def build(self):
        return DocumentUploadPage()

if __name__ == "__main__":
    DocumentManagerApp().run()
