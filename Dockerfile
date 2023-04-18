# Install Python slim to keep the package size small
FROM python:3.11.3-slim

# Install Java
RUN apt-get update && apt-get install -y --no-install-recommends openjdk-11-jdk \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install wget unzip
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    wget \
    unzip \
    && apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Define environment variables
ENV S3_URL=https://coding-challenge-public.s3.ap-southeast-2.amazonaws.com/test-data.zip \
    LOCAL_FILE=/app/src/data/test-data.zip

COPY . /app/
WORKDIR /app/

# Download the S3 file using wget and extract it using the password
RUN wget --progress=dot:giga $S3_URL -O $LOCAL_FILE \
    && unzip -o -P "By9FNTZXp4j4izuufAs=" $LOCAL_FILE -d /app/src/data/ \
    && rm $LOCAL_FILE

# pip upgrade and dependencies installation
RUN pip install -r config/requirements.txt

RUN chmod +x entryPoint.sh

# Set the entrypoint to the script with CMD arguments
ENTRYPOINT ["./entryPoint.sh"]

#CMD ["hulk", "batman", "superman"]