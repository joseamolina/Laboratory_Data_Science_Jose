FROM python:3.10
RUN mkdir /app
WORKDIR /app
ADD . /app/
RUN pip install pandas
CMD ["python", "hola_mundo.py"]