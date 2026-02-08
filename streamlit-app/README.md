# Streamlit PC Price Predictor App

This project is a Streamlit application that allows users to predict PC prices based on various input parameters. The app features a sidebar for easy navigation between different pages.

## Project Structure

```
streamlit-app
├── src
│   ├── app.py                     # Main entry point of the Streamlit application
│   ├── pages
│   │   ├── home.py                # Home page content
│   │   ├── pc_price_predictor.py   # PC Price Predictor functionality
│   │   └── about.py               # About page information
│   └── utils
│       └── __init__.py            # Utility functions and classes
├── requirements.txt                # List of dependencies
└── README.md                       # Project documentation
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd streamlit-app
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the Streamlit application:
   ```
   streamlit run src/app.py
   ```

## Usage

- **Home**: The landing page of the application.
- **PC Price Predictor**: Input various parameters to predict the price of a PC.
- **About**: Learn more about the application and its purpose.

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes.