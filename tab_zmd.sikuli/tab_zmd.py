#test
click("1540790334473.png")
sleep(5)

if exists(Pattern("1536814622496.png").similar(0.85)):
    click(Pattern("1536814622496.png").similar(0.85))
click(Pattern("1533613772075.png").similar(0.83))
sleep(2)

splash = Pattern("1535689420965.png").exact()
if exists(splash):
    click(splash)
    
sign = "sign.png"

if exists(sign):
    print("find sign")
    click(sign)
    sleep(5)
    if exists("1541135091392.png"):
        click("1541135091392.png")
    if exists("1542449267862.png"):
        click("1542449280018.png")
    sleep(10)

    if exists(Pattern("1536294368703.png").similar(0.94)):
        click("1536294395821.png")
        sleep(2)
        click(Pattern("1533615527529.png").similar(0.94))
        
    #sleep(5)

    #click("1533706172680.png")


sleep(2)
#click("1540791155024.png")

wheel("1540790610381.png", WHEEL_DOWN, 8)

sleep(15)

unfinish = Pattern("1533615372888.png").similar(0.93)
bonus = Pattern("bonus.png").similar(0.86)
for i in findAll(unfinish):
    
    click(i)
    sleep(2)

    if exists(Pattern("1541477041150.png").similar(0.84)):
        click(Pattern("1541477041150.png").similar(0.83))

    if exists(Pattern("1541477156477.png").similar(0.90)):
        click(Pattern("1541477156477.png").similar(0.90))
    sleep(2)

    if exists("1544072549930.png"):
        click("1533613906973.png")
    if exists("1535948744547.png"):
        click("1533613906973.png")
    if exists(Pattern("1543403911200.png").similar(0.83)):
        click("1543403924500.png")
    if exists(Pattern("1537159170533.png").similar(0.75)):
        click(Pattern("1537159202343.png").similar(0.84).targetOffset(78,-70))
    sleep(2)


for i in findAll(bonus):
    print("find bonus")
    click(bonus) 
    sleep(2)
    click(Pattern("1533615527529.png").similar(0.94))
    sleep(2)

click("1544072801586.png")

sleep(1)

click(Pattern("1536727093763.png").similar(0.81))

sleep(5)

click("1536727151029.png")

sleep(5)

click("1536727189343.png")

sleep(5)

click("1544072859975.png")

sleep(2)

click("1533615650190.png")
sleep(10)
click("1541136703643.png")
sleep(3)
click(Pattern("1533615718156.png").similar(0.72))

sleep(20)
wait("1535097385646.png")
click("1535097385646.png")

sleep(5)

click("1535097417157.png")
sleep(5)
click("1535097438222.png")

sleep(10)

click("1533613906973.png")

sleep(10)

click(bonus) 

click(Pattern("1533615527529.png").similar(0.96))



sleep(10)

click("1536727189343.png")

sleep(2)
click(bonus) 

click(Pattern("1533615527529.png").similar(0.96))

click(bonus)

click(Pattern("1533615527529.png").similar(0.96))














