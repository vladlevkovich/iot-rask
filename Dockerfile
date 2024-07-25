FROM python:3.11

ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH=/global_mind_associated

WORKDIR /global_mind_associated

# Copy requirements.txt to the working directory
COPY requirements.txt /global_mind_associated/

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY app /global_mind_associated/app/

EXPOSE 8000

CMD ["python", "app/main.py"]



