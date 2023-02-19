from ZT_Exhibit import parse_zt_exhibit

def test_parse_zt_exhibit_exhibit_6_keeper_assigned():
    with open("./savefile_subsets/Exhibit 6_in_use.zoo", 'rb') as binary_file:
        zt_exhibit = parse_zt_exhibit(binary_file)
        assert len(binary_file.read()) == 0
