FROM python:slim

COPY requirements.txt wait-for-it.sh /
RUN pip install -r requirements.txt
COPY WebScraper.py /
CMD ["./wait-for-it.sh", "mydb:3306", "--timeout=60", "--", "python", "WebScraper.py"]
