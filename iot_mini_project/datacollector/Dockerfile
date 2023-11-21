FROM python:3.12-slim as test-env
LABEL version="0.1"
WORKDIR /src
COPY *.py .
CMD [ "python", "datacollector_main_tests.py" ]