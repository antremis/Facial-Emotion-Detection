"""

File : app.py
File_Info : This file contains python streamlit code for main app
Author : Rishaab Kalra
License : None

"""

# Dependencies

import streamlit as st
from random import random
#import cv2

from Scripts.model_runner import predict_emotion

# setting streamlit page configurations

st.set_page_config(
    page_title="Emotion Detection",
    layout="centered",
    page_icon=None,
    initial_sidebar_state="auto",
    menu_items={
        "Get Help": None,
        "Report a bug": None,
        "About" : None
    }
)


@st.cache(ttl=None)
def load_data():
    pass


def add_results(st, results):
    
    emotion = ["Angry", "Disgusted", "Fearful", "Happy", "Neutral", "Sad", "Surprised"]
    emojis = ["😠", "😬", "😱", "😃", "😐", "😢", "😲"]
    result_columns = st.columns([1, 10])

    for i in range(7):
        result_columns[0].header(emojis[i])
        result_columns[0].caption(emotion[i])

        if i in [2, 3, 5]:
            result_columns[1].write("")

        result_columns[1].write("")
        result_columns[1].write("")
        result_columns[1].progress(round(results[i]*100))
        result_columns[1].write("")
        result_columns[1].write("")


def add_website_info(st):

    st.header("What Is Emotion Detection?")
    st.markdown("""
    Emotion recognition is the process of detecting displayed human emotions using artificial intelligence based technologies in order to evaluate non-verbal responses to products, services or goods.
    """)


    st.header("Why Is Emotion Detection Important?")
    st.markdown("""  
        Emotion recognition is already widely used by different companies to gauge consumer mood towards their products, brands, marketing efforts, staff or in-location experiences. Understanding customer emotions is vital to ensure business growth and enhance experiences, however the opportunities brought by this technology goes further than market research and digital advertising.
    """)

    st.header("Overall Benefits Of Emotion Detection")
    st.markdown("""
    The overall benefits of sentiment analysis include :

    * Automotive industry and emotion analysis  
    The automotive industry is also applying emotion recognition technology, as car manufacturers around the world are increasingly focusing on making cars more personal and safe for people to drive. In their pursuit to build smart car features, it makes sense that car manufacturers use AI to help them understand human emotions. Using facial emotion detection smart cars can alert the driver when he is feeling drowsy and in turn help to decrease road casualties.

    * Emotion recognition in for online admissions and interviews   
    Emotion recognition can be used to understand how candidates feel during interviews and to measure how they react to certain questions. This information can be used to optimize interview structure for future candidates and streamline the application process.

    * Emotion analysis for online education  
    Anonymous emotion detection for online education is an ideal way to analyze the online student journey and improve it where necessary. Use true facial responses and engagement levels to find points of interest or course stumbling blocks and make optimizations.

    * Emotion recognition in health care  
    AI-powered recognition software helps to decide when patients need medicine, assess their emotional response in clinical trials or to help physicians in deciding how to best triage their patients.  

    * Emotion analysis in video game testing    
    Video games are designed with a specific target audience in mind and aim to evoke a particular behavior and set of emotions from the users. During the testing phase, users are asked to play the game for a given period and their feedback is incorporated to make the final product. Using facial emotion recognition can aid in understanding which emotions a user is experiencing in real-time. This is a great addition to verbal feedback as it provides a more complex review of the gaming experience.
    """)

    st.header("About This Project")
    st.markdown("""
    This project was made to help people understand the emotion shown in an image, not only that but people can alos view their emotion in real-time using video support.

    This project is made with the help of deep learning models made using keras and a lot of data. The dataset used for this project was taken from https://www.kaggle.com/deadskull7/fer2013 which consisting of 30,000+ images along with their emotions to train the model on.
    """)

def main():
    st.title("Facial Emotion Detection Project")
    st.text("(Project Made By Rishaab Kalra)")
    st.caption("Use dark theme for better experience... You can manually switch dark theme for this website by clicking on the top-right three-bars, selecting 'Settings' option and changing 'Theme' to 'Dark'")

    #selected_option = st.selectbox("Choose a method here", ["Upload Image", "Upload Video", "Realtime Image using Webcame", "Realtime Video using Webcame"])
    selected_option = "Image"
    output_box = st.empty()
    result = None

    if selected_option == "Image":

        buffer = st.file_uploader(
                label = "Upload an image for emotion detection",
                type = [".jpg", ".jpeg", ".png"],
                accept_multiple_files = False,
                on_change = None
            )

        if buffer != None:
            output_box.success("Image uploaded successfully")
            st.image(buffer, caption="original uploaded image")
            result = predict_emotion(input_buffer = buffer)
            
            st.subheader("Analysis Results")
            add_results(st, result)

    st.write("")
    add_website_info(st)



main()
