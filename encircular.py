# Problem: Encircular

"""

You are given a 2D plane a robot at (0, 0). The robot initially faces north. You are given
a list of commands. Each command is a string composed of steps 'G', 'L', and 'R'.

G - move the robot forward
L - move the robot left
R - move the robot right

The robot will infinitely repeat the command. Determine if the robot moves in a circle.

Solution: Repeat the command 4 times. If the robot is not at (0, 0), the robot does not move
in a circle.

There are 4 directions; N, E, S, W. For the movement to be a circle, there must be "4 sides", meaning
movement in each of the 4 directions (as a circle is 360 degrees, meaning movement in each direction).

Each side can only be one command. Proof: Assume each side is more than one command,
then the other side cannot be formed as each command does not turn as two or more commands represent
the same side. Thus, each side is one command.

Thus, after 4 commands, all the 4 sides should be formed and the circle should be complete.

"""
# Complete the function below.

def doesCircleExist(commands):
    res = []
    for c in commands:
        pos = [0, 0]                # [x, y]
        direction = 1               # N => 1, S => -1, E => 2, W => -2
        for i in range(4):
            for step in c:
                modifier = 1
                if direction < 0:
                    # S or W
                    modifier = -1
                if abs(direction) == 1:
                    # N or S
                    if step == 'G':
                        pos[1] += (1 * modifier)
                    elif step == 'L':
                        pos[0] -= (1 * modifier)
                        direction = 2 * -modifier
                    else:
                        pos[0] += (1 * modifier)
                        direction = 2 * modifier
                else:
                    # E or W
                    if step == 'G':
                        pos[0] += (1 * modifier)
                    elif step == 'L':
                        pos[1] += (1 * modifier)
                        direction = 1 * modifier
                    else:
                        pos[1] -= (1 * modifier)
                        direction = 1 * -modifier
        if pos[0] == 0 and pos[1] == 0:
            res.append('YES')
        else:
            res.append('NO')
    return res