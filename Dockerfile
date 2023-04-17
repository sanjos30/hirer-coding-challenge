# Install Python slim to keep the package size small
FROM python:3.11.3-slim

# Install Java
RUN apt-get update && apt-get install -y --no-install-recommends openjdk-11-jdk \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY . /app/
WORKDIR /app/

# pip upgrade and dependencies installation
RUN pip install -r config/requirements.txt

CMD ["ls"]