# ARGs
ARG POETRY_VERSION=1.1.13
ARG VIRTUAL_ENV="/opt/venv"
ARG APP_PATH="/app"

### Create Base Image ###
FROM python:3.9 as base

# Install needed software
RUN apt-get update && apt-get install -y \
    build-essential \
    libssl-dev \
    libffi-dev \
    python3-dev \
    libzbar0 \
    && rm -rf /var/lib/apt/lists/*

# Install rust compiler
RUN curl https://sh.rustup.rs -sSf | sh -s -- -y
ENV PATH="/root/.cargo/bin:${PATH}"

# Install poetry
ARG POETRY_VERSION
RUN /usr/local/bin/python -m pip install --upgrade pip && pip install poetry==${POETRY_VERSION}

### Create the requirements.txt from poetry ###
FROM base as requirements-stage

WORKDIR /tmp
COPY ["./pyproject.toml", "./poetry.lock", "/tmp/"]
RUN python -m poetry export -f requirements.txt --output requirements.txt --without-hashes

### Create venv ###
FROM base AS venv-stage
ARG VIRTUAL_ENV

# Create venv
RUN python -m venv ${VIRTUAL_ENV}

# Use venv
# RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="${VIRTUAL_ENV}/bin:$PATH"

# Install Dependencies
COPY --from=requirements-stage "/tmp/requirements.txt" "/tmp/requirements.txt"
RUN ${VIRTUAL_ENV}/bin/python -m pip install --upgrade pip && \
    ${VIRTUAL_ENV}/bin/python -m pip install --no-cache-dir -r "/tmp/requirements.txt"


### Start final stage ###
FROM python:3.9
ARG APP_PATH
ARG VIRTUAL_ENV

# Install Firefox && libzbar0 for pyzbar
RUN apt-get update && apt-get install -y \
    firefox-esr \
    libzbar0 \
    && rm -rf /var/lib/apt/lists/*

# Copy application
RUN ["mkdir", "-p", "${APP_PATH}"]
COPY "./whatsappMessanger" "${APP_PATH}/whatsappMessanger"
COPY "main.py" "${APP_PATH}/main.py"
WORKDIR "${APP_PATH}"

# Copy venv
COPY --from=venv-stage "${VIRTUAL_ENV}" "${APP_PATH}/.venv"

# Use venv
ENV PATH="${APP_PATH}/.venv/bin:$PATH"

# Save the driver
VOLUME "/root/.wdm"

ENTRYPOINT ["python", "main.py"]