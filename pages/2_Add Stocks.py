import streamlit as st
from datetime import datetime
from pymongo import MongoClient

st.set_page_config(
    page_icon= "➕",
    page_title= "Add Stocks"
)
st.header("Add Stocks")

client = MongoClient(st.secrets["connection_string"])

db = client["stockify"]

selectedBranch = st.selectbox("Select the branch", ["Head", "Ambur", "Khadherpet"])

itemsList = [i["name"] for i in db["items"].find()]

name = st.selectbox("What type of stock", itemsList)
nos = st.number_input("Number of units",step=1)
price = st.number_input("Price of each unit", step=0.5)
remarks = st.text_input("Remarks")

if st.button("Add Entry"):
    data = {
        "Item name" : name,
        "Price of one unit" : price,
        "Number of units" : nos,
        "Total price" : (price * nos),
        "Added on" : datetime.today().replace(microsecond=0),
        "Report" : remarks
    }   

    stock = db[selectedBranch]

    stock.insert_one(data)
