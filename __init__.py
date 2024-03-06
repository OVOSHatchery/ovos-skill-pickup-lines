import random
from os.path import join, dirname

import requests
from bs4 import BeautifulSoup
from ovos_workshop.decorators import intent_handler
from ovos_workshop.decorators import resting_screen_handler
from ovos_workshop.intents import IntentBuilder
from ovos_workshop.skills import OVOSSkill


class PickupLineSkill(OVOSSkill):
    categories = [
        'cheesy', 'crude', 'women', 'tinder', 'computer', 'harrypotter',
        'math', 'biochem', 'physics', 'musician', 'disney', 'vegan', 'scifi',
        'warcraft', 'videogame', 'pokemon', 'rejections', 'desi', 'astronomy',
        'redneck', 'food', 'engineering', 'gameofthrones', 'lotr',
        'hungergames', 'twilight', 'doctorwho', 'breakingbad', 'madmen',
        'himym', 'bigbangtheory', 'brandname', 'gaylesbian', 'travel', 'bad',
        'mean', 'golf', 'basketball', 'football', 'baseball', 'bowling',
        'hockey', 'soccer', 'lacrosse', 'tennis', 'volleyball', 'cheerleader',
        'gym', 'yoga', 'biker', 'beach', 'casino', 'waitress', 'anime', 'halo',
        'callofduty', 'mario', 'zelda', 'minecraft', 'fortnite',
        'leaguelegends', 'superman', 'avengers', 'justinbieber', 'drake',
        'political', 'trump', 'twitter', 'marijuana', 'doctor', 'dentist',
        'law', 'stockmarket', 'economics', 'realestate', 'business', 'tall',
        'shakespeare', 'senior', 'psychology', 'gothic', 'robot', 'celebrity',
        'treehugger', 'artist', 'olympics', 'police', 'walkingdead',
        'bookworm', 'wedding', 'airport', 'satprep', 'modelun', 'backtoschool',
        'christian', 'jewish', 'islamic', 'catholic', 'hindu', 'mormon',
        'buddhist', 'atheist', 'scientology', 'car', 'cowboy', 'mexican',
        'french', 'spanish', 'portuguese', 'germany', 'italian', 'sweden',
        'finnish', 'czech', 'dutch', 'australian', 'jamaican', 'denmark',
        'norway', 'iceland', 'croatian', 'filipino', 'polish', 'indonesian',
        'canadian', 'stpattys', 'bollywood', 'movie', 'musicfestival',
        'fencing', 'historical', 'alien', 'ethnicity', 'breakup',
        'valentinesday', 'coffee', 'accountant', 'animal', 'military',
        'chocolate', 'icecream', 'blackfriday', 'ghetto', 'magic',
        'firefighter', 'pizza', 'christmas', 'halloween', 'easter',
        'thanksgiving', 'independence', 'nye', 'pirate', 'medieval', 'dog',
        'memes'
    ]

    @staticmethod
    def get_line(category="random"):
        if category == "random":
            category = random.choice(PickupLineSkill.categories)

        url = f"http://www.pickuplinesgalore.com/{category}.html"

        soup = BeautifulSoup(requests.get(url).text, "html.parser")
        lines = "".join([
            i.text for i in soup.select(
                "main > p.action-paragraph.paragraph > span.paragraph-text-7"
            )
        ]).split("\n\n")
        return random.choice(lines)

    def initialize(self):
        if "default_category" not in self.settings:
            self.settings["default_category"] = "cheesy"

    def update_line(self, category="cheesy"):
        self.gui['line'] = self.get_line(category)

    @resting_screen_handler("PickupLines")
    def idle(self, message):
        self.gui.clear()
        self.gui['pickup_line'] = self.get_line(self.settings["default_category"])
        self.gui.show_text(self.gui['pickup_line'])

    def speak_line(self, category="random"):
        self.gui.clear()
        line = self.get_line(category)
        self.gui['pickup_line'] = line
        self.gui.show_text(line)
        self.speak(line, wait=True)
        self.gui.clear()

    @intent_handler(IntentBuilder("PickupLineIntent")
                    .require("pickup_line"))
    def handle_line(self, message):
        self.speak_line(self.settings["default_category"])

    @intent_handler("source.intent")
    def handle_source(self, message):
        self.gui.show_image(join(dirname(__file__), "logo.png"),
                            fill='PreserveAspectFit')
        self.speak_dialog("source", wait=True)
        self.gui.clear()

    @intent_handler(IntentBuilder("PickupLineIntent")
                    .require("pickup_line").require("random"))
    def handle_random_line(self, message):
        self.speak_line("random")

    # categories (auto generated)
    @intent_handler(IntentBuilder("CheesyPickupLineIntent")
                    .require("pickup_line").require("cheesy")
                    .optionally("about"))
    def handle_cheesy_pickup_line(self, message):
        self.speak_line("cheesy")

    @intent_handler(IntentBuilder("CrudePickupLineIntent")
                    .require("pickup_line").require("crude")
                    .optionally("about"))
    def handle_crude_pickup_line(self, message):
        self.speak_line("crude")

    @intent_handler(IntentBuilder("WomenPickupLineIntent")
                    .require("pickup_line").require("women")
                    .optionally("about"))
    def handle_women_pickup_line(self, message):
        self.speak_line("women")

    @intent_handler(IntentBuilder("TinderPickupLineIntent")
                    .require("pickup_line").require("tinder")
                    .optionally("about"))
    def handle_tinder_pickup_line(self, message):
        self.speak_line("tinder")

    @intent_handler(IntentBuilder("ComputerPickupLineIntent")
                    .require("pickup_line").require("computer")
                    .optionally("about"))
    def handle_computer_pickup_line(self, message):
        self.speak_line("computer")

    @intent_handler(IntentBuilder("HarrypotterPickupLineIntent")
                    .require("pickup_line").require("harrypotter")
                    .optionally("about"))
    def handle_harrypotter_pickup_line(self, message):
        self.speak_line("harrypotter")

    @intent_handler(IntentBuilder("MathPickupLineIntent")
                    .require("pickup_line").require("math")
                    .optionally("about"))
    def handle_math_pickup_line(self, message):
        self.speak_line("math")

    @intent_handler(IntentBuilder("BiochemPickupLineIntent")
                    .require("pickup_line").require("biochem")
                    .optionally("about"))
    def handle_biochem_pickup_line(self, message):
        self.speak_line("biochem")

    @intent_handler(IntentBuilder("PhysicsPickupLineIntent")
                    .require("pickup_line").require("physics")
                    .optionally("about"))
    def handle_physics_pickup_line(self, message):
        self.speak_line("physics")

    @intent_handler(IntentBuilder("MusicianPickupLineIntent")
                    .require("pickup_line").require("musician")
                    .optionally("about"))
    def handle_musician_pickup_line(self, message):
        self.speak_line("musician")

    @intent_handler(IntentBuilder("DisneyPickupLineIntent")
                    .require("pickup_line").require("disney")
                    .optionally("about"))
    def handle_disney_pickup_line(self, message):
        self.speak_line("disney")

    @intent_handler(IntentBuilder("VeganPickupLineIntent")
                    .require("pickup_line").require("vegan")
                    .optionally("about"))
    def handle_vegan_pickup_line(self, message):
        self.speak_line("vegan")

    @intent_handler(IntentBuilder("ScifiPickupLineIntent")
                    .require("pickup_line").require("scifi")
                    .optionally("about"))
    def handle_scifi_pickup_line(self, message):
        self.speak_line("scifi")

    @intent_handler(IntentBuilder("WarcraftPickupLineIntent")
                    .require("pickup_line").require("warcraft")
                    .optionally("about"))
    def handle_warcraft_pickup_line(self, message):
        self.speak_line("warcraft")

    @intent_handler(IntentBuilder("VideogamePickupLineIntent")
                    .require("pickup_line").require("videogame")
                    .optionally("about"))
    def handle_videogame_pickup_line(self, message):
        self.speak_line("videogame")

    @intent_handler(IntentBuilder("PokemonPickupLineIntent")
                    .require("pickup_line").require("pokemon")
                    .optionally("about"))
    def handle_pokemon_pickup_line(self, message):
        self.speak_line("pokemon")

    @intent_handler(IntentBuilder("RejectionsPickupLineIntent")
                    .require("pickup_line").require("rejections")
                    .optionally("about"))
    def handle_rejections_pickup_line(self, message):
        self.speak_line("rejections")

    @intent_handler(IntentBuilder("DesiPickupLineIntent")
                    .require("pickup_line").require("desi")
                    .optionally("about"))
    def handle_desi_pickup_line(self, message):
        self.speak_line("desi")

    @intent_handler(IntentBuilder("AstronomyPickupLineIntent")
                    .require("pickup_line").require("astronomy")
                    .optionally("about"))
    def handle_astronomy_pickup_line(self, message):
        self.speak_line("astronomy")

    @intent_handler(IntentBuilder("RedneckPickupLineIntent")
                    .require("pickup_line").require("redneck")
                    .optionally("about"))
    def handle_redneck_pickup_line(self, message):
        self.speak_line("redneck")

    @intent_handler(IntentBuilder("FoodPickupLineIntent")
                    .require("pickup_line").require("food")
                    .optionally("about"))
    def handle_food_pickup_line(self, message):
        self.speak_line("food")

    @intent_handler(IntentBuilder("EngineeringPickupLineIntent")
                    .require("pickup_line").require("engineering")
                    .optionally("about"))
    def handle_engineering_pickup_line(self, message):
        self.speak_line("engineering")

    @intent_handler(IntentBuilder("GameofthronesPickupLineIntent")
                    .require("pickup_line").require("gameofthrones")
                    .optionally("about"))
    def handle_gameofthrones_pickup_line(self, message):
        self.speak_line("gameofthrones")

    @intent_handler(IntentBuilder("LotrPickupLineIntent")
                    .require("pickup_line").require("lotr")
                    .optionally("about"))
    def handle_lotr_pickup_line(self, message):
        self.speak_line("lotr")

    @intent_handler(IntentBuilder("HungergamesPickupLineIntent")
                    .require("pickup_line").require("hungergames")
                    .optionally("about"))
    def handle_hungergames_pickup_line(self, message):
        self.speak_line("hungergames")

    @intent_handler(IntentBuilder("TwilightPickupLineIntent")
                    .require("pickup_line").require("twilight")
                    .optionally("about"))
    def handle_twilight_pickup_line(self, message):
        self.speak_line("twilight")

    @intent_handler(IntentBuilder("DoctorwhoPickupLineIntent")
                    .require("pickup_line").require("doctorwho")
                    .optionally("about"))
    def handle_doctorwho_pickup_line(self, message):
        self.speak_line("doctorwho")

    @intent_handler(IntentBuilder("BreakingbadPickupLineIntent")
                    .require("pickup_line").require("breakingbad")
                    .optionally("about"))
    def handle_breakingbad_pickup_line(self, message):
        self.speak_line("breakingbad")

    @intent_handler(IntentBuilder("MadmenPickupLineIntent")
                    .require("pickup_line").require("madmen")
                    .optionally("about"))
    def handle_madmen_pickup_line(self, message):
        self.speak_line("madmen")

    @intent_handler(IntentBuilder("HimymPickupLineIntent")
                    .require("pickup_line").require("himym")
                    .optionally("about"))
    def handle_himym_pickup_line(self, message):
        self.speak_line("himym")

    @intent_handler(IntentBuilder("BigbangtheoryPickupLineIntent")
                    .require("pickup_line").require("bigbangtheory")
                    .optionally("about"))
    def handle_bigbangtheory_pickup_line(self, message):
        self.speak_line("bigbangtheory")

    @intent_handler(IntentBuilder("BrandnamePickupLineIntent")
                    .require("pickup_line").require("brandname")
                    .optionally("about"))
    def handle_brandname_pickup_line(self, message):
        self.speak_line("brandname")

    @intent_handler(IntentBuilder("GaylesbianPickupLineIntent")
                    .require("pickup_line").require("gaylesbian")
                    .optionally("about"))
    def handle_gaylesbian_pickup_line(self, message):
        self.speak_line("gaylesbian")

    @intent_handler(IntentBuilder("TravelPickupLineIntent")
                    .require("pickup_line").require("travel")
                    .optionally("about"))
    def handle_travel_pickup_line(self, message):
        self.speak_line("travel")

    @intent_handler(IntentBuilder("BadPickupLineIntent")
                    .require("pickup_line").require("bad")
                    .optionally("about"))
    def handle_bad_pickup_line(self, message):
        self.speak_line("bad")

    @intent_handler(IntentBuilder("MeanPickupLineIntent")
                    .require("pickup_line").require("mean")
                    .optionally("about"))
    def handle_mean_pickup_line(self, message):
        self.speak_line("mean")

    @intent_handler(IntentBuilder("GolfPickupLineIntent")
                    .require("pickup_line").require("golf")
                    .optionally("about"))
    def handle_golf_pickup_line(self, message):
        self.speak_line("golf")

    @intent_handler(IntentBuilder("BasketballPickupLineIntent")
                    .require("pickup_line").require("basketball")
                    .optionally("about"))
    def handle_basketball_pickup_line(self, message):
        self.speak_line("basketball")

    @intent_handler(IntentBuilder("FootballPickupLineIntent")
                    .require("pickup_line").require("football")
                    .optionally("about"))
    def handle_football_pickup_line(self, message):
        self.speak_line("football")

    @intent_handler(IntentBuilder("BaseballPickupLineIntent")
                    .require("pickup_line").require("baseball")
                    .optionally("about"))
    def handle_baseball_pickup_line(self, message):
        self.speak_line("baseball")

    @intent_handler(IntentBuilder("BowlingPickupLineIntent")
                    .require("pickup_line").require("bowling")
                    .optionally("about"))
    def handle_bowling_pickup_line(self, message):
        self.speak_line("bowling")

    @intent_handler(IntentBuilder("HockeyPickupLineIntent")
                    .require("pickup_line").require("hockey")
                    .optionally("about"))
    def handle_hockey_pickup_line(self, message):
        self.speak_line("hockey")

    @intent_handler(IntentBuilder("SoccerPickupLineIntent")
                    .require("pickup_line").require("soccer")
                    .optionally("about"))
    def handle_soccer_pickup_line(self, message):
        self.speak_line("soccer")

    @intent_handler(IntentBuilder("LacrossePickupLineIntent")
                    .require("pickup_line").require("lacrosse")
                    .optionally("about"))
    def handle_lacrosse_pickup_line(self, message):
        self.speak_line("lacrosse")

    @intent_handler(IntentBuilder("TennisPickupLineIntent")
                    .require("pickup_line").require("tennis")
                    .optionally("about"))
    def handle_tennis_pickup_line(self, message):
        self.speak_line("tennis")

    @intent_handler(IntentBuilder("VolleyballPickupLineIntent")
                    .require("pickup_line").require("volleyball")
                    .optionally("about"))
    def handle_volleyball_pickup_line(self, message):
        self.speak_line("volleyball")

    @intent_handler(IntentBuilder("CheerleaderPickupLineIntent")
                    .require("pickup_line").require("cheerleader")
                    .optionally("about"))
    def handle_cheerleader_pickup_line(self, message):
        self.speak_line("cheerleader")

    @intent_handler(IntentBuilder("GymPickupLineIntent")
                    .require("pickup_line").require("gym")
                    .optionally("about"))
    def handle_gym_pickup_line(self, message):
        self.speak_line("gym")

    @intent_handler(IntentBuilder("YogaPickupLineIntent")
                    .require("pickup_line").require("yoga")
                    .optionally("about"))
    def handle_yoga_pickup_line(self, message):
        self.speak_line("yoga")

    @intent_handler(IntentBuilder("BikerPickupLineIntent")
                    .require("pickup_line").require("biker")
                    .optionally("about"))
    def handle_biker_pickup_line(self, message):
        self.speak_line("biker")

    @intent_handler(IntentBuilder("BeachPickupLineIntent")
                    .require("pickup_line").require("beach")
                    .optionally("about"))
    def handle_beach_pickup_line(self, message):
        self.speak_line("beach")

    @intent_handler(IntentBuilder("CasinoPickupLineIntent")
                    .require("pickup_line").require("casino")
                    .optionally("about"))
    def handle_casino_pickup_line(self, message):
        self.speak_line("casino")

    @intent_handler(IntentBuilder("WaitressPickupLineIntent")
                    .require("pickup_line").require("waitress")
                    .optionally("about"))
    def handle_waitress_pickup_line(self, message):
        self.speak_line("waitress")

    @intent_handler(IntentBuilder("AnimePickupLineIntent")
                    .require("pickup_line").require("anime")
                    .optionally("about"))
    def handle_anime_pickup_line(self, message):
        self.speak_line("anime")

    @intent_handler(IntentBuilder("HaloPickupLineIntent")
                    .require("pickup_line").require("halo")
                    .optionally("about"))
    def handle_halo_pickup_line(self, message):
        self.speak_line("halo")

    @intent_handler(IntentBuilder("CallofdutyPickupLineIntent")
                    .require("pickup_line").require("callofduty")
                    .optionally("about"))
    def handle_callofduty_pickup_line(self, message):
        self.speak_line("callofduty")

    @intent_handler(IntentBuilder("MarioPickupLineIntent")
                    .require("pickup_line").require("mario")
                    .optionally("about"))
    def handle_mario_pickup_line(self, message):
        self.speak_line("mario")

    @intent_handler(IntentBuilder("ZeldaPickupLineIntent")
                    .require("pickup_line").require("zelda")
                    .optionally("about"))
    def handle_zelda_pickup_line(self, message):
        self.speak_line("zelda")

    @intent_handler(IntentBuilder("MinecraftPickupLineIntent")
                    .require("pickup_line").require("minecraft")
                    .optionally("about"))
    def handle_minecraft_pickup_line(self, message):
        self.speak_line("minecraft")

    @intent_handler(IntentBuilder("FortnitePickupLineIntent")
                    .require("pickup_line").require("fortnite")
                    .optionally("about"))
    def handle_fortnite_pickup_line(self, message):
        self.speak_line("fortnite")

    @intent_handler(IntentBuilder("LeaguelegendsPickupLineIntent")
                    .require("pickup_line").require("leaguelegends")
                    .optionally("about"))
    def handle_leaguelegends_pickup_line(self, message):
        self.speak_line("leaguelegends")

    @intent_handler(IntentBuilder("SupermanPickupLineIntent")
                    .require("pickup_line").require("superman")
                    .optionally("about"))
    def handle_superman_pickup_line(self, message):
        self.speak_line("superman")

    @intent_handler(IntentBuilder("AvengersPickupLineIntent")
                    .require("pickup_line").require("avengers")
                    .optionally("about"))
    def handle_avengers_pickup_line(self, message):
        self.speak_line("avengers")

    @intent_handler(IntentBuilder("JustinbieberPickupLineIntent")
                    .require("pickup_line").require("justinbieber")
                    .optionally("about"))
    def handle_justinbieber_pickup_line(self, message):
        self.speak_line("justinbieber")

    @intent_handler(IntentBuilder("DrakePickupLineIntent")
                    .require("pickup_line").require("drake")
                    .optionally("about"))
    def handle_drake_pickup_line(self, message):
        self.speak_line("drake")

    @intent_handler(IntentBuilder("PoliticalPickupLineIntent")
                    .require("pickup_line").require("political")
                    .optionally("about"))
    def handle_political_pickup_line(self, message):
        self.speak_line("political")

    @intent_handler(IntentBuilder("TrumpPickupLineIntent")
                    .require("pickup_line").require("trump")
                    .optionally("about"))
    def handle_trump_pickup_line(self, message):
        self.speak_line("trump")

    @intent_handler(IntentBuilder("TwitterPickupLineIntent")
                    .require("pickup_line").require("twitter")
                    .optionally("about"))
    def handle_twitter_pickup_line(self, message):
        self.speak_line("twitter")

    @intent_handler(IntentBuilder("MarijuanaPickupLineIntent")
                    .require("pickup_line").require("marijuana")
                    .optionally("about"))
    def handle_marijuana_pickup_line(self, message):
        self.speak_line("marijuana")

    @intent_handler(IntentBuilder("DoctorPickupLineIntent")
                    .require("pickup_line").require("doctor")
                    .optionally("about"))
    def handle_doctor_pickup_line(self, message):
        self.speak_line("doctor")

    @intent_handler(IntentBuilder("DentistPickupLineIntent")
                    .require("pickup_line").require("dentist")
                    .optionally("about"))
    def handle_dentist_pickup_line(self, message):
        self.speak_line("dentist")

    @intent_handler(IntentBuilder("LawPickupLineIntent")
                    .require("pickup_line").require("law")
                    .optionally("about"))
    def handle_law_pickup_line(self, message):
        self.speak_line("law")

    @intent_handler(IntentBuilder("StockmarketPickupLineIntent")
                    .require("pickup_line").require("stockmarket")
                    .optionally("about"))
    def handle_stockmarket_pickup_line(self, message):
        self.speak_line("stockmarket")

    @intent_handler(IntentBuilder("EconomicsPickupLineIntent")
                    .require("pickup_line").require("economics")
                    .optionally("about"))
    def handle_economics_pickup_line(self, message):
        self.speak_line("economics")

    @intent_handler(IntentBuilder("RealestatePickupLineIntent")
                    .require("pickup_line").require("realestate")
                    .optionally("about"))
    def handle_realestate_pickup_line(self, message):
        self.speak_line("realestate")

    @intent_handler(IntentBuilder("BusinessPickupLineIntent")
                    .require("pickup_line").require("business")
                    .optionally("about"))
    def handle_business_pickup_line(self, message):
        self.speak_line("business")

    @intent_handler(IntentBuilder("TallPickupLineIntent")
                    .require("pickup_line").require("tall")
                    .optionally("about"))
    def handle_tall_pickup_line(self, message):
        self.speak_line("tall")

    @intent_handler(IntentBuilder("ShakespearePickupLineIntent")
                    .require("pickup_line").require("shakespeare")
                    .optionally("about"))
    def handle_shakespeare_pickup_line(self, message):
        self.speak_line("shakespeare")

    @intent_handler(IntentBuilder("SeniorPickupLineIntent")
                    .require("pickup_line").require("senior")
                    .optionally("about"))
    def handle_senior_pickup_line(self, message):
        self.speak_line("senior")

    @intent_handler(IntentBuilder("PsychologyPickupLineIntent")
                    .require("pickup_line").require("psychology")
                    .optionally("about"))
    def handle_psychology_pickup_line(self, message):
        self.speak_line("psychology")

    @intent_handler(IntentBuilder("GothicPickupLineIntent")
                    .require("pickup_line").require("gothic")
                    .optionally("about"))
    def handle_gothic_pickup_line(self, message):
        self.speak_line("gothic")

    @intent_handler(IntentBuilder("RobotPickupLineIntent")
                    .require("pickup_line").require("robot")
                    .optionally("about"))
    def handle_robot_pickup_line(self, message):
        self.speak_line("robot")

    @intent_handler(IntentBuilder("CelebrityPickupLineIntent")
                    .require("pickup_line").require("celebrity")
                    .optionally("about"))
    def handle_celebrity_pickup_line(self, message):
        self.speak_line("celebrity")

    @intent_handler(IntentBuilder("TreehuggerPickupLineIntent")
                    .require("pickup_line").require("treehugger")
                    .optionally("about"))
    def handle_treehugger_pickup_line(self, message):
        self.speak_line("treehugger")

    @intent_handler(IntentBuilder("ArtistPickupLineIntent")
                    .require("pickup_line").require("artist")
                    .optionally("about"))
    def handle_artist_pickup_line(self, message):
        self.speak_line("artist")

    @intent_handler(IntentBuilder("OlympicsPickupLineIntent")
                    .require("pickup_line").require("olympics")
                    .optionally("about"))
    def handle_olympics_pickup_line(self, message):
        self.speak_line("olympics")

    @intent_handler(IntentBuilder("PolicePickupLineIntent")
                    .require("pickup_line").require("police")
                    .optionally("about"))
    def handle_police_pickup_line(self, message):
        self.speak_line("police")

    @intent_handler(IntentBuilder("WalkingdeadPickupLineIntent")
                    .require("pickup_line").require("walkingdead")
                    .optionally("about"))
    def handle_walkingdead_pickup_line(self, message):
        self.speak_line("walkingdead")

    @intent_handler(IntentBuilder("BookwormPickupLineIntent")
                    .require("pickup_line").require("bookworm")
                    .optionally("about"))
    def handle_bookworm_pickup_line(self, message):
        self.speak_line("bookworm")

    @intent_handler(IntentBuilder("WeddingPickupLineIntent")
                    .require("pickup_line").require("wedding")
                    .optionally("about"))
    def handle_wedding_pickup_line(self, message):
        self.speak_line("wedding")

    @intent_handler(IntentBuilder("AirportPickupLineIntent")
                    .require("pickup_line").require("airport")
                    .optionally("about"))
    def handle_airport_pickup_line(self, message):
        self.speak_line("airport")

    @intent_handler(IntentBuilder("SatprepPickupLineIntent")
                    .require("pickup_line").require("satprep")
                    .optionally("about"))
    def handle_satprep_pickup_line(self, message):
        self.speak_line("satprep")

    @intent_handler(IntentBuilder("ModelunPickupLineIntent")
                    .require("pickup_line").require("modelun")
                    .optionally("about"))
    def handle_modelun_pickup_line(self, message):
        self.speak_line("modelun")

    @intent_handler(IntentBuilder("BacktoschoolPickupLineIntent")
                    .require("pickup_line").require("backtoschool")
                    .optionally("about"))
    def handle_backtoschool_pickup_line(self, message):
        self.speak_line("backtoschool")

    @intent_handler(IntentBuilder("ChristianPickupLineIntent")
                    .require("pickup_line").require("christian")
                    .optionally("about"))
    def handle_christian_pickup_line(self, message):
        self.speak_line("christian")

    @intent_handler(IntentBuilder("JewishPickupLineIntent")
                    .require("pickup_line").require("jewish")
                    .optionally("about"))
    def handle_jewish_pickup_line(self, message):
        self.speak_line("jewish")

    @intent_handler(IntentBuilder("IslamicPickupLineIntent")
                    .require("pickup_line").require("islamic")
                    .optionally("about"))
    def handle_islamic_pickup_line(self, message):
        self.speak_line("islamic")

    @intent_handler(IntentBuilder("CatholicPickupLineIntent")
                    .require("pickup_line").require("catholic")
                    .optionally("about"))
    def handle_catholic_pickup_line(self, message):
        self.speak_line("catholic")

    @intent_handler(IntentBuilder("HinduPickupLineIntent")
                    .require("pickup_line").require("hindu")
                    .optionally("about"))
    def handle_hindu_pickup_line(self, message):
        self.speak_line("hindu")

    @intent_handler(IntentBuilder("MormonPickupLineIntent")
                    .require("pickup_line").require("mormon")
                    .optionally("about"))
    def handle_mormon_pickup_line(self, message):
        self.speak_line("mormon")

    @intent_handler(IntentBuilder("BuddhistPickupLineIntent")
                    .require("pickup_line").require("buddhist")
                    .optionally("about"))
    def handle_buddhist_pickup_line(self, message):
        self.speak_line("buddhist")

    @intent_handler(IntentBuilder("AtheistPickupLineIntent")
                    .require("pickup_line").require("atheist")
                    .optionally("about"))
    def handle_atheist_pickup_line(self, message):
        self.speak_line("atheist")

    @intent_handler(IntentBuilder("ScientologyPickupLineIntent")
                    .require("pickup_line").require("scientology")
                    .optionally("about"))
    def handle_scientology_pickup_line(self, message):
        self.speak_line("scientology")

    @intent_handler(IntentBuilder("CarPickupLineIntent")
                    .require("pickup_line").require("car")
                    .optionally("about"))
    def handle_car_pickup_line(self, message):
        self.speak_line("car")

    @intent_handler(IntentBuilder("CowboyPickupLineIntent")
                    .require("pickup_line").require("cowboy")
                    .optionally("about"))
    def handle_cowboy_pickup_line(self, message):
        self.speak_line("cowboy")

    @intent_handler(IntentBuilder("MexicanPickupLineIntent")
                    .require("pickup_line").require("mexican")
                    .optionally("about"))
    def handle_mexican_pickup_line(self, message):
        self.speak_line("mexican")

    @intent_handler(IntentBuilder("FrenchPickupLineIntent")
                    .require("pickup_line").require("french")
                    .optionally("about"))
    def handle_french_pickup_line(self, message):
        self.speak_line("french")

    @intent_handler(IntentBuilder("SpanishPickupLineIntent")
                    .require("pickup_line").require("spanish")
                    .optionally("about"))
    def handle_spanish_pickup_line(self, message):
        self.speak_line("spanish")

    @intent_handler(IntentBuilder("PortuguesePickupLineIntent")
                    .require("pickup_line").require("portuguese")
                    .optionally("about"))
    def handle_portuguese_pickup_line(self, message):
        self.speak_line("portuguese")

    @intent_handler(IntentBuilder("GermanyPickupLineIntent")
                    .require("pickup_line").require("germany")
                    .optionally("about"))
    def handle_germany_pickup_line(self, message):
        self.speak_line("germany")

    @intent_handler(IntentBuilder("ItalianPickupLineIntent")
                    .require("pickup_line").require("italian")
                    .optionally("about"))
    def handle_italian_pickup_line(self, message):
        self.speak_line("italian")

    @intent_handler(IntentBuilder("SwedenPickupLineIntent")
                    .require("pickup_line").require("sweden")
                    .optionally("about"))
    def handle_sweden_pickup_line(self, message):
        self.speak_line("sweden")

    @intent_handler(IntentBuilder("FinnishPickupLineIntent")
                    .require("pickup_line").require("finnish")
                    .optionally("about"))
    def handle_finnish_pickup_line(self, message):
        self.speak_line("finnish")

    @intent_handler(IntentBuilder("CzechPickupLineIntent")
                    .require("pickup_line").require("czech")
                    .optionally("about"))
    def handle_czech_pickup_line(self, message):
        self.speak_line("czech")

    @intent_handler(IntentBuilder("DutchPickupLineIntent")
                    .require("pickup_line").require("dutch")
                    .optionally("about"))
    def handle_dutch_pickup_line(self, message):
        self.speak_line("dutch")

    @intent_handler(IntentBuilder("AustralianPickupLineIntent")
                    .require("pickup_line").require("australian")
                    .optionally("about"))
    def handle_australian_pickup_line(self, message):
        self.speak_line("australian")

    @intent_handler(IntentBuilder("JamaicanPickupLineIntent")
                    .require("pickup_line").require("jamaican")
                    .optionally("about"))
    def handle_jamaican_pickup_line(self, message):
        self.speak_line("jamaican")

    @intent_handler(IntentBuilder("DenmarkPickupLineIntent")
                    .require("pickup_line").require("denmark")
                    .optionally("about"))
    def handle_denmark_pickup_line(self, message):
        self.speak_line("denmark")

    @intent_handler(IntentBuilder("NorwayPickupLineIntent")
                    .require("pickup_line").require("norway")
                    .optionally("about"))
    def handle_norway_pickup_line(self, message):
        self.speak_line("norway")

    @intent_handler(IntentBuilder("IcelandPickupLineIntent")
                    .require("pickup_line").require("iceland")
                    .optionally("about"))
    def handle_iceland_pickup_line(self, message):
        self.speak_line("iceland")

    @intent_handler(IntentBuilder("CroatianPickupLineIntent")
                    .require("pickup_line").require("croatian")
                    .optionally("about"))
    def handle_croatian_pickup_line(self, message):
        self.speak_line("croatian")

    @intent_handler(IntentBuilder("FilipinoPickupLineIntent")
                    .require("pickup_line").require("filipino")
                    .optionally("about"))
    def handle_filipino_pickup_line(self, message):
        self.speak_line("filipino")

    @intent_handler(IntentBuilder("PolishPickupLineIntent")
                    .require("pickup_line").require("polish")
                    .optionally("about"))
    def handle_polish_pickup_line(self, message):
        self.speak_line("polish")

    @intent_handler(IntentBuilder("IndonesianPickupLineIntent")
                    .require("pickup_line").require("indonesian")
                    .optionally("about"))
    def handle_indonesian_pickup_line(self, message):
        self.speak_line("indonesian")

    @intent_handler(IntentBuilder("CanadianPickupLineIntent")
                    .require("pickup_line").require("canadian")
                    .optionally("about"))
    def handle_canadian_pickup_line(self, message):
        self.speak_line("canadian")

    @intent_handler(IntentBuilder("StpattysPickupLineIntent")
                    .require("pickup_line").require("stpattys")
                    .optionally("about"))
    def handle_stpattys_pickup_line(self, message):
        self.speak_line("stpattys")

    @intent_handler(IntentBuilder("BollywoodPickupLineIntent")
                    .require("pickup_line").require("bollywood")
                    .optionally("about"))
    def handle_bollywood_pickup_line(self, message):
        self.speak_line("bollywood")

    @intent_handler(IntentBuilder("MoviePickupLineIntent")
                    .require("pickup_line").require("movie")
                    .optionally("about"))
    def handle_movie_pickup_line(self, message):
        self.speak_line("movie")

    @intent_handler(IntentBuilder("MusicfestivalPickupLineIntent")
                    .require("pickup_line").require("musicfestival")
                    .optionally("about"))
    def handle_musicfestival_pickup_line(self, message):
        self.speak_line("musicfestival")

    @intent_handler(IntentBuilder("FencingPickupLineIntent")
                    .require("pickup_line").require("fencing")
                    .optionally("about"))
    def handle_fencing_pickup_line(self, message):
        self.speak_line("fencing")

    @intent_handler(IntentBuilder("HistoricalPickupLineIntent")
                    .require("pickup_line").require("historical")
                    .optionally("about"))
    def handle_historical_pickup_line(self, message):
        self.speak_line("historical")

    @intent_handler(IntentBuilder("AlienPickupLineIntent")
                    .require("pickup_line").require("alien")
                    .optionally("about"))
    def handle_alien_pickup_line(self, message):
        self.speak_line("alien")

    @intent_handler(IntentBuilder("EthnicityPickupLineIntent")
                    .require("pickup_line").require("ethnicity")
                    .optionally("about"))
    def handle_ethnicity_pickup_line(self, message):
        self.speak_line("ethnicity")

    @intent_handler(IntentBuilder("BreakupPickupLineIntent")
                    .require("pickup_line").require("breakup")
                    .optionally("about"))
    def handle_breakup_pickup_line(self, message):
        self.speak_line("breakup")

    @intent_handler(IntentBuilder("ValentinesdayPickupLineIntent")
                    .require("pickup_line").require("valentinesday")
                    .optionally("about"))
    def handle_valentinesday_pickup_line(self, message):
        self.speak_line("valentinesday")

    @intent_handler(IntentBuilder("CoffeePickupLineIntent")
                    .require("pickup_line").require("coffee")
                    .optionally("about"))
    def handle_coffee_pickup_line(self, message):
        self.speak_line("coffee")

    @intent_handler(IntentBuilder("AccountantPickupLineIntent")
                    .require("pickup_line").require("accountant")
                    .optionally("about"))
    def handle_accountant_pickup_line(self, message):
        self.speak_line("accountant")

    @intent_handler(IntentBuilder("AnimalPickupLineIntent")
                    .require("pickup_line").require("animal")
                    .optionally("about"))
    def handle_animal_pickup_line(self, message):
        self.speak_line("animal")

    @intent_handler(IntentBuilder("MilitaryPickupLineIntent")
                    .require("pickup_line").require("military")
                    .optionally("about"))
    def handle_military_pickup_line(self, message):
        self.speak_line("military")

    @intent_handler(IntentBuilder("ChocolatePickupLineIntent")
                    .require("pickup_line").require("chocolate")
                    .optionally("about"))
    def handle_chocolate_pickup_line(self, message):
        self.speak_line("chocolate")

    @intent_handler(IntentBuilder("IcecreamPickupLineIntent")
                    .require("pickup_line").require("icecream")
                    .optionally("about"))
    def handle_icecream_pickup_line(self, message):
        self.speak_line("icecream")

    @intent_handler(IntentBuilder("BlackfridayPickupLineIntent")
                    .require("pickup_line").require("blackfriday")
                    .optionally("about"))
    def handle_blackfriday_pickup_line(self, message):
        self.speak_line("blackfriday")

    @intent_handler(IntentBuilder("GhettoPickupLineIntent")
                    .require("pickup_line").require("ghetto")
                    .optionally("about"))
    def handle_ghetto_pickup_line(self, message):
        self.speak_line("ghetto")

    @intent_handler(IntentBuilder("MagicPickupLineIntent")
                    .require("pickup_line").require("magic")
                    .optionally("about"))
    def handle_magic_pickup_line(self, message):
        self.speak_line("magic")

    @intent_handler(IntentBuilder("FirefighterPickupLineIntent")
                    .require("pickup_line").require("firefighter")
                    .optionally("about"))
    def handle_firefighter_pickup_line(self, message):
        self.speak_line("firefighter")

    @intent_handler(IntentBuilder("PizzaPickupLineIntent")
                    .require("pickup_line").require("pizza")
                    .optionally("about"))
    def handle_pizza_pickup_line(self, message):
        self.speak_line("pizza")

    @intent_handler(IntentBuilder("ChristmasPickupLineIntent")
                    .require("pickup_line").require("christmas")
                    .optionally("about"))
    def handle_christmas_pickup_line(self, message):
        self.speak_line("christmas")

    @intent_handler(IntentBuilder("HalloweenPickupLineIntent")
                    .require("pickup_line").require("halloween")
                    .optionally("about"))
    def handle_halloween_pickup_line(self, message):
        self.speak_line("halloween")

    @intent_handler(IntentBuilder("EasterPickupLineIntent")
                    .require("pickup_line").require("easter")
                    .optionally("about"))
    def handle_easter_pickup_line(self, message):
        self.speak_line("easter")

    @intent_handler(IntentBuilder("ThanksgivingPickupLineIntent")
                    .require("pickup_line").require("thanksgiving")
                    .optionally("about"))
    def handle_thanksgiving_pickup_line(self, message):
        self.speak_line("thanksgiving")

    @intent_handler(IntentBuilder("IndependencePickupLineIntent")
                    .require("pickup_line").require("independence")
                    .optionally("about"))
    def handle_independence_pickup_line(self, message):
        self.speak_line("independence")

    @intent_handler(IntentBuilder("NyePickupLineIntent")
                    .require("pickup_line").require("nye")
                    .optionally("about"))
    def handle_nye_pickup_line(self, message):
        self.speak_line("nye")

    @intent_handler(IntentBuilder("PiratePickupLineIntent")
                    .require("pickup_line").require("pirate")
                    .optionally("about"))
    def handle_pirate_pickup_line(self, message):
        self.speak_line("pirate")

    @intent_handler(IntentBuilder("MedievalPickupLineIntent")
                    .require("pickup_line").require("medieval")
                    .optionally("about"))
    def handle_medieval_pickup_line(self, message):
        self.speak_line("medieval")

    @intent_handler(IntentBuilder("DogPickupLineIntent")
                    .require("pickup_line").require("dog")
                    .optionally("about"))
    def handle_dog_pickup_line(self, message):
        self.speak_line("dog")

    @intent_handler(IntentBuilder("MemesPickupLineIntent")
                    .require("pickup_line").require("memes")
                    .optionally("about"))
    def handle_memes_pickup_line(self, message):
        self.speak_line("memes")
