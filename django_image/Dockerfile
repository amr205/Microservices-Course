FROM python
RUN pip install django
RUN mkdir workdir
WORKDIR workdir
ENTRYPOINT ["django-admin", "startproject"]
CMD ["myproject"]
