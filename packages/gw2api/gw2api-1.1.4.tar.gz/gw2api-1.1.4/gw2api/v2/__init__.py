VERSION = "v2"
BASE_URL = "https://api.guildwars2.com/%s/" % VERSION
LANGUAGES = {
    "en": "English",
    "es": "Spanish",
    "de": "German",
    "fr": "French",
    "ko": "Korean",
    "zh": "Chinese"
}


from .endpoint import Endpoint, BuildEndpoint, LocaleAwareEndpoint
from .recipes import RecipeSearchEndpoint
from .account import (AuthenticatedEndpoint, AccountEndpoint,
                      TokenInfoEndpoint, CharacterEndpoint,
                      PvpStatsEndpoint, GuildEndpoint)
from .transactions import TransactionEndpoint
from .achievements import AchievementEndpoint
from .wvw import WvwMatchesEndpoint, WvwMatchStatsEndpoint
from .pvp import PvpSeasonEndpoint


build = BuildEndpoint("build")
colors = LocaleAwareEndpoint("colors")
exchange = Endpoint("commerce/exchange")
listings = Endpoint("commerce/listings")
prices = Endpoint("commerce/prices")
continents = LocaleAwareEndpoint("continents")
events = LocaleAwareEndpoint("events")
events_state = Endpoint("events-state")
files = Endpoint("files")
floors = LocaleAwareEndpoint("floors")
items = LocaleAwareEndpoint("items")
leaderboards = Endpoint("leaderboards")
maps = LocaleAwareEndpoint("maps")
quaggans = Endpoint("quaggans")
recipes = Endpoint("recipes")
recipe_search = RecipeSearchEndpoint(recipes)
skins = LocaleAwareEndpoint("skins")
specializations = LocaleAwareEndpoint("specializations")
traits = LocaleAwareEndpoint("traits")
worlds = LocaleAwareEndpoint("worlds")
wvw_matches = WvwMatchesEndpoint("wvw/matches")
wvw_matches_overview = WvwMatchesEndpoint("wvw/matches/overview")
wvw_matches_scores = WvwMatchesEndpoint("wvw/matches/scores")
wvw_matches_stats = WvwMatchStatsEndpoint("wvw/matches/stats")
wvw_objectives = LocaleAwareEndpoint("wvw/objectives")
wvw_abilities = LocaleAwareEndpoint("wvw/abilities")
wvw_ranks = LocaleAwareEndpoint("wvw/ranks")
wvw_upgrades = LocaleAwareEndpoint("wvw/upgrades")
materials = LocaleAwareEndpoint("materials")
currencies = LocaleAwareEndpoint("currencies")
achievements = AchievementEndpoint("achievements")
achievement_categories = LocaleAwareEndpoint("achievements/categories")
achievement_groups = LocaleAwareEndpoint("achievements/groups")
minis = LocaleAwareEndpoint("minis")
emblem_foregrounds = Endpoint("emblem/foregrounds")
emblem_backgrounds = Endpoint("emblem/backgrounds")
guild_upgrades = LocaleAwareEndpoint("guild/upgrades")
guild_permissions = LocaleAwareEndpoint("guild/permissions")
skills = LocaleAwareEndpoint("skills")
pvp_seasons = PvpSeasonEndpoint("pvp/seasons")
pvp_amulets = LocaleAwareEndpoint("pvp/amulets")
pvp_ranks = LocaleAwareEndpoint("pvp/ranks")
pvp_heroes = LocaleAwareEndpoint("pvp/heroes")
professions = LocaleAwareEndpoint("professions")
legends = Endpoint("legends")
pets = LocaleAwareEndpoint("pets")
item_stats = LocaleAwareEndpoint("itemstats")
titles = LocaleAwareEndpoint("titles")
backstory_questions = LocaleAwareEndpoint("backstory/questions")
backstory_answers = LocaleAwareEndpoint("backstory/answers")
finishers = LocaleAwareEndpoint("finishers")
masteries = LocaleAwareEndpoint("masteries")
stories = LocaleAwareEndpoint("stories")
story_seasons = LocaleAwareEndpoint("stories/seasons")
outfits = LocaleAwareEndpoint("outfits")
dungeons = LocaleAwareEndpoint("dungeons")
raids = LocaleAwareEndpoint("raids")
races = LocaleAwareEndpoint("races")
gliders = LocaleAwareEndpoint("gliders")
mail_carriers = LocaleAwareEndpoint("mailcarriers")
nodes = Endpoint("nodes")
cats = Endpoint("cats")

account = AccountEndpoint("account")
token_info = TokenInfoEndpoint("tokeninfo")
characters = CharacterEndpoint("characters")
transactions = TransactionEndpoint("commerce/transactions")
pvp_games = AuthenticatedEndpoint("pvp/games")
pvp_stats = PvpStatsEndpoint("pvp/stats")
pvp_standings = PvpStatsEndpoint("pvp/standings")
guild = GuildEndpoint("guild")
