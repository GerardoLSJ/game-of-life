# Conway's Game of Life in Docker

This project provides a complete, self-contained, and interactive terminal visualization of Conway's Game of Life. The entire application is designed to run inside a Docker container and is managed by a `justfile` for easy building, execution, and cleanup.

## Features

- **Terminal Visualization:** Renders the simulation directly in your terminal using the `curses` library.
- **Interactive Controls:** Pause, play, and quit the simulation using simple keyboard commands.
- **Containerized:** Runs in a minimal, isolated Docker container for maximum portability.
- **Automated Tasks:** Uses a `justfile` to simplify common development tasks like building and running the application.

## Prerequisites

- [Docker](https://docs.docker.com/get-docker/)
- [just](https://github.com/casey/just#installation)

## Quick Start

1.  **Build the Docker Image:**
    ```sh
    just build
    ```

2.  **Run the Application:**
    ```sh
    just run
    ```
    Alternatively, you can run `just` which defaults to the `run` command.

## How to Use

The simulation starts automatically. For a detailed guide on the interactive controls, please see the [User Guide](./docs/user_guide.md).

### `justfile` Commands

The following commands are available in the `justfile`:

| Command | Action                                              |
|---------|-----------------------------------------------------|
| `build` | Builds the `game-of-life` Docker image.             |
| `run`   | Runs the application in an interactive container.   |
| `clean` | Stops and removes any running `game-of-life` containers. |
| `prune` | Removes the `game-of-life` Docker image.            |
