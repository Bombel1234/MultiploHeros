
"""
Script for managing hot reloading of the project.
For more details see the documentation page -

https://kivymd.readthedocs.io/en/latest/api/kivymd/tools/patterns/create_project/

To run the application in hot boot mode, execute the command in the console:
DEBUG=1 python main.py
"""

import importlib
import os

from kivy import Config

# from PIL import ImageGrab
from kivymd.uix.transition import MDFadeSlideTransition

# TODO: You may know an easier way to get the size of a computer display.
# resolution = ImageGrab.grab().size
# Change the values of the application window size as you need.
# Config.set("graphics", "height", resolution[1])
# Config.set("graphics", "width", "400")

from kivy.core.window import Window

# Place the application window on the right side of the computer screen.
# Window.top = 0
# Window.left = resolution[0] - Window.width

from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager


class MultiploHeros(MDApp):
    KV_DIRS = [os.path.join(os.getcwd(), "View")]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.manager_screens = None

    def build_app(self) -> MDScreenManager:
        """
        In this method, you don't need to change anything other than the
        application theme.
        """

        import View.screens

        self.manager_screens = MDScreenManager(transition=MDFadeSlideTransition())
        # Window.bind(on_key_down=self.on_keyboard_down)
        importlib.reload(View.screens)
        screens = View.screens.screens

        for i, name_screen in enumerate(screens.keys()):
            model = screens[name_screen]["model"]()
            controller = screens[name_screen]["controller"](model)
            view = controller.get_view()
            view.manager_screens = self.manager_screens
            view.name = name_screen
            self.manager_screens.add_widget(view)

        return self.manager_screens

    # def on_keyboard_down(self, window, keyboard, keycode, text, modifiers) -> None:

        # if "meta" in modifiers or "ctrl" in modifiers and text == "r":
        #     self.rebuild()


MultiploHeros().run()



