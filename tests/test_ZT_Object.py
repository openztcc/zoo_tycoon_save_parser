import datetime

from ZT_Object import parse_zt_object


def test_parse_zt_object_trashcan():
    with open("./savefile_subsets/Trash Can 8_37_35.zoo", 'rb') as binary_file:
        zt_object = parse_zt_object(binary_file)
        assert zt_object.object_class == "building"
        assert zt_object.object_type == "building"
        assert zt_object.object_subtype == "trshcan"
        assert zt_object.coords == (37, 35, 0)
        assert zt_object.object_id == 9246
        assert zt_object.object_name == "Trash Can 8"
        assert zt_object.object_creation_time == datetime.datetime(year=2001, month=1, day=18, hour=16, minute=46, second=40, microsecond=800000)

        assert len(binary_file.read()) == 0

def test_parse_zt_object_animal_theatre_with_guests():
    with open("./savefile_subsets/Animal Theatre_1_5_current_guests.zoo", 'rb') as binary_file:
        zt_object = parse_zt_object(binary_file)