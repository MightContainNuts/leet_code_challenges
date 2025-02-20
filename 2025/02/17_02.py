class Solution:
    def numTilePossibilities(self, tiles: str) -> int:

        tile_set = []

        for start in range(len(tiles)):
            for end in range(1,len(tiles)+1):
                print(tiles[start:end])
                tile_set.append(tiles[start:end])

        reverse_tiles = tiles[::-1]

        for start in range(len(reverse_tiles)):
            for end in range(1,len(reverse_tiles)+1):
                print(reverse_tiles[start:end])
                tile_set.append(reverse_tiles[start:end])

        return len(set(tile_set))


if __name__ == "__main__":
    s =Solution()
    print(s.numTilePossibilities("AAB"))

