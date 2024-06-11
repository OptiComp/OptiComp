Change config class to be same as search_space
change comment to be visible outside '''comment'''
^^^ Dit kan ook onder config
je kan alle wrappers in de init zetten 


enum is class with only variables

gooi alles in classes implaats van dynamic import
def import():
	import wrapper
	return wrapper

verwijder wrappers class to only be functions

<!-- verwijder __init__s -->

Plaats import in init file in opticomp, dan kan je daar direct uit importeren

<!-- Remove import comments -->

Comments that explain why code does something > comments that explain what code does

Keep comments short

def init(self, objective, search_space: dict[str, tuple[int, int]]):
Zet in string als je hier error bij krijgt 

def test() -> int: # Tells the user what it returns





    library_version = "Unknown"     # Default library version that wrapper is based on
    default_direction :str

    __objective: str



# kan niet worden geroepen als normale class
from abc import ABC
class WrapperInterface(ABC):



# ========================
    library_version: str    # Default library version that wrapper is based on
    default_direction: str   # Default direction

    __objective: str

    def __init__(self, library_version: str, default_direction: str, objective, search_space):
        self.library_version = library_version
        self.default_direction = default_direction
        self.__objective = objective
        self.__search_space = search_space
# ========================
 # in wrapper
    def __init__(self, objective, search_space):
        super().__init__("1.4.3", "maximize", objective, search_space)
# ========================


wrapper_interface() hoeft geen ()

from typing import Callable
objective: Callable[[list[int]], int]


Multiprocessing voor verschillende processes op meerdere cores

str | WrapperInstance

Use logging library instead of prints
loggers kunnen 'children' loggers hebben, dan kan je ook children andere levels zetten ofzo


Zet eventueel alle outputs in een class. Dan kan je makkelijker alle. 
dan krijg je ook hints wat er in staat en eventueel helpen methods in the method. 

hou local variable naming lower case (zoals OptSuite)

<!-- kijk of er ruff codes zijn voor naming conventions (lower case in local classes)(uper case in classes) -->



python read the docs. Dan kan je ook automatisch dingen laten genereren

contributing.md file for contributions

Github dingen om sommige dingen automatisch te testen.
zoals of alles ruff regels volgt bij push
Of unit tests die een stukje code runnen

Colored info boxes on header. vraag chat gpt. Shield.io of travis-ci.io

Een bestand met een basic richting voor optimiser soort en use-case




    # TODO implement this
    def get_best():
        raise NotImplementedError()



Zoek contact met andere optimizer met de vraag op de readme 'how does it compare to other optimizers'
Zo krijg je soort van reclame
