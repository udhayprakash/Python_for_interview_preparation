def check_if_button_touched(
    point_x, point_y, button_x_min, button_y_min, button_x_max, button_y_max
):
    within_x = button_x_min <= point_x <= button_x_max
    within_y = button_y_min <= point_y <= button_y_max
    return within_x and within_y


def get_mid_point(button_x_min, button_y_min, button_x_max, button_y_max):
    return (button_x_min + button_x_max) / 2.0, (button_y_min + button_y_max) / 2.0


def get_distance(point_1, point_2):
    return ((point_2[0] - point_1[0]) ** 2 + (point_2[1] - point_1[1]) ** 2) ** 0.5


def getTouchedButtons(touchPos, buttonsPos):
    button_list = []
    for (index, button) in enumerate(buttonsPos):
        if check_if_button_touched(
            touchPos[0], touchPos[1], button[0], button[1], button[2], button[3]
        ):
            mid_point = get_mid_point(button[0], button[1], button[2], button[3])
            distance = get_distance(touchPos, mid_point)
            button_list.append((index, distance))

    return [x[0] for x in sorted(button_list, key=lambda x: x[1])]


if __name__ == "__main__":
    touch_pos = [0, 0]
    button_pos = [[-1, -1, 1, 1], [0, 0, 1, 1], [1, 1, 2, 2]]
    print(getTouchedButtons(touch_pos, button_pos))
