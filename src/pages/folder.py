import mesop as me
from ..router import *

def folder():
  me.text("This is the folder page")
  me.button("back", on_click=navigate_to_home)