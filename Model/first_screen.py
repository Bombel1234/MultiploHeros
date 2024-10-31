from Model.base_model import BaseScreenModel


class FirstScreenModel(BaseScreenModel):
    """
    Implements the logic of the
    :class:`~View.first_screen.FirstScreen.FirstScreenView` class.
    """
    def __init__(self):
        self.cards_data = {
            "Canada": 'assets/images/borszcz.jpg',
            "Dubai": 'assets/images/pirogi.jpg',
            "Germany": 'assets/images/salat.jpg',
            "London": 'assets/images/slodke.jpg'
        }