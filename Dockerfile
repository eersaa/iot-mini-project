FROM python:3.12 AS development

RUN pip install -U pytest \
                    aiocoap[all]

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
