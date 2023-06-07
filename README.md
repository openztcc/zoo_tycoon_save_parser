# zoo_tycoon_save_parser
First pass of a Zoo Tycoon (2001) savefile parser. Currently very incomplete.

## Progress
 - Scenery - 95%
 - Buildings - 90%
 - Tiles - 10%


## Details

### Tiles
Tiles are 10 bytes, stored in columns. So far there appear to be bytes for the height, terrain_id and a byte for each edge, but the specifics are still a mystery, at this point I'm hoping a better understanding of the code will help.

### Units

As defined in ai.ztd Unit is the parent of ztunit which is the parent of animals and staff, unsure if this heirarchy is also present in code? Also unsure how guests fit into this heirarchy as guests.ztd just lists them as class "guests" with no mention of ztunit or unit.

Staff, guests and animals have a position, needs, a name and a bunch of AI information. The first three are easy to decipher, ai info is not and will likely benefit from a better understanding of how the underlying system works first.
