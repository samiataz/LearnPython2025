import math
from diagram import make_binding,Frame
from diagram import  diagram, adjust

binding= make_binding("message",'and now something completely different')
binding2= make_binding("n",17)
binding3= make_binding("pi",math.pi)

frame=Frame([binding, binding2, binding3])
width,height,x,y=[3.62,1.01,0.6,0.76]
ax=diagram(width,height)
bbox=frame.draw(ax,x,y,dy=-0.25)
