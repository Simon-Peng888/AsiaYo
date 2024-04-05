FROM python:3.8-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application files
COPY . ./

# Set the FLASK_APP environment variable
ENV FLASK_APP=app/views/main.py

# Run the application
CMD ["flask", "run", "--host=0.0.0.0"]
