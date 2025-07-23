# Project Context: Terminal-Based Conway's Game of Life

This project is a self-contained, terminal-based implementation of Conway's Game of Life. The primary goal was to create a visually compelling simulation that runs directly in the terminal, is easy to manage, and is fully portable.

### Core Concepts & Vibe

The project's "vibe" is centered around a minimalist, retro-terminal aesthetic. An initial output, which appeared as a potential rendering issue, was ultimately embraced by the user as a "sick" visual style. This has become a defining characteristic of the application. The application is designed to be interactive and responsive, running smoothly within a containerized environment.

### Technical Implementation

*   **Language & Libraries:**
    *   **Python:** The core application logic is written in Python.
    *   **`curses`:** This library is used for all screen rendering, color management, and non-blocking keyboard input, enabling a true terminal-native experience.
    *   **`numpy`:** Used for high-performance 2D array manipulations, which is essential for the efficient calculation of the Game of Life generations.

*   **Containerization:**
    *   **Docker:** The application is containerized using a `Dockerfile` based on the lightweight `python:3.11-slim` image. This ensures portability and a consistent runtime environment.

*   **Automation:**
    *   **`justfile`:** A `justfile` serves as a command runner, providing a simple and intuitive interface for common tasks:
        *   `just build`: Builds the Docker image.
        *   `just run`: Runs the application in an interactive terminal.
        *   `just clean`: Stops and removes running containers.
        *   `just prune`: Removes the Docker image.

### Project Structure

The project is organized with the following key files:

*   **`app/main.py`**: The main Python script containing the `GameOfLife` class, which handles game logic, rendering, and user interaction.
*   **`Dockerfile`**: Defines the instructions to build the Docker image for the application.
*   **`justfile`**: Provides automated commands for managing the project lifecycle.
*   **`README.md`**: The main documentation file, providing an overview of the project, setup instructions, and usage.
*   **`docs/user_guide.md`**: Contains detailed information on the interactive controls (`spacebar` to pause/play, `q` to quit).