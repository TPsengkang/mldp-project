import base64
import streamlit as st
import joblib
import numpy as np
import pandas as pd
from pathlib import Path

## Load trained model
model = joblib.load(Path(__file__).parents[3] / "best_linear_regression_model.pkl")

def _img_to_base64(path: Path) -> str:
    return base64.b64encode(path.read_bytes()).decode("utf-8")

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
    "RTX 3070 (👍 Recommended!)": "RTX 30 70",
    "RTX 3080": "RTX 30 80",
    "RTX 3080 Ti": "RTX 30 80 Ti",
    "RTX 3090": "RTX 30 90",
    "RTX 4050": "RTX 40 50",
    "RTX 4060 (🔼 Popular!)": "RTX 40 60",
    "RTX 4070 (🔼 Popular!)": "RTX 40 70",
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
    "RX 6700 (👍 Recommended!)": "RX 6000 70",
    "RX 6800": "RX 6000 80",
    "RX 6800 XT": "RX 6000 80 XT",
    "RX 6900": "RX 6000 90",
    "RX 7500": "RX 7000 50",
    "RX 7600": "RX 7000 60",
    "RX 7700": "RX 7000 70",
    "RX 7800": "RX 7000 80",
    "RX 7800 XT (🔼 Popular!)": "RX 7000 80 XT",
    "RX 7900": "RX 7000 90"
}

##Storage types
storage_type = {
    'SSD (👍 Recommended!)': 'SSD',
    'Hybrid (👍 Recommended!)': 'Hybrid' ,
    'NVMe': 'NVMe', 
    'HDD': 'HDD', 
    
}

##Display types
display_type = {
    'QLED (👍 Recommended!)' : 'QLED',
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
cpu_base_ghz_max = 4.7

# Popular CPU models:
# Format: <Display name> : [<threads>, <base ghz>]
cpu_models = {
    "Intel i5-12400F": [12, 2.5],
    "Intel i5-12600K": [16, 3.7],
    "Intel i5-13400F (👍 Recommended!)": [16, 2.5],
    "Intel i5-13600K": [20, 3.5],
    "Intel i7-12700K": [20, 3.6],
    "Intel i7-13700K": [24, 3.4],
    "Intel i9-12900K": [24, 3.2],
    "Intel i9-13900K": [32, 3.0], 
    "AMD Ryzen 5 3600": [12, 3.6],
    "AMD Ryzen 5 5600": [12, 3.5],
    "AMD Ryzen 5 5600X (👍 Recommended!)": [12, 3.7], 
    "AMD Ryzen 5 7600": [12, 3.8],
    "AMD Ryzen 5 7600X": [12, 4.7], 
    "AMD Ryzen 7 5700G": [16, 3.8], 
    "AMD Ryzen 7 5800X": [16, 3.8], 
    "AMD Ryzen 7 7700X": [16, 4.5], 
    "AMD Ryzen 9 5900X": [24, 3.7], 
    "AMD Ryzen 9 5950X": [32, 3.4], 
    "AMD Ryzen 9 7900X": [24, 4.7],
    "AMD Ryzen 9 7950X": [32, 4.5], 
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
@st.dialog("Estimated PC Price")
def show_prediction_modal(prediction, summary):
    st.success("✅ Prediction Complete!")
    st.metric(
        label="Estimated PC Price",
        value=f"${prediction:,.2f}",
        help="Machine learning predicted price based on your configuration"
    )

    with st.expander("📋 View Configuration Summary"):
        st.markdown("**System Configuration:**")
        st.write(f"• Operating System: {summary['os_display']}")

        st.markdown("**Core Components:**")
        st.write(f"• CPU: {summary['cpu_threads']} threads @ {summary['cpu_base_ghz']} GHz")
        if summary["cpu_reference"] != "Custom":
            st.write(f"  _(Reference: {summary['cpu_reference']})_")
        st.write(f"• GPU: {summary['gpu_display']} ({summary['vram_gb']}GB VRAM)")
        st.write(f"• RAM: {summary['ram_display']}")

        st.markdown("**Storage:**")
        st.write(f"• Type: {summary['storage_type_display']}")
        st.write(f"• Capacity: {summary['storage_gb']}GB")

        st.markdown("**Display:**")
        st.write(f"• Size: {summary['display_size_in']}\" {summary['display_type_display']}")
        st.write(f"• Resolution: {summary['resolution_display']}")
        st.write(f"• Refresh Rate: {summary['refresh_hz_display']}")

        st.markdown("**Power:**")
        st.write(f"• PSU: {summary['psu_watts']}W")

def show():
    st.title("💻 PC Price Predictor")
    st.markdown("Configure your dream PC build and get an instant price estimate!")

    bg_img = _img_to_base64(Path(__file__).resolve().parents[1] / "images" / "predictor_background.jpg")
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image:
                linear-gradient(rgba(0, 0, 0, 0.65), rgba(0, 0, 0, 0.65)),
                url("data:image/jpg;base64,{bg_img}");
            background-size: 100% auto;
            background-repeat: no-repeat;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
    
    st.divider()
    
    # Operating System
    st.subheader("⚙️ System Configuration")
    os_placeholder = "- Select operating system -"
    os_display = st.selectbox(
        "Operating System",
        options=[os_placeholder] + list(OS_options.keys()),
        help="Choose your preferred operating system"
    )
    os_value = None if os_display == os_placeholder else OS_options[os_display]
    
    st.divider()
    
    # CPU Section
    st.subheader("🖥️ Processor (CPU)")
    cpu_reference = st.selectbox(
        "Reference CPU Models (Optional)",
        options=["Custom"] + list(cpu_models.keys()),
        help="Select a popular CPU model to auto-fill specs, or choose 'Custom' to enter manually"
    )
    cpu_reference_value = cpu_reference
    is_custom_cpu = cpu_reference_value == "Custom"
    
    # Auto-fill CPU specs if a reference model is selected
    if not is_custom_cpu:
        default_threads = cpu_models[cpu_reference][0]
        default_ghz = cpu_models[cpu_reference][1]
    else:
        default_threads = cpu_threads_min
        default_ghz = cpu_base_ghz_min
    
    cpu_threads = st.slider(
        "CPU Threads",
        min_value=cpu_threads_min,
        max_value=cpu_threads_max,
        value=default_threads,
        step=2,
        help="Number of CPU threads (higher = better multitasking)",
        disabled=not is_custom_cpu
    )
    
    cpu_base_ghz = st.slider(
        "CPU Base Clock (GHz)",
        min_value=cpu_base_ghz_min,
        max_value=cpu_base_ghz_max,
        value=default_ghz,
        step=0.1,
        help="Base clock speed in GHz (higher = faster single-core performance)",
        disabled=not is_custom_cpu
    )
    
    st.divider()
    
    # GPU Section
    st.subheader("🎮 Graphics Card (GPU)")
    gpu_placeholder = "- Select GPU model -"
    gpu_display = st.selectbox(
        "GPU Model",
        options=[gpu_placeholder] + list(gpu_models.keys()),
        help="Your graphics card model"
    )
    gpu_value = None if gpu_display == gpu_placeholder else gpu_models[gpu_display]
    
    vram_gb = st.slider(
        "VRAM (GB)",
        min_value=vram_gb_min,
        max_value=vram_gb_max,
        value=8,
        step=2,
        help="Video RAM for graphics processing"
    )
    
    st.divider()
    
    # Memory Section
    st.subheader("🧠 Memory (RAM)")
    ram_placeholder = "- Select system memory -"
    ram_display = st.selectbox(
        "System Memory",
        options=[ram_placeholder] + list(ram_gb_options.keys()),
        help="System RAM for general computing"
    )
    ram_value = None if ram_display == ram_placeholder else ram_gb_options[ram_display]
    
    st.divider()
    
    # Storage Section
    st.subheader("💾 Storage")
    storage_type_placeholder = "- Select storage type -"
    storage_type_display = st.selectbox(
        "Storage Type",
        options=[storage_type_placeholder] + list(storage_type.keys()),
        help="Type of storage drive"
    )
    storage_type_value = None if storage_type_display == storage_type_placeholder else storage_type[storage_type_display]
    
    storage_gb = st.slider(
        "Storage Capacity (GB)",
        min_value=storage_gb_min,
        max_value=storage_gb_max,
        value=1024,
        step=256,
        help="Total storage capacity"
    )
    
    st.divider()
    
    # Display Section
    st.subheader("🖥️ Display")
    display_type_placeholder = "- Select display type -"
    display_type_display = st.selectbox(
        "Display Panel Type",
        options=[display_type_placeholder] + list(display_type.keys()),
        help="Monitor panel technology"
    )
    display_type_value = None if display_type_display == display_type_placeholder else display_type[display_type_display]
    
    display_size_in = st.slider(
        "Display Size (inches)",
        min_value=display_size_in_min,
        max_value=display_size_in_max,
        value=27.0,
        step=0.5,
        help="Monitor diagonal size in inches"
    )
    
    resolution_placeholder = "- Select resolution -"
    resolution_display = st.selectbox(
        "Resolution",
        options=[resolution_placeholder] + list(resolution.keys()),
        help="Screen resolution"
    )
    resolution_value = None if resolution_display == resolution_placeholder else resolution[resolution_display]
    
    refresh_hz_placeholder = "- Select refresh rate -"
    refresh_hz_display = st.selectbox(
        "Refresh Rate",
        options=[refresh_hz_placeholder] + list(refresh_hz_options.keys()),
        help="Monitor refresh rate (higher = smoother visuals)"
    )
    refresh_hz_value = None if refresh_hz_display == refresh_hz_placeholder else refresh_hz_options[refresh_hz_display]
    
    st.divider()
    
    # PSU Section
    st.subheader("⚡ Power Supply")
    psu_watts = st.slider(
        "Power Supply (Watts)",
        min_value=psu_watts_min,
        max_value=psu_watts_max,
        value=650,
        step=50,
        help="PSU wattage capacity"
    )
    
    st.divider()
    
    # Prediction button
    predict_button = st.button("🔮 Predict Price", type="primary", use_container_width=True)
    
    if predict_button:
        missing_fields = []
        # Validate required fields by checking normalized values
        if os_value is None:
            missing_fields.append("Operating System")
        if gpu_value is None:
            missing_fields.append("GPU Model")
        if ram_value is None:
            missing_fields.append("System Memory")
        if storage_type_value is None:
            missing_fields.append("Storage Type")
        if display_type_value is None:
            missing_fields.append("Display Type")
        if resolution_value is None:
            missing_fields.append("Resolution")
        if refresh_hz_value is None:
            missing_fields.append("Refresh Rate")

        if missing_fields:
            st.error("Please select: " + ", ".join(missing_fields))
            return

        # Prepare input data for prediction
        X_unseen_df = pd.DataFrame({
            'os': [os_value],
            'cpu_threads': [cpu_threads],
            'cpu_base_ghz': [cpu_base_ghz],
            'gpu_model': [gpu_value],
            'vram_gb': [vram_gb],
            'ram_gb': [ram_value],
            'storage_type': [storage_type_value],
            'storage_gb': [storage_gb],
            'display_type': [display_type_value],
            'display_size_in': [display_size_in],
            'resolution': [resolution_value],
            'refresh_hz': [refresh_hz_value],
            'psu_watts': [psu_watts]
        })
        
        # One-hot encoding
        X_unseen_ohe = pd.get_dummies(X_unseen_df,
                                    columns=['os', 'gpu_model', 'storage_type', 'display_type', 'resolution']
                                    )
        X_unseen_ohe = X_unseen_ohe.reindex(columns=model.feature_names_in_,
                                            fill_value=0)
        
        try:
            prediction = model.predict(X_unseen_ohe)[0]

            summary = {
                "os_display": os_display,
                "cpu_threads": cpu_threads,
                "cpu_base_ghz": cpu_base_ghz,
                "cpu_reference": cpu_reference,
                "gpu_display": gpu_display,
                "vram_gb": vram_gb,
                "ram_display": ram_display,
                "storage_type_display": storage_type_display,
                "storage_gb": storage_gb,
                "display_size_in": display_size_in,
                "display_type_display": display_type_display,
                "resolution_display": resolution_display,
                "refresh_hz_display": refresh_hz_display,
                "psu_watts": psu_watts,
            }

            show_prediction_modal(prediction, summary)
            
        except Exception as e:
            st.error(f"⚠️ Prediction error: {str(e)}")
            st.error(F"Values = {X_unseen_df.values.tolist()}")
            st.error(F"Values (OHE) = {X_unseen_ohe.columns.tolist()}")

if __name__ == "__main__":
    show()