FROM python:3.10-slim

# Install Java and required packages
RUN apt-get update && apt-get install -y \
    default-jdk \
    procps \
    && apt-get clean

# Set JAVA_HOME environment variable


ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-arm64
ENV PATH=$JAVA_HOME/bin:$PATH

# Create app directory
WORKDIR /app

# Copy all files
COPY . .

# Install Python dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Expose port and set entry point
EXPOSE 8000
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]
