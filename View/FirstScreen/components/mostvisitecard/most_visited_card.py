from kivy.properties import StringProperty
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.clock import Clock
from kivy.animation import Animation

from View.FirstScreen.components import ScaleLabel


class MostVisitedCard(MDBoxLayout):
    city_name = StringProperty()
    source = StringProperty()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.register_event_type('on_release')

    def on_city_name(self, instance, value: str) -> None:
        self.create_tags(value)

    def create_tags(self, tag: str) -> None:
        def create_tags(*args):
            self.ids.hero_name_city.tag = f"hero_name_city_{tag}"
            self.ids.hero_image_city.tag = f"hero_image_city_{tag}"
            self.ids.hero_button_plus.tag = f"hero_button_plus_{tag}"
        Clock.schedule_once(create_tags)

    def hero_name_beaches_transform(
            self,
            hero_from_children_widget: ScaleLabel,
            duration: float,
            scale: float,
            x: float

    ):
        Animation(
            scale_value_x=scale,
            scale_value_y=scale,
            duration=duration,
            x=x
        ).start(hero_from_children_widget)

    def on_release(self, *args):
        """
        Handle
        """