clouddistrict
=============

Generate occupants and occupations for your custom village, town or city! (for D&D purposes or related) (please do not imbibe clouddistrict while under the influence of other medications)

Installation
------------

From PyPI::

    $ pip install clouddistrict

... or from the project root directory::

    $ python setup.py install

Usage
-----

Creating a town is simple::

    usage: clouddistrict create [-h] [--config CONFIG] output_dir

Example create (defaults to town.yml if not specified)::

    $ usage: clouddistrict create --config example.yml example

``example.yml``::

    # defaults if not specified in the district (in percentages, but any ratios work)
    race:
        human: 60
        elf: 20
        dwarf: 15
        half-elf: 3
        half-orc: 1
        halfling: 1

    # specific district settings, named however you want
    districts:
        cloud district:
            # 100% human. 
            race:
                human: 100
            # Wealth determines the level of residences and commercial buildings, 1 2 or 3 (lower/middle/upper class).
            # Wealth has to do with how much money a family starts with which determines how many businesses they can purchase and own.
            # there are also some businesses which don't spawn in wealth 1 or 2. A bank won't spawn in 2, and an armorer won't spawn in 1.
            # wealth: 2 will cover most of everything except a few businesses: Art gallery, bank, jeweler
            # However, wealth 3 will allow any and every business and the wages will be higher than average, and the houses will be nicer.
            wealth: 3
            # Only 12 families live here.
            residences: 12
            # No shops, just rich people.
            commercial: 0
        upperclass merchant district:
            # Just 20 shops here, but a mix of humans and elves.
            race:
                human: 70
                elf: 20
            wealth: 3
            commercial: 20
        middleclass merchant district:
            # 30 shops of most things. We might see an Inn, an apothecary, a library. Wealth 2 includes almost everything.
            wealth: 2
            commercial: 30
        middleclass houses district:
            # Houses and Cottages are found here. 20 families (1 family per residence).
            # Families may be a nuclear family, a single-mother or single-father, or older siblings, or even just a single person.
            wealth: 2
            residences: 20
        pier district:
            wealth: 1
            commercial: 5
            # Industrial relates to the "resource" type of buildings that house many workers
            # The industrial currently available are: pier, mine, sawmill, quarry
            # This means there will be 1 pier in this district. You choose how many and which specifically.
            industrial:
                pier: 1
            # We specify water as true so we can have water type buildings like waterside taverns. Piers require it to be true in this case.
            water: true
        slums:
            # The slums welcome anyone, and people run small poor businesses. They may not own them, but they work there.
            # Families in the wealth=1 areas are generally too poor to own businesses, though sometimes one might own a cheaper wealth 1 business,
            # like a butcher shop or a tanner.
            wealth: 1
            residences: 40
            commercial: 20
        the old mine:
            # Another industrial-only area which only takes workers.
            wealth: 1
            industrial:
                mine: 1

Use --help/-h to view info on the arguments::

    $ clouddistrict --help
    $ clouddistrict create --help
    $ clouddistrict load --help

Release Notes
-------------

:0.0.2:
    Release
:0.0.1:
    Project created
