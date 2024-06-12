# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install any dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . .

# Make port 8081 available to the world outside this container
EXPOSE 8081

# Define environment variable
ENV PYTHONUNBUFFERED=1
ENV IP_ADDRESS="0.0.0.0"

# Run the application
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8081"]
