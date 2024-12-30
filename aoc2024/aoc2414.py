s1 = 0
s2 = 0
import re
from functools import reduce

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

import os
prod = True

# Create the "Output" folder if it doesn't exist
output_folder = 'C:/Users/Amal Imangulov/Downloads/Output_14'
os.makedirs(output_folder, exist_ok=True)
x = 101
y = 103
if prod:
    with open('C:/Users/Amal Imangulov/Downloads/input_14.txt', 'r') as f:
        lines = f.readlines()
else:
    lines = """p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3""".split("""
""")
    x = 11
    y = 7


def find_quadrant(field_size, point):
    x, y = field_size
    px, py = point

    # Ensure x and y are odd
    if x % 2 == 0 or y % 2 == 0:
        raise ValueError("Field dimensions must be odd.")

    # Calculate middle column and row
    x_mid = (x - 1) // 2
    y_mid = (y - 1) // 2

    # Check if the point is on the middle row or column
    if px == x_mid or py == y_mid:
        return None  # Point is in the excluded middle row or column

    # Determine the quadrant
    if px < x_mid and py < y_mid:
        return 1  # Quadrant 1 (Top-left)
    elif px > x_mid and py < y_mid:
        return 2  # Quadrant 2 (Top-right)
    elif px < x_mid and py > y_mid:
        return 3  # Quadrant 3 (Bottom-left)
    elif px > x_mid and py > y_mid:
        return 4  # Quadrant 4 (Bottom-right)
    else:
        return None  # Should not happen if conditions are correct


time = 100
dots = {1:0,2:0,3:0,4:0}
origrob = []
origvel = []
for line in lines:
    print(line)
    # p=9,5 v=-3,-3

    prize_pattern = r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)"
    prize_match = re.search(prize_pattern, line)
    p_1 = int(prize_match.group(1))
    p_2 = int(prize_match.group(2))
    v_1 = int(prize_match.group(3))
    v_2 = int(prize_match.group(4))
    new_p = [(p_1 + v_1*100)%x, (p_2 + v_2*100)%y]
    nd = find_quadrant([x,y], new_p)
    if nd:
        dots[nd]+=1
    print(dots)
    origrob.append([p_1,p_2])
    origvel.append([v_1,v_2])

s1 = reduce(lambda x, y: x * y, dots.values())
print(s1)

field_size = (x,y)  # Define the field size (max x, max y)
# Initialize the plot
fig, ax = plt.subplots(figsize=(x, y))
ax.set_xlim(0, field_size[0])  # Set x axis limits
ax.set_ylim(0, field_size[1])  # Set y axis limits
iter = 0

# Initial empty plot (no points)
scat = ax.scatter([], [], color='blue', marker='o')
time_text = ax.text(0.5, 0.95, "", transform=ax.transAxes, ha='center', fontsize=12, color='black')


# Function to update the positions of the dots
def update(frame):
    global origrob, iter

    # Update positions: add velocity to the current positions
    origrob = [((x + vx)%field_size[0], (y + vy)%field_size[1]) for (x, y), (vx, vy) in zip(origrob, origvel)]

    # Unzip the updated coordinates into x and y values
    x_vals, y_vals = zip(*origrob)

    iter += 1

    time_text.set_text(f'Time: {iter}')


    # Update the scatter plot with the new coordinates
    scat.set_offsets(np.column_stack((x_vals, y_vals)))

    if frame < 10000:  # Only save first 10,000 frames
        filename = os.path.join(output_folder, f"frame_{frame:05d}.png")  # Save image as frame_0000.png
        plt.savefig(filename)

    return scat,time_text


# Create the animation
ani = FuncAnimation(fig, update, frames=range(20000), interval=1, blit=True)

# Show the plot
plt.xlabel('X Coordinate')
plt.ylabel('Y Coordinate')
plt.title('Real-Time Dot Visualization')
plt.grid(True)
plt.show()
print(s2)
