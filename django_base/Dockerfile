FROM python
ENV PYTHONUNBUFFERED 1
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app/
ADD requirements.txt /usr/src/app/
RUN pip3 install -r requirements.txt
