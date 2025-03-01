import streamlit as st

def convert_units(value, from_unit, to_unit):
    conversion_factors = {
        'm': {'cm': 100, 'mm': 1000, 'inch': 39.3701, 'ft': 3.28084},
        'cm': {'m': 0.01, 'mm': 10, 'inch': 0.393701, 'ft': 0.0328084},
        'mm': {'m': 0.001, 'cm': 0.1, 'inch': 0.0393701, 'ft': 0.00328084},
        'inch': {'m': 0.0254, 'cm': 2.54, 'mm': 25.4, 'ft': 0.0833333},
        'ft': {'m': 0.3048, 'cm': 30.48, 'mm': 304.8, 'inch': 12}
    }
    
    if from_unit in conversion_factors and to_unit in conversion_factors[from_unit]:
        return value * conversion_factors[from_unit][to_unit]
    else:
        return None

st.set_page_config(page_title="Unit Converter", page_icon="🔢", layout="centered")

st.markdown("""
    <style>
        body {
            background-color: #202124;
            color: white;
            font-family: Arial, sans-serif;
        }
        .container {
            max-width: 400px;
            margin: auto;
            padding: 20px;
            background: #303134;
            border-radius: 10px;
            text-align: center;
        }
        .title {
            font-size: 24px;
            font-weight: bold;
            margin-bottom: 20px;
        }
        .input-box {
            display: flex;
            justify-content: space-between;
            align-items: center;
            background: #3c4043;
            padding: 10px;
            border-radius: 5px;
            margin-bottom: 10px;
        }
        .result-box {
            font-size: 24px;
            font-weight: bold;
            background: #3c4043;
            padding: 10px;
            border-radius: 5px;
            text-align: center;
        }
        .formula-box {
            background: #fbbc04;
            padding: 10px;
            border-radius: 5px;
            font-weight: bold;
            color: black;
            display: inline-block;
            margin-top: 10px;
        }
    </style>
    <div class='container'>
        <div class='title'>Unit Converter</div>
    </div>
""", unsafe_allow_html=True)

value = st.number_input("Enter Value:", min_value=0.0, format="%.2f")
from_unit = st.selectbox("From Unit:", ["m", "cm", "mm", "inch", "ft"], key="from_unit")
to_unit = st.selectbox("To Unit:", ["m", "cm", "mm", "inch", "ft"], key="to_unit")

if st.button("Convert"):
    result = convert_units(value, from_unit, to_unit)
    if result is not None:
        st.markdown(f"""
            <div class='container'>
                <div class='input-box'>
                    <span>{value} {from_unit}</span>
                    <span>=</span>
                    <span>{result:.4f} {to_unit}</span>
                </div>
                <div class='formula-box'>
                    Formula: Multiply the length value by {result/value:.4f}
                </div>
            </div>
        """, unsafe_allow_html=True)
    else:
        st.error("Invalid Conversion")
