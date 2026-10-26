from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from talkingheads import PiClient
from talkingheads.base_browser import BaseBrowser

# Set up Edge WebDriver
options = webdriver.EdgeOptions()
options.add_argument("headless")  # Optional: run in headless mode
driver = webdriver.Edge(EdgeChromiumDriverManager().install(), options=options)

# Customize the BaseBrowser class to use Edge
class EdgePiClient(PiClient):
    def __init__(self, **kwargs):
        BaseBrowser.__init__(self, browser=driver, **kwargs)

# Create two bots
bot1 = EdgePiClient()
bot2 = EdgePiClient()

# Define a function to make them talk
def conversation(bot1, bot2, num_exchanges=10):
    user_input = "Hello"
    for i in range(num_exchanges):
        response1 = bot1.interact(user_input)
        print(f"Bot 1: {response1}")
        response2 = bot2.interact(response1)
        print(f"Bot 2: {response2}")
        user_input = response2

# Make them talk
conversation(bot1, bot2)
