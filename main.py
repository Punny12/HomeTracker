from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.properties import StringProperty
from kivy.lang import Builder


class HomePage(Screen):
    pass


class TransactionPage(Screen):
    pass


class SettingsPage(Screen):
    pass


class IndexPage(BoxLayout):
    label_to_update = StringProperty("")

    def display_home_page(self):
        w = HomePage()
        self.add_widget(w)

    def display_transaction_page(self):
        self.label_to_update = "Trans"

    def display_settings_page(self):
        self.label_to_update = "sett"



class IndexApp(App):
    Window.size = (350, 650)
    Window.background_color: (1, 1, 1, 1)
    kv_directory = "templates"

    def build(self):
        return IndexPage()


if __name__ == "__main__":
    IndexApp().run()
