import streamlit as st
import requests
import csv
from arxiv_api import *
import numpy as np
from time import sleep

st.title("Arxiv MetaData scraper")
st.write("Search details:")


category = st.selectbox("Category", ["AI", "Computation and Language", "Computer Vision", "ML"])
sort_order = st.selectbox("Sort Order", ["ascending", "descending"])
sort_by = st.selectbox("Sort By", ["Relevance", "Lastupdated", "Submitted"])
max_results = st.slider("Max Results", 1, 50000, 100)
# start = st.slider("Start", 1, 50000, 1)
search_button = st.button('Search with Keyword')


search_keyword = ''


if search_button:
    search_keyword = st.text_input('Enter keyword')

cat_map = {"AI":"cs.AI", "Computation and Language":"cs.CL", "Computer Vision":"cs.CV", "ML":"cs.LG"}


if st.button("Download CSV"):
    total_data = []
    page_size = min(max_results, 500)
    starts = np.arange(1, max_results, page_size)
    print(starts)
    progress_bar = st.empty()
    try:
        for i, start in enumerate(starts):
            print(i, start)

            end = min(max_results, start + page_size - 1)


            progress = (i + 1) / len(starts)
            progress_bar.progress(progress)


            response = get_data(search_keyword, cat_map.get(category),sort_by, sort_order, page_size, start)
            sleep(5)

            total_data.extend(response)
        with open("arxiv_details.csv", "w") as f:
            writer = csv.writer(f)
            writer.writerow(["Id","Title","Summary", "Authors", "Published"])
            for row in total_data:
                writer.writerow(row)
            
        with open("arxiv_details.csv", "r") as f:
            st.download_button("Download CSV File", data=f, file_name="arxiv_details.csv", mime="text/csv")
    except:
        st.write("Error occured, Please try again .....")
