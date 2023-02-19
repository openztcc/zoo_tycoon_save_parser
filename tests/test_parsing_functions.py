from parsing_functions import parse_string, parse_grid_coord


def test_parse_string():
    with open("../../zt_files/savefile_subsets/Trash Can 8_37_35.zoo", 'rb') as binary_file:
        assert "building" == parse_string(binary_file)

def test_parse_multiple_string():
    with open("../../zt_files/savefile_subsets/Trash Can 8_37_35.zoo", 'rb') as binary_file:
        assert "building" == parse_string(binary_file)
        assert "building" == parse_string(binary_file)
        assert "trshcan" == parse_string(binary_file)

def test_parse_grid_coord_positive():
    with open("../../zt_files/savefile_subsets/coords_36_35_-1.zoo", "rb") as binary_file:
        assert 36 == parse_grid_coord(binary_file)

def test_parse_grid_coord_negative():
    with open("../../zt_files/savefile_subsets/coords_36_35_-1.zoo", "rb") as binary_file:
        assert 36 == parse_grid_coord(binary_file)
        assert 35 == parse_grid_coord(binary_file)
        assert -1 == parse_grid_coord(binary_file)
