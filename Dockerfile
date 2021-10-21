# Specify our container base image
FROM python:3.8

# Select a directory within our container
WORKDIR /Miniproject

# Copy everything from our project root into our WORK DIRECTORY directory
COPY . .

ENV http_proxy http://internet.jlrint.com:83
ENV https_proxy http://internet.jlrint.com:83

# Install dependencies
RUN pip install -r requirements.txt

# Execute this command on start
ENTRYPOINT ["python", "src/__App__.py"]