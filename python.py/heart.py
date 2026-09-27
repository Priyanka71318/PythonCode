import turtle

# -------------------------
# Screen
# -------------------------

screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(900, 700)
screen.title("Scorpion Cursor")

# -------------------------
# Scorpion body
# -------------------------

parts = []

for i in range(30):

    p = turtle.Turtle()

    p.shape("circle")
    p.color("white")
    p.shapesize(0.4)

    p.penup()
    p.speed(0)

    parts.append(p)


# -------------------------
# Mouse position
# -------------------------

mouse_x = 0
mouse_y = 0


def move_mouse(x, y):
    global mouse_x, mouse_y

    mouse_x = x
    mouse_y = y


# Mouse move hone par position update
screen.cv.bind(
    "<Motion>",
    lambda event: move_mouse(
        screen.cv.canvasx(event.x) - 450,
        350 - screen.cv.canvasy(event.y)
    )
)


# -------------------------
# Scorpion follow function
# -------------------------

def follow():

    # Head mouse ko follow karega
    parts[0].goto(mouse_x, mouse_y)

    # Body ke baaki parts previous part ko follow karenge
    for i in range(1, len(parts)):

        px, py = parts[i - 1].position()

        cx, cy = parts[i].position()

        nx = cx + (px - cx) * 0.35
        ny = cy + (py - cy) * 0.35

        parts[i].goto(nx, ny)

        parts[i].setheading(
            parts[i].towards(px, py)
        )

    # Animation repeat
    screen.ontimer(follow, 20)


# Start
follow()

screen.mainloop()