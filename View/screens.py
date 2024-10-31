# The screens dictionary contains the objects of the models and controllers
# of the screens of the application.


from Model.first_screen import FirstScreenModel
from Controller.first_screen import FirstScreenController
from Model.second_screen import SecondScreenModel
from Controller.second_screen import SecondScreenController

screens = {
    "first screen": {
        "model": FirstScreenModel,
        "controller": FirstScreenController,
    },

    "second screen": {
        "model": SecondScreenModel,
        "controller": SecondScreenController,
    },
}