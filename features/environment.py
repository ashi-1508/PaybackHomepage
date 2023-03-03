import time
from features.utility.utilityclass import utilityclass

def before_scenario(context, driver):
    utilityclass.launch_browser(context)
    time.sleep(1)
    utilityclass.browser_maximise(context)
    time.sleep(1)
    utilityclass.launch_app(context)
    time.sleep(1)

def after_scenario(context, driver):
    time.sleep(1)
    utilityclass.close_browser(context)
