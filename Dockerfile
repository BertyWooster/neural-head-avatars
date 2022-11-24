FROM ubuntu:22.10
WORKDIR /opt/app
ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=America/Los_Angeles

# install system components
RUN apt update -y && apt install -y \
    curl \
    unzip \
    nano \
    wget \
    git \
    zlib1g-dev \
    nasm \
    cmake \
    python3-pip \
    ffmpeg \
    libsm6 \
    libxext6 \
    build-essential \
    software-properties-common \
    ca-certificates


COPY . /root/neural-head-avatars
ENV PYTHONPATH "${PYTHONPATH}:/root/neural-head-avatars"
WORKDIR /root/neural-head-avatars
RUN pip3 install -e .
CMD ["/bin/bash"]
