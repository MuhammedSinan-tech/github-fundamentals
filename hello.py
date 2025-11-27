# Demo A: Build-time clone (no proxy)
FROM alpine:3.18
RUN apk add --no-cache git python3
RUN git clone https://github.com/MuhammedSinan-tech/github-fundamentals.git /repo
WORKDIR /app
RUN cp /repo/docker_playground/hello.py ./hello.py
CMD ["python3", "hello.py"]
