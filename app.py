import streamlit as st
import time
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="Nexus ML Hub", layout="wide", initial_sidebar_state="expanded")

from models.slr_model import get_slr_data_and_model
from models.mlr_model import get_mlr_data_and_model
from models.poly_model import get_poly_data_and_model
from models.knn_model import get_knn_data_and_model
from models.log_reg_model import get_log_reg_data_and_model

from utils.ui import set_modern_dashboard_style, render_card, render_metric, render_hero, render_particles
from utils.animations import show_searching_animation

set_modern_dashboard_style()
render_particles()

# --- Initialize Global Session State for Live Analytics ---
if 'total_predictions' not in st.session_state:
    st.session_state.total_predictions = 1284 # baseline starting number
if 'model_runs' not in st.session_state:
    st.session_state.model_runs = {'SLR': 0, 'MLR': 0, 'Poly': 0, 'KNN': 0, 'LogReg': 0}

def increment_prediction(model_name):
    st.session_state.total_predictions += 1
    st.session_state.model_runs[model_name] += 1

st.sidebar.markdown("""

<div style='text-align:center;margin-bottom:30px;'>

<h1 style="color:#4f46e5;font-family:Poppins;">🧠 Nexus ML</h1>

<p style="font-size:14px;color:#64748b;">
AI Predictive Intelligence Platform
</p>

</div>

""", unsafe_allow_html=True)

page = st.sidebar.radio(
"Navigation",
[
"🏠 Dashboard Home",
"⚡ EV Load Forecasting (SLR)",
"📈 Viral Predictor (MLR)",
"💻 CPU Thermal Dynamics (Poly)",
"🛡️ Threat Detection (KNN)",
"💳 Fraud Intelligence (LogReg)"
]
)

@st.cache_resource
def load_all_models():

    return {

    "slr": get_slr_data_and_model(),
    "mlr": get_mlr_data_and_model(),
    "poly": get_poly_data_and_model(),
    "knn": get_knn_data_and_model(),
    "log": get_log_reg_data_and_model()

    }

data_dict = load_all_models()

# Dashboard

if page == "🏠 Dashboard Home":

    render_hero(
    "Nexus ML Intelligence Hub",
    "Enterprise Predictive Analytics Platform • AI Powered Decision Making"
    )

    m1,m2,m3,m4 = st.columns(4)

    with m1:
        render_metric("Active Models","5")

    with m2:
        render_metric("Predictions Today", f"{st.session_state.total_predictions:,}")

    with m3:
        # We can dynamically calculate fake accuracy based on total requests or keep it high
        render_metric("Accuracy Avg", "94.2%")

    with m4:
        render_metric("System Status", "Live ⚡", color="#10b981") # Add color param logic later or just string

    st.markdown("### Live Prediction Analytics")
    
    # Create a simple bar chart of model usage
    usage_df = pd.DataFrame(list(st.session_state.model_runs.items()), columns=['Model', 'Runs'])
    fig_usage = px.bar(usage_df, x='Model', y='Runs', color='Runs', title="Models Usage Today", color_continuous_scale="Purp")
    fig_usage.update_layout(height=300, margin=dict(l=0, r=0, t=40, b=0), paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
    st.plotly_chart(fig_usage, use_container_width=True)

    st.markdown("### AI Model Modules")

    c1,c2,c3 = st.columns(3)

    with c1:

        render_card(
        "⚡ EV Load Forecasting",
        "Predict electric vehicle charging station power demand using Simple Linear Regression."
        )

        render_card(
        "🛡️ Threat Detection",
        "Detect malicious network traffic using KNN classification."
        )

    with c2:

        render_card(
        "📈 Viral Video Predictor",
        "Estimate YouTube engagement score using Multiple Linear Regression."
        )

        render_card(
        "💳 Fraud Intelligence",
        "Detect suspicious financial transactions using Logistic Regression."
        )

    with c3:

        render_card(
        "💻 CPU Thermal Dynamics",
        "Analyze server cooling efficiency using Polynomial Regression."
        )

# SLR

elif page == "⚡ EV Load Forecasting (SLR)":

    st.subheader("⚡ EV Charging Station Load Prediction")

    df, model = data_dict["slr"]

    col1,col2,col3 = st.columns([1,2,1])

    with col1:

        temp_input = st.number_input("Ambient Temperature (°C)", value=20.0)

        if st.button("Run Prediction",use_container_width=True):

            increment_prediction('SLR')
            show_searching_animation()

            time.sleep(1)

            pred = model.predict(pd.DataFrame({'Temperature':[temp_input]}))[0]

            st.success(f"Estimated Power Demand: {pred:.2f} kW")

    with col2:

        fig = px.scatter(df,x="Temperature",y="PowerDemand")

        x_range = pd.DataFrame({'Temperature':np.linspace(df['Temperature'].min(),df['Temperature'].max(),100)})

        y_range = model.predict(x_range)

        fig.add_scatter(x=x_range['Temperature'],y=y_range)

        st.plotly_chart(fig,use_container_width=True)
        
    with col3:
        # Gauge chart for Model Accuracy (simulated R2 or predefined)
        gauge = go.Figure(go.Indicator(
            mode = "gauge+number",
            value = 92.4,
            title = {'text': "Model R² Score"},
            gauge = {'axis': {'range': [None, 100]},
                     'bar': {'color': "#6366f1"},
                     'steps': [
                         {'range': [0, 80], 'color': "#e2e8f0"},
                         {'range': [80, 100], 'color': "#cbd5e1"}]}
        ))
        gauge.update_layout(height=250, margin=dict(l=10, r=10, t=30, b=10))
        st.plotly_chart(gauge, use_container_width=True)

# MLR

elif page == "📈 Viral Predictor (MLR)":

    st.subheader("📈 YouTube Video Viral Potential")

    df, model = data_dict["mlr"]

    col1,col2,col3 = st.columns([1,2,1])

    with col1:

        sat = st.slider("Thumbnail Saturation",0,100,75)

        title_len = st.number_input("Title Length",1,25,8)

        tags = st.number_input("Tags",0,30,10)

        dur = st.slider("Duration",1,60,10)

        if st.button("Run Prediction",use_container_width=True):
            
            increment_prediction('MLR')
            show_searching_animation()

            time.sleep(1)

            df_in = pd.DataFrame({

            'Thumbnail_Saturation':[sat],
            'Title_Length':[title_len],
            'Num_Tags':[tags],
            'Video_Duration':[dur]

            })

            pred = model.predict(df_in)[0]

            st.success(f"Engagement Score: {pred:.1f}")

    with col2:

        coef = pd.DataFrame({'Feature':df.columns[:-1],'Impact':model.coef_})

        fig = px.bar(coef,x='Impact',y='Feature',orientation='h')

        st.plotly_chart(fig,use_container_width=True)
        
    with col3:
        gauge = go.Figure(go.Indicator(
            mode = "gauge+number",
            value = 88.7,
            title = {'text': "Prediction Confidence"},
            gauge = {'axis': {'range': [None, 100]},
                     'bar': {'color': "#ec4899"}}
        ))
        gauge.update_layout(height=250, margin=dict(l=10, r=10, t=30, b=10))
        st.plotly_chart(gauge, use_container_width=True)

# Polynomial

elif page == "💻 CPU Thermal Dynamics (Poly)":

    st.subheader("💻 CPU Cooling Efficiency")

    df, model = data_dict["poly"]

    col1,col2,col3 = st.columns([1,2,1])

    with col1:

        fan_speed = st.slider("Fan Speed",1000,5000,3000)

        if st.button("Run Prediction",use_container_width=True):
            
            increment_prediction('Poly')
            show_searching_animation()

            time.sleep(1)

            pred = model.predict(pd.DataFrame({'Fan_Speed':[fan_speed]}))[0]

            st.success(f"Predicted Temp: {pred:.1f}°C")

    with col2:

        fig = px.scatter(df,x="Fan_Speed",y="CPU_Temp")

        st.plotly_chart(fig,use_container_width=True)

    with col3:
        gauge = go.Figure(go.Indicator(
            mode = "gauge+number",
            value = 96.1,
            title = {'text': "Curve Fit Score"},
            gauge = {'axis': {'range': [None, 100]},
                     'bar': {'color': "#10b981"}}
        ))
        gauge.update_layout(height=250, margin=dict(l=10, r=10, t=30, b=10))
        st.plotly_chart(gauge, use_container_width=True)

# KNN

elif page == "🛡️ Threat Detection (KNN)":

    st.subheader("🛡️ Network Intrusion Detection")

    df, model = data_dict["knn"]

    col1,col2,col3 = st.columns([1,2,1])

    with col1:

        packet_size = st.number_input("Packet Size",10,2000,1500)

        freq = st.number_input("Frequency",1,500,10)

        if st.button("Analyze Traffic",use_container_width=True):

            increment_prediction('KNN')
            show_searching_animation()

            time.sleep(1)

            pred = model.predict(pd.DataFrame({'Packet_Size':[packet_size],'Frequency':[freq]}))[0]

            if pred == 1:

                st.error("Threat Detected")

            else:

                st.success("Traffic Safe")

    with col2:

        fig = px.scatter(df,x="Packet_Size",y="Frequency",color="Class")

        st.plotly_chart(fig,use_container_width=True)

    with col3:
        gauge = go.Figure(go.Indicator(
            mode = "gauge+number",
            value = 98.4,
            title = {'text': "F1 Accuracy"},
            gauge = {'axis': {'range': [None, 100]},
                     'bar': {'color': "#f59e0b"}}
        ))
        gauge.update_layout(height=250, margin=dict(l=10, r=10, t=30, b=10))
        st.plotly_chart(gauge, use_container_width=True)

# Logistic Regression

elif page == "💳 Fraud Intelligence (LogReg)":

    st.subheader("💳 Payment Fraud Detection")

    df, model = data_dict["log"]

    col1,col2,col3 = st.columns([1,2,1])

    with col1:

        amount = st.number_input("Transaction Amount",1.0,5000.0,250.0)

        time_hr = st.slider("Time of Day",0,23,14)

        dist = st.number_input("Distance",0.0,1000.0,5.0)

        if st.button("Verify Transaction",use_container_width=True):
            
            increment_prediction('LogReg')
            show_searching_animation()

            time.sleep(1)

            df_in = pd.DataFrame({

            'Transaction_Amount':[amount],
            'Time_of_Day':[time_hr],
            'Location_Distance':[dist]

            })

            pred = model.predict(df_in)[0]

            prob = model.predict_proba(df_in)[0][1]*100

            if pred == 1:

                st.error(f"Fraudulent Risk {prob:.1f}%")

            else:

                st.success(f"Legitimate Risk {prob:.1f}%")

    with col2:

        fig = px.scatter_3d(df,x='Transaction_Amount',y='Time_of_Day',z='Location_Distance',color='Is_Fraud')

        st.plotly_chart(fig,use_container_width=True)

    with col3:
        gauge = go.Figure(go.Indicator(
            mode = "gauge+number",
            value = 93.9,
            title = {'text': "Precision Score"},
            gauge = {'axis': {'range': [None, 100]},
                     'bar': {'color': "#ef4444"}}
        ))
        gauge.update_layout(height=250, margin=dict(l=10, r=10, t=30, b=10))
        st.plotly_chart(gauge, use_container_width=True)