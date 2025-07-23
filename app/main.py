import curses
import numpy as np
import time

class GameOfLife:
    """
    A class to manage and display Conway's Game of Life in the terminal.
    """
    def __init__(self, stdscr):
        """
        Initializes the game with the curses screen object.
        """
        self.stdscr = stdscr
        self.paused = False
        self.setup_curses()
        self.create_grid()

    def setup_curses(self):
        """
        Sets up the terminal environment for curses.
        """
        curses.curs_set(0)  # Hide the cursor
        self.stdscr.nodelay(True)  # Non-blocking keyboard input
        self.stdscr.timeout(100)  # Set a timeout for getch()

        # Initialize color pairs
        curses.start_color()
        curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)  # Live cells
        curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK) # Status text

    def create_grid(self):
        """
        Initializes the grid with a random pattern based on terminal size.
        """
        height, width = self.stdscr.getmaxyx()
        # Reserve the last row for the status bar
        self.rows, self.cols = height - 1, width
        # Create a random boolean grid
        self.grid = np.random.choice([True, False], size=(self.rows, self.cols))

    def _next_generation(self):
        """
        Computes the next state of the grid based on Conway's rules.
        This uses efficient numpy array operations.
        """
        # Create a padded grid to handle boundary conditions
        padded = np.pad(self.grid, 1, mode='constant', constant_values=False)
        
        # Count live neighbors for each cell
        neighbors = np.zeros_like(self.grid, dtype=int)
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                neighbors += padded[1+i:self.rows+1+i, 1+j:self.cols+1+j]
        
        # Apply Game of Life rules:
        # 1. A live cell with 2 or 3 neighbors survives.
        # 2. A dead cell with exactly 3 neighbors becomes a live cell.
        survives = self.grid & ((neighbors == 2) | (neighbors == 3))
        births = ~self.grid & (neighbors == 3)
        
        self.grid = survives | births

    def _draw_grid(self):
        """
        Renders the current grid state to the terminal screen.
        """
        live_cell_attr = curses.color_pair(1)
        
        # Iterate through each cell and draw it
        for r in range(self.rows):
            for c in range(self.cols):
                # Ensure we don't write past the screen width
                if c < self.cols:
                    char = '█' if self.grid[r, c] else ' '
                    try:
                        self.stdscr.addstr(r, c, char, live_cell_attr)
                    except curses.error:
                        # This can happen if the window is resized smaller.
                        pass

    def _draw_status_bar(self):
        """
        Draws the status bar at the bottom of the screen.
        """
        height, width = self.stdscr.getmaxyx()
        status_text = " (Space) to Pause/Play | (q) to Quit "
        pause_state = "PAUSED" if self.paused else "PLAYING"
        
        full_status = f" {pause_state} |{status_text}"
        
        # Ensure status text doesn't exceed window width
        # Pad the status text to clear the entire line
        status_line = full_status.ljust(width)
            
        try:
            # Draw the status bar on the last line of the screen
            self.stdscr.addstr(height - 1, 0, status_line, curses.color_pair(2))
        except curses.error:
            # This can happen if the terminal is resized to be too small
            pass

    def run(self):
        """
        The main application loop.
        """
        while True:
            # Handle user input
            key = self.stdscr.getch()
            if key == ord('q'):
                break
            elif key == ord(' '):
                self.paused = not self.paused

            # Update and draw
            self.stdscr.clear()
            self._draw_grid()
            self._draw_status_bar()
            self.stdscr.refresh()

            if not self.paused:
                self._next_generation()

def main(stdscr):
    """
    Main function to run the game, wrapped by curses.
    """
    try:
        game = GameOfLife(stdscr)
        game.run()
    except curses.error as e:
        # Handle potential errors, e.g., terminal too small
        print(f"Error: {e}")
        print("Please ensure your terminal window is large enough.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    curses.wrapper(main)