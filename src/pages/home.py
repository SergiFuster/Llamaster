import mesop as me
from ..router import *

def home():
  me.text("This is the home page")
  me.button("navigate to chat page", on_click=navigate_to_chat)
  me.button("navigate to folder page", on_click=navigate_to_folder)