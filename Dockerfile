### Create the requirements.txt from poetry ###
FROM python:3.9 as requirements-stage

WORKDIR /tmp
RUN apt-get update && apt-get install -y \
    build-essential \
    libssl-dev \
    libffi-dev \
    python3-dev \
    cargo \
    && rm -rf /var/lib/apt/lists/*
RUN /usr/local/bin/python -m pip install --upgrade pip && curl -sSL https://install.python-poetry.org | python3 -
COPY ["./pyproject.toml", "./poetry.lock", "/tmp/"]
RUN $HOME/.local/bin/poetry export -f requirements.txt --output requirements.txt --without-hashes

### Create venv ###
FROM python:3.9 AS venv-stage

# Install needed software
RUN apt-get update && apt-get install -y \
    build-essential \
    libssl-dev \
    libffi-dev \
    python3-dev \
    libzbar0 \
    && rm -rf /var/lib/apt/lists/* \
    && curl https://sh.rustup.rs -sSf | sh -s -- -y

# Create venv
RUN python -m venv "/opt/venv"

# Use venv
# RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="/opt/venv/bin:$PATH"

# Install Dependencies
COPY --from=requirements-stage "/tmp/requirements.txt" "/tmp/requirements.txt"
RUN /usr/local/bin/python -m pip install --upgrade pip && \
    pip install --no-cache-dir -r "/tmp/requirements.txt"


### Start final stage ###
FROM python:3.9

# Install Firefox && libzbar0 for pyzbar
RUN apt-get update && apt-get install -y \
    firefox-esr \
    libzbar0 \
    && rm -rf /var/lib/apt/lists/*


# Copy application
RUN ["mkdir", "-p", "/app"]
COPY "./whatsappMessanger" "/app/whatsappMessanger"
COPY "main.py" "/app/main.py"
WORKDIR "/app"

# Copy venv
COPY --from=venv-stage "/opt/venv" "/app/.venv"

# Use venv
ENV PATH="/app/.venv/bin:$PATH"

# Save the driver
VOLUME "/root/.wdm"

ENTRYPOINT ["python", "main.py"]