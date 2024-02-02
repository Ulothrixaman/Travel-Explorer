# Use Ubuntu latest as the base image
FROM ubuntu:latest

# Set environment variables
ENV DEBIAN_FRONTEND noninteractive
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install Python 3.10 and other dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        python3.10 \
        python3.10-dev \
        python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt requirements.txt

# Install Python dependencies
RUN pip3 install --upgrade pip && \
    pip3 install -r requirements.txt

# Copy the Django project files to the working directory
COPY . .
# Expose the port the app runs on
EXPOSE 8000

# Run the application
CMD ["python3.10", "manage.py", "runserver", "127.0.0.1:8000"]
