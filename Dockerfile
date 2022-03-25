FROM python:3.7.3

RUN apt-get clean && apt-get update && apt-get install -y locales
RUN locale-gen pt_BR.UTF-8

LABEL maintainer="danielgoncalves.info@gmail.com"

ENV HOST 0.0.0.0
ENV PORT 5000
ENV DEBUG true

COPY . /flask-medias-moveis-simples/api
WORKDIR /flask-medias-moveis-simples/api

RUN pip install -r requirements.txt

EXPOSE 5000

RUN pip install gunicorn

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "3", "api.app:app"]

