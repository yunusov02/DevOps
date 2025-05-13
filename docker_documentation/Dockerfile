FROM python:3.9-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requierments.txt

EXPOSE 5000

ENV FLASK_APP=app.py

CMD [ "flask", "run", "--host=0.0.0.0" ]


# this command build this container
# docker build -t nginx-static .

# this command run this container
# docker run -p 80:80 nginx-static
