import streamlit as st

def set_modern_dashboard_style():

    css = """
    <style>

/* Import Elegant Fonts */

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Poppins:wght@500;600&display=swap');

/* Animated Gradient Background */

.stApp{

background: linear-gradient(-45deg,#eef2ff,#f8fafc,#e0e7ff,#f1f5f9);

background-size:400% 400%;

animation:gradientBG 15s ease infinite;

font-family:'Inter',sans-serif;

}

@keyframes gradientBG{

0%{background-position:0% 50%;}
50%{background-position:100% 50%;}
100%{background-position:0% 50%;}

}


/* Sidebar */

[data-testid="stSidebar"]{

background:rgba(255,255,255,0.85);

backdrop-filter:blur(10px);

border-right:1px solid #e2e8f0;

}

/* Headers */

h1,h2,h3{

font-family:'Poppins',sans-serif;

color:#1e293b;

}

/* Buttons */

.stButton>button{

background:linear-gradient(135deg,#6366f1,#3b82f6);

color:white;

border:none;

border-radius:12px;

padding:10px 18px;

font-weight:600;

transition:0.3s;

box-shadow:0 6px 14px rgba(79,70,229,0.25);

}

.stButton>button:hover{

transform:translateY(-3px);

box-shadow:0 14px 24px rgba(79,70,229,0.35);

}


/* Text Elements Visibility */
p, label, span, .stMarkdown, .stText {
    color: #334155 !important;
}

[data-testid="stSidebar"] * {
    color: #334155 !important;
}

[data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2 {
    color: #1e293b !important;
}

.stButton>button * {
    color: white !important;
}

/* Inputs */

[data-baseweb="input"],
[data-baseweb="select"],
[data-baseweb="number-input"] {
    border-radius: 10px;
    border: 1px solid #cbd5e1 !important;
}

/* Force Input Backgrounds to White */
[data-baseweb="input"], [data-baseweb="input"] *,
[data-baseweb="select"], [data-baseweb="select"] *,
[data-baseweb="number-input"], [data-baseweb="number-input"] *,
div[data-baseweb="base-input"], div[data-baseweb="base-input"] * {
    background-color: #ffffff !important;
}

/* Input Text Colors */
[data-baseweb="input"] input, [data-baseweb="select"] div, [data-baseweb="number-input"] input, .stNumberInput input, .stTextInput input, [data-baseweb="slider"] *, div[data-baseweb="base-input"] input {
    color: #0f172a !important;
}


/* Glass Cards */

.clean-card{

background:rgba(255,255,255,0.7);

backdrop-filter:blur(12px);

border-radius:16px;

border:1px solid rgba(255,255,255,0.4);

box-shadow:0 10px 30px rgba(0,0,0,0.08);

padding:24px;

margin-bottom:20px;

transition:0.3s;

}

.clean-card:hover{

transform:translateY(-6px);

box-shadow:0 20px 40px rgba(0,0,0,0.15);

}

.clean-card h3{

color:#4f46e5;

margin-bottom:10px;

}


/* Metric Cards */

.metric-card{

background:white;

border-radius:14px;

padding:18px;

box-shadow:0 6px 14px rgba(0,0,0,0.05);

text-align:center;

transition:0.2s;

}

.metric-card:hover{

transform:translateY(-3px);

box-shadow:0 10px 20px rgba(0,0,0,0.08);

}

.metric-title{

font-size:14px;

color:#64748b;

}

.metric-value{

font-size:26px;

font-weight:700;

color:#4f46e5;

}


/* Hero Section */

.hero{

padding:45px;

border-radius:20px;

background:linear-gradient(135deg,#6366f1,#3b82f6);

color:white;

text-align:center;

margin-bottom:35px;

box-shadow:0 10px 25px rgba(0,0,0,0.2);

}

.hero h1{

font-size:40px;

margin-bottom:10px;

}

.hero p{

font-size:18px;

opacity:0.9;

}

    </style>
    """
    st.markdown(css, unsafe_allow_html=True)
    
def render_particles():
    import streamlit.components.v1 as components
    # We use particles.js from a CDN for a subtle tech-y background animation.
    # The canvas is set to position fixed with z-index -1 so it stays behind everything.
    particles_html = """
    <div id="particles-js" style="position:fixed; top:0; left:0; width:100vw; height:100vh; z-index:-1;"></div>
    <script src="https://cdn.jsdelivr.net/particles.js/2.0.0/particles.min.js"></script>
    <script>
        particlesJS("particles-js", {
          "particles": {
            "number": {"value": 80, "density": {"enable": true, "value_area": 800}},
            "color": {"value": "#6366f1"},
            "shape": {"type": "circle"},
            "opacity": {"value": 0.5, "random": false},
            "size": {"value": 3, "random": true},
            "line_linked": {"enable": true, "distance": 150, "color": "#6366f1", "opacity": 0.4, "width": 1},
            "move": {"enable": true, "speed": 2, "direction": "none", "random": false, "straight": false, "out_mode": "out"}
          },
          "interactivity": {
            "detect_on": "canvas",
            "events": {
              "onhover": {"enable": true, "mode": "grab"},
              "onclick": {"enable": true, "mode": "push"},
              "resize": true
            },
            "modes": {
              "grab": {"distance": 140, "line_linked": {"opacity": 1}},
              "push": {"particles_nb": 4}
            }
          },
          "retina_detect": true
        });
    </script>
    """
    components.html(particles_html, height=0, width=0)

def render_card(title, content):

    st.markdown(f"""
    <div class="clean-card">
        <h3>{title}</h3>
        <p>{content}</p>
    </div>
    """, unsafe_allow_html=True)


def render_metric(title, value, color="#4f46e5"):

    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">{title}</div>
        <div class="metric-value" style="color: {color};">{value}</div>
    </div>
    """,unsafe_allow_html=True)


def render_hero(title,subtitle):

    st.markdown(f"""
    <div class="hero">
    <h1>{title}</h1>
    <p>{subtitle}</p>
    </div>
    """,unsafe_allow_html=True)