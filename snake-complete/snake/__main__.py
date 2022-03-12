from game.casting.cast import Cast
from game.casting.cycle1_score import Score1
from game.casting.cycle2_score import Score2
from game.casting.cycle1 import CycleOne
from game.casting.cycle2 import CycleTwo
from game.scripting.script import Script
from game.scripting.control_cycle1_action import ControlCycleOneAction
from game.scripting.control_cycle2_action import ControlCycleTwoAction
from game.scripting.move_actors_action import MoveActorsAction
from game.scripting.handle_collisions_action import HandleCollisionsAction
from game.scripting.draw_actors_action import DrawActorsAction
from game.directing.director import Director
from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService
from game.scripting.grow_trail_action import GrowTrailAction

def main():
    
    # create the cast
    cast = Cast()
    cast.add_actor("cycle1", CycleOne())
    cast.add_actor("cycle2", CycleTwo())
    cast.add_actor("score1", Score1())
    cast.add_actor("score2", Score2())
    
   
    # start the game
    keyboard_service = KeyboardService()
    video_service = VideoService()

    script = Script()
    script.add_action("input", ControlCycleOneAction(keyboard_service))
    script.add_action("input", ControlCycleTwoAction(keyboard_service))
    
    script.add_action("update", MoveActorsAction())
    script.add_action("update", GrowTrailAction())
    script.add_action("update", HandleCollisionsAction())
    script.add_action("output", DrawActorsAction(video_service))
    
    director = Director(video_service)
    director.start_game(cast, script)


if __name__ == "__main__":
    main()
