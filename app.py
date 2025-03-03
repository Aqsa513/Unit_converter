import streamlit as st 

# App Title
st.title(" Unit Converter🧡💫 ")

# Conversion Types
conversion_types = ["Length", " Weight", "Temperature"]

# User Selection
conversion_choice = st.selectbox("Choose Conversion Type:", conversion_types)

# Conversion Dictionaries
length_conversion = {
    "Meter": 1, 
    "Kilometers": 1000,
    "Feets": 0.3048,
    "Inches": 0.0254,
    "Centimeters": 0.01
}

weight_conversion = {
    "Kilograms": 1,
    "Grams": 0.001,
    "Pounds": 0.453592,
    "Ounces": 0.0283495
}

def convert_temperature(value, from_unit, to_unit):
    if from_unit == "Celsius":
        if to_unit == "Fahrenheit":
            return (value * 9/5) + 32
        elif to_unit == "Kelvin":
            return value + 273.15
    elif from_unit == "Fahrenheit":
        if to_unit == "Celsius":
            return (value - 32) * 5/9
        elif to_unit == "Kelvin":
            return (value - 32) * 5/9 + 273.15
    elif from_unit == "Kelvin":
        if to_unit == "Celsius":
            return value - 273.15
        elif to_unit == "Fahrenheit":
            return (value - 273.15) * 9/5 + 32
    return value  # Return same value if units are the same

with st.form("converter_form"):
    input_value = st.number_input("Enter value:", min_value=0.0, format="%.2f")
    
    if conversion_choice == "Length":
        units = list(length_conversion.keys())
    elif conversion_choice == " Weight":
        units = list(weight_conversion.keys())
    elif conversion_choice == " Temperature":
        units = ["Celsius", "Fahrenheit", "Kelvin"]
    
    from_unit = st.selectbox("From Unit:", units)
    to_unit = st.selectbox("To Unit:", units)
    submit_button = st.form_submit_button(" Convert")

if submit_button:
    if conversion_choice == "Length":
        result = input_value * length_conversion[from_unit] / length_conversion[to_unit]
    elif conversion_choice == " Weight":
        result = input_value * weight_conversion[from_unit] / weight_conversion[to_unit]
    elif conversion_choice == "Temperature":
        result = convert_temperature(input_value, from_unit, to_unit)
    
    st.success(f' {input_value} {from_unit} is equal to {result:.2f} {to_unit} ')
