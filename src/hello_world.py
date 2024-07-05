import random
import time

import mesop as me
import mesop.labs as mel


@me.page(
  security_policy=me.SecurityPolicy(
    allowed_iframe_parents=["https://google.github.io"]
  ),
  path="/chat",
  title="Mesop Demo Chat",
)
def chat(path="/chat"):
  me.button("back", on_click=navigate_to_home)
  mel.chat(transform, title="Mesop Demo Chat", bot_user="Mesop Bot")



def transform(input: str, history: list[mel.ChatMessage]):
  for line in random.sample(LINES, random.randint(3, len(LINES) - 1)):
    time.sleep(0.3)
    yield line + " "


LINES = [
  "Mesop is a Python-based UI framework designed to simplify web UI development for engineers without frontend experience.",
  "It leverages the power of the Angular web framework and Angular Material components, allowing rapid construction of web demos and internal tools.",
  "With Mesop, developers can enjoy a fast build-edit-refresh loop thanks to its hot reload feature, making UI tweaks and component integration seamless.",
  "Deployment is straightforward, utilizing standard HTTP technologies.",
  "Mesop's component library aims for comprehensive Angular Material component coverage, enhancing UI flexibility and composability.",
  "It supports custom components for specific use cases, ensuring developers can extend its capabilities to fit their unique requirements.",
  "Mesop's roadmap includes expanding its component library and simplifying the onboarding processs.",
]

def navigate_to_home(event: me.ClickEvent):
  me.navigate("/")

@me.page(path="/folder")
def folder():
  me.text("This is the folder page")
  me.button("back", on_click=navigate_to_home)

def navigate_to_chat(event: me.ClickEvent):
  me.navigate("/chat")
  

def navigate_to_folder(event: me.ClickEvent):
  me.navigate("/folder")


@me.page(path="/")
def home():
  me.text("This is the home page")
  me.button("navigate to chat page", on_click=navigate_to_chat)
  me.button("navigate to folder page", on_click=navigate_to_folder)