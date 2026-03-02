import streamlit as st
from streamlit_lottie import st_lottie
import json
import requests

def load_lottie(url):

    r = requests.get(url)

    if r.status_code != 200:
        return None

    return r.json()


def show_searching_animation():

    lottie = load_lottie(
    "https://assets5.lottiefiles.com/packages/lf20_j1adxtyb.json"
    )

    st_lottie(
    lottie,
    height=200,
    key="loading"
    )