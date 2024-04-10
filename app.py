import streamlit as st
import joblib
# Load the saved model
model = joblib.load('linear_regression_model.pkl')
def main():
    # Set the app title
    st.title("Nominal GDP Prediction")

    # Add a sidebar for user input
    st.sidebar.header("Input Features")
    year = st.sidebar.number_input("Year")

    # Make predictions using the loaded model
    prediction = model.predict([[year]])

    # Display the predicted nominal GDP
    st.subheader("Predicted Nominal GDP")
    st.write(prediction[0])

if __name__ == "__main__":
    main()