FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code  && apt-get update && apt-get install -y ncbi-blast+
# COPY blast_app/data/ /code/data
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
CMD ["python", "manage.py", "makemigrations"]
CMD ["python", "manage.py", "migrate"]