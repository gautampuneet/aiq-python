ARG FUNCTION_DIR="/home/app"

# Set the base image
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10 AS build-image

# Install build dependencies
RUN apt-get update && apt-get install -y build-essential

# Create function directory
ARG FUNCTION_DIR
RUN mkdir -p ${FUNCTION_DIR}

# Set working directory to function root directory
WORKDIR ${FUNCTION_DIR}

# Install python requirements
COPY requirements*.txt ./
RUN pip install -r requirements.txt

# Build a runtime image
FROM build-image AS runtime-image

# Set working directory to function root directory
ARG FUNCTION_DIR
WORKDIR ${FUNCTION_DIR}

# Copy in the build image dependencies
COPY --from=build-image ${FUNCTION_DIR} ${FUNCTION_DIR}

# Copy function code
COPY src ${FUNCTION_DIR}/src

# Set the CMD to your handler (could also be done as a parameter override outside of the Dockerfile)
CMD ["uvicorn", "src.main:aiq_app"]
