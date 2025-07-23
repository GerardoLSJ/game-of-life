# Use an official, minimal Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the application code into the container
COPY app/ /app/

# Install any needed packages specified in requirements.txt
# In this case, we only need numpy
RUN pip install --no-cache-dir numpy

# Set the locale to support UTF-8 characters for drawing
ENV LANG=C.UTF-8
ENV LC_ALL=C.UTF-8

# Define the command to run the application
CMD ["python", "main.py"]