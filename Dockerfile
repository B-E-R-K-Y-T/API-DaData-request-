FROM python:3.12

EXPOSE 8000

RUN mkdir /opti_macros

WORKDIR /opti_macros

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
