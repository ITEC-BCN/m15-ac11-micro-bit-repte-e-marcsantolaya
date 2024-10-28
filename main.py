## EJERCICIO 6
## def on_forever():
    ##    temperatura = input.temperature()
    ##    led.plot_bar_graph(temperatura, 50)
    ## basic.forever(on_forever)

## EJERCICIO 7
x = 2
y = 2
def on_forever():
    global x,y
    led.plot(x, y)
    pause(50)
    led.unplot(x, y)
    accX = input.acceleration(Dimension.X)
    accY = input.acceleration(Dimension.Y)
    if (accX <= 50) and (x > 0):
        x = x - 1
    if (accX > 50) and (x < 4):
        x = x + 1
    if (accY <= 50) and (y > 0):
        y = y - 1
    if (accY > 50) and (y < 4):
        y = y + 1    
basic.forever(on_forever)