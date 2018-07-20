FROM python
RUN mkdir -p /code
COPY . /code
WORKDIR /code
RUN pip install -r requirements.txt