from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, Item, Category, User

# todo: connect to psql db
# engine = create_engine('sqlite:///itemcatalog.db')
engine = create_engine('postgres://catalog:c@t@log@localhost/catalog')

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

User1 = User(name="Joe Guitar Guy", email="tinnyTim@udacity.com",
             picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(User1)
session.commit()

User2 = User(name="Mr. No Stairway", email="nostairway@udacity.com",
             picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(User2)
session.commit()

# Categories

cat1 = Category(name="Keys and Synths")
session.add(cat1)
session.commit()

Item1 = Item(user_id=1, name = "Yamaha DX7", description = "Classic FM Synthesis",
	picture="/static/img/dx7.jpg", category = cat1)
session.add(Item1)
session.commit()

Item2 = Item(user_id=1, name = "microKORG", description = "Synthesizer + Vocoder",
	picture="/static/img/microKORG.jpg", category = cat1)
session.add(Item2)
session.commit()

Item3 = Item(user_id=1, name = "ARP 2600", description = "In your dreams",
	picture="/static/img/ARP_2600.jpg", category = cat1)
session.add(Item3)
session.commit()

Item4 = Item(user_id=1, name = "Roland Jupiter 4", description = "Her name is Rio",
	picture="/static/img/jupiter4.jpg", category = cat1)
session.add(Item4)
session.commit()

Item5 = Item(user_id=1, name = "Moog Modular", description = "Monophonic Nirvana",
	picture="/static/img/moogMod.jpg", category = cat1)
session.add(Item5)
session.commit()

## Category Two

cat2 = Category(name="Guitars")
session.add(cat1)
session.commit()

Item1 = Item(user_id=2, name = "Fender Stratocaster", description = "Single re-coiling.",
	picture="/static/img/stratocaster.jpg", category = cat2)
session.add(Item1)
session.commit()

Item2 = Item(user_id=2, name = "Fender Telecaster", description = "Two singles: Why need more?",
	picture="/static/img/telecaster.jpg", category = cat2)
session.add(Item2)
session.commit()

Item3 = Item(user_id=2, name = "Gibson Les Paul", description = "Heavy enough.",
	picture="/static/img/lespaul.jpg", category = cat2)
session.add(Item3)
session.commit()

Item4 = Item(user_id=2, name = "Gretsch Country Gentleman", description = "Yes Yes Yes.",
	picture="/static/img/gretsch-countryg.jpg", category = cat2)
session.add(Item4)
session.commit()

Item5 = Item(user_id=2, name = "Gibson ES 335", description = "Archtop Semi-acoustic.",
	picture="/static/img/gibson-es335.jpg", category = cat2)
session.add(Item5)
session.commit()

# basses

cat3 = Category(name="Basses")
session.add(cat1)
session.commit()

Item1 = Item(user_id=1, name = "Fender Jazz Bass", description = "Smooth",
	picture="/static/img/fender-jazz.jpg", category = cat3)
session.add(Item1)
session.commit()

Item2 = Item(user_id=1, name = "Fender Precision Bass", description = "A Classic",
	picture="/static/img/Fender-P.jpg", category = cat3)
session.add(Item2)
session.commit()

Item3 = Item(user_id=1, name = "Rickenbacker", description = "Heavy Enough For Lemmy",
	picture="/static/img/rickenbackerb.jpg", category = cat3)
session.add(Item3)
session.commit()

Item4 = Item(user_id=1, name = "Gibson Explorer Bass", description = "Get Yer Growl On",
	picture="/static/img/gibson-xbass.jpg", category = cat3)
session.add(Item4)
session.commit()

Item5 = Item(user_id=1, name = "Ernie Ball Music Man", description = "Suck My Kiss",
	picture="/static/img/ernieball-mm.jpg", category = cat3)
session.add(Item5)
session.commit()

#KEEP ADDING STUFF

## add users here

print "added lots of items and users!"

