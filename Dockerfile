FROM python:3.8
WORKDIR /app
COPY ./requirements.txt .
RUN python3 pip install --no-cache-dir -r ./requirements.txt
COPY . .
CMD ["uvicorn", "src.app:app", "-host=0.0.0.0", "-reload"]
EXPOSE 8000