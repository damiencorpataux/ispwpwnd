FROM python:3-alpine

RUN pip install requests

ADD ispwpwnd.py /ispwpwnd.py

ENTRYPOINT [ "python", "/ispwpwnd.py" ]