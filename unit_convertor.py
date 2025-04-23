import streamlit as st

# Custom CSS style
st.markdown("""
    <style>
    .header-text {
        color: white;
        text-align: center;
        font-size: 28px;
        font-weight: bold;
        margin-bottom: 20px;
    }
    .footer {
        text-align: center;
        font-size: 14px;
        margin-top: 40px;
        color: grey;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='header-text'> Unit Converter</div>", unsafe_allow_html=True)

# Input section
value = st.number_input("Enter value:", min_value=0)
from_unit = st.selectbox("From Unit", ["Meter", "Kilometer", "Centimeter"])
to_unit = st.selectbox("To Unit", ["Meter", "Kilometer", "Centimeter"])

# Conversion logic
def convert(value, from_u, to_u):
    # Convert input to meters first
    if from_u == "Kilometer":
        value = value * 1000
    elif from_u == "Centimeter":
        value = value / 100

    # Convert meters to desired unit
    if to_u == "Kilometer":
        return value / 1000
    elif to_u == "Centimeter":
        return value * 100
    return value

# Output
result = convert(value, from_unit, to_unit)
st.success(f"{value} {from_unit} = {result} {to_unit}")


# Footer
st.markdown("---")
st.caption("Made by Uzair Muhammad using Streamlit")
