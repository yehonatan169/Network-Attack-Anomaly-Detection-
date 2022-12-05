FROM python:3.8

WORKDIR /app

COPY requirements.txt ./requirements.txt

RUN pip3 install -r requirements.txt
RUN pip3 install streamlit
RUN pip3 install pandas
RUN pip3 install -U scikit-learn
RUN pip3 install joblib


EXPOSE 8502

COPY . /app

ENTRYPOINT ["streamlit","run"] 

CMD ["app.py"]


