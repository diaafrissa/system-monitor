FROM python 
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir gunicorn
EXPOSE 5000
CMD ["gunicorn", "-b", "0.0.0.0:5000", "monitor_web:app"]

