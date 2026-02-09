FROM python:3.13-slim

#set working Directory
WORKDIR /app

#Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

#COPY project files
COPY . .

#eXPOSE PORT
EXPOSE 8000

#start server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

