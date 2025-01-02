from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager


class Battel(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = 'Battel'


class Menu(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = 'Menu'


class MAIN_WIDGET(MDScreenManager):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Application(MDApp):
    def build(self):
        self.main_widget = MAIN_WIDGET()
        return self.main_widget


if __name__ == '__main__':
    Application().run()
