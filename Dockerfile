FROM python:3.11

WORKDIR /app


COPY . /app/

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

