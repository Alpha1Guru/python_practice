import time

def solution_5(minn=0, maxx=5, c=1, design="********"):
    # Pre-build the sequence of spaces for one full bounce: [0, 1, 2, 3, 4, 5, 4, 3, 2, 1]
    sequence = list(range(minn, maxx)) + list(range(maxx, minn, -1))
    
    for _ in range(c): # c represents full cycles
        for n in sequence:
            time.sleep(0.1)
            print(" " * n + design)
            
    print("\nDone with solution 5\n\n")

solution_5()