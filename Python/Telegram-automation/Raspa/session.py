from time import sleep

import tests


while True:
    try:
        tests.menus()
    except:
        pass
    sleep(1)