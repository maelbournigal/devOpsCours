FROM python:3.7.3
ADD  * /
RUN pip install mysql-connector
COPY export_data.py ./export_data.py
COPY insertData.py ./insertData.py
RUN chmod 744 ./export_data.py
RUN chmod 744 ./insertData.py
ENTRYPOINT python ./export_data.py