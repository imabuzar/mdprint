# Base image
FROM python:3.12-slim

# Install required system packages (for weasyprint)
RUN apt-get update
RUN apt-get install -y libpango-1.0-0 libpangoft2-1.0-0 libharfbuzz-subset0 libjpeg-dev libopenjp2-7-dev libffi-dev
RUN apt-get clean

# Setting working directory
WORKDIR /app

# Copy requirements.txt to install python packages
COPY requirements.txt .

# Install python packages using pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy everything
COPY . .

# Set environment variables
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Expose port
EXPOSE 5000

# Run Flask app
CMD [ "flask", "run" ]