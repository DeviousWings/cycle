import constants
from game.casting.actor import Actor
from game.shared.point import Point


class Cycle(Actor):
    """
    A long limbless reptile.
    
    The responsibility of Cycle is to move itself.

    Attributes:
        _cycle_color - Color of the cycle
    """
    def __init__(self, color, position):
        super().__init__()
        self._cycle_color = color
        # setting cycle positions
        self._segments = []
        self._head = Actor()
        self._head.set_color(color)
        self._head.set_text('@')
        self._head.set_position(position)
        self._segments.append(self._head)
        
        
    def get_segments(self):
        return self._segments

    def move_next(self):
        # Makes the cylces Move
        self._segments[0].move_next()
        # update velocities
        self._tail = Actor()
        self._tail.set_color(self._cycle_color)
        self._tail.set_text('#')
        self._segments.append(self._tail)
        self._tail.set_position(self._head.get_position())
                
        
        """ # move all segments
        for segment in self._segments:
            segment.move_next()
        # update velocities
        for i in range(len(self._segments) - 1, 0, -1):
            trailing = self._segments[i]
            previous = self._segments[i - 1]
            velocity = previous.get_velocity()
            trailing.set_velocity(velocity) """

    def get_head(self):
        return self._segments[0]

    """def grow_tail(self, number_of_segments):
        for i in range(number_of_segments):
            tail = self._segments[-1]
            velocity = tail.get_velocity()
            offset = velocity.reverse()
            position = tail.get_position().add(offset)
            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text("#")
            segment.set_color(constants.GREEN)
            segment.set_color(constants.RED)
            self._segments.append(segment) """

    def turn_head(self, velocity):
        self._segments[0].set_velocity(velocity)
    
    """def _prepare_body(self):
        x = int(constants.MAX_X / 2)
        y = int(constants.MAX_Y / 2)

        for i in range(constants.CYCLE_LENGTH):
            position = Point(x - i * constants.CELL_SIZE, y)
            velocity = Point(1 * constants.CELL_SIZE, 0)
            text = "8" if i == 0 else "#"
            color = constants.YELLOW if i == 0 else constants.GREEN
            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text(text)
            segment.set_color(color)
            self._segments.append(segment) """