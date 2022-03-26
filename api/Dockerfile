FROM python:3.8

#RUN apt-get clean && apt-get update && apt-get install -y locales
#RUN locale-gen pt_BR.UTF-8

LABEL maintainer="danielgoncalves.info@gmail.com"

ENV HOST 0.0.0.0
ENV PORT 8003
ENV DEBUG true

COPY . /flask-medias-moveis-simples/api
WORKDIR /flask-medias-moveis-simples/api

RUN pip install -r requirements.txt

EXPOSE 8003

RUN pip install gunicorn
RUN pip install gevent

CMD ["gunicorn", "--bind", "0.0.0.0:8003", "--workers", "5", "--threads", "5", "app:app", "--timeout", "600", "--worker-class", "gevent"]

