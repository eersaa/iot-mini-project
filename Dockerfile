FROM python:3.12 AS development

RUN apt-get update && apt-get install -y \
    net-tools \
    iproute2
    
RUN pip install -U aiocoap[all]

ARG USERNAME=developer
ARG USER_UID=1000
ARG USER_GID=$USER_UID

# Create the user
RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m -s /bin/bash $USERNAME

USER $USERNAME

LABEL version="0.1"
WORKDIR /app
COPY *.py .
CMD [ "pytest" ]

FROM python:3.12-slim AS production
LABEL version="0.1"
WORKDIR /app
COPY *.py .
CMD [ "python" ]

FROM python:3.12 as acceptance-tests
RUN pip install -U aiocoap[all]

WORKDIR /src
ENV PYTHONPATH=/src/cloud

COPY ./cloud/tests/*.py ./cloud/tests/
COPY ./cloud/util/util.py ./cloud/util/util.py
WORKDIR /src/cloud/tests
CMD [ "python", "acceptance_tests.py" ]