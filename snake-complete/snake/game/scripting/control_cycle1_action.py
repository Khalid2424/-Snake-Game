import constants
from game.casting.cycle1 import CycleOne
from game.scripting.action import Action
from game.shared.point import Point


class ControlCycleOneAction(Action):
    """
    An input action that controls cycle1.
    
    The responsibility of ControlCycleOneAction is to get the direction and move cycle1 in that direction.
    Attributes:
        _keyboard_service (KeyboardService): An instance of KeyboardService.
    """

    def __init__(self, keyboard_service):
        """Constructs a new ControlCycleOneAction using the specified KeyboardService.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
        """
        self._keyboard_service = keyboard_service
        self._direction = Point(0, constants.CELL_SIZE)
        #self._direction = Point(0, 0)

    def execute(self, cast, script):
        """Executes the control cycle1 action.
        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        # left
        if self._keyboard_service.is_key_down('a'):
            self._direction = Point(-constants.CELL_SIZE, 0)
        
        # right
        if self._keyboard_service.is_key_down('d'):
            self._direction = Point(constants.CELL_SIZE, 0)
        
        # up
        if self._keyboard_service.is_key_down('w'):
            self._direction = Point(0, -constants.CELL_SIZE)
        
        # down
        if self._keyboard_service.is_key_down('s'):
            self._direction = Point(0, constants.CELL_SIZE) 

        cycle1 = cast.get_first_actor("cycle1")
        cycle1.turn_head(self._direction)