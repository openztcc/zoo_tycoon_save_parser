from ZT_Savefile import parse_zt_savefile


def test_parse_zt_savefile():
    with open("./full_savefiles/basic_grass_small_beta_levelled_terrain_index_6_with_exhibits_6.zoo", 'rb') as binary_file:
        save_file = parse_zt_savefile(binary_file)
        assert save_file.header.x_tile_size == 75
        assert save_file.header.y_tile_size == 75
        assert save_file.exhibits.num_exhibits == 3
        assert len(save_file.tile_list.tiles) == 75
        assert len(save_file.tile_list.tiles[0]) == 75


# def test_parse_zt_savefile_guests_animals():
#     with open("./full_savefiles/basic_grass_small_beta_financials.zoo", 'rb') as binary_file:
#         save_file = parse_zt_savefile(binary_file)
#         assert save_file.header.x_tile_size == 75
#         assert save_file.header.y_tile_size == 75
#         assert save_file.exhibits.num_exhibits == 3
#         assert len(save_file.tile_list.tiles) == 75
#         assert len(save_file.tile_list.tiles[0]) == 75
