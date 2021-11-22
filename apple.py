import streamlit as st
from multiapp import MultiApp
from apps import cartoonify,filters,toonify

app = MultiApp.MultiApp()
app.add_app("filters", filters.app)
app.add_app("cartoonify", cartoonify.app)
app.add_app("toonify",toonify.app)
app.run()
