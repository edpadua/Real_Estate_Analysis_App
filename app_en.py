import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import joblib

# ====================================================================
# PART 1: MODEL TRAINING AND DATA SIMULATION (The Analysis Engine)
# ====================================================================

# @st.cache_data ensures the model is trained only once, regardless of user interaction.
@st.cache_data
def train_model():
    st.info("Training the pricing model... (This message disappears after initial training)")
    
    # 1. Simulated Data Generation
    # **In a real project, replace this step by reading a CSV/Database file.**
    np.random.seed(42)
    size = 1000

    # Features
    area = np.random.randint(50, 300, size) # Area in sqm
    bedrooms = np.random.randint(1, 5, size) # Number of bedrooms
    distance_downtown = np.random.uniform(1, 20, size) # Distance from downtown in km
    
    # Generating Price: Price = f(Area, Bedrooms, Distance) + Noise
    price = (1200 * area +
             40000 * bedrooms -
             9000 * distance_downtown +
             np.random.normal(0, 70000, size))

    # Creating the DataFrame
    df = pd.DataFrame({
        'Area_sqm': area,
        'Bedrooms': bedrooms,
        'Distance_Downtown_km': distance_downtown,
        'Price_BRL': price
    })

    # Ensure minimum prices are reasonable
    df['Price_BRL'] = df['Price_BRL'].apply(lambda x: max(100000, x))

    # 2. Model Training
    X = df[['Area_sqm', 'Bedrooms', 'Distance_Downtown_km']]
    y = df['Price_BRL']

    model = LinearRegression()
    model.fit(X, y)

    # 3. Saving the model (Good practice)
    joblib.dump(model, 'real_estate_model.pkl')
    
    return model, df, X.columns # Returns the model, data, and feature names

# Train the model and load objects upon app startup
model, data, feature_names = train_model()


# ====================================================================
# PART 2: STREAMLIT WEB INTERFACE
# ====================================================================

def main():
    st.set_page_config(page_title="Real Estate Analysis App", layout="wide")
    
    st.title("🏡 Real Estate Analysis and Recommendation App")
    st.markdown("---")
    st.subheader("⚙️ Enter Property Characteristics for Analysis")

    # Function to format currency (Using a generic BRL format for consistency with the simulated data)
    def format_currency(value):
        # Using comma as thousand separator and period as decimal separator for a clear display (BRL standard)
        return f"R$ {value:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


    # ------------------------------------
    # USER INPUT SECTION
    # ------------------------------------
    
    col_input_1, col_input_2, col_input_3, col_input_4 = st.columns(4)

    # User Inputs
    with col_input_1:
        area_user = st.slider("Area (sqm)", 50, 300, 100)
    with col_input_2:
        bedrooms_user = st.slider("Number of Bedrooms", 1, 5, 2)
    with col_input_3:
        distance_user = st.slider("Distance from Downtown (km)", 1.0, 20.0, 5.0, step=0.5)
    with col_input_4:
        asking_price_user = st.number_input("Asking Price (BRL)", min_value=100000, value=300000, step=5000)

    # 1. Prepare input data
    input_data = pd.DataFrame({
        'Area_sqm': [area_user],
        'Bedrooms': [bedrooms_user],
        'Distance_Downtown_km': [distance_user]
    })

    # 2. Make Prediction
    predicted_price = model.predict(input_data)[0]

    # 3. Present Results
    st.markdown("---")
    st.subheader("✅ Price Analysis Results")
    
    col_result_1, col_result_2 = st.columns(2)
    
    with col_result_1:
        st.metric(label="Reported Asking Price", value=format_currency(asking_price_user))
    
    with col_result_2:
        st.metric(label="Fair Price Estimated by the Model", value=format_currency(predicted_price))
        
    # 4. Recommendation Analysis (The Portfolio Differentiator)
    difference = asking_price_user - predicted_price
    
    st.markdown("### Investment Suggestion")
    
    if difference < -10000: # Asking price significantly below predicted
        st.success(f"**Recommendation:** 💰 Great Opportunity! The asking price is **{format_currency(abs(difference))}** below the estimated fair value. The model suggests this is a good deal.")
        st.balloons()
        
    elif difference > 10000: # Asking price significantly above predicted
        st.error(f"**Recommendation:** ⚠️ Elevated Price. The asking price is **{format_currency(difference)}** above the estimated fair value. Caution or strong negotiation is recommended.")
        
    else: # Price is within the acceptable range
        st.info("🤝 **Recommendation:** Aligned Price. The asking price is very close to the fair value estimated by the model.")

    st.markdown("---")
    
    # Displaying model coefficients for transparency (Data Science)
    st.subheader("📈 Statistical Influence of Features")
    
    # Creating the Coefficients DataFrame
    coefficients = pd.DataFrame({
        'Feature': feature_names,
        'Coefficient': model.coef_
    })
    
    # Calculating the formatted Impact
    coefficients['Estimated Impact'] = coefficients['Coefficient'].apply(
        lambda x: f"Adds {format_currency(abs(x))} to the final price" if x > 0 else f"Subtracts {format_currency(abs(x))} from the final price"
    )
    
    # Adjust feature names for better display
    coefficients['Feature'] = ['Area (sqm)', 'Bedrooms', 'Distance from Downtown (km)']

    st.dataframe(coefficients[['Feature', 'Estimated Impact']], hide_index=True, use_container_width=True)
    st.caption("*The estimated impact is the value the model adds/subtracts from the price for each 1-unit increase in the feature, holding others constant.*")

# Run the main function
if __name__ == '__main__':
    main(