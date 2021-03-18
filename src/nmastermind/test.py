from MasterMindAsked import (ALL_COLORS,
                             get_nb_black_white_matches,
                             create_combination,
                             any_color_in_combination,
                             all_colors_in_combination,
                             is_sublist_of)


simple_combination = ["red", "green", "blue", "white"]


# Tests for get_nb_black_white_matches(given, guess)
assert get_nb_black_white_matches(["blue", "yellow", "yellow", "blue"], ["blue", "yellow", "blue", "yellow"]) == (2, 2)


# Test for create_combination(nb_elements)
for i in range(10):
    combination = create_combination(i)
    assert len(combination) == i
    for color in combination:
        assert color in ALL_COLORS


# Tests for any_color_in_combination(any, given)
assert any_color_in_combination(["purple", "red"], simple_combination)


# Tests for all_colors_in_combination(colors, given)
assert not all_colors_in_combination(["red", "green", "yellow"], simple_combination)


# Test for create_combination(nb_elements) and
# all_colors_in_combination(colors, given)
for i in range(20):
    assert all_colors_in_combination(create_combination(i), ALL_COLORS)


# Tests for is_sublist_of(sublist, given)
simple_list = [1, 2, 3, 4]
for element in simple_list:
    assert is_sublist_of([element], simple_list)
assert not is_sublist_of([5], simple_list)