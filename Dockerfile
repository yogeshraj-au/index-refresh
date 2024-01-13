# Use the official python:3.9 image as a parent image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
# (Since this script doesn't have any external dependencies, we don't need this in this case)
RUN python3 -m pip install -r requirements.txt

# Run indexrefresh.py when the container launches
CMD ["python3", "indexrefresh.py"]
