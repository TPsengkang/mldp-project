import streamlit as st
import joblib
import numpy as np
import pandas as pd
from pathlib import Path

## Load trained model
model = joblib.load(Path(__file__).parents[3] / "best_linear_regression_model.pkl")

## Define the input options
#Format = <Display name> : <value to be used in model>

 ### - Categorical features - ###
## Operating System options
OS_options = {
    'Windows (🔼 Popular!)': 'Windows', 
    'macOS': 'macOS', 
    'Linux': 'Linux', 
    'ChromeOS': 'ChromeOS'
}

#GPU models
gpu_models = {
    "RTX 2050": "RTX 20 50",
    "RTX 2060": "RTX 20 60",
    "RTX 2070": "RTX 20 70",
    "RTX 2080": "RTX 20 80",
    "RTX 2080 Ti": "RTX 20 80 Ti",
    "RTX 2090": "RTX 20 90",
    "RTX 3050": "RTX 30 50",
    "RTX 3060": "RTX 30 60",
    "RTX 3070": "RTX 30 70",
    "RTX 3080": "RTX 30 80",
    "RTX 3080 Ti": "RTX 30 80 Ti",
    "RTX 3090": "RTX 30 90",
    "RTX 4050": "RTX 40 50",
    "RTX 4060": "RTX 40 60",
    "RTX 4070": "RTX 40 70",
    "RTX 4080": "RTX 40 80",
    "RTX 4080 Ti": "RTX 40 80 Ti",
    "RTX 4090": "RTX 40 90",
    "RX 5500": "RX 5000 50",
    "RX 5600": "RX 5000 60",
    "RX 5700": "RX 5000 70",
    "RX 5800": "RX 5000 80",
    "RX 5800 XT": "RX 5000 80 XT",
    "RX 5900": "RX 5000 90",
    "RX 6500": "RX 6000 50",
    "RX 6600": "RX 6000 60",
    "RX 6700": "RX 6000 70",
    "RX 6800": "RX 6000 80",
    "RX 6800 XT": "RX 6000 80 XT",
    "RX 6900": "RX 6000 90",
    "RX 7500": "RX 7000 50",
    "RX 7600": "RX 7000 60",
    "RX 7700": "RX 7000 70",
    "RX 7800": "RX 7000 80",
    "RX 7800 XT": "RX 7000 80 XT",
    "RX 7900": "RX 7000 90"
}

##Storage types
storage_type = {
    'SSD (👍 Reccomended!)': 'SSD',
    'Hybrid (👍 Reccomended!)': 'Hybrid' ,
    'NVMe': 'NVMe', 
    'HDD': 'HDD', 
    
}

##Display types
display_type = {
    'QLED (👍 Reccomended!)' : 'QLED',
    'LED' : 'LED', 
    'IPS' : 'IPS', 
    'OLED' : 'OLED', 
    'VA' : 'VA', 
    'Mini-LED' : 'Mini-LED', 
}

##Resolution options
resolution = {
    '1920x1080 (🔼 Popular!)': '1920x1080',
    '2560x1440 (👍 Recommended!)': '2560x1440',
    '3440x1440': '3440x1440',
    '3840x2160': '3840x2160',
}

### - Numerical features - ###
# cpu_threads	
cpu_threads_min = 6
cpu_threads_max = 40

# cpu_base_ghz	
cpu_base_ghz_min = 2.4
cpu_base_ghz_max = 3.2

# Popular CPU models:
# Format: <Display name> : [<threads>, <base ghz>]
cpu_models = {
    "Intel i5-12400F": [6, 2.5],
    "Intel i5-12600K": [10, 3.7],
    "Intel i5-13400F": [10, 2.5],
    "Intel i5-13600K": [14, 3.5],
    "Intel i7-12700K": [12, 3.6],
    "Intel i7-13700K": [16, 3.4],
    "Intel i9-12900K": [16, 3.2],
    "Intel i9-13900K": [24, 3.0],
    "AMD Ryzen 5 5600": [6, 3.5],
    "AMD Ryzen 5 5600X": [6, 3.7],
    "AMD Ryzen 5 7600": [8, 3.4],
    "AMD Ryzen 5 7600X": [6, 4.7],
    "AMD Ryzen 7 5700G": [8, 3.8],
    "AMD Ryzen 7 5800X": [8, 3.8],
    "AMD Ryzen 7 7700X": [8, 4.5],
    "AMD Ryzen 9 5900X": [12, 3.7],
    "AMD Ryzen 9 5950X": [16, 3.4],
    "AMD Ryzen 9 7900X": [12, 4.7],
    "AMD Ryzen 9 7950X": [16, 4.5],
}

# vram_gb	
vram_gb_min = 4
vram_gb_max = 16

# ram_gb	
ram_gb_options = {
    "8 GB": 8, 
    "16 GB (👍 Recommended!)": 16, 
    "32 GB (🔼 Popular!)": 32, 
    "64 GB": 64, 
    "128 GB": 128
}

# storage_gb	
storage_gb_min = 256
storage_gb_max = 4000

# display_size_in	
display_size_in_min = 24.0
display_size_in_max = 32.0

# refresh_hz	
refresh_hz_options = {
    "60 hz": 60, 
    "75 hz": 75, 
    "90 hz": 90, 
    "120 hz (👍 Recommended!)": 120, 
    "144 hz (🔼 Popular!)": 144, 
    "165 hz": 165, 
    "180 hz (🔼 Popular!)": 180, 
    "240 hz": 240
}

# psu_watts
psu_watts_min = 300
psu_watts_max = 1000



## Streamlit app
def show():
    st.title("PC Price Predictor")
    
    st.header("Predict the Price of Your PC")
    
    # User input for PC specifications
    cpu = st.selectbox("Select CPU:", ["Intel i3", "Intel i5", "Intel i7", "AMD Ryzen 3", "AMD Ryzen 5", "AMD Ryzen 7"])
    ram = st.selectbox("Select RAM (in GB):", [4, 8, 16, 32])
    storage = st.selectbox("Select Storage (in GB):", [128, 256, 512, 1024])
    gpu = st.selectbox("Select GPU:", ["Integrated", "NVIDIA GTX 1650", "NVIDIA GTX 1660", "NVIDIA RTX 2060", "NVIDIA RTX 3060"])
    
    if st.button("Predict Price"):
        # Placeholder for prediction logic
        predicted_price = predict_price(cpu, ram, storage, gpu)
        st.success(f"The predicted price of the PC is: ${predicted_price}")

def predict_price(cpu, ram, storage, gpu):
    # Dummy prediction logic (replace with actual model)
    base_price = 300
    if "i5" in cpu:
        base_price += 100
    elif "i7" in cpu:
        base_price += 200
    if ram > 8:
        base_price += (ram - 8) * 50
    if storage > 512:
        base_price += (storage - 512) * 0.5
    if "NVIDIA" in gpu:
        base_price += 150
    
    return round(base_price, 2)

if __name__ == "__main__":
    show()