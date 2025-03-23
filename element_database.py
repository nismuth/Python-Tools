# Seven function including main: mass, number, symbol, valence, family, facts

# Atomic masses
def atomic_mass():
    masses = {
        'hydrogen': 1.008,
        'helium': 4.0026,
        'lithium': 6.94,
        'beryllium': 9.0122,
        'boron': 10.81,
        'carbon': 12.011,
        'nitrogen': 14.007,
        'oxygen': 15.999,
        'fluorine': 18.998,
        'neon': 20.180,
        'sodium': 22.990,
        'magnesium': 24.305,
        'aluminum': 26.982,
        'silicon': 28.085,
        'phosphorus': 30.974,
        'sulfur': 32.06,
        'chlorine': 35.45,
        'argon': 39.948,
        'potassium': 39.098,
        'calcium': 40.078,
        'scandium': 44.956,
        'titanium': 47.867,
        'vanadium': 50.942,
        'chromium': 51.996,
        'manganese': 54.938,
        'iron': 55.845,
        'cobalt': 58.933,
        'nickel': 58.933,
        'copper': 63.546,
        'zinc': 65.38,
        'gallium': 69.723,
        'germanium': 72.63,
        'arsenic': 74.922,
        'selenium': 78.971,
        'bromine': 79.904,
        'krypton': 83.798,
        'rubidium': 85.468,
        'strontium': 87.62,
        'yttrium': 88.906,
        'zirconium': 91.224,
        'niobium': 92.906,
        'molybdenum': 95.95,
        'technetium': 98,
        'ruthenium': 101.07,
        'rhodium': 102.91,
        'palladium': 106.42,
        'silver': 107.87,
        'cadmium': 112.41,
        'indium': 114.82,
        'tin': 118.71,
        'antimony': 121.76,
        'tellurium': 127.60,
        'iodine': 126.90,
        'xenon': 131.29,
        'cesium': 132.91,
        'barium': 137.33,
        'lanthanum': 138.91,
        'cerium': 140.12,
        'praseodymium': 140.91,
        'neodymium': 144.24,
        'promethium': 145,
        'samarium': 150.36,
        'europium': 151.96,
        'gadolinium': 157.25,
        'terbium': 158.93,
        'dysprosium': 162.50,
        'holmium': 164.93,
        'erbium': 167.26,
        'thulium': 168.93,
        'ytterbium': 173.04,
        'lutetium': 174.97,
        'hafnium': 178.49,
        'tantalum': 180.95,
        'tungsten': 183.84,
        'rhenium': 186.21,
        'osmium': 190.23,
        'iridium': 192.22,
        'platinum': 195.08,
        'gold': 196.97,
        'mercury': 200.59,
        'thallium': 204.38,
        'lead': 207.2,
        'bismuth': 209.98,
        'polonium': 209,
        'astatine': 210,
        'radon': 222,
        'francium': 223,
        'radium': 226,
        'actinium': 227,
        'thorium': 232.04,
        'protactinium': 231.04,
        'uranium': 238.03,
        'neptunium': 237,
        'plutonium': 244,
        'americium': 243,
        'curium': 247,
        'berkelium': 247,
        'californium': 251,
        'einsteinium': 252,
        'fermium': 257,
        'mendelevium': 258,
        'nobelium': 259,
        'lawrencium': 262,
        'rutherfordium': 267,
        'dubnium': 270,
        'seaborgium': 271,
        'bohrium': 270,
        'hassium': 277,
        'meitnerium': 278,
        'darmstadtium': 281,
        'roentgenium': 282,
        'copernicium': 285,
        'nihonium': 286,
        'flerovium': 289,
        'moscovium': 290,
        'livermorium': 293,
        'tennessine': 294,
        'oganesson': 295
    }
    return masses

# Atomic numbers
def atomic_number():
    numbers = {
        'hydrogen': 1,
        'helium': 2,
        'lithium': 3,
        'beryllium': 4,
        'boron': 5,
        'carbon': 6,
        'nitrogen': 7,
        'oxygen': 8,
        'fluorine': 9,
        'neon': 10,
        'sodium': 11,
        'magnesium': 12,
        'aluminum': 13,
        'silicon': 14,
        'phosphorus': 15,
        'sulfur': 16,
        'chlorine': 17,
        'argon': 18,
        'potassium': 19,
        'calcium': 20,
        'scandium': 21,
        'titanium': 22,
        'vanadium': 23,
        'chromium': 24,
        'manganese': 25,
        'iron': 26,
        'cobalt': 27,
        'nickel': 28,
        'copper': 29,
        'zinc': 30,
        'gallium': 31,
        'germanium': 32,
        'arsenic': 33,
        'selenium': 34,
        'bromine': 35,
        'krypton': 36,
        'rubidium': 37,
        'strontium': 38,
        'yttrium': 39,
        'zirconium': 40,
        'niobium': 41,
        'molybdenum': 42,
        'technetium': 43,
        'ruthenium': 44,
        'rhodium': 45,
        'palladium': 46,
        'silver': 47,
        'cadmium': 48,
        'indium': 49,
        'tin': 50,
        'antimony': 51,
        'tellurium': 52,
        'iodine': 53,
        'xenon': 54,
        'cesium': 55,
        'barium': 56,
        'lanthanum': 57,
        'cerium': 58,
        'praseodymium': 59,
        'neodymium': 60,
        'promethium': 61,
        'samarium': 62,
        'europium': 63,
        'gadolinium': 64,
        'terbium': 65,
        'dysprosium': 66,
        'holmium': 67,
        'erbium': 68,
        'thulium': 69,
        'ytterbium': 70,
        'lutetium': 71,
        'hafnium': 72,
        'tantalum': 73,
        'tungsten': 74,
        'rhenium': 75,
        'osmium': 76,
        'iridium': 77,
        'platinum': 78,
        'gold': 79,
        'mercury': 80,
        'thallium': 81,
        'lead': 82,
        'bismuth': 83,
        'polonium': 84,
        'astatine': 85,
        'radon': 86,
        'francium': 87,
        'radium': 88,
        'actinium': 89,
        'thorium': 90,
        'protactinium': 91,
        'uranium': 92,
        'neptunium': 93,
        'plutonium': 94,
        'americium': 95,
        'curium': 96,
        'berkelium': 97,
        'californium': 98,
        'einsteinium': 99,
        'fermium': 100,
        'mendelevium': 101,
        'nobelium': 102,
        'lawrencium': 103,
        'rutherfordium': 104,
        'dubnium': 105,
        'seaborgium': 106,
        'bohrium': 107,
        'hassium': 108,
        'meitnerium': 109,
        'darmstadtium': 110,
        'roentgenium': 111,
        'copernicium': 112,
        'nihonium': 113,
        'flerovium': 114,
        'moscovium': 115,
        'livermorium': 116,
        'tennessine': 117,
        'oganesson': 118
    }
    return numbers

# Atomic symbols
def atomic_symbols():
    symbols = {
        'hydrogen': 'H',
        'helium': 'He',
        'lithium': 'Li',
        'beryllium': 'Be',
        'boron': 'B',
        'carbon': 'C',
        'nitrogen': 'N',
        'oxygen': 'O',
        'fluorine': 'F',
        'neon': 'Ne',
        'sodium': 'Na',
        'magnesium': 'Mg',
        'aluminum': 'Al',
        'silicon': 'Si',
        'phosphorus': 'P',
        'sulfur': 'S',
        'chlorine': 'Cl',
        'argon': 'Ar',
        'potassium': 'K',
        'calcium': 'Ca',
        'scandium': 'Sc',
        'titanium': 'Ti',
        'vanadium': 'V',
        'chromium': 'Cr',
        'manganese': 'Mn',
        'iron': 'Fe',
        'cobalt': 'Co',
        'nickel': 'Ni',
        'copper': 'Cu',
        'zinc': 'Zn',
        'gallium': 'Ga',
        'germanium': 'Ge',
        'arsenic': 'As',
        'selenium': 'Se',
        'bromine': 'Br',
        'krypton': 'Kr',
        'rubidium': 'Rb',
        'strontium': 'Sr',
        'yttrium': 'Y',
        'zirconium': 'Zr',
        'niobium': 'Nb',
        'molybdenum': 'Mo',
        'technetium': 'Tc',
        'ruthenium': 'Ru',
        'rhodium': 'Rh',
        'palladium': 'Pd',
        'silver': 'Ag',
        'cadmium': 'Cd',
        'indium': 'In',
        'tin': 'Sn',
        'antimony': 'Sb',
        'tellurium': 'Te',
        'iodine': 'I',
        'xenon': 'Xe',
        'cesium': 'Cs',
        'barium': 'Ba',
        'lanthanum': 'La',
        'cerium': 'Ce',
        'praseodymium': 'Pr',
        'neodymium': 'Nd',
        'promethium': 'Pm',
        'samarium': 'Sm',
        'europium': 'Eu',
        'gadolinium': 'Gd',
        'terbium': 'Tb',
        'dysprosium': 'Dy',
        'holmium': 'Ho',
        'erbium': 'Er',
        'thulium': 'Tm',
        'ytterbium': 'Yb',
        'lutetium': 'Lu',
        'hafnium': 'Hf',
        'tantalum': 'Ta',
        'tungsten': 'W',
        'rhenium': 'Re',
        'osmium': 'Os',
        'iridium': 'Ir',
        'platinum': 'Pt',
        'gold': 'Au',
        'mercury': 'Hg',
        'thallium': 'Tl',
        'lead': 'Pb',
        'bismuth': 'Bi',
        'polonium': 'Po',
        'astatine': 'At',
        'radon': 'Rn',
        'francium': 'Fr',
        'radium': 'Ra',
        'actinium': 'Ac',
        'thorium': 'Th',
        'protactinium': 'Pa',
        'uranium': 'U',
        'neptunium': 'Np',
        'plutonium': 'Pu',
        'americium': 'Am',
        'curium': 'Cm',
        'berkelium': 'Bk',
        'californium': 'Cf',
        'einsteinium': 'Es',
        'fermium': 'Fm',
        'mendelevium': 'Md',
        'nobelium': 'No',
        'lawrencium': 'Lr',
        'rutherfordium': 'Rf',
        'dubnium': 'Db',
        'seaborgium': 'Sg',
        'bohrium': 'Bh',
        'hassium': 'Hs',
        'meitnerium': 'Mt',
        'darmstadtium': 'Ds',
        'roentgenium': 'Rg',
        'copernicium': 'Cn',
        'nihonium': 'Nh',
        'flerovium': 'Fl',
        'moscovium': 'Mc',
        'livermorium': 'Lv',
        'tennessine': 'Ts',
        'oganesson': 'Og'
    }
    return symbols

# Number of electrons in the outer shell
def num_valence():
    valence = {
        'hydrogen': 1,
        'helium': 2,
        'lithium': 1,
        'beryllium': 2,
        'boron': 3,
        'carbon': 4,
        'nitrogen': 5,
        'oxygen': 6,
        'fluorine': 7,
        'neon': 8,
        'sodium': 1,
        'magnesium': 2,
        'aluminum': 3,
        'silicon': 4,
        'phosphorus': 5,
        'sulfur': 6,
        'chlorine': 7,
        'argon': 8,
        'potassium': 1,
        'calcium': 2,
        'scandium': 3,
        'titanium': 4,
        'vanadium': 5,
        'chromium': 6,
        'manganese': 7,
        'iron': 2,
        'cobalt': 2,
        'nickel': 2,
        'copper': 1,
        'zinc': 2,
        'gallium': 3,
        'germanium': 4,
        'arsenic': 5,
        'selenium': 6,
        'bromine': 7,
        'krypton': 8,
        'rubidium': 1,
        'strontium': 2,
        'yttrium': 3,
        'zirconium': 4,
        'niobium': 5,
        'molybdenum': 6,
        'technetium': 7,
        'ruthenium': 7,
        'rhodium': 9,
        'palladium': 10,
        'silver': 1,
        'cadmium': 2,
        'indium': 3,
        'tin': 4,
        'antimony': 5,
        'tellurium': 6,
        'iodine': 7,
        'xenon': 8,
        'cesium': 1,
        'barium': 2,
        'lanthanum': 2,
        'cerium': 2,
        'praseodymium': 2,
        'neodymium': 2,
        'promethium': 2,
        'samarium': 2,
        'europium': 2,
        'gadolinium': 2,
        'terbium': 2,
        'dysprosium': 2,
        'holmium': 2,
        'erbium': 2,
        'thulium': 2,
        'ytterbium': 2,
        'lutetium': 2,
        'hafnium': 4,
        'tantalum': 5,
        'tungsten': 6,
        'rhenium': 7,
        'osmium': 8,
        'iridium': 9,
        'platinum': 10,
        'gold': 1,
        'mercury': 2,
        'thallium': 3,
        'lead': 4,
        'bismuth': 5,
        'polonium': 6,
        'astatine': 7,
        'radon': 8,
        'francium': 1,
        'radium': 2,
        'actinium': 3,
        'thorium': 4,
        'protactinium': 5,
        'uranium': 6,
        'neptunium': 7,
        'plutonium': 8,
        'americium': 9,
        'curium': 10,
        'berkelium': 3,
        'californium': 3,
        'einsteinium': 3,
        'fermium': 3,
        'mendelevium': 3,
        'nobelium': 3,
        'lawrencium': 3,
        'rutherfordium': 4,
        'dubnium': 5,
        'seaborgium': 6,
        'bohrium': 7,
        'hassium': 8,
        'meitnerium': 9,
        'darmstadtium': 10,
        'roentgenium': 11,
        'copernicium': 12,
        'nihonium': 3,
        'flerovium': 4,
        'moscovium': 5,
        'livermorium': 6,
        'tennessine': 7,
        'oganesson': 8
    }
    return valence

# Element families
def atomic_families():
    families = {
        'hydrogen': 'Nonmetal',
        'helium': 'Noble Gas',
        'lithium': 'Alkali Metal',
        'beryllium': 'Alkaline Earth Metal',
        'boron': 'Metalloid',
        'carbon': 'Nonmetal',
        'nitrogen': 'Nonmetal',
        'oxygen': 'Nonmetal',
        'fluorine': 'Halogen',
        'neon': 'Noble Gas',
        'sodium': 'Alkali Metal',
        'magnesium': 'Alkaline Earth Metal',
        'aluminum': 'Post-Transition Metal',
        'silicon': 'Metalloid',
        'phosphorus': 'Nonmetal',
        'sulfur': 'Nonmetal',
        'chlorine': 'Halogen',
        'argon': 'Noble Gas',
        'potassium': 'Alkali Metal',
        'calcium': 'Alkaline Earth Metal',
        'scandium': 'Transition Metal',
        'titanium': 'Transition Metal',
        'vanadium': 'Transition Metal',
        'chromium': 'Transition Metal',
        'manganese': 'Transition Metal',
        'iron': 'Transition Metal',
        'cobalt': 'Transition Metal',
        'nickel': 'Transition Metal',
        'copper': 'Transition Metal',
        'zinc': 'Transition Metal',
        'gallium': 'Post-Transition Metal',
        'germanium': 'Metalloid',
        'arsenic': 'Metalloid',
        'selenium': 'Nonmetal',
        'bromine': 'Halogen',
        'krypton': 'Noble Gas',
        'rubidium': 'Alkali Metal',
        'strontium': 'Alkaline Earth Metal',
        'yttrium': 'Transition Metal',
        'zirconium': 'Transition Metal',
        'niobium': 'Transition Metal',
        'molybdenum': 'Transition Metal',
        'technetium': 'Transition Metal',
        'ruthenium': 'Transition Metal',
        'rhodium': 'Transition Metal',
        'palladium': 'Transition Metal',
        'silver': 'Transition Metal',
        'cadmium': 'Transition Metal',
        'indium': 'Post-Transition Metal',
        'tin': 'Post-Transition Metal',
        'antimony': 'Metalloid',
        'tellurium': 'Metalloid',
        'iodine': 'Halogen',
        'xenon': 'Noble Gas',
        'cesium': 'Alkali Metal',
        'barium': 'Alkaline Earth Metal',
        'lanthanum': 'Lanthanide',
        'cerium': 'Lanthanide',
        'praseodymium': 'Lanthanide',
        'neodymium': 'Lanthanide',
        'promethium': 'Lanthanide',
        'samarium': 'Lanthanide',
        'europium': 'Lanthanide',
        'gadolinium': 'Lanthanide',
        'terbium': 'Lanthanide',
        'dysprosium': 'Lanthanide',
        'holmium': 'Lanthanide',
        'erbium': 'Lanthanide',
        'thulium': 'Lanthanide',
        'ytterbium': 'Lanthanide',
        'lutetium': 'Lanthanide',
        'hafnium': 'Transition Metal',
        'tantalum': 'Transition Metal',
        'tungsten': 'Transition Metal',
        'rhenium': 'Transition Metal',
        'osmium': 'Transition Metal',
        'iridium': 'Transition Metal',
        'platinum': 'Transition Metal',
        'gold': 'Transition Metal',
        'mercury': 'Transition Metal',
        'thallium': 'Post-Transition Metal',
        'lead': 'Post-Transition Metal',
        'bismuth': 'Post-Transition Metal',
        'polonium': 'Metalloid',
        'astatine': 'Metalloid',
        'radon': 'Noble Gas',
        'francium': 'Alkali Metal',
        'radium': 'Alkaline Earth Metal',
        'actinium': 'Actinide',
        'thorium': 'Actinide',
        'protactinium': 'Actinide',
        'uranium': 'Actinide',
        'neptunium': 'Actinide',
        'plutonium': 'Actinide',
        'americium': 'Actinide',
        'curium': 'Actinide',
        'berkelium': 'Actinide',
        'californium': 'Actinide',
        'einsteinium': 'Actinide',
        'fermium': 'Actinide',
        'mendelevium': 'Actinide',
        'nobelium': 'Actinide',
        'lawrencium': 'Actinide',
        'rutherfordium': 'Transition Metal',
        'dubnium': 'Transition Metal',
        'seaborgium': 'Transition Metal',
        'bohrium': 'Transition Metal',
        'hassium': 'Transition Metal',
        'meitnerium': 'Transition Metal',
        'darmstadtium': 'Transition Metal',
        'roentgenium': 'Transition Metal',
        'copernicium': 'Transition Metal',
        'nihonium': 'Post-Transition Metal',
        'flerovium': 'Post-Transition Metal',
        'moscovium': 'Post-Transition Metal',
        'livermorium': 'Post-Transition Metal',
        'tennessine': 'Halogen',
        'oganesson': 'Noble Gas'
    }
    return families

# Convert dictionary keys to a list for finding elements names
def convert_to_list():
    families = atomic_families()
    return list(families.keys())

# Reactivity to oxygen
def name_origins():
    origin = {
        'hydrogen': 'Greek "hydro" (water) and "genes" (forming)',
        'helium': 'Greek "helios" (sun)',
        'lithium': 'Greek "lithos" (stone)',
        'beryllium': 'Greek "beryllos" (beryl)',
        'boron': 'From "borax", a mineral',
        'carbon': 'Latin "carbo" (coal)',
        'nitrogen': 'Greek "nitron" (niter) and "genes" (forming)',
        'oxygen': 'Greek "oxys" (acid) and "genes" (forming)',
        'fluorine': 'Latin "fluere" (to flow)',
        'neon': 'Greek "neos" (new)',
        'sodium': 'English "soda" (sodium carbonate)',
        'magnesium': 'Magnesia, a district in Greece',
        'aluminum': 'Latin "alumen" (alum)',
        'silicon': 'Latin "silex" (flint)',
        'phosphorus': 'Greek "phosphoros" (light-bringer)',
        'sulfur': 'Latin "sulphur" (brimstone)',
        'chlorine': 'Greek "chloros" (green)',
        'argon': 'Greek "argos" (inactive)',
        'potassium': 'English "potash" (potash)',
        'calcium': 'Latin "calx" (lime)',
        'scandium': 'Latin "Scandia" (Scandinavia)',
        'titanium': 'Greek "Titans" (mythological giants)',
        'vanadium': 'Vanadis, a Scandinavian goddess',
        'chromium': 'Greek "chroma" (color)',
        'manganese': 'Corruption of "magnesia", a mineral',
        'iron': 'Anglo-Saxon "iren" (iron)',
        'cobalt': 'German "kobalt" (goblin)',
        'nickel': 'German "kupfernickel" (devil’s copper)',
        'copper': 'Latin "cuprum" (Cyprus)',
        'zinc': 'German "zinke" (prong or tooth)',
        'gallium': 'Latin "Gallia" (France)',
        'germanium': 'Latin "Germania" (Germany)',
        'arsenic': 'Greek "arsenikon" (yellow orpiment)',
        'selenium': 'Greek "selene" (moon)',
        'bromine': 'Greek "bromos" (stench)',
        'krypton': 'Greek "kryptos" (hidden)',
        'rubidium': 'Latin "rubidus" (deep red)',
        'strontium': 'Strontian, a village in Scotland',
        'yttrium': 'Ytterby, a village in Sweden',
        'zirconium': 'Persian "zargun" (gold-colored)',
        'niobium': 'Greek "Niobe" (mythological figure)',
        'molybdenum': 'Greek "molybdos" (lead)',
        'technetium': 'Greek "technetos" (artificial)',
        'ruthenium': 'Latin "Ruthenia" (Russia)',
        'rhodium': 'Greek "rhodon" (rose)',
        'palladium': 'Pallas, a Greek goddess',
        'silver': 'Anglo-Saxon "seolfor" (silver)',
        'cadmium': 'Latin "cadmia" (calamine)',
        'indium': 'Indigo, the color',
        'tin': 'Anglo-Saxon "tin" (tin)',
        'antimony': 'Greek "anti" (against) and "monos" (alone)',
        'tellurium': 'Latin "tellus" (earth)',
        'iodine': 'Greek "iodes" (violet)',
        'xenon': 'Greek "xenos" (stranger)',
        'cesium': 'Latin "caesius" (sky blue)',
        'barium': 'Greek "barys" (heavy)',
        'lanthanum': 'Greek "lanthanein" (to lie hidden)',
        'cerium': 'Ceres, a Roman goddess',
        'praseodymium': 'Greek "prasios" (green) and "didymos" (twin)',
        'neodymium': 'Greek "neos" (new) and "didymos" (twin)',
        'promethium': 'Prometheus, a Greek god',
        'samarium': 'Samarskite, a mineral',
        'europium': 'Europe, the continent',
        'gadolinium': 'Gadolinite, a mineral',
        'terbium': 'Ytterby, a village in Sweden',
        'dysprosium': 'Greek "dysprositos" (hard to get)',
        'holmium': 'Holmia, the Latin name for Stockholm',
        'erbium': 'Ytterby, a village in Sweden',
        'thulium': 'Thule, a mythical land',
        'ytterbium': 'Ytterby, a village in Sweden',
        'lutetium': 'Latin "Lutetia" (Paris)',
        'hafnium': 'Latin "Hafnia" (Copenhagen)',
        'tantalum': 'Tantalus, a Greek mythological figure',
        'tungsten': 'Swedish "tung sten" (heavy stone)',
        'rhenium': 'Latin "Rhenus" (Rhine River)',
        'osmium': 'Greek "osme" (smell)',
        'iridium': 'Greek "iris" (rainbow)',
        'platinum': 'Spanish "platina" (little silver)',
        'gold': 'Anglo-Saxon "geolu" (yellow)',
        'mercury': 'Mercury, the Roman god',
        'thallium': 'Greek "thallos" (green shoot)',
        'lead': 'Anglo-Saxon "lead" (lead)',
        'bismuth': 'German "bisemutum" (a mineral)',
        'polonium': 'Latin "Polonia" (Poland)',
        'astatine': 'Greek "astatos" (unstable)',
        'radon': 'Latin "radius" (ray)',
        'francium': 'Latin "Francia" (France)',
        'radium': 'Latin "radius" (ray)',
        'actinium': 'Greek "aktinos" (ray)',
        'thorium': 'Thor, a Norse god',
        'protactinium': 'Greek "protos" (first) and "actinium"',
        'uranium': 'Uranus, a Greek god',
        'neptunium': 'Neptune, a Roman god',
        'plutonium': 'Pluto, a Roman god',
        'americium': 'The Americas',
        'curium': 'Marie Curie, a scientist',
        'berkelium': 'Berkeley, California',
        'californium': 'California, USA',
        'einsteinium': 'Albert Einstein, a scientist',
        'fermium': 'Enrico Fermi, a scientist',
        'mendelevium': 'Dmitri Mendeleev, a scientist',
        'nobelium': 'Alfred Nobel, a scientist',
        'lawrencium': 'Ernest Lawrence, a scientist',
        'rutherfordium': 'Ernest Rutherford, a scientist',
        'dubnium': 'Dubna, a town in Russia',
        'seaborgium': 'Glenn Seaborg, a scientist',
        'bohrium': 'Niels Bohr, a scientist',
        'hassium': 'Hassia, the Latin name for Hesse, Germany',
        'meitnerium': 'Lise Meitner, a scientist',
        'darmstadtium': 'Darmstadt, a city in Germany',
        'roentgenium': 'Wilhelm Röntgen, a scientist',
        'copernicium': 'Nicolaus Copernicus, a scientist',
        'nihonium': 'Nihon, the Japanese name for Japan',
        'flerovium': 'Georgy Flerov, a scientist',
        'moscovium': 'Moscow, Russia',
        'livermorium': 'Lawrence Livermore National Laboratory',
        'tennessine': 'Tennessee, USA',
        'oganesson': 'Yuri Oganessian, a scientist'
    }
    return origin

def main():
    print('\n//////////////////////////////////////////\n/// Database for Elemental Information ///\n//////////////////////////////////////////\n')
    choice = 0
    while choice == 1 or 2 or 3 or 4:
        choice = int(input('Choose from the menu:\n1) Atomic Number\n2) Atomic Mass\n3) Symbol\n4) Valence\n5) More info\n6) Find element\n7) Exit\nEnter 1-7: '))
        # Atomic number
        if choice == 1:
            numbers = atomic_number()
            atomic_choice = input('Enter the element: ').lower()

            if atomic_choice in numbers:
                print(f'\nThe atomic number of {atomic_choice} is: {numbers[atomic_choice]}')
            else:
                print(f'Element {atomic_choice.capitalize()} not found.')
        # Atomic mass
        if choice == 2:
            masses = atomic_mass()
            atomic_choice = input('Enter the element: ').lower()

            if atomic_choice in masses:
                print('\nThe atomic mass of ' + str(atomic_choice.capitalize()) + ' is: ' + str(masses[atomic_choice]))
            else:
                print('Element ' + str(atomic_choice.capitalize()) + ' not found.')
        # Atomic symbol
        if choice == 3:
            symbols = atomic_symbols()
            atomic_choice = input('Enter the element: ').lower()

            if atomic_choice in symbols:
                print('\nThe atomic symbol of ' + str(atomic_choice.capitalize()) + ' is: ' + str(symbols[atomic_choice]))
            else:
                print('Element ' + str(atomic_choice.capitalize()) + ' not found.')
        # Valence number
        if choice == 4:
            valence = num_valence()
            atomic_choice = input('Enter the element: ').lower()

            if atomic_choice in valence:
                print(str("\n" + atomic_choice.capitalize()) + ' has ' + str(valence[atomic_choice]) + ' valence electron(s).')
                if (valence[atomic_choice]) >= 8 or atomic_choice == 'hydrogen' or 'helium':
                    print('\nThis element is stable due to the Octet Rule or the 2 valence exception of hydrogen and helium.')
                elif (valence[atomic_choice]) < 8 and atomic_choice != 'hydrogen' or 'helium':
                    print('This element is not stable due to the Octet Rule.')
            else:
                print('Element ' + str(atomic_choice.capitalize()) + ' not found.')
        if choice == 5:
            families = atomic_families()
            origin = name_origins()
            atomic_choice = input('Enter the element: ').lower()

            if atomic_choice in families:
                print('\nThe family of ' + str(atomic_choice.capitalize()) + ' is ' + str(families[atomic_choice]) + '.')
                print('The element\'s name originates from ' + str(origin[atomic_choice]) + '.\n')
            else:
                print('Element ' + str(atomic_choice.capitalize()) + ' not found.')
        if choice == 6:
            finder = input("\nWhat letter does your element start with?\n").lower()
            find_list = convert_to_list()
            letter = finder

            filtered_items = [item for item in find_list if item.startswith(letter)]

            if filtered_items:
                print("Results: ", " | ".join(filtered_items))
            else:
                print("No element begins wih ", letter)

        if choice == 7:
            break

        end_choice = input("\nIs there anything else I can help with? (Y/N)\n").upper()
        if end_choice == "Y":
            continue
        if end_choice == "N":
            break

main()

