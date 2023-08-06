

# start with the basic instructions provided by Collab images
FROM python:3.6-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# this uses '-U' for debugging purposes only, so that it always downloads the latest version of my dependencies whenever I change them
RUN pip install -r requirements.txt -U

# Run app.py when the container launches
CMD ["python", "app.py"]

