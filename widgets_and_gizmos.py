"""An online retailer sells two products: widgets and gizmos. Each widget weighs 75
grams. Each gizmo weighs 112 grams. Write a program that reads the number of
widgets and the number of gizmos in an order from the user. Then your program
should compute and display the total weight of the order."""

def widgets_and_gizmos():
    widgets = int(input("How many widgets? "))
    gizmos = int(input("How many gizmos? "))

    widget_weight = 75
    gizmo_weight = 112

    total_weight = (widget_weight*widgets) + (gizmo_weight*gizmos)
    print("The total weight of your order is %.2f grams"%total_weight)

widgets_and_gizmos()
