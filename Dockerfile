# Use the official CentOS 7 image as a parent image
FROM centos:7

# Set the working directory in the container
WORKDIR /app

# Install necessary dependencies
RUN yum update -y && \
    yum install -y epel-release && \
    yum install -y gcc openssl-devel bzip2-devel libffi-devel zlib-devel wget \
    yum clean all

RUN yum install -y make && yum clean all

RUN wget https://www.python.org/ftp/python/3.9.16/Python-3.9.16.tgz

RUN tar xzf Python-3.9.16.tgz

RUN cd Python-3.9.16 && ./configure --enable-optimizations && make altinstall

RUN rm Python-3.9.16.tgz && python3.9 -V

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
# (Since this script doesn't have any external dependencies, we don't need this in this case)
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Define environment variable
ENV NAME index_refresh

# Run your_script_name.py when the container launches
CMD ["python3.9", "-u", "indexrefresh.py"]
