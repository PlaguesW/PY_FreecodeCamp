import random
import copy

class Hat:
    def __init__(self, **kwargs):
        """
        While creating a Hat object all params ( kwargs ) are a color
        and the number of balls of that color.
        """
        self.contents = []
        for color, count in kwargs.items():
            for _ in range(count):
                self.contents.append(color)

    def draw(self, num_balls):
        """
        Extract and removes num_balls randomly from self.contents. 
        If num_balls bigger or equal len(self.contents), return all balls 
        and clears Hat.
        Returns a list of the colors of extracted balls.
        """
        if num_balls >= len(self.contents):
            drawn = self.contents[:]
            self.contents.clear()
            return drawn

        drawn = []
        for _ in range(num_balls):
            index = random.randrange(len(self.contents))
            drawn.append(self.contents.pop(index))
        return drawn


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    """
    Performs num_experiments experiments:
1) Copy the original hat (so as not to spoil the original).
2) Extract num_balls_drawn balls from the copy.
3) Check if the extracted set contains at least each required
color (from expected_balls).

Returns the approximate probability of (M / num_experiments),
where M is the number of experiments in which it was possible to obtain at least the required number of balls of each color from expected_balls.
    """
    success_count = 0

    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        drawn_balls = hat_copy.draw(num_balls_drawn)

        # Count the extracted balls be color
        counts = {}
        for color in drawn_balls:
            counts[color] = counts.get(color, 0) + 1
        
        # Check if there is enough of each expected color
        success = True
        for color, needed in expected_balls.items():
            if counts.get(color, 0) < needed:
                success = False
                break
        
        if success:
            success_count += 1

    return success_count / num_experiments