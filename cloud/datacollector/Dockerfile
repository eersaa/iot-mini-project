FROM python:3.12 as test-env
RUN pip install -U aiocoap[all]
WORKDIR /src
ENV PYTHONPATH=/src/datacollector
COPY *.py datacollector/
COPY tests/*.py datacollector/tests/
CMD [ "python", "datacollector/tests/datacollector_main_tests.py" ]