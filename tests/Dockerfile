FROM python:3.12
RUN pip install -U aiocoap[all]
LABEL version="0.3"
WORKDIR /tests
COPY *.py .
CMD [ "python", "acceptance_tests.py" ]