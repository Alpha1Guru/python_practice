import time

def solution_2d(width=20, height=10, c=100, design="O"):
    # We use the mathematical triangle wave (Solution 6) for both X and Y.
    # Because width (20) and height (10) are different, they will bounce at different speeds.
    
    # Pre-calculate periods for efficiency
    period_x = width * 2
    period_y = height * 2
    
    for i in range(c):
        # --- CALCULATE POSITIONS ---
        # 1. Horizontal Position (X)
        x = width - abs((i % period_x) - width)
        
        # 2. Vertical Position (Y)
        y = height - abs((i % period_y) - height)
        
        # --- DRAW FRAME ---
        # This "Magic String" clears the console so we can animate in place.
        # \033[H = Move cursor to home (top-left)
        # \033[J = Clear screen from cursor down
        print("\033[H\033[J", end="")
        
        # Print 'y' newlines to push the text down
        print("\n" * y, end="")
        
        # Print 'x' spaces to push the text right
        print(" " * x + design)
        
        time.sleep(0.05)

    print("\nDone with solution 2D\n")

# Note: You may need to run this in a real terminal (like Command Prompt or Terminal)
# for the screen clearing to work perfectly.
solution_2d(c=100)