FROM python:3.9

WORKDIR /projet

COPY requirements.txt .

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 80

WORKDIR /projet/app

CMD [ "python", "app.py" ]
