FROM ubuntu:18.04

# Install Python dependencies
RUN apt-get update && apt-get install -y python3 python3-pip

# Install Z3
RUN pip3 install --user z3-solver pytest

# Clean up the apt-get lists
RUN rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . /app

WORKDIR /app
