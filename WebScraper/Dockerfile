FROM python:slim

COPY requirements.txt /
RUN pip install -r requirements.txt
COPY WebScraper.py /
CMD ["python", "WebScraper.py"]
