from game.scripting.action import Action

# TODO: Implement MoveActorsAction class here! 

# Override the execute(cast, script) method as follows:
class MoveActorsAction(Action):
    """
    An new action that moves all the actors.
    
    The responsibility of MoveActorsAction is to move all the actors that have a velocity greater
    than zero.
    """
    # 1) get all the actors from the cast
    def execute(self, cast, script):
        """Executes the move actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        actors = cast.get_all_actors()
        # 2) loop through the actors
        for actor in actors:
        # 3) call the move_next() method on each actor
            actor.move_next()





