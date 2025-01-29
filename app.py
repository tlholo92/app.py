import streamlit as st
import pandas as pd


# Title of the app
st.title("Researcher Profile Page")

# Display an image
st.image("GAS.jpg")

# Collect basic information
name = "Peloane Tlhologelo"
field = "Medical Microbiology"
institution = "Sefako Makgatho Health Sciences University"

# Display basic profile information
st.header("Researcher Overview")
st.write(f"**Name:** {'Peloane Tlhologelo'}")

st.write(f"**Field of Research:** {'Medical Microbiology'}")
st.write(f"**Institution:** {'Sefako Makgatho Health Sciences University'}")

# Add a section for publications
st.header("Publications")
uploaded_file = st.file_uploader("Upload a CSV of Publications", type="csv")

if uploaded_file:
    publications = pd.read_csv(uploaded_file)
    st.dataframe(publications)

    # Add filtering for year or keyword
    keyword = st.text_input("Filter by keyword", "")
    if keyword:
        filtered = publications[
            publications.apply(lambda row: keyword.lower() in row.astype(str).str.lower().values, axis=1)
        ]
        st.write(f"Filtered Results for '{keyword}':")
        st.dataframe(filtered)
    else:
        st.write("Showing all publications")

# Add a section for visualizing publication trends
st.header("Publication Trends")
if uploaded_file:
    if "Year" in publications.columns:
        year_counts = publications["Year"].value_counts().sort_index()
        st.bar_chart(year_counts)
    else:
        st.write("The CSV does not have a 'Year' column to visualize trends.")

# Add a contact section
st.header("Contact Information")
email = "tlhologelo.peloane@gmail.com"
st.write(f"You can reach {'Peloane Tlhologelo'} at {'tlhologelo.peloane@gmail.com'}.")
