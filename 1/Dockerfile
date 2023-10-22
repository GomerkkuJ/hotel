FROM python:3.10

WORKDIR /HotelProject

COPY .requirements.txt /HotelProject/requirements.txt

RUN pip3.10 install -r requirements.txt

COPY . /HotelProject

CMD ["uvicorn", "main:app", "--reload", "-host=0.0.0.0"]