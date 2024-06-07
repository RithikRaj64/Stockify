import streamlit as st
from pymongo import MongoClient

st.set_page_config(
    page_icon= "🆕",
    page_title= "Add New Item"
)
st.header("Add New Item")

client = MongoClient(st.secrets["connection_string"])
db = client["stockify"]
items = db["items"]

name = st.text_input("Enter the name of the new Item")

if st.button("Add Item"):
    item = {"name" : name}
    items.insert_one(item)