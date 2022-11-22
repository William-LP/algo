# what if rectange completely overlap --> True
# what if rectange only share an angle --> False
# what if we pass a list of rectange --> return list of compatible pairs
# what if we pass a list of rectange --> return list of all matching rectange 
def check_overlap(rect_a : dict, rect_b : dict) -> bool :
    rect_a_bas = rect_a["bottom_y"]
    rect_a_haut = rect_a["bottom_y"] + rect_a["height"]
    rect_b_bas = rect_b["bottom_y"]
    rect_b_haut = rect_b["bottom_y"] + rect_b["height"]

    rect_a_left = rect_a["left_x"]
    rect_a_right = rect_a["left_x"] + rect_a["width"]
    rect_b_left = rect_b["left_x"]
    rect_b_right = rect_b["left_x"] + rect_b["width"]

    if rect_a_bas < rect_b_bas < rect_a_haut or rect_a_bas < rect_b_haut < rect_a_haut :
        vertical_alignment = True
    else :
        vertical_alignment = False
    if rect_a_left < rect_b_left < rect_a_right or rect_a_left < rect_b_right < rect_a_right :
        horizontal_alignment = True
    else :
        horizontal_alignment = False
    if horizontal_alignment and vertical_alignment:
        return True
    else:
        return False
  





rectangle_a = {
    # Coordinates of bottom-left corner
    "left_x": 1,
    "bottom_y": 1,
    # Width and height
    "width": 6,
    "height": 3,
}
rectangle_b = {
    # Coordinates of bottom-left corner
    "left_x": 7,
    "bottom_y": 4,
    # Width and height
    "width": 4,
    "height": 6,
}
# print(check_overlap(rectangle_a, rectangle_b))
