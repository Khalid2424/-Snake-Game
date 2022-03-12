import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point
from game.casting.cycle1 import CycleOne
from game.casting.cycle2 import CycleTwo
from game.services.keyboard_service import KeyboardService
from game.scripting.control_cycle1_action import ControlCycleOneAction
from game.scripting.control_cycle2_action import ControlCycleTwoAction
from game.scripting.handle_restart_action import HandleRestartAction



class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the cycles collide with their own segments, or the segments of it's opponent, or the game is over.
    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False
        self._winner = "";
        self._keyboard_service = KeyboardService()
        self._action = HandleRestartAction(self._keyboard_service)

    def execute(self, cast, script):
        """Executes the handle collisions action.
        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:

            self._handle_segment_collision(cast)
            self._handle_game_over(cast, script)
            
        else:
            self._restart(cast, script)


    
    def _handle_segment_collision(self, cast):
        """Sets the game over flag if the cycle collides with one of its segments.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        cycle1 = cast.get_first_actor("cycle1")
        cycle1_head = cycle1.get_segments()[0]
        cycle1_segments = cycle1.get_segments()[1:]
        
        
        cycle2 = cast.get_first_actor("cycle2")
        cycle2_head = cycle2.get_segments()[0]
        cycle2_segments = cycle2.get_segments()[1:]
        
        for isegments in cycle2_segments:
            for segment in cycle1_segments:
                if cycle1_head.get_position().equals(segment.get_position()) or cycle1_head.get_position().equals(isegments.get_position()):
                    self._winner = 2
                    self._is_game_over = True
                    
                #Check head to head collision, deduct 1 point from each
                elif cycle1_head.get_position().equals(cycle2_head.get_position()):
                    self._winner = 3
                    self._is_game_over = True
                 
                    
        for isegments in cycle1_segments:
            for segment in cycle2_segments:
                if cycle2_head.get_position().equals(segment.get_position()) or cycle2_head.get_position().equals(isegments.get_position()):
                    self._winner = 1                   
                                       
                    self._is_game_over = True
                
    def _restart(self, cast, script):
        """When the game is over, this would be the method running in the game loop.
        It takes the cast and script as parameters and renders the white colored cycles without collisions.
        There is an if statement that checks if the user has pressed R to restart the game.
        
        
        Args:
            cast (_type_): _description_
            script (_type_): _description_
        """
        cycle1 = cast.get_first_actor("cycle1")
        segments1 = cycle1.get_segments()

        cycle2 = cast.get_first_actor("cycle2")
        segments2 = cycle2.get_segments()

        for segment in segments1:
            segment.set_color(constants.WHITE)

        for segment in segments2:
            segment.set_color(constants.WHITE)
        
        
        
        
    
        #checks for input  
        restart = script.get_end("input")       
        if restart.get_restart():
            message = cast.get_last_actor("messages")
                
            message.set_text("")

            old_cycle1 = cast.get_first_actor("cycle1")   
            cast.remove_actor("cycle1", old_cycle1)
            cast.add_actor("cycle1", CycleOne())

            old_cycle2 = cast.get_first_actor("cycle2")   
            cast.remove_actor("cycle2", old_cycle2)
            cast.add_actor("cycle2", CycleTwo())

            
            
            script.add_action("input", ControlCycleTwoAction(self._keyboard_service))
            script.add_action("input", ControlCycleOneAction(self._keyboard_service))
            self._action = HandleRestartAction(self._keyboard_service)
            
            
            self._is_game_over = False
            
        else:    pass    
        
        
    def _handle_game_over(self, cast, script):
        """Shows the 'game over' message including the playere that won the round, also applies scores to the appropriate individuals.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        

        if self._is_game_over:
            
            script.add_action("input", self._action)
            
            score1 = cast.get_first_actor("score1")
            score2 = cast.get_first_actor("score2")
            
            message = Actor()
            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y /2)
            position = Point(x, y)
            message.set_position(position)
            
            if self._winner == 1:
                score1.add_points(1)
                message.set_text("Player One Wins! (Press R to continue.)") 
            elif self._winner == 2:
                score2.add_points(1)   
                message.set_text("Player Two Wins! (Press R to continue.)")                 
                
            elif self._winner == 3:
                score1.add_points(-1)                   
                score2.add_points(-1)
                message.set_text("Head On, Both Players Loose! (Press R to continue.)")  
                
            cast.add_actor("messages", message)
                
            

            

    
            self._is_game_over = True