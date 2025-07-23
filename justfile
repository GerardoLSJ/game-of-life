# Define a variable for the image name to avoid repetition
IMAGE_NAME := "game-of-life"

# Default recipe to run the application
default: run

# Build the Docker image
build:
    @echo "Building Docker image: {{IMAGE_NAME}}..."
    @docker build -t {{IMAGE_NAME}} .

# Run the application in an interactive terminal
# The container will be automatically removed on exit (--rm)
run: build
    @echo "Running application... (Press 'q' to quit)"
    @docker run -it --rm --name {{IMAGE_NAME}} {{IMAGE_NAME}}

# Stop and remove any running containers based on the image
clean:
    @echo "Stopping and removing any running '{{IMAGE_NAME}}' containers..."
    @docker ps -a -q --filter "ancestor={{IMAGE_NAME}}" | xargs -r docker stop | xargs -r docker rm

# Remove the Docker image itself
prune: clean
    @echo "Removing Docker image: {{IMAGE_NAME}}..."
    @docker rmi {{IMAGE_NAME}}