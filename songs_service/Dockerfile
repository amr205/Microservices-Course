FROM python:slim-bullseye

RUN apt update

RUN apt install -y curl gnupg2
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
RUN curl https://packages.microsoft.com/config/debian/11/prod.list > /etc/apt/sources.list.d/mssql-release.list

RUN apt update
RUN apt-get install -y unixodbc-dev
RUN ACCEPT_EULA=Y apt-get install -y msodbcsql18
RUN ACCEPT_EULA=Y apt-get install -y mssql-tools18
RUN apt-get install -y libgssapi-krb5-2

RUN mkdir app
WORKDIR app
COPY requirements.txt /app
RUN pip3 install -r requirements.txt --no-cache-dir
COPY . /app
CMD ["./startup.sh"]