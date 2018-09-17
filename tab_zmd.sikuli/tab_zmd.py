#test
click("1537158539534.png")
sleep(5)

if exists(Pattern("1536814622496.png").similar(0.85)):
    click(Pattern("1536814622496.png").similar(0.85))
click(Pattern("1533613772075.png").similar(0.83))
sleep(2)

splash = Pattern("1535689420965.png").exact()
if exists(splash):
    click(splash)
    
sign = Pattern("1533613852474.png").similar(0.94)

if exists(sign):
    print("find sign")
    click(sign)
    sleep(2)
    click("1533706148466.png")
    
    sleep(10)

    if exists(Pattern("1536294368703.png").similar(0.94)):
        click("1536294395821.png")
        sleep(2)
        click(Pattern("1533615527529.png").similar(0.96))
        
    sleep(5)

    click("1533706172680.png")

click(Pattern("1533706666690.png").similar(0.86))

sleep(15)

unfinish = Pattern("1533615372888.png").similar(0.93)
bonus = Pattern("1535096171127.png").similar(0.93)
for i in findAll(unfinish):
    
    click(i)
    sleep(5)

    if exists(Pattern("1533615450308.png").similar(0.96)):
        click(Pattern("1533615450308.png").similar(0.96))

    sleep(2)

    if not exists(unfinish):
        click("1533613906973.png")
    if exists("1535948744547.png"):
        click("1533613906973.png")

    if exists(Pattern("1537159170533.png").similar(0.75)):
        click(Pattern("1537159202343.png").similar(0.84).targetOffset(78,-70))
    sleep(10)






#bonus = Pattern("1533615499991.png").exact()
for i in findAll(bonus):
    print("find bonus")
    click(bonus) 
    sleep(5)
    click(Pattern("1533615527529.png").similar(0.96))
    sleep(5)



click(Pattern("1536034554876.png").similar(0.96))

sleep(2)

click("1533615650190.png")
sleep(10)
click(Pattern("1535097199163.png").similar(0.78))
sleep(3)
click(Pattern("1533615718156.png").similar(0.93))

sleep(20)

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

click("1536727067521.png")

sleep(1)

click(Pattern("1536727093763.png").similar(0.81))

sleep(5)

click("1536727151029.png")

sleep(10)

click("1536727189343.png")

sleep(2)
click(bonus) 

click(Pattern("1533615527529.png").similar(0.96))

 














