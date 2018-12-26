click("1544416756914.png")

sleep(10)

click("1536298819141.png")

sleep(3)

if exists("1542547047842.png"):
    click("1542547061688.png")

if exists("1540791906070.png"):
    click("1540791920457.png")




sleep(3)
bonus="1541134556132.png"
click(bonus)
sleep(20)

count = 400

butt = "butt.png"

if exists(butt):
    click(butt)
  
        
    sleep(5)
    print("after click the button")

    if exists("1544072130030.png"):
        click("1544072130030.png")

        sleep(2)

    click("1537938034477.png")

    sleep(5)       
    click(bonus)
        
sleep(1)

wheel("1542448611623.png", WHEEL_DOWN, 5)

bonus = Pattern("bonus.png").similar(0.60).targetOffset(141,-7)

while count:
    if exists(bonus):
        click(bonus)

    count = count - 1

