import streamlit as st
import joblib
def main():
    # Set the app title
    st.title("Real GDP Price Prediction")

    # Add a sidebar for user input
    st.sidebar.header("Input Features")
    nominal_gdp = st.sidebar.number_input("Nominal GDP Prices (Ksh Million)")

    # Make predictions using the loaded model
    prediction = model.predict([[nominal_gdp]])

    # Display the predicted real GDP price
    st.subheader("Predicted Real GDP Price")
    st.write(prediction[0])

if __name__ == "__main__":
    main()