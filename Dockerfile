FROM python:3.10

WORKDIR C:\Users\User\Desktop\LeetCode\forter

COPY . .

CMD ["python", "unique_names_counter.py"]