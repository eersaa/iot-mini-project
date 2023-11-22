FROM python:3.12 as test-env
RUN pip install -U aiocoap[all]
WORKDIR /src
COPY *.py .
CMD [ "python", "datacollector_main_tests.py" ]