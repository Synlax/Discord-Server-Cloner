# Dockerfile for a Python 3.8 application

# Use the Python 3.8 image as the base
FROM python:3.8

# Set the working directory to /app
WORKDIR /app

# Copy the requirements.txt file to /app in the container
COPY requirements.txt .

# Install dependencies from the requirements.txt file
RUN pip install --no-cache-dir -r requirements.txt

# Copy all remaining files from the current directory to /app in the container
COPY . .

# Run the application upon container start using the "python main.py" command
CMD ["python", "main.py"]
