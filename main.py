import pygame
import BubblesGrid
import Bubble
import consts
import Screen
import Stack


state = {
        "original_arrow": Screen.create_arrow(consts.ARROW_IMG),
        "rotated_arrow": "None",
        "is_bubble_fired": False,
        "bubbles_popping": [],
        "turns_left_to_add_row": consts.NUM_OF_TURNS_TO_ADD_ROW,
        "is_window_open": True,
        "state": consts.RUNNING_STATE,
        "bullet_bubble": None,
        "bubble_direction": None,
        "mouse_angle": None,
        "score":0,
        "max_score":0

}

state["rotated_arrow"] = state["original_arrow"]


def main():
    pygame.init()
    bubble_pop = pygame.mixer.Sound('bubble_pop.mp3')
    BubblesGrid.create()
    Stack.create(consts.STACK_SIZE)

    while state["is_window_open"]:

        handle_user_events()

        if state["is_bubble_fired"]:

            move_bubble()

            if Bubble.should_stop(BubblesGrid.bubbles_grid,
                                  state["bullet_bubble"]):
                state["is_bubble_fired"] = False

                new_bubble_location = BubblesGrid.find_bubble_location_in_grid(
                    state["bullet_bubble"])
                BubblesGrid.put_bubble_in_grid(state["bullet_bubble"],
                                               new_bubble_location)

                same_color_cluster = BubblesGrid.get_same_color_cluster(
                    new_bubble_location,
                    state["bullet_bubble"]["color"],
                    [])

                if BubblesGrid.should_bubbles_pop(same_color_cluster):
                    state["bubbles_popping"] = BubblesGrid.pop_bubbles(same_color_cluster, bubble_pop)
                    # points appended to total score as much of bubbles that were popped
                    state["score"] += len(state["bubbles_popping"])
                    if state["score"] > state["max_score"]:
                        state["max_score"] = state["score"]


                # The counter counts only if bubbles weren't popped
                else:
                    state["turns_left_to_add_row"] -= 1

                    # for each round without popping, 3 points deducted
                    state["score"] -= 3

                    if state["turns_left_to_add_row"] == 0:
                        BubblesGrid.add_new_line()

                        # Reseting the counter
                        state["turns_left_to_add_row"] = \
                            consts.NUM_OF_TURNS_TO_ADD_ROW

                remove_isolated_bubbles(bubble_pop)

                BubblesGrid.set_one_empty_line()
                remove_extinct_colors(consts.bubble_colors)

                Stack.add_bubble(Stack.get_length())

                if is_lose():
                    state["state"] = consts.LOSE_STATE
                elif is_win():
                    state["state"] = consts.WIN_STATE

        Screen.draw_game(state)

def handle_user_events():
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            state["is_window_open"] = False

        elif state["state"] != consts.RUNNING_STATE:
            continue

        if event.type == pygame.MOUSEMOTION:
            rotate_arrow()

        elif event.type == pygame.MOUSEBUTTONDOWN and \
                not state["is_bubble_fired"] and \
                not state["bubbles_popping"]:
            fire_bubble()

def rotate_arrow():
    state["mouse_angle"] = Screen.calc_mouse_angle(pygame.mouse.get_pos())
    state["rotated_arrow"] = pygame.transform.rotate(state["original_arrow"],
                                                     state["mouse_angle"] - 90)


def fire_bubble():
    state["is_bubble_fired"] = True
    state["bubble_direction"] = \
        Bubble.calc_direction(state["mouse_angle"])
    state["bullet_bubble"] = Stack.remove_first()


def move_bubble():
    Bubble.move_in_direction(state["bullet_bubble"], state["bubble_direction"])

    if Bubble.is_colliding_with_wall(state["bullet_bubble"]):
        state["bubble_direction"] = (state["bubble_direction"][0] * (-1),
                                     state["bubble_direction"][1])


def remove_isolated_bubbles(bubble_pop):
    isolated_bubbles_locations = BubblesGrid.find_isolated_bubbles()

    if len(isolated_bubbles_locations) > 0:
        state["bubbles_popping"] += \
            BubblesGrid.pop_bubbles(isolated_bubbles_locations, bubble_pop)


# -----------------------------------------------------------------------------
# ---------------------------------your code-----------------------------------
# -----------------------------------------------------------------------------

def remove_extinct_colors(bubble_colors):
    # TODO: implement
    grid_colors = BubblesGrid.colors_on_grid()
    stack_colors = Stack.colors_on_stack()

    for color in bubble_colors:
        if color not in grid_colors:
            if color not in stack_colors:
                bubble_colors.remove(color)


def is_lose():
    # TODO: implement
    if BubblesGrid.get_length() -1 >= consts.NUM_OF_LINES_LOSE:
        return True
    return False


def is_win():
    # TODO: implement
    # passing only on first row
    for bubble in BubblesGrid.bubbles_grid[0]:
        if bubble["color"] != "EMPTY":
            return False
    return True


# -----------------------------------------------------------------------------
# ------------------------------your code end----------------------------------
# -----------------------------------------------------------------------------

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
