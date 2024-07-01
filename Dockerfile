# Use the official Python image as a base image
FROM python:latest

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1cd

# Set the working directory in the container
WORKDIR /rf_app

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Django project code to the working directory
COPY . .

# Expose the port on which your Django app will run (change 8000 to your desired port)
EXPOSE 8000

# Run database migrations
RUN python manage.py makemigrations
RUN python manage.py migrate

# Command to run your Django application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]