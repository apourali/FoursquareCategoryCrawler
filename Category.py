# Foursquare subcategories crawler for datasets 
# Created by: Alireza Pourali
import urllib2

import json



def venueCategoryExtractor(VenueID,clientID,clientSecret):
    #clientID = 'XXX'
    #clientSecret = 'XXX'
    address = 'https://api.foursquare.com/v2/venues/' + VenueID + '?client_id=' + clientID + '&client_secret=' + clientSecret + '&v=20170429'

    weather = urllib2.urlopen(address)
    wjson = weather.read()
    wjdata = json.loads(wjson)
    try :
        category = wjdata['response']['venue']['categories'][0]['icon']['prefix']
    except IndexError:
        category = "UNKNOWN"
    return category





def categoryHierarchy (category):
    text = category
    if  (text.find("/arts_entertainment/aquarium_") != -1):
            return "/arts_entertainment/aquarium_"
    elif (text.find("/arts_entertainment/arcade_") != -1):
            return "/arts_entertainment/arcade_"
    elif (text.find("/arts_entertainment/artgallery_") != -1):
            return "/arts_entertainment/artgallery_"
    elif (text.find("/arts_entertainment/billiards_") != -1):
            return "/arts_entertainment/billiards_"
    elif (text.find("/arts_entertainment/bowling_") != -1):
            return "/arts_entertainment/bowling_"
    elif (text.find("/arts_entertainment/casino_") != -1):
            return "/arts_entertainment/casino_"
    elif (text.find("/arts_entertainment/comedyclub_") != -1):
            return "/arts_entertainment/comedyclub_"
    elif (text.find("/arts_entertainment/default_") != -1):
            return "/arts_entertainment/default_"
    elif (text.find("/arts_entertainment/historicsite_") != -1):
            return "/arts_entertainment/historicsite_"
    elif (text.find("/arts_entertainment/movietheater_") != -1):
            return "/arts_entertainment/movietheater_"
    elif (text.find("/arts_entertainment/museum_") != -1):
            return "/arts_entertainment/museum_"
    elif (text.find("/arts_entertainment/museum_planetarium_") != -1):
            return "/arts_entertainment/museum_planetarium_"
    elif (text.find("/arts_entertainment/musicvenue_") != -1):
            return "/arts_entertainment/musicvenue_"
    elif (text.find("/arts_entertainment/musicvenue_rockclub_") != -1):
            return "/arts_entertainment/musicvenue_rockclub_"
    elif (text.find("/arts_entertainment/performingarts_") != -1):
            return "/arts_entertainment/performingarts_"
    elif (text.find("/arts_entertainment/performingarts_dancestudio_") != -1):
            return "/arts_entertainment/performingarts_dancestudio_"
    elif (text.find("/arts_entertainment/performingarts_theater_") != -1):
            return "/arts_entertainment/performingarts_theater_"
    elif (text.find("/arts_entertainment/racetrack_") != -1):
            return "/arts_entertainment/racetrack_"
    elif (text.find("/arts_entertainment/stadium_") != -1):
            return "/arts_entertainment/stadium_"
    elif (text.find("/arts_entertainment/stadium_track_") != -1):
            return "/arts_entertainment/stadium_track_"
    elif (text.find("/arts_entertainment/themepark_") != -1):
            return "/arts_entertainment/themepark_"
    elif (text.find("/arts_entertainment/waterpark_") != -1):
            return "/arts_entertainment/waterpark_"
    elif (text.find("/arts_entertainment/zoo_") != -1):
            return "/arts_entertainment/zoo_"
    elif (text.find("/building/animalshelter_") != -1):
            return "/building/animalshelter_"
    elif (text.find("/building/apartment_") != -1):
            return "/building/apartment_"
    elif (text.find("/building/auditorium_") != -1):
            return "/building/auditorium_"
    elif (text.find("/building/conventioncenter_") != -1):
            return "/building/conventioncenter_"
    elif (text.find("/building/cityhall_") != -1):
            return "/building/cityhall_"
    elif (text.find("/building/default_") != -1):
            return "/building/default_"
    elif (text.find("/building/eventspace_") != -1):
            return "/building/eventspace_"
    elif (text.find("/building/factory_") != -1):
            return "/building/factory_"
    elif (text.find("/building/fair_") != -1):
            return "/building/fair_"
    elif (text.find("/building/funeralhome_") != -1):
            return "/building/funeralhome_"
    elif (text.find("/building/government_") != -1):
            return "/building/government_"
    elif (text.find("/building/gym_") != -1):
            return "/building/gym_"
    elif (text.find("/building/home_") != -1):
            return "/building/home_"
    elif (text.find("/building/housingdevelopment_") != -1):
            return "/building/housingdevelopment_"
    elif (text.find("/building/library_") != -1):
            return "/building/library_"
    elif (text.find("/building/medical_") != -1):
            return "/building/medical_"
    elif (text.find("/building/medical_opticalshop_") != -1):
            return "/building/medical_opticalshop_"
    elif (text.find("/building/militarybase_") != -1):
            return "/building/militarybase_"
    elif (text.find("/building/parking_") != -1):
            return "/building/parking_"
    elif (text.find("/building/postoffice_") != -1):
            return "/building/postoffice_"
    elif (text.find("/building/religious_") != -1):
            return "/building/religious_"
    elif (text.find("/building/office_coworkingspace_") != -1):
            return "/building/office_coworkingspace_"
    elif (text.find ("/building/office_conferenceroom_") != -1):
            return "/building/office_conferenceroom_"
    elif (text.find("/building/school_") != -1):
            return "/building/school_"
    elif (text.find("/building/school_music_") != -1):
            return "/building/school_music_"
    elif (text.find("/building/votingbooth_") != -1):
            return "/building/votingbooth_"
    elif (text.find("/education/academicbuilding_") != -1):
            return "/education/academicbuilding_"
    elif (text.find("/education/administrativebuilding_") != -1):
            return "/education/administrativebuilding_"
    elif (text.find("/education/cafeteria_") != -1):
            return "/education/cafeteria_"
    elif (text.find("/education/classroom_") != -1):
            return "/education/classroom_"
    elif (text.find("/education/communitycollege_") != -1):
            return "/education/communitycollege_"
    elif (text.find("/education/collegeacademicbuildings_communications_") != -1):
            return "/education/collegeacademicbuildings_communications_"
    elif (text.find("/education/collegeacademicbuildings_engineering_") != -1):
            return "/education/collegeacademicbuildings_engineering_"
    elif (text.find("education/collegeacademicbuildings_history_") != -1):
            return "education/collegeacademicbuildings_history_"
    elif (text.find("/education/collegeacademicbuildings_science_") != -1):
            return "/education/collegeacademicbuildings_science_"
    elif (text.find("/education/collegeacademicbuildings_technology_") != -1):
            return "/education/collegeacademicbuildings_technology_"
    elif (text.find("/education/collegeacademicbuildings_math_") != -1):
            return "/education/collegeacademicbuildings_math_"
    elif (text.find("/education/default_") != -1):
            return "/education/default_"
    elif (text.find("/education/frathouse_") != -1):
            return "/education/frathouse_"
    elif (text.find("/education/lab_") != -1):
            return "/education/lab_"
    elif (text.find("/education/lawschool_") != -1):
            return "/education/lawschool_"
    elif (text.find("/education/other_") != -1):
            return "/education/other_"
    elif (text.find("/education/quad_") != -1):
            return "/education/quad_"
    elif (text.find("/education/reccenter_") != -1):
            return "/education/reccenter_"
    elif (text.find("/education/residencehall_") != -1):
            return "/education/residencehall_"
    elif (text.find("/education/studentcenter_") != -1):
            return "/education/studentcenter_"
    elif (text.find("/education/tradeschool_") != -1):
            return "/education/tradeschool_"
    elif (text.find("/event/default_") != -1):
            return "/event/default_"
    elif (text.find("/food/afghan_") != -1):
            return "/food/afghan_"
    elif (text.find("/food/african_") != -1):
            return "/food/african_"
    elif (text.find("/food/arepas_") != -1):
            return "/food/arepas_"
    elif (text.find("/food/argentinian_") != -1):
            return "/food/argentinian_"
    elif (text.find("/food/asian_") != -1):
            return "/food/asian_"
    elif (text.find("/food/australian_") != -1):
            return "/food/australian_"
    elif (text.find("/food/austrian_") != -1):
            return "/food/austrian_"
    elif (text.find("/food/bagels_") != -1):
            return "/food/bagels_"
    elif (text.find("/food/bakery_") != -1):
            return "/food/bakery_"
    elif (text.find("/food/bbqalt_") != -1):
            return "/food/bbqalt_"
    elif (text.find("/food/breakfast_") != -1):
            return "/food/breakfast_"
    elif (text.find("/food/brewery_") != -1):
            return "/food/brewery_"
    elif (text.find("/food/bubble_") != -1):
            return "/food/bubble_"
    elif (text.find("/food/burger_") != -1):
            return "/food/burger_"
    elif (text.find("/food/burrito_") != -1):
            return "/food/burrito_"
    elif (text.find("/food/cafe_") != -1):
            return "/food/cafe_"
    elif (text.find("/food/cajun_") != -1):
            return "/food/cajun_"
    elif (text.find("/food/caribbean_") != -1):
            return "/food/caribbean_"
    elif (text.find("/food/caucasian_") != -1):
            return "/food/caucasian_"
    elif (text.find("/food/coffeeshop_") != -1):
            return "/food/coffeeshop_"
    elif (text.find("/food/creperie_") != -1):
            return "/food/creperie_"
    elif (text.find("/food/cuban_") != -1):
            return "/food/cuban_"
    elif (text.find("/food/cupcakes_") != -1):
            return "/food/cupcakes_"
    elif (text.find("/food/default_") != -1):
            return "/food/default_"
    elif (text.find("/food/deli_") != -1):
            return "/food/deli_"
    elif (text.find("/food/dessert_") != -1):
            return "/food/dessert_"
    elif (text.find("/food/diner_") != -1):
            return "/food/diner_"
    elif (text.find("/food/donuts_") != -1):
            return "/food/donuts_"
    elif (text.find ("/food/dimsum_") != -1):
            return "/food/dimsum_"
    elif (text.find("/food/dumplings_") != -1):
            return "/food/dumplings_"
    elif (text.find("/food/ethiopian_") != -1):
            return "/food/ethiopian_"
    elif (text.find("/food/falafel_") != -1):
            return "/food/falafel_"
    elif (text.find("/food/fastfood_") != -1):
            return "/food/fastfood_"
    elif (text.find("/food/fishandchips_") != -1):
            return "/food/fishandchips_"
    elif (text.find("/food/filipino_") != -1):
            return "/food/filipino_"
    elif (text.find("/food/french_") != -1):
            return "/food/french_"
    elif (text.find("/food/friedchicken_") != -1):
            return "/food/friedchicken_"
    elif (text.find("/food/frozenyogurt_") != -1):
            return "/food/frozenyogurt_"
    elif (text.find("/food/gastropub_") != -1):
            return "/food/gastropub_"
    elif (text.find("/food/german_") != -1):
            return "/food/german_"
    elif (text.find("/food/glutenfree_") != -1):
            return "/food/glutenfree_"
    elif (text.find("/food/greek_") != -1):
            return "/food/greek_"
    elif (text.find("/food/halal_") != -1):
            return "/food/halal_"
    elif (text.find("/food/hotdog_") != -1):
            return "/food/hotdog_"
    elif (text.find ("/food/icecream_") != -1):
            return "/food/icecream_"
    elif (text.find("/food/indian_") != -1):
            return "/food/indian_"
    elif (text.find("/food/indonesian_") != -1):
            return "/food/indonesian_"
    elif (text.find("/food/italian_") != -1):
            return "/food/italian_"
    elif (text.find("/food/juicebar_") != -1):
            return "/food/juicebar_"
    elif (text.find("/food/japanese_") != -1):
            return "/food/japanese_"
    elif (text.find("/food/korean_") != -1):
            return "/food/korean_"
    elif (text.find("/food/malaysian_") != -1):
            return "/food/malaysian_"
    elif (text.find("/food/latinamerican_") != -1):
            return "/food/latinamerican_"
    elif (text.find("/food/macandcheese_") != -1):
            return "/food/macandcheese_"
    elif (text.find("/food/mediterranean_") != -1):
            return "/food/mediterranean_"
    elif (text.find("/food/mexican_") != -1):
            return "/food/mexican_"
    elif (text.find("/food/middleeastern_") != -1):
            return "/food/middleeastern_"
    elif (text.find("/food/moleculargastronomy_") != -1):
            return "/food/moleculargastronomy_"
    elif (text.find("/food/moroccan_") != -1):
            return "/food/moroccan_"
    elif (text.find("/food/newamerican_") != -1):
            return "/food/newamerican_"
    elif (text.find("/food/peruvian_") != -1):
            return "/food/peruvian_"
    elif (text.find("/food/paella_") != -1):
            return "/food/paella_"
    elif (text.find("/food/pieshop_") != -1):
            return "/food/pieshop_"
    elif (text.find("/food/pizza_") != -1):
            return "/food/pizza_"
    elif (text.find("/food/portuguese_") != -1):
            return "/food/portuguese_"
    elif (text.find("/food/ramen_") != -1):
            return "/food/ramen_"
    elif (text.find("/food/russian_") != -1):
            return "/food/russian_"
    elif (text.find("/food/salad_") != -1):
            return "/food/salad_"
    elif (text.find("/food/scandinavian_") != -1):
            return "/food/scandinavian_"
    elif (text.find("/food/seafood_") != -1):
            return "/food/seafood_"
    elif (text.find("/food/snacks_") != -1):
            return "/food/snacks_"
    elif (text.find("/food/soup_") != -1):
            return "/food/soup_"
    elif (text.find("/food/southern_") != -1):
            return "/food/southern_"
    elif (text.find("/food/spanish_") != -1):
            return "/food/spanish_"
    elif (text.find("/food/steakhouse_") != -1):
            return "/food/steakhouse_"
    elif (text.find("/food/streetfood_") != -1):
            return "/food/streetfood_"
    elif (text.find("/food/sushi_") != -1):
            return "/food/sushi_"
    elif (text.find("/food/swiss_") != -1):
            return "/food/swiss_"
    elif(text.find("/food/taco_") != -1):
            return "/food/taco_"
    elif (text.find("/food/tapas_") != -1):
            return "/food/tapas_"
    elif (text.find("/food/tearoom_") != -1):
            return "/food/tearoom_"
    elif (text.find("/food/tibetan_") != -1):
            return "/food/tibetan_"
    elif (text.find("/food/thai_") != -1):
            return "/food/thai_"
    elif (text.find("/food/turkish_") != -1):
            return "/food/turkish_"
    elif (text.find("/food/vegetarian_") != -1):
            return "/food/vegetarian_"
    elif (text.find("/food/vietnamese_") != -1):
            return "/food/vietnamese_"
    elif (text.find("/food/winery_") != -1):
            return "/food/winery_"
    elif (text.find("/food/wings_") != -1):
            return "/food/wings_"
    elif (text.find("/nightlife/beergarden_") != -1):
            return "/nightlife/beergarden_"
    elif (text.find("/nightlife/cocktails_") != -1):
            return "/nightlife/cocktails_"
    elif (text.find("/nightlife/default_") != -1):
            return "/nightlife/default_"
    elif (text.find("/nightlife/gaybar_") != -1):
            return "/nightlife/gaybar_"
    elif (text.find("/nightlife/divebar_") != -1):
            return "/nightlife/divebar_"
    elif (text.find("/nightlife/hookahbar_") != -1):
            return "/nightlife/hookahbar_"
    elif (text.find("/nightlife/karaoke_") != -1):
            return "/nightlife/karaoke_"
    elif (text.find("/nightlife/sake_") != -1):
            return "/nightlife/sake_"
    elif (text.find("/nightlife/secretbar_") != -1):
            return "/nightlife/secretbar_"
    elif (text.find("/nightlife/sportsbar_") != -1):
            return "/nightlife/sportsbar_"
    elif (text.find("/nightlife/nightclub_") != -1):
            return "/nightlife/nightclub_"
    elif (text.find("/nightlife/pub_") != -1):
            return "/nightlife/pub_"
    elif (text.find("/nightlife/stripclub_") != -1):
            return "/nightlife/stripclub_"
    elif (text.find("/nightlife/whiskey_") != -1):
            return "/nightlife/whiskey_"
    elif (text.find("/parks_outdoors/baseballfield_") != -1):
            return "/parks_outdoors/baseballfield_"
    elif (text.find("/parks_outdoors/basketballcourt_") != -1):
            return "/parks_outdoors/basketballcourt_"
    elif (text.find("/parks_outdoors/beach_") != -1):
            return "/parks_outdoors/beach_"
    elif (text.find("/parks_outdoors/botanicalgarden_") != -1):
            return "/parks_outdoors/botanicalgarden_"
    elif (text.find("/parks_outdoors/bridge_") != -1):
            return "/parks_outdoors/bridge_"
    elif (text.find("/parks_outdoors/campground_") != -1):
            return "/parks_outdoors/campground_"
    elif (text.find("/parks_outdoors/cemetery_") != -1):
            return "/parks_outdoors/cemetery_"
    elif (text.find("/parks_outdoors/default_") != -1):
            return "/parks_outdoors/default_"
    elif (text.find("/parks_outdoors/divespot_") != -1):
            return "/parks_outdoors/divespot_"
    elif (text.find("/parks_outdoors/dogrun_") != -1):
            return "/parks_outdoors/dogrun_"
    elif (text.find("/parks_outdoors/farm_") != -1):
            return "/parks_outdoors/farm_"
    elif (text.find("/parks_outdoors/field_") != -1):
            return "/parks_outdoors/field_"
    elif (text.find("/parks_outdoors/garden_") != -1):
            return "/parks_outdoors/garden_"
    elif (text.find("/parks_outdoors/gardencenter_") != -1):
            return "/parks_outdoors/gardencenter_"
    elif (text.find("/parks_outdoors/golfcourse_") != -1):
            return "/parks_outdoors/golfcourse_"
    elif (text.find("/parks_outdoors/gun_") != -1):
            return "/parks_outdoors/gun_"
    elif (text.find("/parks_outdoors/harbor_") != -1):
            return "/parks_outdoors/harbor_"
    elif (text.find("/parks_outdoors/hikingtrail_") != -1):
            return "/parks_outdoors/hikingtrail_"
    elif (text.find("/parks_outdoors/hotspring_") != -1):
            return "/parks_outdoors/hotspring_"
    elif (text.find("/parks_outdoors/lake_") != -1):
            return "/parks_outdoors/lake_"
    elif (text.find("/parks_outdoors/lighthouse_") != -1):
            return "/parks_outdoors/lighthouse_"
    elif (text.find("/parks_outdoors/mountain_") != -1):
            return "/parks_outdoors/mountain_"
    elif (text.find("/parks_outdoors/naturepreserve_") != -1):
            return "/parks_outdoors/naturepreserve_"
    elif (text.find("/parks_outdoors/neighborhood_") != -1):
            return "/parks_outdoors/neighborhood_"
    elif (text.find("/parks_outdoors/outdoors_") != -1):
            return "/parks_outdoors/outdoors_"
    elif (text.find("/parks_outdoors/park_") != -1):
            return "/parks_outdoors/park_"
    elif (text.find("/parks_outdoors/playground_") != -1):
            return "/parks_outdoors/playground_"
    elif (text.find("/parks_outdoors/plaza_") != -1):
            return "/parks_outdoors/plaza_"
    elif (text.find("/parks_outdoors/pool_") != -1):
            return "/parks_outdoors/pool_"
    elif (text.find("/parks_outdoors/rafting_") != -1):
            return "/parks_outdoors/rafting_"
    elif (text.find("/parks_outdoors/river_") != -1):
            return "/parks_outdoors/river_"
    elif (text.find("/parks_outdoors/rockclimbing_") != -1):
            return "/parks_outdoors/rockclimbing_"
    elif (text.find("/parks_outdoors/sceniclookout_") != -1):
            return "/parks_outdoors/sceniclookout_"
    elif (text.find("/parks_outdoors/sculpture_") != -1):
            return "/parks_outdoors/sculpture_"
    elif (text.find("/parks_outdoors/skate_park_") != -1):
            return "/parks_outdoors/skate_park_"
    elif (text.find("/parks_outdoors/skatingrink_") != -1):
            return "/parks_outdoors/skatingrink_"
    elif (text.find("/parks_outdoors/ski_chairlift_	") != -1):
            return "/parks_outdoors/ski_chairlift_"
    elif (text.find("/parks_outdoors/ski_snowboard_") != -1):
            return "/parks_outdoors/ski_snowboard_"
    elif (text.find("/parks_outdoors/ski_lodge_") != -1):
            return "/parks_outdoors/ski_lodge_"
    elif (text.find("/parks_outdoors/ski_apresskibar_") != -1):
            return "/parks_outdoors/ski_apresskibar_"
    elif (text.find("/parks_outdoors/stable_") != -1):
            return "/parks_outdoors/stable_"
    elif (text.find("/parks_outdoors/ski_chalet_") != -1):
            return "/parks_outdoors/ski_chalet_"
    elif (text.find("/parks_outdoors/surfspot_") != -1):
            return "/parks_outdoors/surfspot_"
    elif (text.find("/parks_outdoors/volleyballcourt_") != -1):
            return "/parks_outdoors/volleyballcourt_"
    elif (text.find("/parks_outdoors/vineyard_") != -1):
            return "/parks_outdoors/vineyard_"
    elif (text.find("/parks_outdoors/well_") != -1):
            return "/parks_outdoors/well_"
    elif (text.find ("/parks_outdoors/ski_trail_") != -1):
            return "/parks_outdoors/ski_trail_"
    elif (text.find("/shops/airport_rentalcar_") != -1):
            return "/shops/airport_rentalcar_"
    elif (text.find("/shops/antique_") != -1):
            return "/shops/antique_"
    elif (text.find("/shops/apparel_") != -1):
            return "/shops/apparel_"
    elif (text.find("/shops/apparel_kids_") != -1):
            return "/shops/apparel_kids_"
    elif (text.find("/shops/apparel_shoestore_") != -1):
            return "/shops/apparel_shoestore_"
    elif (text.find("/shops/artstore_") != -1):
            return "/shops/artstore_"
    elif (text.find("/shops/automotive_") != -1):
            return "/shops/automotive_"
    elif (text.find("/shops/beauty_cosmetic_") != -1):
            return "/shops/beauty_cosmetic_"
    elif (text.find("/shops/bikeshop_") != -1):
        return "/shops/bikeshop_"
    elif (text.find("/shops/bookstore_") != -1):
        return "/shops/bookstore_"
    elif (text.find("/shops/bridal_") != -1):
        return "/shops/bridal_"
    elif (text.find("/shops/camerastore_") != -1):
        return "/shops/camerastore_"
    elif (text.find("/shops/candystore_") != -1):
        return "/shops/candystore_"
    elif (text.find("/shops/carwash_") != -1):
        return "/shops/carwash_"
    elif (text.find("/shops/comic_") != -1):
        return "/shops/comic_"
    elif (text.find("/shops/conveniencestore_") != -1):
        return "/shops/conveniencestore_"
    elif (text.find("/shops/daycare_") != -1):
        return "/shops/daycare_"
    elif (text.find("/shops/default_") != -1):
        return "/shops/default_"
    elif (text.find("/shops/departmentstore_") != -1):
        return "/shops/departmentstore_"
    elif (text.find("/shops/design_") != -1):
        return "/shops/design_"
    elif (text.find("/shops/discountstore_") != -1):
        return "/shops/discountstore_"
    elif (text.find("/shops/dispensary_") != -1):
        return "/shops/dispensary_"
    elif (text.find("/shops/drycleaner_") != -1):
        return "/shops/drycleaner_"
    elif (text.find("/shops/food_cheese_") != -1):
        return "/shops/food_cheese_"
    elif (text.find("/shops/food_farmersmarket_") != -1):
        return "/shops/food_farmersmarket_"
    elif (text.find("/shops/food_liquor_") != -1):
        return "/shops/food_liquor_"
    elif (text.find("/shops/financial_") != -1):
        return "/shops/financial_"
    elif (text.find("/shops/fleamarket_") != -1):
        return "/shops/fleamarket_"
    elif (text.find("/shops/flowershop_") != -1):
        return "/shops/flowershop_"
    elif (text.find("/shops/food_butcher_") != -1):
        return "/shops/food_butcher_"
    elif (text.find("/shops/food_fishmarket_") != -1):
        return "/shops/food_fishmarket_"
    elif (text.find("/shops/food_foodcourt_") != -1):
        return "/shops/food_foodcourt_"
    elif (text.find("/shops/food_gourmet_") != -1):
        return "/shops/food_gourmet_"
    elif (text.find("/shops/food_grocery_") != -1):
        return "/shops/food_grocery_"
    elif (text.find("/shops/food_wineshop_") != -1):
        return "/shops/food_wineshop_"
    elif (text.find("/shops/foodanddrink_") != -1):
        return "/shops/foodanddrink_"
    elif (text.find("/shops/furniture_") != -1):
        return "/shops/furniture_"
    elif (text.find("/shops/gamingcafe_") != -1):
        return "/shops/gamingcafe_"
    elif (text.find("/shops/gas_") != -1):
        return "/shops/gas_"
    elif (text.find("/shops/giftshop_") != -1):
        return "/shops/giftshop_"
    elif (text.find("/shops/gym_yogastudio_") != -1):
        return "/shops/gym_yogastudio_"
    elif (text.find("/shops/gym_martialarts_") != -1):
        return "/shops/gym_martialarts_"
    elif (text.find("/shops/hardware_") != -1):
        return "/shops/hardware_"
    elif (text.find("/shops/hobbyshop_") != -1):
        return "/shops/hobbyshop_"
    elif (text.find("/shops/internetcafe_") != -1):
        return "/shops/internetcafe_"
    elif (text.find("/shops/jewelry_") != -1):
        return "/shops/jewelry_"
    elif (text.find("/shops/laundry_") != -1):
        return "/shops/laundry_"
    elif (text.find("/shops/mall_") != -1):
        return "/shops/mall_"
    elif (text.find("/shops/market_") != -1):
        return "/shops/market_"
    elif (text.find("/shops/mobilephoneshop_") != -1):
        return "/shops/mobilephoneshop_"
    elif (text.find("/shops/motorcycle_") != -1):
        return "/shops/motorcycle_"
    elif (text.find("/shops/music_instruments_") != -1):
        return "/shops/music_instruments_"
    elif (text.find("/shops/nailsalon_") != -1):
        return "/shops/nailsalon_"
    elif (text.find("/shops/newsstand_") != -1):
        return "/shops/newsstand_"
    elif (text.find("/shops/papergoods_") != -1):
        return "/shops/papergoods_"
    elif (text.find("/shops/pet_store_") != -1):
        return "/shops/pet_store_"
    elif (text.find("/shops/pharmacy_") != -1):
        return "/shops/pharmacy_"
    elif (text.find("/shops/photographylab_") != -1):
        return "/shops/photographylab_"
    elif (text.find("/shops/piercing_") != -1):
        return "/shops/piercing_"
    elif (text.find("/shops/realestate_") != -1):
        return "/shops/realestate_"
    elif (text.find("/shops/record_shop_") != -1):
        return "/shops/record_shop_"
    elif (text.find("/shops/recycling_") != -1):
        return "/shops/recycling_"
    elif (text.find("/shops/salon_barber_") != -1):
        return "/shops/salon_barber_"
    elif (text.find("/shops/spa_") != -1):
        return "/shops/spa_"
    elif (text.find("/shops/sports_outdoors_") != -1):
        return "/shops/sports_outdoors_"
    elif (text.find("/shops/storage_") != -1):
        return "/shops/storage_"
    elif (text.find("/shops/tanning_salon_") != -1):
        return "/shops/tanning_salon_"
    elif (text.find("/shops/tattoos_") != -1):
        return "/shops/tattoos_"
    elif (text.find("/shops/technology_") != -1):
        return "/shops/technology_"
    elif (text.find("/shops/tobacco_") != -1):
        return "/shops/tobacco_"
    elif (text.find("/shops/toys_") != -1):
        return "/shops/toys_"
    elif (text.find("/shops/video_") != -1):
        return "/shops/video_"
    elif (text.find("/shops/videogames_") != -1):
        return "/shops/videogames_"
    elif (text.find("/travel/airport_") != -1):
        return "/travel/airport_"
    elif (text.find("/travel/boat_") != -1):
        return "/travel/boat_"
    elif (text.find("/travel/busstation_") != -1):
        return "/travel/busstation_"
    elif (text.find("/travel/bedandbreakfast_") != -1):
        return "/travel/bedandbreakfast_"
    elif (text.find("/travel/default_") != -1):
        return "/travel/default_"
    elif (text.find("/travel/embassy_") != -1):
        return "/travel/embassy_"
    elif (text.find("/travel/ferry_pier_") != -1):
        return "/travel/ferry_pier_"
    elif (text.find("/travel/highway_") != -1):
        return "/travel/highway_"
    elif (text.find("/travel/hotel_") != -1):
        return "/travel/hotel_"
    elif (text.find("/travel/hostel_") != -1):
        return "/travel/hostel_"
    elif (text.find("/travel/lightrail_") != -1):
        return "/travel/lightrail_"
    elif (text.find("/travel/movingtarget_") != -1):
        return "/travel/movingtarget_"
    elif (text.find("/travel/restarea_") != -1):
        return "/travel/restarea_"
    elif (text.find("/travel/subway_") != -1):
        return "/travel/subway_"
    elif (text.find("/travel/taxi_") != -1):
        return "/travel/taxi_"
    elif (text.find("/travel/touristinformation_") != -1):
        return "/travel/touristinformation_"
    elif (text.find("/travel/trainstation_") != -1):
        return "/travel/trainstation_"
    elif (text.find("/travel/travelagency_") != -1):
        return "/travel/travelagency_"
    elif (text.find("/travel/resort_") != -1):
        return "/travel/resort_"
    else:
            return "Unknown" + str(text)

# Example 
'''
subcategoryOfVenueX = venueCategoryExtractor(categoryHierarchy(VenueX,clientID,clientSecret))
Replace VenueX with your Venue ID and Client ID and Secret with your Foursquare account application keys
'''

