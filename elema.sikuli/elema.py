click("1540792082363.png")

sleep(10)

click("1536298819141.png")

sleep(3)

if exists("1540791906070.png"):
    click("1540791920457.png")

click("1540792031876.png")

sleep(5)

count = 400

butt = "1536299482112.png"

if exists(butt):
    click(butt)
  
        
    sleep(3)
    if exists("1536728302365.png"):
        click("1536728312022.png")

        
    else: 
        if exists("1536727946502.png"):
            click("1536727946502.png")

            sleep(2)

            click("1537938034477.png")

            sleep(2)       
            click("1536298862210.png")
        
sleep(1)

wheel("1536899668334.png", WHEEL_DOWN, 5)

bonus = Pattern("bonus.png").similar(0.83).targetOffset(133,-2)

while count:
    if exists(bonus):
        click(bonus)

    count = count - 1

