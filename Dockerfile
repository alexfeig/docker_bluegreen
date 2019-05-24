FROM python:alpine
LABEL maintainer="alex.feigenson@gmail.com"
LABEL description="A sample blue/green application meant to be used with Kubernetes."
COPY app/ /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["index.py"]
EXPOSE 5000