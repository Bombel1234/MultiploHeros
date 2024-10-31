import importlib
import View.FirstScreen.first_screen
from View.FirstScreen.components import MostVisitedCard

# We have to manually reload the view module in order to apply the
# changes made to the code on a subsequent hot reload.
# If you no longer need a hot reload, you can delete this instruction.
importlib.reload(View.FirstScreen.first_screen)


class FirstScreenController:
    """
    The `FirstScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model):
        self.model = model  # Model.first_screen.FirstScreenModel
        self.view = View.FirstScreen.first_screen.FirstScreenView(controller=self, model=self.model)

    def on_tab_most_visited_card_button(self, instance_card: MostVisitedCard) -> None:
        city_name = instance_card.city_name
        self.view.manager_screens.current_heroes = [
            f"hero_name_beaches_{city_name}",
            f"hero_image_city_{city_name}",
            f"hero_name_city_{city_name}",
            f"hero_button_plus_{city_name}",
            f"hero_navigate_{city_name}"
        ]
        self.view.ids.hero_name_beaches.tag = f"hero_name_beaches_{city_name}"
        self.view.ids.hero_navigate.tag = f"hero_navigate_{city_name}"

        self.view.manager_screens.get_screen('second screen').current_city = (
            city_name
        )
        self.view.manager_screens.current = 'second screen'


    def get_view(self) -> View.FirstScreen.first_screen:
        return self.view
