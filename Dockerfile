# Use an official Python runtime as the parent image
FROM python:3.9-slim

# Set the working directory in the container to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install FastAPI and Uvicorn
RUN pip install --no-cache-dir fastapi[all] uvicorn

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable for Uvicorn to know where our app is
ENV MODULE_NAME=main

# Run Uvicorn when the container launches
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
