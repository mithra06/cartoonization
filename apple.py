import streamlit as st
from multiapp import MultiApp
from apps import cartoonify,filters,toonify
var port = process.env.PORT || 8080

app = MultiApp()
app.add_app("filters", filters.app)
app.add_app("cartoonify", cartoonify.app)
app.add_app("toonify",toonify.app)
app.run()

app.listen(port,()=>{
  console.log('server is running')});
