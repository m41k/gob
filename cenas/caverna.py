import time

def run(oled, joy_x, joy_y, botaoA, botaoB):
    while True:
        oled.fill(0)
        oled.text("CAVERNA", 36, 18)
        oled.text("Cena GitHub", 20, 34)
        oled.text("A: voltar", 20, 50)
        oled.show()

        if not botaoA.value():
            while not botaoA.value():
                time.sleep_ms(10)
            return "mapselect"

        time.sleep_ms(20)
