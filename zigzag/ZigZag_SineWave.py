import time
import math

def solution_sine(minn=0, maxx=5, c=50, speed=0.2, design="********"):
    # Calculate the total width of the play area
    width = maxx - minn
    
    for i in range(c):
        # 1. Get a value between -1 and 1 based on time (i)
        # We multiply i by 'speed' to control the frequency. 
        # (Lower speed = slower, longer waves)
        raw_val = math.sin(i * speed)
        
        # 2. Shift the range from [-1, 1] to [0, 1]
        # Adding 1 makes it [0, 2]. Dividing by 2 makes it [0, 1].
        normalized_val = (raw_val + 1) / 2
        
        # 3. Scale to our target width and add the starting position
        # We use int() because we can't print 3.4 spaces.
        n = int(minn + (normalized_val * width))
        
        time.sleep(0.05) # Running slightly faster to emphasize the smoothness
        print(" " * n + design)

    print("\nDone with solution sine\n\n")

# Run for 50 frames to see the full effect
solution_sine(c=5000, maxx=50, speed=0.2)