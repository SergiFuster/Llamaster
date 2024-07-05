import mesop as me
import mesop.labs as mel
from ..router import *
from ..utils import *

def chat():
  me.button("back", on_click=navigate_to_home)
  mel.chat(transform, title="Mesop Demo Chat", bot_user="Mesop Bot")