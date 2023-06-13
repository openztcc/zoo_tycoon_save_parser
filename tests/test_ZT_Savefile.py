from ZT_Savefile import parse_zt_savefile


def test_parse_zt_savefile():
    with open("./full_savefiles/exhibits_index.zoo", 'rb') as binary_file:
        save_file = parse_zt_savefile(binary_file)
        assert save_file.header.x_tile_size == 75
        assert save_file.header.y_tile_size == 75
        assert save_file.exhibits.num_exhibits == 7
        assert len(save_file.tile_list.tiles) == 75
        assert len(save_file.tile_list.tiles[0]) == 75
