import streamlit as st
from datetime import datetime
from pymongo import MongoClient

st.set_page_config(
    page_icon= "🚚",
    page_title= "Take Stocks"
)
st.header("Take Stocks")

client = MongoClient(st.secrets["connection_string"])

db = client["stockify"]

selectedBranch = st.selectbox("Select the branch", ["Head", "Ambur", "Khadherpet"])

itemsList = [i["name"] for i in db["items"].find()]

name = st.selectbox("What type of stock", itemsList)
nos = st.number_input("Number of units",step=1)
remarks = st.text_input("Remarks")

if st.button("Take Stock"):
    stock = db[selectedBranch]
    register = db[selectedBranch + "_Reg"]

    li = list(stock.find({"Item name" : name}))

    li = sorted(li, key=lambda x : x["Added on"])
    taken = []

    while True:
        entry = li[0]
        query = {"_id" : li[0]["_id"]}
        if(entry["Number of units"] > nos):            
            new = { "$set" : {"Number of units" :  entry["Number of units"] - nos}}
            stock.update_one(query, new)
            entry["Number of units"] = nos
            taken.append(entry)
            break
        elif(entry["Number of units"] == nos):
            stock.delete_one(query)
            entry["Number of units"] = nos
            taken.append(entry)
            break
        else:
            nos = nos - entry["Number of units"]
            stock.delete_one(query)
            li.remove(entry)
            entry["Number of units"] = nos
            taken.append(entry)

    register.insert_many(taken)

    st.write(li)