Fairbnb: AI-Powered Real Estate Valuation Engine

🔗 View Live App: https://fairbnb-ai.streamlit.app/

📌 The Problem:

The New York City short-term rental market is highly volatile and densely saturated. Property hosts frequently rely on intuition rather than data to price their listings, leading to either massive revenue loss (underpricing) or stagnant vacancies (overpricing).

💡 The Solution:

Fairbnb is an end-to-end Machine Learning web application that predicts the optimal nightly rental price for NYC Airbnb properties. By architecting a customized Random Forest Regressor, the engine mathematically compares a user's specific property parameters against thousands of historical market successes to calculate a highly competitive, data-driven valuation.

🚀 Key Technical Achievements:

Optimized Predictive Accuracy (MAE: $29) - Iteratively tuned a Random Forest Regressor (n_estimators=250, max_depth=28) to achieve a Median Absolute Error of just $29 and an $R^2$ of 0.72. In a highly chaotic, human-driven real estate dataset, this provides hosts with an incredibly tight and actionable pricing buffer.

Outlier Guillotine & Data Cleaning - Sanitized heavily skewed historical pricing and property data using strict statistical bounds and engineered feature extraction. This rigorous preprocessing pipeline ensures the core model weights remain uncorrupted by extreme luxury anomalies or erroneous data entries.

Interactive Geospatial Intelligence - Engineered an interactive map coordinate extractor (`streamlit-folium`) to capture exact Latitude and Longitude of the property instead of relying on generic neighborhood labels.

⚙️ Local Installation & Usage:

To run this application locally on your machine - 

1. Clone the repository

    git clone https://github.com/YOUR_USERNAME/Fairbnb.git

    cd Fairbnb

2. Install the required dependencies

   pip install -r requirements.txt

3. Boot up the Valuation Engine
   
   IN YOUR FIRST TERMINAL - uvicorn api:app --reload

   IN YOUR SECOND TERMINAL - streamlit run app.py

🔮 Future Scope:

Computer Vision Integration - Adding an image upload feature allowing a CNN to grade interior design quality.

Production Cloud Deployment - Containerizing the microservices using Docker and deploying the FastAPI backend to a dedicated cloud provider (like Render or AWS) to completely decouple the heavy ML compute from the Streamlit frontend UI.