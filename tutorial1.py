from ggame import App, Color, LineStyle, Sprite
from ggame import RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset
myapp = App()
myapp.run()

#colors
red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)

#line style
thinline = LineStyle(1, black)

# rectangles
rectangle = RectangleAsset(50, 20, thinline, blue)
rectangle2 = RectangleAsset(50, 20, thinline, green)

#display the rectangles
Sprite(rectangle, (200, 50))
Sprite(rectangle2, (225, 40))

myapp = App()
myapp.run()