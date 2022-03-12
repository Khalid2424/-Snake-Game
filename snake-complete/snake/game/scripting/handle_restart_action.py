import constants

from game.scripting.action import Action
from game.shared.point import Point


class HandleRestartAction(Action):
    """
    An input action that controls cycle2.
    
    The responsibility of ControlCycleTwoAction is to get the direction and move cycle2 in that direction.
    Attributes:
        _keyboard_service (KeyboardService): An instance of KeyboardService.
    """

    def __init__(self, keyboard_service):
        """Constructs a new ControlCycleTwoAction using the specified KeyboardService.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
        """
        self._keyboard_service = keyboard_service
        
        self._restart = False

    def execute(self, cast, script):
        """Executes the control cycle2 action.
        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        # restart
        if self._keyboard_service.is_key_down('r'):
            self._restart = True
            
            
            
        
    def get_restart(self):
        return self._restart