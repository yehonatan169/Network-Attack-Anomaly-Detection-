import streamlit as st
import joblib
from PIL import Image



is_anomaly = joblib.load("kmeans_model")


def predict_data(data):
    result = is_anomaly.predict(data)
    return result


if __name__ == '__main__':
    """Anomaly Classifier App
    With Streamlit
  """

    st.title("Anomaly Classifier")
    html_temp = """
    <div style="background-color:blue;padding:10px">
    <h2 style="color:grey;text-align:center;">Streamlit App </h2>
    </div>

    """

    st.markdown(html_temp, unsafe_allow_html=True)
    

    duration_ = st.text_input("Enter duration", "Please Type Here")
    src_bytes = st.text_input("Enter src_bytes", "Please Type Here")
    dst_bytes = st.text_input("Enter dst_bytes", "Please Type Here")

    if st.button("Predict"):
        result = predict_data([[0,duration_, src_bytes, dst_bytes]])
        print(result)
        if result[0] == 0:
            prediction = 'malware'
        else:
            # result[0] == 1
             prediction = 'not malware!!!'

        st.success('DATA: {} was classified as {}'.format([duration_, src_bytes, dst_bytes], prediction))

