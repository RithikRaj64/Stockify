import streamlit as st

st.set_page_config(
    page_icon= "📦",
    page_title= "Stockify"
)

st.header("Welcome to Stockify")

st.markdown("------")

st.header("Introduction")
st.write("Your all-in-one solution for efficient stock management. Whether you're overseeing inventory for a small business or a large enterprise, our platform simplifies the process, saving you time and resources.")

st.header("Features")
st.markdown('''
- **View Stocks:**

    Easily monitor your inventory in real-time with our intuitive view stocks page. Get insights into stock levels, locations, and more at a glance.

- **Add Stocks:** 
            
    Seamlessly add new items to your inventory with our add stocks page. Streamline the process and keep your inventory up-to-date with just a few clicks.

- **Take Stocks:** 
            
    Keep track of stock movements effortlessly with our take stocks page. Update stock quantities, locations, and statuses with ease.

- **Add New Item:** 
            
    Introduce new items to your inventory effortlessly using our add new item page. Simply input the necessary details, and your new item is ready to be tracked.

- **View Taken Register:** 
            
    Stay informed about stock transactions with our view taken register page. Access comprehensive logs of stock movements, ensuring transparency and accountability.
''')
