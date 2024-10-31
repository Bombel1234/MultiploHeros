
from View.FirstScreen.components import ScaleLabel, MostVisitedCard
from View.base_screen import BaseScreenView
from kivy.animation import Animation


class FirstScreenView(BaseScreenView):
    def on_enter(self, *args):
        self.generate_cards()

    def generate_cards(self):
        if not self.ids.card_box.children:
            for name_city in self.model.cards_data.keys():
                card = MostVisitedCard(
                    city_name=name_city,
                    source=self.model.cards_data[name_city]
                )
                callback = self.controller.on_tab_most_visited_card_button
                card.bind(on_release=lambda x=card: callback(x))
                self.ids.card_box.add_widget(card)

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


    def model_is_changed(self) -> None:
        """
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """

