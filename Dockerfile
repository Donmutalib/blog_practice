FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
EXPOSE $PORT
CMD gunicorn blog_pracitce_project.wsgi:application --bind 0.0.0.0:$PORT



