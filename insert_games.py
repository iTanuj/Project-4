from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Category, Base, Game, User

engine = create_engine('sqlite:///gamescatalog.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


User1 = User(name="Tanuj Sharma", email="tanuj.goodboy77@gmail.com")
session.add(User1)
session.commit()

category = Category(user_id=1, name="Action")
session.add(category)
session.commit()

game = Game(
    user_id=1, name="Grand Theft Auto: V", description="""Grand Theft Auto V is
     an open-world crime epic set in the LA-inspired city of Los Santos around
     the lives of Franklin, a street hustler looking for real opportunities;
     Michael, a professional ex-con whose retirement isn't all he hoped it
     would be; and Trevor, a violent psychopath.""", category=category)
session.add(game)
session.commit()

game = Game(
    user_id=1, name="Battlefield 1", description="""Battlefield 1 reinvents the
    history of warfare by taking players to World War I in this epic entry into
    the first-person shooter franchise. Through ever-changing environments at
    the dawn of all-out war, no battle is ever the same. The game takes you
    across multiple and varied locations in a bid to fight your way through
    immersive battles. From tight urban fights in a besieged French city, to
    big open spaces in the Italian Alps and frantic combats in the deserts of
    Arabia, discover a world at war through an adventure-filled campaign.""",
    category=category)
session.add(game)
session.commit()

game = Game(user_id=1, name="Batman Arkham Knight", description="""In the
    explosive finale to the Arkham series, Batman
    faces the ultimate threat against the city he is sworn to protect. The
     Scarecrow returns to unite an impressive roster of super villains,
     including Penguin, Two-Face and Harley Quinn, to destroy The Dark
     Knight forever. Batman: Arkham Knight introduces the Batmobile to this
      version of the world of Gotham City, which is drivable for the first
       time in the franchise. The addition of this legendary vehicle,
       combined with the acclaimed gameplay of the Batman Arkham series,
       offers gamers the ultimate and complete Batman experience as they
       tear through the streets and soar across the skyline of the entirety
        of Gotham City.""", category=category)
session.add(game)
session.commit()

game = Game(
    user_id=1, name="DOOM", description="""You’ve come here for a reason.
    The Union Aerospace Corporation’s massive research facility on Mars is
    overwhelmed by fierce and powerful demons, and only one person stands
    between their world and ours. As the lone Doom Marine, you’ve been
    activated to do one thing — kill them all.""", category=category)
session.add(game)
session.commit()

category = Category(user_id=1, name="Adventure")
session.add(category)
session.commit()

game = Game(
    user_id=1, name="Rise Of The Tomb Raider",
    description="""In the wake of her father’s death, Lara’s uncle challeng
    es her ownership of Croft Manor. Lara must explore her childhood home
     in the new “Blood Ties” story mode to reclaim her legacy and uncover
      a family mystery that will change her life forever. In “Lara’s
      Nightmare” hordes of the undead overrun Croft Manor, and Lara must
      defend it before the nightmare overwhelms her! “Blood Ties” includes
       over an hour of additional single player story, as well as community
    challenges with card modifiers that allow you to compete against your
    friends’ scores in “Lara’s Nightmare”.""", category=category)
session.add(game)
session.commit()

game = Game(
    user_id=1, name="Assassins Creed Revelations",
    description="""In Assassin’s Creed® Revelations, master assassin Ezio A
    uditore walks in the footsteps of the legendary mentor Altair, on a jou
    rney of discovery and revelation. It is a perilous path – one that will
     take Ezio to Constantinople, the heart of the Ottoman Empire, where a
     growing army of Templars threatens to destabilize the region.""",
    category=category)
session.add(game)
session.commit()

game = Game(
    user_id=1, name="Far Cry Primal",
    description="""Welcome to the Stone Age, a time of extreme danger and l
    imitless adventure, when giant mammoths and sabretooth tigers ruled the
     Earth and humanity is at the bottom of the food chain. As the last sur
     vivor of your hunting group, you will learn to craft a deadly arsenal,
      fend off fierce predators, and outsmart enemy tribes to conquer the
      land of Oros and become the Apex Predator.""", category=category)
session.add(game)
session.commit()

game = Game(
    user_id=1, name="The Witcher 3: Wild Hunt",
    description="""Geralt of Rivia, is a witcher, or monster hunter for
    hire, a white-haired and cat-eyed legend in his own time. Trained from
    early childhood and mutated to gain superhuman skills, strength and
    reflexes, witchers like Geralt are a natural consequence of and
    counterbalance to the monster-infested world in which they live. As
    Geralt, you’ll embark on an epic journey in a war-ravaged world that
    will inevitably lead you to confront a foe darker than anything
    humanity has faced so far—the Wild Hunt.""", category=category)
session.add(game)
session.commit()

category = Category(user_id=1, name="Horror")
session.add(category)
session.commit()

game = Game(user_id=1, name="Layers of Fear", description="""
        Dare you help paint a true Masterpiece of Fear? Layers of Fear is a
        first-person psychedelic horror game with a heavy focus on story and
        exploration. Delve deep into the mind of an insane painter and discover
         the secret of his madness, as you walk through a vast and constantly
         changing Victorian-era mansion. Uncover the visions, fears and horrors
          that entwine the painter and finish the masterpiece he has strived so
           long to create.""", category=category)
session.add(game)
session.commit()

game = Game(
    user_id=1, name="Outlast 2", description="""
    Outlast 2 introduces you to Sullivan Knoth and his followers, who left
     our wicked world behind to give birth to Temple Gate, a town, deep in
     the wilderness and hidden from civilization. Knoth and his flock are
     preparing for the tribulations of the end of times and you’re right in
      the thick of it.

    You are Blake Langermann, a cameraman working with your wife, Lynn. The
     two of you are investigative journalists willing to take risks and dig
      deep to uncover the stories no one else will dare touch.""",
    category=category)
session.add(game)
session.commit()

game = Game(user_id=1, name="Resident Evil 7 Biohazard", description=""""
        Resident Evil 7 biohazard is the next major entry in the renowned
        Resident Evil series and sets a new course for the franchise as it
        leverages its roots and opens the door to a truly terrifying horror
        experience. A dramatic new shift for the series to first person view
        in a photorealistic style powered by Capcom’s new RE Engine, Resident
        Evil 7 delivers an unprecedented level of immersion that brings the
        thrilling horror up close and personal.""", category=category)
session.add(game)
session.commit()

game = Game(user_id=1, name="Friday the 13th", description="""
        Friday the 13th: The Game is a third-person horror, survival game
        where players take on the role of a teen counselor, or for the first
        time ever, Jason Voorhees. You and six other unlucky souls will do
        everything possible to escape and survive while the most well-known
        killer in the world tracks you down and brutally slaughters you.
        Friday the 13th: The Game will strive to give every single player the
        tools to survive, escape or even try to take down the man who cannot
        be killed. Each and every gameplay session will give you an entirely
        new chance to prove if you have what it takes not only to survive, but
        to best the most prolific killer in cinema history, a slasher with
        more kills than any of his rivals!""", category=category)
session.add(game)
session.commit()

category = Category(user_id=1, name="Racing")
session.add(category)
session.commit()

game = Game(user_id=1, name="Forza Horizon 3", description="""
        In Forza Horizon 3 you’re in charge of the Horizon Festival. Customize
        everything, hire and fire your friends, and explore Australia in over
        350 of the world’s greatest cars. Make your Horizon the ultimate
        celebration of cars, music, and freedom of the open road. How you get
        there is up to you.""", category=category)
session.add(game)
session.commit()

game = Game(user_id=1, name="Need for Speed Most Wanted", description="""
        Do you have what it takes to become Most Wanted? Designed for a new,
        more connected generation of racing fans, Need for Speed Most Wanted
        offers players an expansive open world packed with exhilarating action
        where they can choose their own path to become the Most Wanted.
        Players will have the freedom to drive anywhere, discover hidden
        gameplay, takedown rivals, challenge friends or just hang out and toy
        with the cops. Everything they do counts towards the end goal of
        becoming #1 on their personal Most Wanted List.""", category=category)
session.add(game)
session.commit()

game = Game(user_id=1, name="GRID 2", description="""
        Be fast, be first and be famous as the race returns in GRID 2, the
        sequel to the BAFTA-award winning, multi-million selling Race Driver:
        GRID. Experience aggressive racing against advanced AI and become
        immersed in the race with GRID 2’s new TrueFeel™ Handling system which
        powers edge of control exhilaration behind the wheel of every iconic
        car. The next generation of the EGO Game Technology Platform delivers
        genre-defining visuals and jaw-dropping damage as you prove yourself
        across three continents in a new, evolving world of motorsport. Earn
        fame, fans and fortune as you blaze your way to the top in intense,
        relentless races on licensed circuits, beautifully realised city
        streets and lethal mountain roads.""", category=category)
session.add(game)
session.commit()

game = Game(
    user_id=1, name="DiRT 4", description="""
    Motorsport by its very nature is dangerous. DiRT 4 is all about
    embracing that danger. It’s about the thrill, exhilaration and
    adrenaline that is absolutely vital to off-road racing. And more than
    that, it’s about loving that feeling. It’s about pushing flat out next
    to a sheer cliff drop. Going for the gap that’s slightly too small.
    Seeing how much air you can get in a truck. They call it ‘being
    fearless’.""", category=category)
session.add(game)
session.commit()

category = Category(user_id=1, name="RPG")
session.add(category)
session.commit()

game = Game(
    user_id=1, name="Diablo III", description="""
    Diablo III is a fantasy action RPG that continues the land of
    Sanctuary's battle against a reoccurring demonic evil, and provides
    players around the world with the opportunity to create the ultimate
    hero to quest against it with friends online, or on their own.""",
    category=category)
session.add(game)
session.commit()

game = Game(
    user_id=1, name="Fallout 4", description="""
    Bethesda Game Studios, the award-winning creators of Fallout 3 and The
    Elder Scrolls V: Skyrim, welcome you to the world of Fallout 4 – their
    most ambitious game ever, and the next generation of open-world gaming.
     As the sole survivor of Vault 111, you enter a world destroyed by
     nuclear war. Every second is a fight for survival, and every choice
     is yours. Only you can rebuild and determine the fate of the
     Wasteland. Welcome home.""", category=category)
session.add(game)
session.commit()

game = Game(
    user_id=1, name="The Elder Scrolls V: Skyrim", description="""
    In The Elder Scrolls V: Skyrim, you take up arms against dragons, and
    your encounters with them are invariably exciting--yet depending on
    where your adventure takes you, such battles may not even represent
    the pinnacle of your experience. A side quest that starts as a
    momentary distraction may turn into a full-fledged tale that could
    form the entirety of a less ambitious game. Yes, Skyrim is another
    enormous fantasy RPG from a developer that specializes in them, and it
    could suck up hundreds of hours of your time as you inspect each nook
    and crevasse for the secrets to be found within.""", category=category)
session.add(game)
session.commit()

game = Game(user_id=1, name="Bloodborne", description="""
        Bloodborne is a 2015 Action RPG from renowned Japanese developer
        FromSoftware exclusively for the PlayStation 4 system. Face your fears
        as you search for answers in the ancient city of Yharnam, now cursed
        with a strange endemic illness spreading through the streets like
        wildfire. Danger, death and madness lurk around every corner of this
        dark and horrific world, and you must discover its darkest secrets in
        order to survive.""", category=category)
session.add(game)
session.commit()

category = Category(user_id=1, name="Shooting")
session.add(category)
session.commit()

game = Game(user_id=1, name="Call of Duty Black Ops", description="""
        The biggest first-person action series of all time and the follow-up
        to last year’s blockbuster Call of Duty®: Modern Warfare 2 returns
        with Call of Duty®: Black Ops. Call of Duty®: Black Ops will take you
        behind enemy lines as a member of an elite special forces unit
        engaging in covert warfare, classified operations, and explosive
        conflicts across the globe. With access to exclusive weaponry and
        equipment, your actions will tip the balance during the most dangerous
        time period mankind has ever known.""", category=category)
session.add(game)
session.commit()

game = Game(user_id=1, name="Counter Strike: Global Offensive", description="""
        Counter-Strike: Global Offensive (abbreviated as CS:GO) is an online
        first-person shooter developed by Valve Corporation and Hidden Path
        Entertainment, who also maintained Counter-Strike: Source after its
        release. It is the fourth game in the Counter-Strike franchise,
        excluding Counter-Strike Neo and Online.""", category=category)
session.add(game)
session.commit()

game = Game(
    user_id=1, name="Overwatch", description="""
    Overwatch™ is a highly stylized team-based shooter set in a future
    worth fighting for. Every match is an intense multiplayer showdown
    pitting a diverse cast of soldiers, scientists, adventurers, and
    oddities against each other in an epic, globe-spanning conflict. """,
    category=category)
session.add(game)
session.commit()

game = Game(user_id=1, name="Wolfenstein The Old Blood", description="""
        Part one of Wolfenstein: The Old Blood – Rudi Jäger and the Den of
        Wolves – pits BJ Blazkowicz against a maniacal prison warden as he
        breaks into Castle Wolfenstein in an attempt to steal the coordinates
        to General Deathshead’s compound. In part two – The Dark Secrets of
        Helga Von Schabbs – our hero’s search for the coordinates leads him to
        the city of Wulfburg where an obsessed Nazi archaeologist is exhuming
        mysterious artifacts that threaten to unleash a dark and ancient
        power.""", category=category)
session.add(game)
session.commit()

category = Category(user_id=1, name="Sports")
session.add(category)
session.commit()

game = Game(
    user_id=1, name="FIFA 17", description="""
    FIFA 17 immerses you in authentic football experiences by leveraging
    the sophistication of a new game engine, while introducing you to
    football players full of depth and emotion, and taking you to brand
    new worlds accessible only in the game. Complete innovation in the way
    players think and move, physically interact with opponents, and
    execute in attack lets you own every moment on the pitch.""",
    category=category)
session.add(game)
session.commit()

game = Game(
    user_id=1, name="Rocket League", description="""
    Soccer meets driving once again in the long-awaited, physics-based
    sequel to the beloved arena classic, Supersonic Acrobatic Rocket-
    Powered Battle-Cars! A futuristic Sports-Action game, Rocket League,
    equips players with booster-rigged vehicles that can be crashed into
    balls for incredible goals or epic saves across multiple, highly-
    detailed arenas. Using an advanced physics system to simulate
    realistic interactions, Rocket League relies on mass and momentum to
    give players a complete sense of intuitive control in this
    unbelievable, high-octane re-imagining of association football.""",
    category=category)
session.add(game)
session.commit()

game = Game(user_id=1, name="WWE 2K16", description="""
        Step into the ring for the 2016 edition of WWE wrestling action! WWE
        2K16 delivers authentic, high-powered and hard-hitting action,
        including fan-favorite features and new WWE Superstars, Divas and
        Legends, gameplay innovations, presentation updates and more. Offering
        more than 120 unique playable characters, including cover Superstar
        Stone Cold Steve Austin alongside Seth Rollins, Daniel Bryan, Dean
        Ambrose, Bad News Barrett, Paige and Finn Bálor, WWE 2K16 includes the
        largest roster in WWE games history!""", category=category)
session.add(game)
session.commit()

game = Game(user_id=1, name="Steep", description="""
        In Steep, players can use the innovative trail feature to relive their
        most inspiring rides and trailblazing achievements, and share them on
        social networks with friends. Along with sharing ride replays, players
        can also use this feature to challenge friends to outrace them on a
        shared path, create epic stunts or set out to discover the massive
        mountain playground.""", category=category)
session.add(game)
session.commit()

print("Games and their categories have been added!")
