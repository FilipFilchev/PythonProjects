import easyocr as ocr  #OCR
import streamlit as st  #Web App
import numpy
from PIL import Image #Image Processing
import numpy as np #Image Processing 

#title
st.title("OCR App")

#subtitle
st.markdown("## Optical Character Recognition")

st.markdown("by Iris Vision")

#image uploader
image = st.file_uploader(label = "Upload your image here",type=['png','jpg','jpeg'])


@st.cache
def load_model(): 
    reader = ocr.Reader(['en'],model_storage_directory='.')
    return reader 

reader = load_model() #load model

if image is not None:

    input_image = Image.open(image) #read image
    st.image(input_image) #display image

    with st.spinner("🤖 OCR is working... "):
        

        result = reader.readtext(np.array(input_image))

        result_text = [] #empty list for results


        for text in result:
            result_text.append(text[1])

        st.write(result_text)
    #st.success("Here you go!")
    st.balloons()
else:
    st.write("Upload an Image")

st.caption("Enjoy!")




#streamlit run streamlitapp.py


"""No CUDA-GPU available --> using the CPU

Neither CUDA nor MPS are available - defaulting to CPU. Note: This module is much faster with a GPU.
Downloading detection model, please wait. This may take several minutes depending upon your network connection.
Progress: |██████████----------------------------------------| 21.6% CompleteNeither CUDA nor MPS are available - defaulting to CPU. Note: This module is much faster with a GPU.
Downloading detection model, please wait. This may take several minutes depending upon your network connection.
Progress: |█████████████████████████████████████████████-----| 91.9% Completec
"""

