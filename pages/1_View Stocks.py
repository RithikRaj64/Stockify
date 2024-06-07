import streamlit as st
import pandas as pd
from pymongo import MongoClient

st.set_page_config(
    page_icon= "📃",
    page_title= "View Stocks"
)
st.header("View Stocks")

client = MongoClient(st.secrets["connection_string"])

db = client["stockify"]
stock = None

selectedBranch = st.selectbox("Select the branch", ["Head", "Ambur", "Khadherpet"])

stock = db[selectedBranch]

itemsList = [i["name"] for i in db["items"].find()]
itemsList.insert(0, "All Items")
selectedItem = st.selectbox("Select the item", itemsList)

li = None
df = None

if st.button("View Stocks"):
    if selectedItem == "All Items":
        li = list(stock.find())
        for i in li:
            i["Added on"] = i["Added on"].strftime("%d-%m-%Y")
        df = pd.DataFrame(li, columns=("Item name", "Number of units", "Price of one unit", "Total price", "Added on", "Remarks"))
    else:
        li = list(stock.find({"Item name" : selectedItem}))
        for i in li:
            i["Added on"] = i["Added on"].strftime("%d-%m-%Y")
        df = pd.DataFrame(li, columns=("Number of units", "Price of one unit", "Total price", "Added on", "Remarks"))

    df = df.reset_index(drop=True) 
    df.index = df.index + 1

    st.dataframe(df)