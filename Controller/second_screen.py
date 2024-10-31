import importlib

import View.SecondScreen.second_screen

# We have to manually reload the view module in order to apply the
# changes made to the code on a subsequent hot reload.
# If you no longer need a hot reload, you can delete this instruction.
importlib.reload(View.SecondScreen.second_screen)


class SecondScreenController:
    """
    The `SecondScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model):
        self.model = model  # Model.second_screen.SecondScreenModel
        self.view = View.SecondScreen.second_screen.SecondScreenView(
            controller=self,
            model=self.model)

    def on_tab_back_toolbar_button(self):
        self.view.manager_screens.current = 'first screen'

    def get_view(self) -> View.SecondScreen.second_screen:
        return self.view
