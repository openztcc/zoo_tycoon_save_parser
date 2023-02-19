from ZT_Exhibits import parse_zt_exhibits

def test_parse_zt_exhibits():
    with open("./savefile_subsets/3_exhibits.zoo", 'rb') as binary_file:
        zt_exhibits = parse_zt_exhibits(binary_file)
        assert len(binary_file.read()) == 0
        assert zt_exhibits.num_exhibits == 3
