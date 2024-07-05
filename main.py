from src.pages.home import home
from src.pages.chat import chat
from src.pages.folder import folder
import mesop as me

@me.page(
  security_policy=me.SecurityPolicy(allowed_iframe_parents=["https://google.github.io"]),
  path="/chat",
  title="Mesop Demo Chat",
)
def c(): chat()

@me.page(path="/folder")
def f(): folder() 

@me.page(path="/")
def h(): home()