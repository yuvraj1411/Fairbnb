import streamlit as st
import joblib
import pandas as pd
import os

# Model Loading
@st.cache_resource
def load_models():
    model_path = os.path.join('models', 'model.pkl')
    scaler_path = os.path.join('models', 'scaler.pkl')
    
    model = joblib.load(model_path)
    scaler = joblib.load(scaler_path)
    return model, scaler

model, scaler = load_models()

# Page Configuration
st.set_page_config(
    page_title="Fairbnb", 
    layout="wide",
    initial_sidebar_state="collapsed" 
)

# CSS Styling
st.markdown("""
    <style>
    .stApp {
        background-image: url("https://i.pinimg.com/1200x/cb/d4/24/cbd42403e5805a929b0e20f0f92021fa.jpg");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }
    
    .stApp::before {
        content: "";
        position: absolute;
        top: 0; left: 0; right: 0; bottom: 0;
        background-color: rgba(0, 0, 0, 0.85);
        z-index: 0;
    }

    .main, header, [data-testid="stSidebar"] {
        background-color: transparent !important;
        position: relative;
        z-index: 1;
    }
    
    [data-testid="stSidebar"] > div:first-child {
        background-color: rgba(0, 0, 0, 0.6) !important;
        backdrop-filter: blur(15px);
    }
    
    [data-testid="collapsedControl"] { display: none !important; }
    
    [data-testid="stRadio"] label[data-baseweb="radio"] > div:first-child {
        display: none !important;
    }
    
    [data-testid="stRadio"] label[data-baseweb="radio"] {
        background-color: rgba(255, 255, 255, 0.05) !important;
        padding: 14px 18px !important;
        border-radius: 8px !important;
        margin-bottom: 12px;
        cursor: pointer !important;
        transition: all 0.3s ease !important;
        border-left: 4px solid transparent !important;
        width: 100% !important;
    }
    
    [data-testid="stRadio"] label[data-baseweb="radio"]:hover {
        background-color: rgba(255, 255, 255, 0.15) !important;
        border-left: 4px solid #ff4b4b !important;
    }
    
    [data-testid="stRadio"] label[data-baseweb="radio"][aria-checked="true"] {
        background-color: rgba(255, 255, 255, 0.1) !important;
        border-left: 4px solid #ff4b4b !important;
    }
    
    h1, h2, h3, p, span, label, li, div[data-testid="stMarkdownContainer"] {
        color: #ffffff !important; 
        font-family: 'Inter', sans-serif;
    }
    
    div[data-baseweb="select"] input { caret-color: transparent; }
    
    .stButton>button {
        background-color: #ff4b4b; 
        color: white; 
        border-radius: 4px; 
        font-weight: 600; 
        width: 100%;
        border: none;
        padding: 10px;
    }
    
    .stButton>button:hover { background-color: #ff3333; color: white; }
    
    .prediction-card {
        background-color: rgba(255, 255, 255, 0.1); 
        backdrop-filter: blur(12px); 
        padding: 40px; 
        border-radius: 8px; 
        border-top: 4px solid #ff4b4b;
        box-shadow: 0 4px 15px rgba(0,0,0,0.5); 
        text-align: center;
        margin-top: 20px;
        margin-bottom: 20px;
    }
    
    .price-text {
        font-size: 3.5rem; 
        color: #ffffff; 
        font-weight: 700; 
        margin: 10px 0;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar Navigation
with st.sidebar:
    st.title("Menu")
    st.markdown("---")
    page = st.radio("Navigation", ["Valuation Engine", "How It Works", "Limitations"], label_visibility="collapsed")
    st.markdown("---")

# Main Pages
if page == "Valuation Engine":
    st.title("FAIRBNB")
    st.subheader("AI-Powered Real Estate Valuation Engine")
    st.markdown("Hosting an Airbnb in New York City? Input the details below and get a fair, data-driven estimate for your property's optimal rental rate.")
    st.markdown("---")
    
    st.markdown("### Property Specifications")

    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("##### Location & Classification")
        
        # Cascading Dropdown Logic
        neighborhood_map = {
            "Manhattan": ["Chelsea", "Chinatown", "East Harlem", "East Village", "Financial District", "Gramercy", "Harlem", "Hell's Kitchen", "Kips Bay", "Lower East Side", "Midtown", "Murray Hill", "Theater District", "Upper East Side", "Upper West Side", "Washington Heights", "West Village", "Other"],
            "Brooklyn": ["Bedford-Stuyvesant", "Bushwick", "Canarsie", "Clinton Hill", "Crown Heights", "Cypress Hills", "East Flatbush", "East New York", "Flatbush", "Greenpoint", "Park Slope", "Prospect-Lefferts Gardens", "Sunset Park", "Williamsburg", "Other"],
            "Queens": ["Astoria", "East Elmhurst", "Elmhurst", "Flushing", "Jamaica", "Long Island City", "Ridgewood", "Sunnyside", "Woodside", "Other"],
            "Bronx": ["Other"],
            "Staten Island": ["Other"]
        }
        
        borough = st.selectbox("Borough", list(neighborhood_map.keys()))
        specific_neighborhood = st.selectbox("Neighborhood", neighborhood_map[borough])
        room_type = st.selectbox("Room Type", ["Entire home/apt", "Private room", "Shared room", "Hotel room"])
    
    with col2:
        st.markdown("##### Architectural Capacity")
        accommodates = st.slider("Accommodates (Guests)", min_value=1, max_value=16, value=2)
        bedrooms = st.slider("Bedrooms", min_value=1, max_value=10, value=1)
        beds = st.slider("Beds", min_value=1, max_value=15, value=1)
        bathrooms = st.slider(
            "Bathrooms", 
            min_value=0.0, 
            max_value=5.0, 
            value=1.0, 
            step=0.5, 
            help="A 0.5 bathroom (half-bath) includes a toilet and a sink, but no shower or bathtub."
        )
        shared_bath = st.checkbox("Shared Bathroom Facility")
        
    with col3:
        st.markdown("##### Constraints")
        min_nights = st.number_input("Minimum Nights Requirement", min_value=1, max_value=365, value=1, step=1)
        availability = st.number_input("Annual Availability (Days)", min_value=0, max_value=365, value=180, step=1)
        
    st.markdown("##### Property Details")
    description = st.text_area("Give a brief description of your property", height=100)

    st.markdown("---")
    submitted = st.button("Generate Valuation")

    if submitted:
        with st.spinner("Analyzing property parameters & calculating metrics..."):
            try:
                # Calculating Luxury Score from description text
                desc_lower = description.lower()
                premium_words = [
                    'luxury', 'penthouse', 'doorman', 'view', 'rooftop', 'elevator', 
                    'balcony', 'terrace', 'spacious', 'renovated', 'designer',
                    'exposed brick', 'high ceilings', 'loft', 'hardwood', 'floor-to-ceiling', 
                    'skyline', 'panoramic', 'brownstone', 'pre-war', 'prewar', 'crown molding', 
                    'skylight', 'working fireplace', 'wood burning', 'french doors',
                    'marble', 'granite', 'quartz', 'stainless steel', "chef's", 
                    'wine fridge', 'wine cooler', 'sub-zero', 'miele', 'viking', 
                    'kitchen island', 'breakfast bar', 'walk-in pantry', 'custom cabinetry',
                    'jacuzzi', 'soaking tub', 'rain shower', 'heated floors', 'radiant heat', 
                    'steam shower', 'freestanding tub', 'clawfoot tub', 'double vanity', 'bidet',
                    'in-unit', 'washer', 'dryer', 'ac', 'tv', 'central air', 'central ac', 
                    'concierge', 'fitness center', 'gym', 'pool', 'roof deck', 
                    'private garden', 'private backyard', 'valet', 'private parking',
                    'espresso', 'nespresso', 'smart home', 'sonos', 'apple tv', 'peloton', 
                    'fast wifi', 'gigabit', 'keyless', 'motorized shades', 'home theater', 
                    'projector', 'walk-in closet', 'custom closet', 'duplex', 'triplex', 
                    'bespoke', 'curated', 'artisanal', 'egyptian cotton', 'hotel-quality'
                    ]
                luxury_score = sum(1 for word in premium_words if word in desc_lower)

                # Creating a blank dictionary that perfectly matches the model's expected columns
                expected_cols = model.feature_names_in_
                input_dict = {col: [0] for col in expected_cols}
                
                # Fill in the numerical features
                input_dict['accommodates'] = [accommodates]
                input_dict['bedrooms'] = [bedrooms]
                input_dict['beds'] = [beds]
                input_dict['bathrooms'] = [bathrooms]
                input_dict['minimum_nights'] = [min_nights]
                input_dict['availability_365'] = [availability]
                input_dict['is_shared_bath'] = [1 if shared_bath else 0]
                input_dict['luxury_score'] = [luxury_score]
                
                # Turning on the correct categorical dummy columns
                borough_col = f'neighbourhood_group_cleansed_{borough}'
                if borough_col in expected_cols:
                    input_dict[borough_col] = [1]
                    
                neigh_col = f'neighborhood_specific_{specific_neighborhood}'
                if neigh_col in expected_cols:
                    input_dict[neigh_col] = [1]
                    
                room_col = f'room_type_{room_type}'
                if room_col in expected_cols:
                    input_dict[room_col] = [1]
                
                # Building DataFrame and Scale
                input_df = pd.DataFrame(input_dict)
                cols_to_scale = ['accommodates', 'bedrooms', 'beds', 'bathrooms', 'minimum_nights', 'availability_365', 'luxury_score']
                input_df[cols_to_scale] = scaler.transform(input_df[cols_to_scale])
                
                # Predicting
                prediction_array = model.predict(input_df)
                predicted_price = float(prediction_array[0])
                
                error_margin = 31.76 
                
                lower_bound = max(30, predicted_price - error_margin) 
                upper_bound = predicted_price + error_margin
                
                st.markdown(
                    f"""
<div class="prediction-card">
<div style="font-size: 1.1rem; color: #ff4b4b; font-weight: 600; text-transform: uppercase; letter-spacing: 1px;">Target Nightly Rate</div>
<div class="price-text">${predicted_price:.0f} <span style="font-size: 1.5rem; color: #aaaaaa;">/ night</span></div>
<div style="margin-top: 25px; padding-top: 20px; border-top: 1px solid rgba(255,255,255,0.1);">
<div style="color: #eeeeee; font-size: 1.2rem;">Competitive Price Bracket: <b>${lower_bound:.0f} - ${upper_bound:.0f}</b></div>
</div>
</div>
                    """, 
                    unsafe_allow_html=True
                )
                
            except Exception as e:
                st.error(f"Error making prediction: {e}")

elif page == "How It Works":
    st.title("Demystifying the Algorithm")
    st.markdown("---")
    st.write("If you aren't a data scientist, \"Artificial Intelligence\" can sound like magic. But underneath the hood, it is simply advanced pattern recognition. Here is exactly what happens when you click **Generate Valuation**:")
    
    st.markdown("#### 1. Historical Learning (The Dataset)")
    st.write("Before this app was ever built, our AI studied thousands of real, historical rental listings across New York City. It looked at the relationships between a property's features (like having 3 bedrooms in Manhattan vs. 1 bedroom in Queens) and its final nightly price.")
    
    st.markdown("#### 2. The 'Council of Agents' (The Algorithm)")
    st.write("Fairbnb uses a machine learning structure called a Random Forest, which acts a lot like a council of real estate agents. When you enter your property details, the algorithm creates hundreds of different 'decision trees'—think of them as individual agents, each looking at your property from a slightly different perspective.")
    
    st.markdown("#### 3. Reaching a Consensus")
    st.write("Some 'agents' might focus heavily on your neighborhood, while others might focus on the number of bathrooms and your minimum night requirement. They all make a price prediction based on the historical data they memorized. Finally, the algorithm averages all of those individual guesses together to give you one highly accurate, optimal nightly rate.")
    
    st.info("**In short:** Fairbnb doesn't just guess a price. It mathematically compares your specific property setup to thousands of past successes to find the exact price point the current market dictates.")

elif page == "Limitations":
    st.title("Model Confidence & Limitations")
    st.markdown("---")
    
    st.write("We believe in being completely transparent about how this tool works so you can make the best pricing decisions.")
    st.write("") 
    
    lim_col1, lim_col2 = st.columns([1, 2])
    
    with lim_col1:
        st.metric(
            label="Median Absolute Error (MAE)", 
            value="±$31.76", 
            delta="Expected Variance", 
            delta_color="off",
            help="On average, our baseline prediction sits within $31.76 of the actual market rate for standard units."
        )
        st.info("**Pro Tip:** Use this AI estimate as your baseline, then adjust it up or down based on your property's unique charm.")
        
    with lim_col2:
        st.markdown("#### What this means for you:")
        
        st.markdown(r"""
        * **The Heavy Lifting:** The NYC rental market is chaotic. Our algorithm successfully cuts through that noise to calculate the core value of your property based strictly on hard data (location, bedrooms, architectural capacity, and natural language processing).

        * **The Human Factor (The \$31 Buffer):** Mathematics cannot see your interior design, maybe a stunning skyline view or your exceptional hospitality as a host. This \$31 median range acts as a "Competitive Pricing Buffer." 

        * **How to use this tool:** Treat this tight range as a data-driven foundation. Take our baseline, factor in the unique vibe of your space, and confidently set your final price.
        """)