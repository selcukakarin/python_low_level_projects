"""
tinder like code
"""


import pyautogui
import time
"""
>>> import pyautogui
>>> pyautogui.position()
aşağıdaki x y değerlerini yani onay buttonunun sayfadaki koordinatlarını yukarıda belirttiğim kodlar ile bulup gerekli yere yazın.
"""
x,y = 1094,691
sayac = 10
while True:
    for i in range(0,sayac):
        pyautogui.click(x,y)
        time.sleep(0.3)

    cevap = pyautogui.confirm(text="Devam etmek ister misin?",title="selcuk",buttons=["Evet","Hayır"])
    if cevap == "Hayır":
        break
    else:
        while True:
            try:
                sayac = int(pyautogui.prompt("Daha kaç kişi daha likelamak istersin?",title="selcuk",default=""))
                break
            except ValueError:
                pyautogui.alert(text="Lütfen tam sayı gir",title="selcuk",buttons="Tamamdır!")


