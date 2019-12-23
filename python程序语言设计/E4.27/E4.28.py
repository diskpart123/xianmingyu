x1, y1, width1, height1 = eval(input("Enter r1's center x-,y-coordinates, width, and height:\n"))
x2, y2, width2, height2 = eval(input("Enter r2's center x-,y-coordinates, width, and height:\n"))

x = ( ( x2 - x1 ) * ( x2 - x1 ) ) ** 0.5
y = ( ( y2 - y1 ) * ( y2 - y1 ) ) ** 0.5

overlaps = ( ( ( x + width2 / 2 ) > width1 / 2 ) and ( ( y + height2 / 2 ) <= height1 / 2 ) ) or \
           ( ( ( x + width2 / 2 ) <= width1 / 2 ) and ( ( y + height2 / 2 ) > height1 / 2 ) )

if ( ( x + width2 / 2 ) <= width1 / 2 ) and ( ( y + height2 / 2 ) <= height1 / 2 ):
    print("r2 is inside r1")
elif overlaps:
    print("r2 overlaps r1")
else:
    print("r2 does not overlap r1")