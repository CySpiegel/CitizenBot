# Doesn't usually have an "upgrade"
RUN apt-get update \
 && DEBIAN_FRONTEND=noninteractive \
    apt-get install --no-install-recommends --assume-yes \
      python3 \
      python3-pip \
      python-dev