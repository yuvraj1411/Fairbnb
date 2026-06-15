Fairbnb: AI-Powered Real Estate Valuation Engine

🔗 View Live App: https://fairbnb-ai.streamlit.app/

📌 The Problem:

The New York City short-term rental market is highly volatile and densely saturated. Property hosts frequently rely on intuition rather than data to price their listings, leading to either massive revenue loss (underpricing) or stagnant vacancies (overpricing).

💡 The Solution:

Fairbnb is an end-to-end Machine Learning web application that predicts the optimal nightly rental price for NYC Airbnb properties. By architecting a customized Random Forest Regressor, the engine mathematically compares a user's specific property parameters against thousands of historical market successes to calculate a highly competitive, data-driven valuation.

🚀 Key Technical Achievements:

Optimized Predictive Accuracy (MAE: $29) - Iteratively tuned a Random Forest Regressor (n_estimators=200, max_depth=30) to achieve a Median Absolute Error of just $29 and an $R^2$ of 0.72. In a highly chaotic, human-driven real estate dataset, this provides hosts with an incredibly tight and actionable pricing buffer.

Custom NLP Feature Engineering - Engineered a dynamic "Luxury Index" by building a specialized NLP scanner. The pipeline scans raw property descriptions against an 85-word premium dictionary (capturing NYC-specific architectural "gold dust" like 'exposed brick', 'doorman', and 'pre-war'), quantifying qualitative aesthetic value into actionable numerical data.

Geographic Feature Protection - Prevented macro/micro-geographical data mismatching by engineering cascading dropdowns in the Streamlit frontend. The UI strictly forces valid macro-borough to micro-neighborhood mapping, ensuring the model never hallucinates predictions on impossible coordinates.

Outlier Guillotine & Data Cleaning - Sanitized heavily skewed historical pricing and bathroom data using RegEx extraction and strict statistical bounds, ensuring the model weights were not corrupted by luxury anomalies.

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

Computer Vision Integration - Adding an image upload feature allowing a CNN to grade interior design quality to replace the manual text-based Luxury Index.

Production Cloud Deployment - Containerizing the microservices using Docker and deploying the FastAPI backend to a dedicated cloud provider (like Render or AWS) to completely decouple the heavy ML compute from the Streamlit frontend UI.