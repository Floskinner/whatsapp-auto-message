# This is the first stage, to create the requirements.txt
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

# Start final stage
FROM python:3.9

# Install Firefox
RUN apt-get update && apt-get install -y \
    firefox-esr \
    libzbar0 \
    && rm -rf /var/lib/apt/lists/*

# Install Dependencies
COPY --from=requirements-stage /tmp/requirements.txt /tmp/requirements.txt
RUN /usr/local/bin/python -m pip install --upgrade pip && \
    pip install --no-cache-dir -r /tmp/requirements.txt


# Copy application
RUN ["mkdir", "-p", "/app"]
COPY "./whatsappMessanger" "/app/whatsappMessanger"
COPY "main.py" "/app/main.py"
WORKDIR "/app"

# Save the driver
VOLUME /root/.wdm

ENTRYPOINT ["python", "main.py"]