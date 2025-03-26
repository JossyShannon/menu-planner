import streamlit as st

def file():
    #uploaded_file = st.file_uploader(label="Upload a recipie file")
#
    #if uploaded_file is not None:
    #    st.write(uploaded_file)
#
    import streamlit as st
    import pandas as pd
    from io import StringIO

    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        # To read file as bytes:
        bytes_data = uploaded_file.getvalue()
        st.write(bytes_data.decode("utf-8"))

        # To convert to a string based IO:
        #stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
        #st.write(stringio)

        # To read file as string:
        #string_data = stringio.read()
        #st.write(string_data)

        # Can be used wherever a "file-like" object is accepted:
        dataframe = pd.read_csv(uploaded_file)
        st.write(dataframe)

