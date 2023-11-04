from BaseClasses import Location
import typing

base_location_id = 128000000


class ApeEscapeLocation(Location):
    game: str = "Ape Escape"

    def __init__(self, player: int, name: str, address: typing.Optional[int], parent):
        super().__init__(player, name, address, parent)
        self.event = not address

location_table = {
    #1-1 Fossil Field
    "1-1 Fossil Field Monkey 1 - Noonan": 1,
    "1-1 Fossil Field Monkey 2 - Jorjy": 2,
    "1-1 Fossil Field Monkey 3 - Nati": 3,
    "1-1 Fossil Field Monkey 4 - Tray C": 4,
    #1-2 Primordial Ooze
    "1-2 Primordial Ooze Monkey 1 - Shay": 5,
    "1-2 Primordial Ooze Monkey 2 - Dr. Monk": 6,
    "1-2 Primordial Ooze Monkey 3 - Grunt": 7,
    "1-2 Primordial Ooze Monkey 4 - Ah-choo": 8,
    "1-2 Primordial Ooze Monkey 5 - Gornif": 9,
    "1-2 Primordial Ooze Monkey 6 - Tyrone": 10,
    #1-3 Molten Lava
    "1-3 Molten Lava Monkey 1 - Scotty": 11,
    "1-3 Molten Lava Monkey 2 - Coco": 12,
    "1-3 Molten Lava Monkey 3 - J. Thomas": 13,
    "1-3 Molten Lava Monkey 4 - Mattie": 14,
    "1-3 Molten Lava Monkey 5 - Barney": 15,
    "1-3 Molten Lava Monkey 6 - Rocky": 16,
    "1-3 Molten Lava Monkey 7 - Moggan": 17,
    #2-1 Thick Jungle
    "2-1 Thick Jungle Monkey 1 - Marquez": 18,
    "2-1 Thick Jungle Monkey 2 - Livinston": 19,
    "2-1 Thick Jungle Monkey 3 - George": 20,
    "2-1 Thick Jungle Monkey 4 - Maki": 21,
    "2-1 Thick Jungle Monkey 5 - Herb": 22,
    "2-1 Thick Jungle Monkey 6 - Dilweed": 23,
    "2-1 Thick Jungle Monkey 7 - Mitong": 24,
    "2-1 Thick Jungle Monkey 8 - Stoddy": 25,
    "2-1 Thick Jungle Monkey 9 - Nasus": 26,
    "2-1 Thick Jungle Monkey 10 - Selur": 27,
    "2-1 Thick Jungle Monkey 11 - Elehcim": 28,
    "2-1 Thick Jungle Monkey 12 - Gonzo": 29,
    "2-1 Thick Jungle Monkey 13 - Alphonse": 30,
    "2-1 Thick Jungle Monkey 14 - Zanzibar": 31,
    #2-2 Dark Ruins
    "2-2 Dark Ruins Monkey 1 - Mooshy": 32,
    "2-2 Dark Ruins Monkey 2 - Kyle": 33,
    "2-2 Dark Ruins Monkey 3 - Cratman": 34,
    "2-2 Dark Ruins Monkey 4 - Nuzzy": 35,
    "2-2 Dark Ruins Monkey 5 - Mav": 36,
    "2-2 Dark Ruins Monkey 6 - Stan": 37,
    "2-2 Dark Ruins Monkey 7 - Bernt": 38,
    "2-2 Dark Ruins Monkey 8 - Runt": 39,
    "2-2 Dark Ruins Monkey 9 - Hoolah": 40,
    "2-2 Dark Ruins Monkey 10 - Papou": 41,
    "2-2 Dark Ruins Monkey 11 - Kenny": 42,
    "2-2 Dark Ruins Monkey 12 - Trance": 43,
    "2-2 Dark Ruins Monkey 13 - Chino": 44,
    #2-3 Cryptic Relics
    "2-3 Cryptic Relics Monkey 1 - Troopa": 45,
    "2-3 Cryptic Relics Monkey 2 - Spanky": 46,
    "2-3 Cryptic Relics Monkey 3 - Stymie": 47,
    "2-3 Cryptic Relics Monkey 4 - Pally": 48,
    "2-3 Cryptic Relics Monkey 5 - Freeto": 49,
    "2-3 Cryptic Relics Monkey 6 - Jesta": 50,
    "2-3 Cryptic Relics Monkey 7 - Bazzle": 51,
    "2-3 Cryptic Relics Monkey 8 - Crash": 52,
    #4-1 Crabby Beach
    "4-1 Crabby Beach Monkey 1 - Cool Blue": 53,
    "4-1 Crabby Beach Monkey 2 - Sandy": 54,
    "4-1 Crabby Beach Monkey 3 - Shell E.": 55,
    "4-1 Crabby Beach Monkey 4 - Gidget": 56,
    "4-1 Crabby Beach Monkey 5 - Shaka": 57,
    "4-1 Crabby Beach Monkey 6 - MaxMahalo": 58,
    "4-1 Crabby Beach Monkey 7 - Moko": 59,
    "4-1 Crabby Beach Monkey 8 - Puka": 60,
    #4-2 Coral Cave
    "4-2 Coral Cave Monkey 1 - Chip": 61,
    "4-2 Coral Cave Monkey 2 - Oreo": 62,
    "4-2 Coral Cave Monkey 3 - Puddles": 63,
    "4-2 Coral Cave Monkey 4 - Kalama": 64,
    "4-2 Coral Cave Monkey 5 - Iz": 65,
    "4-2 Coral Cave Monkey 6 - Jux": 66,
    "4-2 Coral Cave Monkey 7 - Bong-Bong": 67,
    "4-2 Coral Cave Monkey 8 - Pickles": 68,
    #4-3 Dexter's Island
    "4-3 Dexters Island Monkey 1 - Stuw": 69,
    "4-3 Dexters Island Monkey 2 - Ton Ton": 70,
    "4-3 Dexters Island Monkey 3 - Murky": 71,
    "4-3 Dexters Island Monkey 4 - Howeerd": 72,
    "4-3 Dexters Island Monkey 5 - Robbin": 73,
    "4-3 Dexters Island Monkey 6 - Jakkee": 74,
    "4-3 Dexters Island Monkey 7 - Frederic": 75,
    "4-3 Dexters Island Monkey 8 - Baba": 76,
    "4-3 Dexters Island Monkey 9 - Mars": 77,
    "4-3 Dexters Island Monkey 10 - Horke": 78,
    "4-3 Dexters Island Monkey 11 - Quirck": 79,
    #5-1 Snowy Mammoth
    "5-1 Snowy Mammoth Monkey 1 - Popcicle": 80,
    "5-1 Snowy Mammoth Monkey 2 - Iced": 81,
    "5-1 Snowy Mammoth Monkey 3 - Denggoy": 82,
    "5-1 Snowy Mammoth Monkey 4 - Skeens": 83,
    "5-1 Snowy Mammoth Monkey 5 - Rickets": 84,
    "5-1 Snowy Mammoth Monkey 6 - Chilly": 85,
    #5-2 Frosty Retreat
    "5-2 Frosty Retreat Monkey 1 - Storm": 86,
    "5-2 Frosty Retreat Monkey 2 - Qube": 87,
    "5-2 Frosty Retreat Monkey 3 - Gash": 88,
    "5-2 Frosty Retreat Monkey 4 - Kundra": 89,
    "5-2 Frosty Retreat Monkey 5 - Shadow": 90,
    "5-2 Frosty Retreat Monkey 6 - Ranix": 91,
    "5-2 Frosty Retreat Monkey 7 - Sticky": 92,
    "5-2 Frosty Retreat Monkey 8 - Sharpe": 93,
    "5-2 Frosty Retreat Monkey 9 - Droog": 94,
    #5-3 Hot Springs
    "5-3 Hot Springs Monkey 1": 95,
    "5-3 Hot Springs Monkey 2": 96,
    "5-3 Hot Springs Monkey 3": 97,
    "5-3 Hot Springs Monkey 4": 98,
    "5-3 Hot Springs Monkey 5": 99,
    "5-3 Hot Springs Monkey 6": 100,
    "5-3 Hot Springs Monkey 7": 101,
    "5-3 Hot Springs Monkey 8": 102,
    "5-3 Hot Springs Monkey 9": 103,
    #7-1 Sushi Temple
    "7-1 Sushi Temple Monkey 1": 104,
    "7-1 Sushi Temple Monkey 2": 105,
    "7-1 Sushi Temple Monkey 3": 106,
    "7-1 Sushi Temple Monkey 4": 107,
    "7-1 Sushi Temple Monkey 5": 108,
    "7-1 Sushi Temple Monkey 6": 109,
    "7-1 Sushi Temple Monkey 7": 110,
    "7-1 Sushi Temple Monkey 8": 111,
    "7-1 Sushi Temple Monkey 9": 112,
    "7-1 Sushi Temple Monkey 10": 113,
    "7-1 Sushi Temple Monkey 11": 114,
    "7-1 Sushi Temple Monkey 12": 115,
    #7-2 Wabi Sabi Wall
    "7-2 Wabi Sabi Wall Monkey 1": 116,
    "7-2 Wabi Sabi Wall Monkey 2": 117,
    "7-2 Wabi Sabi Wall Monkey 3": 118,
    "7-2 Wabi Sabi Wall Monkey 4": 119,
    "7-2 Wabi Sabi Wall Monkey 5": 120,
    "7-2 Wabi Sabi Wall Monkey 6": 121,
    "7-2 Wabi Sabi Wall Monkey 7": 122,
    "7-2 Wabi Sabi Wall Monkey 8": 123,
    "7-2 Wabi Sabi Wall Monkey 9": 124,
    "7-2 Wabi Sabi Wall Monkey 10": 125,
    #7-3 Crumbling Castle
    "7-3 Crumbling Castle Monkey 1": 126,
    "7-3 Crumbling Castle Monkey 2": 127,
    "7-3 Crumbling Castle Monkey 3": 128,
    "7-3 Crumbling Castle Monkey 4": 129,
    "7-3 Crumbling Castle Monkey 5": 130,
    "7-3 Crumbling Castle Monkey 6": 131,
    "7-3 Crumbling Castle Monkey 7": 132,
    "7-3 Crumbling Castle Monkey 8": 133,
    "7-3 Crumbling Castle Monkey 9": 134,
    "7-3 Crumbling Castle Monkey 10": 135,
    "7-3 Crumbling Castle Monkey 11": 136,
    "7-3 Crumbling Castle Monkey 12": 137,
    "7-3 Crumbling Castle Monkey 13": 138,
    "7-3 Crumbling Castle Monkey 14": 139,
    "7-3 Crumbling Castle Monkey 15": 140,
    "7-3 Crumbling Castle Monkey 16": 141,
    "7-3 Crumbling Castle Monkey 17": 142,
    "7-3 Crumbling Castle Monkey 18": 143,
    "7-3 Crumbling Castle Monkey 19": 144,
    "7-3 Crumbling Castle Monkey 20": 145,
    #8-1 City Park
    "8-1 City Park Monkey 1": 146,
    "8-1 City Park Monkey 2": 147,
    "8-1 City Park Monkey 3": 148,
    "8-1 City Park Monkey 4": 149,
    "8-1 City Park Monkey 5": 150,
    "8-1 City Park Monkey 6": 151,
    "8-1 City Park Monkey 7": 152,
    "8-1 City Park Monkey 8": 153,
    "8-1 City Park Monkey 9": 154,
    "8-1 City Park Monkey 10": 155,
    "8-1 City Park Monkey 11": 156,
    "8-1 City Park Monkey 12": 157,
    "8-1 City Park Monkey 13": 158,
    #8-2 Specter's Factory
    "8-2 Specters Factory Monkey 1": 159,
    "8-2 Specters Factory Monkey 2": 160,
    "8-2 Specters Factory Monkey 3": 161,
    "8-2 Specters Factory Monkey 4": 162,
    "8-2 Specters Factory Monkey 5": 163,
    "8-2 Specters Factory Monkey 6": 164,
    "8-2 Specters Factory Monkey 7": 165,
    "8-2 Specters Factory Monkey 8": 166,
    "8-2 Specters Factory Monkey 9": 167,
    "8-2 Specters Factory Monkey 10": 168,
    #8-3 TV Tower
    "8-3 TV Tower Monkey 1": 169,
    "8-3 TV Tower Monkey 2": 170,
    "8-3 TV Tower Monkey 3": 171,
    "8-3 TV Tower Monkey 4": 172,
    "8-3 TV Tower Monkey 5": 173,
    "8-3 TV Tower Monkey 6": 174,
    "8-3 TV Tower Monkey 7": 175,
    "8-3 TV Tower Monkey 8": 176,
    "8-3 TV Tower Monkey 9": 177,
    "8-3 TV Tower Monkey 10": 178,
    "8-3 TV Tower Monkey 11": 179,
    "8-3 TV Tower Monkey 12": 180,
    #9-1 Monkey Madness
    "9-1 Monkey Madness Monkey 1": 181,
    "9-1 Monkey Madness Monkey 2": 182,
    "9-1 Monkey Madness Monkey 3": 183,
    "9-1 Monkey Madness Monkey 4": 184,
    "9-1 Monkey Madness Monkey 5": 185,
    "9-1 Monkey Madness Monkey 6": 186,
    "9-1 Monkey Madness Monkey 7": 187,
    "9-1 Monkey Madness Monkey 8": 188,
    "9-1 Monkey Madness Monkey 9": 189,
    "9-1 Monkey Madness Monkey 10": 190,
    "9-1 Monkey Madness Monkey 11": 191,
    "9-1 Monkey Madness Monkey 12": 192,
    "9-1 Monkey Madness Monkey 13": 193,
    "9-1 Monkey Madness Monkey 14": 194,
    "9-1 Monkey Madness Monkey 15": 195,
    "9-1 Monkey Madness Monkey 16": 196,
    "9-1 Monkey Madness Monkey 17": 197,
    "9-1 Monkey Madness Monkey 18": 198,
    "9-1 Monkey Madness Monkey 19": 199,
    "9-1 Monkey Madness Monkey 20": 200,
    "9-1 Monkey Madness Monkey 21": 201,
    "9-1 Monkey Madness Monkey 22": 202,
    "9-1 Monkey Madness Monkey 23": 203,
    "9-1 Monkey Madness Monkey 24": 204,
    "9-1 Specter": 205
}