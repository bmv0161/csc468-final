FROM rasa/rasa:main-spacy-en
WORKDIR '/app'
COPY . /app
USER root
#COPY ./data /app/data
RUN  rasa train
VOLUME /app/models
CMD ["run","-m","/app/models","--enable-api","--cors","*", "--debug", "--endpoints", "endpoints.yml", "--log-file", "out.log", "--debug"]
