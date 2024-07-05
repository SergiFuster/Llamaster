import mesop as me

def navigate_to_home(event: me.ClickEvent):
  me.navigate("/")


def navigate_to_chat(event: me.ClickEvent):
  me.navigate("/chat")
  

def navigate_to_folder(event: me.ClickEvent):
  me.navigate("/folder")