# Use Debian Slim Buster image
FROM python:3.8.5-slim-buster

# Set environment variables
ENV PIP_NO_CACHE_DIR=1
ENV DEBIAN_FRONTEND=nonactive

# Update APT sources
RUN sed -i.bak 's/us-west-2\.ec2\.//' /etc/apt/sources.list

# Install required packages
RUN apt update && apt upgrade -y && \
    apt install --no-install-recommends -y \
    debian-keyring \
    debian-archive-keyring \
    bash \
    bzip2 \
    curl \
    figlet \
    git \
    util-linux \
    libffi-dev \
    libjpeg-dev
    libjpeg62-turbo-dev \
    libwebp-dev \
    linux-headers-amd64 \
    musl-dev \
    musl \
    neofetch \
    php-pgsql \
    python3-lxml \
    postgresql \
    postgresql-client \
    python3-psycopg2 \
    libpq-dev \
    libcurl4-openssl-dev \
    libxml2-dev \
    libxslt1-dev \
    python3-pip \
    python3-requests \
    python3-sqlalchemy \
    python3-tz \
    python3-aiohttp \
    openssl \
    pv \
    jq \
    wget \
    python3 \
    python3-dev \
    libreadline-dev \
    libyaml-dev \
    gcc \
    sqlite3 \
    libsqlite3-dev \
    sudo
    z1g \
    ffmpeg \
    libssl-dev \
    libgconf-2-4 \
    libxi6 \
    xvfb \
    unzip \
    libopus0 \
    libopus-dev \
    && rm -rf /var/lib/apt/lists/* /var/cache/apt/archives/* /tmp

# Upgrade pip and setuptools
RUN pip3 install --upgrade pip setuptools

# Clone the ERA repository
RUN git clone https://github.com/IamDuru/ERAROBOT /root/ERA
WORKDIR /root/ERA

# Copy config file to /root/ERA/ERA
COPY ./ERAROBOT/config.py /root/ERA/ERA/

# Set environment variables
 PATHhome/bot/bin:$PATH"

# Install Python requirements
COPY requirements.txt .
RUN pip3 install -U -r requirements.txt

# Expose necessary ports
EXPOSE 80

# Set up a basic health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=30s --retries=3 \
    CMD curl -f http://localhost/health || exit 1

# Starting the bot
CMD ["python3", "-m "ERA"]
