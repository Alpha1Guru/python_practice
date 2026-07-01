import time

def solution_math(minn=0, maxx=5, c=20, design="********"):
    # The total distance we travel one way (Amplitude)
    amplitude = maxx - minn
    
    # The number of steps to get back to the start state (Period)
    # e.g., if range is 5, it takes 10 steps to go 0->5->0
    period = amplitude * 2 
    
    for i in range(c):
        # 1. (i % period) creates a repeating saw pattern: 0, 1, ... 9, 0, 1 ...
        # 2. Subtracting amplitude shifts it: -5, -4, ... 0 ... 4, -5
        # 3. Absolute value turns the 'V' shape into a bounce: 5, 4, ... 0 ... 4, 5
        # 4. Subtracting that from amplitude flips it to start at 0: 0, 1, ... 5 ... 1, 0
        oscillation = amplitude - abs((i % period) - amplitude)
        
        # Add minn back in case we didn't start at 0
        n = minn + oscillation
        
        time.sleep(0.05)
        print(" " * n + design)

    print("\nDone with solution math\n\n")

# Run for 20 frames
solution_math(c=20, maxx=10)