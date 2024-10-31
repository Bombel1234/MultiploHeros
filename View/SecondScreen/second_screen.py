from kivy.properties import StringProperty

from View.base_screen import BaseScreenView


class SecondScreenView(BaseScreenView):
    current_city = StringProperty()

    def on_current_city(self, instance, value) -> None:
        self.ids.hero_name_beaches.tag = f"hero_name_beaches_{value}"
        self.ids.hero_image_city.tag = f"hero_image_city_{value}"
        self.ids.hero_name_city.tag = f"hero_name_city_{value}"
        self.ids.hero_button_plus.tag = f"hero_button_plus_{value}"
        self.ids.hero_navigate.tag = f"hero_navigate_{value}"

    def model_is_changed(self) -> None:
        """
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """
