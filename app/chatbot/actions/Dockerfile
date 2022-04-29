FROM rasa/rasa-sdk

WORKDIR /app
COPY requirements.txt .
USER root
RUN pip install --verbose -r requirements.txt
COPY . ./actions

EXPOSE 5055
USER 1001
