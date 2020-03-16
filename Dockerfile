FROM python:3
ADD metrics.py /
RUN pip3 install psutil
ENTRYPOINT [ "python3", "./metrics.py" ]
