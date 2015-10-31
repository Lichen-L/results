from biogeme import *
from headers import *
from loglikelihood import *
from statistics import *

# rowid	H1_HHID	H1_Pcode	Pax_ID	day_pattern_code	In_day_pattern_choice_set	modified_code	begin_in_tour_table	End_in_tour_table	simple_day_pattern	universitystudent	person_type_id	age_id	income_id	incmid	missingincome	fixedworkplace	missingworkplace	female_dummy	HH_with_under_4	HH_with_under_15	HH_all_adults	HH_all_workers	work_at_home_dummy	hh_car_avail	hh_motor_avail	1_tour_purpose	2_tour_purpose	3_tour_purpose	Work	Edu	Shopping	Others		

# Day Pattern ID #28 is No Tours.

# Base characteristics for subjects are as follows:
# Employed Full Time - person_type ID = 1
# Male
# No Children under age 15
# Family Household - All adults and All workers
# Age 36-50

# Variables

#activity specific
WorkT1 = 0
WorkT2 = 0
WorkT3 = 0
WorkT4 = 0
WorkT5 = 0
WorkT6 = 0
WorkT7 = 0
WorkT8 = 0
WorkT9 = 0
WorkT10 = 0
WorkT11 = 0
WorkT12 = 0
WorkT13 = 0
WorkT14 = 0
WorkT15 = 0
WorkT16 = 0
WorkT17 = 0
WorkT18 = 0
WorkT19 = 0
WorkT20 = 0
WorkT21 = 0
WorkT22 = 0
WorkT23 = 0
WorkT24 = 0
WorkT25 = 0
WorkT26 = 0
WorkT27 = 0
WorkT28 = 0
WorkT29 = 1
WorkT30 = 1
WorkT31 = 1
WorkT32 = 1
WorkT33 = 1
WorkT34 = 1
WorkT35 = 1
WorkT36 = 1
WorkT37 = 1
WorkT38 = 1
WorkT39 = 1
WorkT40 = 1
WorkT41 = 1
WorkT42 = 1
WorkT43 = 1
WorkT44 = 1
WorkT45 = 1
WorkT46 = 1
WorkT47 = 1
WorkT48 = 1
WorkT49 = 1
WorkT50 = 1
WorkT51 = 1
EduT1 = 0
EduT2 = 0
EduT3 = 0
EduT4 = 0
EduT5 = 0
EduT6 = 0
EduT7 = 0
EduT8 = 0
EduT9 = 0
EduT10 = 0
EduT11 = 0
EduT12 = 0
EduT13 = 1
EduT14 = 1
EduT15 = 1
EduT16 = 1
EduT17 = 1
EduT18 = 1
EduT19 = 1
EduT20 = 1
EduT21 = 1
EduT22 = 1
EduT23 = 1
EduT24 = 1
EduT25 = 1
EduT26 = 1
EduT27 = 1
EduT28 = 1
EduT29 = 0
EduT30 = 0
EduT31 = 0
EduT32 = 0
EduT33 = 0
EduT34 = 0
EduT35 = 0
EduT36 = 0
EduT37 = 0
EduT38 = 0
EduT39 = 0
EduT40 = 0
EduT41 = 0
EduT42 = 0
EduT43 = 0
EduT44 = 0
EduT45 = 1
EduT46 = 1
EduT47 = 1
EduT48 = 1
EduT49 = 1
EduT50 = 1
EduT51 = 1
ShopT1 = 0
ShopT2 = 0
ShopT3 = 0
ShopT4 = 0
ShopT5 = 0
ShopT6 = 1
ShopT7 = 1
ShopT8 = 1
ShopT9 = 1
ShopT10 = 1
ShopT11 = 1
ShopT12 = 1
ShopT13 = 0
ShopT14 = 0
ShopT15 = 0
ShopT16 = 0
ShopT17 = 0
ShopT18 = 0
ShopT19 = 0
ShopT20 = 0
ShopT21 = 0
ShopT22 = 0
ShopT23 = 0
ShopT24 = 1
ShopT25 = 1
ShopT26 = 1
ShopT27 = 1
ShopT28 = 1
ShopT29 = 0
ShopT30 = 0
ShopT31 = 0
ShopT32 = 0
ShopT33 = 0
ShopT34 = 0
ShopT35 = 0
ShopT36 = 0
ShopT37 = 0
ShopT38 = 0
ShopT39 = 0
ShopT40 = 1
ShopT41 = 1
ShopT42 = 1
ShopT43 = 1
ShopT44 = 1
ShopT45 = 0
ShopT46 = 0
ShopT47 = 0
ShopT48 = 0
ShopT49 = 0
ShopT50 = 0
ShopT51 = 1
OthersT1 = 0
OthersT2 = 1
OthersT3 = 1
OthersT4 = 1
OthersT5 = 1
OthersT6 = 0
OthersT7 = 0
OthersT8 = 0
OthersT9 = 0
OthersT10 = 1
OthersT11 = 1
OthersT12 = 1
OthersT13 = 0
OthersT14 = 0
OthersT15 = 0
OthersT16 = 0
OthersT17 = 0
OthersT18 = 0
OthersT19 = 0
OthersT20 = 1
OthersT21 = 1
OthersT22 = 1
OthersT23 = 1
OthersT24 = 0
OthersT25 = 0
OthersT26 = 0
OthersT27 = 0
OthersT28 = 1
OthersT29 = 0
OthersT30 = 0
OthersT31 = 0
OthersT32 = 0
OthersT33 = 0
OthersT34 = 0
OthersT35 = 0
OthersT36 = 1
OthersT37 = 1
OthersT38 = 1
OthersT39 = 1
OthersT40 = 0
OthersT41 = 0
OthersT42 = 0
OthersT43 = 0
OthersT44 = 1
OthersT45 = 0
OthersT46 = 0
OthersT47 = 0
OthersT48 = 0
OthersT49 = 0
OthersT50 = 1
OthersT51 = 0
WorkI1 = 0
WorkI2 = 0
WorkI3 = 0
WorkI4 = 0
WorkI5 = 0
WorkI6 = 0
WorkI7 = 0
WorkI8 = 0
WorkI9 = 0
WorkI10 = 0
WorkI11 = 0
WorkI12 = 0
WorkI13 = 0
WorkI14 = 0
WorkI15 = 0
WorkI16 = 0
WorkI17 = 0
WorkI18 = 0
WorkI19 = 0
WorkI20 = 0
WorkI21 = 0
WorkI22 = 0
WorkI23 = 0
WorkI24 = 0
WorkI25 = 0
WorkI26 = 0
WorkI27 = 0
WorkI28 = 0
WorkI29 = 0
WorkI30 = 0
WorkI31 = 0
WorkI32 = 0
WorkI33 = 1
WorkI34 = 1
WorkI35 = 1
WorkI36 = 0
WorkI37 = 0
WorkI38 = 0
WorkI39 = 1
WorkI40 = 0
WorkI41 = 0
WorkI42 = 0
WorkI43 = 1
WorkI44 = 0
WorkI45 = 0
WorkI46 = 0
WorkI47 = 0
WorkI48 = 0
WorkI49 = 1
WorkI50 = 0
WorkI51 = 0
EduI1 = 0
EduI2 = 0
EduI3 = 0
EduI4 = 0
EduI5 = 0
EduI6 = 0
EduI7 = 0
EduI8 = 0
EduI9 = 0
EduI10 = 0
EduI11 = 0
EduI12 = 0
EduI13 = 0
EduI14 = 0
EduI15 = 0
EduI16 = 0
EduI17 = 1
EduI18 = 1
EduI19 = 1
EduI20 = 0
EduI21 = 0
EduI22 = 0
EduI23 = 1
EduI24 = 0
EduI25 = 0
EduI26 = 0
EduI27 = 1
EduI28 = 0
EduI29 = 0
EduI30 = 0
EduI31 = 0
EduI32 = 0
EduI33 = 0
EduI34 = 0
EduI35 = 0
EduI36 = 0
EduI37 = 0
EduI38 = 0
EduI39 = 0
EduI40 = 0
EduI41 = 0
EduI42 = 0
EduI43 = 0
EduI44 = 0
EduI45 = 0
EduI46 = 0
EduI47 = 0
EduI48 = 1
EduI49 = 0
EduI50 = 0
EduI51 = 0
ShopI1 = 0
ShopI2 = 0
ShopI3 = 0
ShopI4 = 1
ShopI5 = 1
ShopI6 = 0
ShopI7 = 0
ShopI8 = 1
ShopI9 = 1
ShopI10 = 0
ShopI11 = 0
ShopI12 = 1
ShopI13 = 0
ShopI14 = 0
ShopI15 = 1
ShopI16 = 1
ShopI17 = 0
ShopI18 = 0
ShopI19 = 1
ShopI20 = 0
ShopI21 = 0
ShopI22 = 1
ShopI23 = 0
ShopI24 = 0
ShopI25 = 0
ShopI26 = 1
ShopI27 = 0
ShopI28 = 0
ShopI29 = 0
ShopI30 = 0
ShopI31 = 1
ShopI32 = 1
ShopI33 = 0
ShopI34 = 0
ShopI35 = 1
ShopI36 = 0
ShopI37 = 0
ShopI38 = 1
ShopI39 = 0
ShopI40 = 0
ShopI41 = 0
ShopI42 = 1
ShopI43 = 0
ShopI44 = 0
ShopI45 = 0
ShopI46 = 0
ShopI47 = 1
ShopI48 = 0
ShopI49 = 0
ShopI50 = 0
ShopI51 = 0
OthersI1 = 0
OthersI2 = 0
OthersI3 = 1
OthersI4 = 0
OthersI5 = 1
OthersI6 = 0
OthersI7 = 1
OthersI8 = 0
OthersI9 = 1
OthersI10 = 0
OthersI11 = 1
OthersI12 = 0
OthersI13 = 0
OthersI14 = 1
OthersI15 = 0
OthersI16 = 1
OthersI17 = 0
OthersI18 = 1
OthersI19 = 0
OthersI20 = 0
OthersI21 = 1
OthersI22 = 0
OthersI23 = 0
OthersI24 = 0
OthersI25 = 1
OthersI26 = 0
OthersI27 = 0
OthersI28 = 0
OthersI29 = 0
OthersI30 = 1
OthersI31 = 0
OthersI32 = 1
OthersI33 = 0
OthersI34 = 1
OthersI35 = 0
OthersI36 = 0
OthersI37 = 1
OthersI38 = 0
OthersI39 = 0
OthersI40 = 0
OthersI41 = 1
OthersI42 = 0
OthersI43 = 0
OthersI44 = 0
OthersI45 = 0
OthersI46 = 1
OthersI47 = 0
OthersI48 = 0
OthersI49 = 0
OthersI50 = 0
OthersI51 = 0


#Tour and Stop specific
onetour_onestop1 = 0
onetour_onestop2 = 0
onetour_onestop3 = 1
onetour_onestop4 = 1
onetour_onestop5 = 0
onetour_onestop6 = 0
onetour_onestop7 = 1
onetour_onestop8 = 1
onetour_onestop9 = 0
onetour_onestop10 = 0
onetour_onestop11 = 0
onetour_onestop12 = 0
onetour_onestop13 = 0
onetour_onestop14 = 1
onetour_onestop15 = 1
onetour_onestop16 = 0
onetour_onestop17 = 1
onetour_onestop18 = 0
onetour_onestop19 = 0
onetour_onestop20 = 0
onetour_onestop21 = 0
onetour_onestop22 = 0
onetour_onestop23 = 0
onetour_onestop24 = 0
onetour_onestop25 = 0
onetour_onestop26 = 0
onetour_onestop27 = 0
onetour_onestop28 = 0
onetour_onestop29 = 0
onetour_onestop30 = 1
onetour_onestop31 = 1
onetour_onestop32 = 0
onetour_onestop33 = 1
onetour_onestop34 = 0
onetour_onestop35 = 0
onetour_onestop36 = 0
onetour_onestop37 = 0
onetour_onestop38 = 0
onetour_onestop39 = 0
onetour_onestop40 = 0
onetour_onestop41 = 0
onetour_onestop42 = 0
onetour_onestop43 = 0
onetour_onestop44 = 0
onetour_onestop45 = 0
onetour_onestop46 = 0
onetour_onestop47 = 0
onetour_onestop48 = 0
onetour_onestop49 = 0
onetour_onestop50 = 0
onetour_onestop51 = 0
onetour_twostop1 = 0
onetour_twostop2 = 0
onetour_twostop3 = 0
onetour_twostop4 = 0
onetour_twostop5 = 1
onetour_twostop6 = 0
onetour_twostop7 = 0
onetour_twostop8 = 0
onetour_twostop9 = 1
onetour_twostop10 = 0
onetour_twostop11 = 0
onetour_twostop12 = 0
onetour_twostop13 = 0
onetour_twostop14 = 0
onetour_twostop15 = 0
onetour_twostop16 = 1
onetour_twostop17 = 0
onetour_twostop18 = 1
onetour_twostop19 = 1
onetour_twostop20 = 0
onetour_twostop21 = 0
onetour_twostop22 = 0
onetour_twostop23 = 0
onetour_twostop24 = 0
onetour_twostop25 = 0
onetour_twostop26 = 0
onetour_twostop27 = 0
onetour_twostop28 = 0
onetour_twostop29 = 0
onetour_twostop30 = 0
onetour_twostop31 = 0
onetour_twostop32 = 1
onetour_twostop33 = 0
onetour_twostop34 = 1
onetour_twostop35 = 1
onetour_twostop36 = 0
onetour_twostop37 = 0
onetour_twostop38 = 0
onetour_twostop39 = 0
onetour_twostop40 = 0
onetour_twostop41 = 0
onetour_twostop42 = 0
onetour_twostop43 = 0
onetour_twostop44 = 0
onetour_twostop45 = 0
onetour_twostop46 = 0
onetour_twostop47 = 0
onetour_twostop48 = 0
onetour_twostop49 = 0
onetour_twostop50 = 0
onetour_twostop51 = 0
onetour_threestop1 = 0
onetour_threestop2 = 0
onetour_threestop3 = 0
onetour_threestop4 = 0
onetour_threestop5 = 0
onetour_threestop6 = 0
onetour_threestop7 = 0
onetour_threestop8 = 0
onetour_threestop9 = 0
onetour_threestop10 = 0
onetour_threestop11 = 0
onetour_threestop12 = 0
onetour_threestop13 = 0
onetour_threestop14 = 0
onetour_threestop15 = 0
onetour_threestop16 = 0
onetour_threestop17 = 0
onetour_threestop18 = 0
onetour_threestop19 = 0
onetour_threestop20 = 0
onetour_threestop21 = 0
onetour_threestop22 = 0
onetour_threestop23 = 0
onetour_threestop24 = 0
onetour_threestop25 = 0
onetour_threestop26 = 0
onetour_threestop27 = 0
onetour_threestop28 = 0
onetour_threestop29 = 0
onetour_threestop30 = 0
onetour_threestop31 = 0
onetour_threestop32 = 0
onetour_threestop33 = 0
onetour_threestop34 = 0
onetour_threestop35 = 0
onetour_threestop36 = 0
onetour_threestop37 = 0
onetour_threestop38 = 0
onetour_threestop39 = 0
onetour_threestop40 = 0
onetour_threestop41 = 0
onetour_threestop42 = 0
onetour_threestop43 = 0
onetour_threestop44 = 0
onetour_threestop45 = 0
onetour_threestop46 = 0
onetour_threestop47 = 0
onetour_threestop48 = 0
onetour_threestop49 = 0
onetour_threestop50 = 0
onetour_threestop51 = 0
twotour_onestop1 = 0
twotour_onestop2 = 0
twotour_onestop3 = 0
twotour_onestop4 = 0
twotour_onestop5 = 0
twotour_onestop6 = 0
twotour_onestop7 = 0
twotour_onestop8 = 0
twotour_onestop9 = 0
twotour_onestop10 = 0
twotour_onestop11 = 1
twotour_onestop12 = 1
twotour_onestop13 = 0
twotour_onestop14 = 0
twotour_onestop15 = 0
twotour_onestop16 = 0
twotour_onestop17 = 0
twotour_onestop18 = 0
twotour_onestop19 = 0
twotour_onestop20 = 0
twotour_onestop21 = 1
twotour_onestop22 = 1
twotour_onestop23 = 1
twotour_onestop24 = 0
twotour_onestop25 = 1
twotour_onestop26 = 1
twotour_onestop27 = 1
twotour_onestop28 = 0
twotour_onestop29 = 0
twotour_onestop30 = 0
twotour_onestop31 = 0
twotour_onestop32 = 0
twotour_onestop33 = 0
twotour_onestop34 = 0
twotour_onestop35 = 0
twotour_onestop36 = 0
twotour_onestop37 = 1
twotour_onestop38 = 1
twotour_onestop39 = 1
twotour_onestop40 = 0
twotour_onestop41 = 1
twotour_onestop42 = 1
twotour_onestop43 = 1
twotour_onestop44 = 0
twotour_onestop45 = 0
twotour_onestop46 = 1
twotour_onestop47 = 1
twotour_onestop48 = 1
twotour_onestop49 = 1
twotour_onestop50 = 0
twotour_onestop51 = 0
twotour_twostop1 = 0
twotour_twostop2 = 0
twotour_twostop3 = 0
twotour_twostop4 = 0
twotour_twostop5 = 0
twotour_twostop6 = 0
twotour_twostop7 = 0
twotour_twostop8 = 0
twotour_twostop9 = 0
twotour_twostop10 = 0
twotour_twostop11 = 0
twotour_twostop12 = 0
twotour_twostop13 = 0
twotour_twostop14 = 0
twotour_twostop15 = 0
twotour_twostop16 = 0
twotour_twostop17 = 0
twotour_twostop18 = 0
twotour_twostop19 = 0
twotour_twostop20 = 0
twotour_twostop21 = 0
twotour_twostop22 = 0
twotour_twostop23 = 0
twotour_twostop24 = 0
twotour_twostop25 = 0
twotour_twostop26 = 0
twotour_twostop27 = 0
twotour_twostop28 = 0
twotour_twostop29 = 0
twotour_twostop30 = 0
twotour_twostop31 = 0
twotour_twostop32 = 0
twotour_twostop33 = 0
twotour_twostop34 = 0
twotour_twostop35 = 0
twotour_twostop36 = 0
twotour_twostop37 = 0
twotour_twostop38 = 0
twotour_twostop39 = 0
twotour_twostop40 = 0
twotour_twostop41 = 0
twotour_twostop42 = 0
twotour_twostop43 = 0
twotour_twostop44 = 0
twotour_twostop45 = 0
twotour_twostop46 = 0
twotour_twostop47 = 0
twotour_twostop48 = 0
twotour_twostop49 = 0
twotour_twostop50 = 0
twotour_twostop51 = 0
twotour_threestop1 = 0
twotour_threestop2 = 0
twotour_threestop3 = 0
twotour_threestop4 = 0
twotour_threestop5 = 0
twotour_threestop6 = 0
twotour_threestop7 = 0
twotour_threestop8 = 0
twotour_threestop9 = 0
twotour_threestop10 = 0
twotour_threestop11 = 0
twotour_threestop12 = 0
twotour_threestop13 = 0
twotour_threestop14 = 0
twotour_threestop15 = 0
twotour_threestop16 = 0
twotour_threestop17 = 0
twotour_threestop18 = 0
twotour_threestop19 = 0
twotour_threestop20 = 0
twotour_threestop21 = 0
twotour_threestop22 = 0
twotour_threestop23 = 0
twotour_threestop24 = 0
twotour_threestop25 = 0
twotour_threestop26 = 0
twotour_threestop27 = 0
twotour_threestop28 = 0
twotour_threestop29 = 0
twotour_threestop30 = 0
twotour_threestop31 = 0
twotour_threestop32 = 0
twotour_threestop33 = 0
twotour_threestop34 = 0
twotour_threestop35 = 0
twotour_threestop36 = 0
twotour_threestop37 = 0
twotour_threestop38 = 0
twotour_threestop39 = 0
twotour_threestop40 = 0
twotour_threestop41 = 0
twotour_threestop42 = 0
twotour_threestop43 = 0
twotour_threestop44 = 0
twotour_threestop45 = 0
twotour_threestop46 = 0
twotour_threestop47 = 0
twotour_threestop48 = 0
twotour_threestop49 = 0
twotour_threestop50 = 0
twotour_threestop51 = 0
threetour_onestop1 = 0
threetour_onestop2 = 0
threetour_onestop3 = 0
threetour_onestop4 = 0
threetour_onestop5 = 0
threetour_onestop6 = 0
threetour_onestop7 = 0
threetour_onestop8 = 0
threetour_onestop9 = 0
threetour_onestop10 = 0
threetour_onestop11 = 0
threetour_onestop12 = 0
threetour_onestop13 = 0
threetour_onestop14 = 0
threetour_onestop15 = 0
threetour_onestop16 = 0
threetour_onestop17 = 0
threetour_onestop18 = 0
threetour_onestop19 = 0
threetour_onestop20 = 0
threetour_onestop21 = 0
threetour_onestop22 = 0
threetour_onestop23 = 0
threetour_onestop24 = 0
threetour_onestop25 = 0
threetour_onestop26 = 0
threetour_onestop27 = 0
threetour_onestop28 = 0
threetour_onestop29 = 0
threetour_onestop30 = 0
threetour_onestop31 = 0
threetour_onestop32 = 0
threetour_onestop33 = 0
threetour_onestop34 = 0
threetour_onestop35 = 0
threetour_onestop36 = 0
threetour_onestop37 = 0
threetour_onestop38 = 0
threetour_onestop39 = 0
threetour_onestop40 = 0
threetour_onestop41 = 0
threetour_onestop42 = 0
threetour_onestop43 = 0
threetour_onestop44 = 0
threetour_onestop45 = 0
threetour_onestop46 = 0
threetour_onestop47 = 0
threetour_onestop48 = 0
threetour_onestop49 = 0
threetour_onestop50 = 0
threetour_onestop51 = 0
threetour_twostop1 = 0
threetour_twostop2 = 0
threetour_twostop3 = 0
threetour_twostop4 = 0
threetour_twostop5 = 0
threetour_twostop6 = 0
threetour_twostop7 = 0
threetour_twostop8 = 0
threetour_twostop9 = 0
threetour_twostop10 = 0
threetour_twostop11 = 0
threetour_twostop12 = 0
threetour_twostop13 = 0
threetour_twostop14 = 0
threetour_twostop15 = 0
threetour_twostop16 = 0
threetour_twostop17 = 0
threetour_twostop18 = 0
threetour_twostop19 = 0
threetour_twostop20 = 0
threetour_twostop21 = 0
threetour_twostop22 = 0
threetour_twostop23 = 0
threetour_twostop24 = 0
threetour_twostop25 = 0
threetour_twostop26 = 0
threetour_twostop27 = 0
threetour_twostop28 = 0
threetour_twostop29 = 0
threetour_twostop30 = 0
threetour_twostop31 = 0
threetour_twostop32 = 0
threetour_twostop33 = 0
threetour_twostop34 = 0
threetour_twostop35 = 0
threetour_twostop36 = 0
threetour_twostop37 = 0
threetour_twostop38 = 0
threetour_twostop39 = 0
threetour_twostop40 = 0
threetour_twostop41 = 0
threetour_twostop42 = 0
threetour_twostop43 = 0
threetour_twostop44 = 0
threetour_twostop45 = 0
threetour_twostop46 = 0
threetour_twostop47 = 0
threetour_twostop48 = 0
threetour_twostop49 = 0
threetour_twostop50 = 0
threetour_twostop51 = 0


#Activity dummies
work1 = 0
work2 = 0
work3 = 0
work4 = 0
work5 = 0
work6 = 0
work7 = 0
work8 = 0
work9 = 0
work10 = 0
work11 = 0
work12 = 0
work13 = 0
work14 = 0
work15 = 0
work16 = 0
work17 = 0
work18 = 0
work19 = 0
work20 = 0
work21 = 0
work22 = 0
work23 = 0
work24 = 0
work25 = 0
work26 = 0
work27 = 0
work28 = 0
work29 = 1
work30 = 1
work31 = 1
work32 = 1
work33 = 1
work34 = 1
work35 = 1
work36 = 1
work37 = 1
work38 = 1
work39 = 1
work40 = 1
work41 = 1
work42 = 1
work43 = 1
work44 = 1
work45 = 1
work46 = 1
work47 = 1
work48 = 1
work49 = 1
work50 = 1
work51 = 1
edu1 = 0
edu2 = 0
edu3 = 0
edu4 = 0
edu5 = 0
edu6 = 0
edu7 = 0
edu8 = 0
edu9 = 0
edu10 = 0
edu11 = 0
edu12 = 0
edu13 = 1
edu14 = 1
edu15 = 1
edu16 = 1
edu17 = 1
edu18 = 1
edu19 = 1
edu20 = 1
edu21 = 1
edu22 = 1
edu23 = 1
edu24 = 1
edu25 = 1
edu26 = 1
edu27 = 1
edu28 = 1
edu29 = 0
edu30 = 0
edu31 = 0
edu32 = 0
edu33 = 0
edu34 = 0
edu35 = 0
edu36 = 0
edu37 = 0
edu38 = 0
edu39 = 0
edu40 = 0
edu41 = 0
edu42 = 0
edu43 = 0
edu44 = 0
edu45 = 1
edu46 = 1
edu47 = 1
edu48 = 1
edu49 = 1
edu50 = 1
edu51 = 1
shop1 = 0
shop2 = 0
shop3 = 0
shop4 = 1
shop5 = 1
shop6 = 1
shop7 = 1
shop8 = 1
shop9 = 1
shop10 = 1
shop11 = 1
shop12 = 1
shop13 = 0
shop14 = 0
shop15 = 1
shop16 = 1
shop17 = 0
shop18 = 0
shop19 = 1
shop20 = 0
shop21 = 0
shop22 = 1
shop23 = 0
shop24 = 1
shop25 = 1
shop26 = 1
shop27 = 1
shop28 = 1
shop29 = 0
shop30 = 0
shop31 = 1
shop32 = 1
shop33 = 0
shop34 = 0
shop35 = 1
shop36 = 0
shop37 = 0
shop38 = 1
shop39 = 0
shop40 = 1
shop41 = 1
shop42 = 1
shop43 = 1
shop44 = 1
shop45 = 0
shop46 = 0
shop47 = 1
shop48 = 0
shop49 = 0
shop50 = 0
shop51 = 1
other1 = 0
other2 = 1
other3 = 1
other4 = 1
other5 = 1
other6 = 0
other7 = 1
other8 = 0
other9 = 1
other10 = 1
other11 = 1
other12 = 1
other13 = 0
other14 = 1
other15 = 0
other16 = 1
other17 = 0
other18 = 1
other19 = 0
other20 = 1
other21 = 1
other22 = 1
other23 = 1
other24 = 0
other25 = 1
other26 = 0
other27 = 0
other28 = 1
other29 = 0
other30 = 1
other31 = 0
other32 = 1
other33 = 0
other34 = 1
other35 = 0
other36 = 1
other37 = 1
other38 = 1
other39 = 1
other40 = 0
other41 = 1
other42 = 0
other43 = 0
other44 = 1
other45 = 0
other46 = 1
other47 = 0
other48 = 0
other49 = 0
other50 = 1
other51 = 0



#Person type
fulltime = (person_type_id == 1) #Base
parttime = (person_type_id == 2)
selfemployed = (person_type_id == 3)
universitystudent = (person_type_id == 4) * (universitystudent == 1)
homemaker = (person_type_id == 5)
retired = (person_type_id == 6)
unemployed = (person_type_id == 7)
nationalservice = (person_type_id == 8)
voluntary =  (person_type_id == 9)
domestic =  (person_type_id == 10)
otherworker = (person_type_id == 12)
student16 = (person_type_id == 4) * (age_id == 3)
student515 = (person_type_id == 4) * ((age_id == 1) + (age_id == 2))
child4 = (age_id == 0) #Under 4 years old

#Adult age group
age20 = (age_id < 4) #Do not include
age2025 = (age_id == 4)
age2635 = (age_id == 5) + (age_id == 6)
age3650 = (age_id == 7) + (age_id == 8) + (age_id == 9) #Base 
age5165 = (age_id == 10) + (age_id == 11) + (age_id == 12)
age65 = (age_id > 12)

#Adult gender/children
maleage4 = (female_dummy == 0) * (HH_with_under_4 == 1)
maleage515 = (female_dummy == 0) * (HH_with_under_15 - HH_with_under_4)
malenone = (female_dummy == 0) * (HH_all_adults == 1) #Base
femalenone = (female_dummy == 1) * (HH_all_adults == 1)
femaleage4 = (female_dummy == 1) * (HH_with_under_4 == 1)
femaleage515 = (female_dummy == 1) * (HH_with_under_15 - HH_with_under_4)

#Household composition
onlyadults = (HH_all_adults == 1)
onlyworkers = (HH_all_workers == 1)
onlyadultsworkers = (HH_all_adults == 1) * (HH_all_workers == 1) #Base
#non-family 2+ person HH is not possible

#Personal Income
income = incmid * (1 - missingincome)/1000

#Others
workathome = (work_at_home_dummy == 1)
caravail = (hh_car_avail == 1)             #?
motoravail = (hh_motor_avail == 1)         #?
	
#Additional constants
tour = (work_tour + edu_tour + shopping_tour + other_tour > 0)
stop = (work_stop + edu_stop + shopping_stop + other_stop > 0)
onet_ones = (onetouronestop == 1)
onet_twos = (onetourtwostop == 1)
onet_threes = (onetourthreestop == 1)
twot_ones = (twotouronestop == 1)
twot_twos = (twotourtwostop == 1)
twot_threes = (twotourthreestop == 1)
threet_ones = (threetouronestop == 1)
threet_twos = (threetourtwostop == 1)

#Parameters

#Tour constants
beta_tour_work = Beta('beta_tour_work',0,-10,10,0)
beta_tour_edu = Beta('beta_tour_edu',0,-10,100,1)
beta_tour_shop = Beta('beta_tour_shop',0,-10,10,0)
beta_tour_others = Beta('beta_tour_others',0,-10,10,0)

#Intermediate Stops constants
beta_stop_work = Beta('beta_stop_work',0,-10,10,1)
beta_stop_edu = Beta('beta_stop_edu',0,-10,10,1)
beta_stop_shop = Beta('beta_stop_shop',0,-10,10,1)
beta_stop_others = Beta('beta_stop_others',0,-10,10,1)

#Person type
beta_parttime_work = Beta('beta_parttime_work',0,-10,10,0)
beta_parttime_edu = Beta('beta_parttime_edu',0,-10,10,1)
beta_parttime_shop = Beta('beta_parttime_shop',0,-10,10,0)
beta_parttime_others = Beta('beta_parttime_others',0,-10,10,0)

beta_selfemployed_work = Beta('beta_selfemployed_work',0,-10,10,0)
beta_selfemployed_edu = Beta('beta_selfemployed_edu',0,-10,10,1)
beta_selfemployed_shop = Beta('beta_selfemployed_shop',0,-10,10,0)
beta_selfemployed_others = Beta('beta_selfemployed_others',0,-10,10,0)

beta_universitystudent_work = Beta('beta_universitystudent_work',0,-10,10,0)
beta_universitystudent_edu = Beta('beta_universitystudent_edu',0,-10,100,1)
beta_universitystudent_shop = Beta('beta_universitystudent_shop',0,-10,10,1)
beta_universitystudent_others = Beta('beta_universitystudent_others',0,-10,10,1)

beta_homemaker_work = Beta('beta_homemaker_work',-20,-10,10,1)
beta_homemaker_edu = Beta('beta_homemaker_edu',0,-10,10,1)
beta_homemaker_shop = Beta('beta_homemaker_shop',0,-10,10,0)
beta_homemaker_others = Beta('beta_homemaker_others',0,-10,10,0)

beta_retired_work = Beta('beta_retired_work',0,-100,10,1)
beta_retired_edu = Beta('beta_retired_edu',0,-10,10,1)
beta_retired_shop = Beta('beta_retired_shop',0,-10,10,0)
beta_retired_others = Beta('beta_retired_others',0,-10,10,0)

beta_unemployed_work = Beta('beta_unemployed_work',-20,-10,10,1)
beta_unemployed_edu = Beta('beta_unemployed_edu',0,-10,10,1)
beta_unemployed_shop = Beta('beta_unemployed_shop',0,-10,10,0)
beta_unemployed_others = Beta('beta_unemployed_others',0,-10,10,0)

beta_nationalservice_work = Beta('beta_nationalservice_work',0,-10,10,0)
beta_nationalservice_edu = Beta('beta_nationalservice_edu',0,-10,10,1)
beta_nationalservice_shop = Beta('beta_nationalservice_shop',0,-10,10,1)
beta_nationalservice_others = Beta('beta_nationalservice_others',0,-10,10,0)

beta_voluntary_work = Beta('beta_voluntary_work',0,-10,10,0)
beta_voluntary_edu = Beta('beta_voluntary_edu',0,-10,10,1)
beta_voluntary_shop = Beta('beta_voluntary_shop',0,-10,10,0)
beta_voluntary_others = Beta('beta_voluntary_others',0,-10,10,1)

beta_domestic_work = Beta('beta_domestic_work',0,-10,10,1)
beta_domestic_edu = Beta('beta_domestic_edu',0,-10,10,1)
beta_domestic_shop = Beta('beta_domestic_shop',0,-10,10,0)
beta_domestic_others = Beta('beta_domestic_others',0,-10,10,0)

beta_otherworker_work = Beta('beta_otherworker_work',0,-10,10,0)
beta_otherworker_edu = Beta('beta_otherworker_edu',0,-10,10,1)
beta_otherworker_shop = Beta('beta_otherworker_shop',0,-10,10,0)
beta_otherworker_others = Beta('beta_otherworker_others',0,-10,10,0)

beta_student16_work = Beta('beta_student16_work',0,-10,10,0)
beta_student16_edu = Beta('beta_student16_edu',0,-10,10,1)
beta_student16_shop = Beta('beta_student16_shop',0,-10,10,0)
beta_student16_others = Beta('beta_student16_others',0,-10,10,0)

beta_student515_work = Beta('beta_student515_work',-20,-10,10,1)
beta_student515_edu = Beta('beta_student515_edu',0,-10,10,1)
beta_student515_shop = Beta('beta_student515_shop',0,-10,10,0)
beta_student515_others = Beta('beta_student515_others',0,-10,10,0)

beta_child4_work = Beta('beta_child4_work',-20,-10,10,1)
beta_child4_edu = Beta('beta_child4_edu',0,-10,10,1)
beta_child4_shop = Beta('beta_child4_shop',0,-10,10,1)
beta_child4_others = Beta('beta_child4_others',0,-10,10,1)

#Adult age group

beta_age2025_work = Beta('beta_age2025_work',0,-10,10,1)
beta_age2025_edu = Beta('beta_age2025_edu',0,-10,10,1)
beta_age2025_shop = Beta('beta_age2025_shop',0,-10,10,1)
beta_age2025_others = Beta('beta_age2025_others',0,-10,10,1)

beta_age2635_work = Beta('beta_age2635_work',0,-10,10,1)
beta_age2635_edu = Beta('beta_age2635_edu',0,-10,10,1)
beta_age2635_shop = Beta('beta_age2635_shop',0,-10,10,1)
beta_age2635_others = Beta('beta_age2635_work',0,-10,10,1)

beta_age5165_work = Beta('beta_age5165_work',0,-10,10,1)
beta_age5165_edu = Beta('beta_age5165_edu',0,-10,10,1)
beta_age5165_shop = Beta('beta_age5165_shop',0,-10,10,1)
beta_age5165_others = Beta('beta_age5165_others',0,-10,10,1)

#Adult gender/children

beta_maleage4_work = Beta('beta_maleage4_work',0,-10,10,1)
beta_maleage4_edu = Beta('beta_maleage4_edu',0,-10,10,1)
beta_maleage4_shop = Beta('beta_maleage4_shop',0,-10,10,0)
beta_maleage4_others = Beta('beta_maleage4_others',0,-10,10,0)

beta_maleage515_work = Beta('beta_maleage515_work',0,-10,10,1)
beta_maleage515_edu = Beta('beta_maleage515_edu',0,-10,10,1)
beta_maleage515_shop = Beta('beta_maleage515_shop',0,-10,10,0)
beta_maleage515_others = Beta('beta_maleage515_others',0,-10,10,0)

beta_femalenone_work = Beta('beta_femalenone_work',0,-10,10,0)
beta_femalenone_edu = Beta('beta_femalenone_edu',0,-10,10,1)
beta_femalenone_shop = Beta('beta_femalenone_shop',0,-10,10,1)
beta_femalenone_others = Beta('beta_femalenone_others',0,-10,10,0)

beta_femaleage4_work = Beta('beta_femaleage4_work',0,-10,10,0)
beta_femaleage4_edu = Beta('beta_femaleage4_edu',0,-10,10,1)
beta_femaleage4_shop = Beta('beta_femaleage4_shop',0,-10,10,0)
beta_femaleage4_others = Beta('beta_femaleage4_others',0,-10,10,0)

beta_femaleage515_work = Beta('beta_femaleage515_work',0,-10,10,1)
beta_femaleage515_edu = Beta('beta_femaleage515_edu',0,-10,10,1)
beta_femaleage515_shop = Beta('beta_femaleage515_shop',0,-10,10,0)
beta_femaleage515_others = Beta('beta_femaleage515_others',0,-10,10,0)

#Household composition
beta_onlyadults_work = Beta('beta_onlyadults_work',0,-10,10,1)
beta_onlyadults_edu = Beta('beta_onlyadults_edu',0,-10,10,1)
beta_onlyadults_shop = Beta('beta_onlyadults_shop',0,-10,10,0)
beta_onlyadults_others = Beta('beta_onlyadults_others',0,-10,10,0)

beta_onlyworkers_work = Beta('beta_onlyworkers_work',0,-10,10,1)
beta_onlyworkers_edu = Beta('beta_onlyworkers_edu',0,-10,10,1)
beta_onlyworkers_shop = Beta('beta_onlyworkers_shop',0,-10,10,0)
beta_onlyworkers_others = Beta('beta_onlyworkers_others',0,-10,10,0)


#Personal income
beta_missingincome_work = Beta('beta_missingincome_work',0,-10,10,0)
beta_missingincome_edu = Beta('beta_missingincome_edu',0,-10,10,1)
beta_missingincome_shop = Beta('beta_missingincome_shop',0,-10,10,0)
beta_missingincome_others = Beta('beta_missingincome_others',0,-10,10,0)


#Missing Income
beta_income_work = Beta('beta_income_work',0,-10,10,0)
beta_income_edu = Beta('beta_income_edu',0,-10,10,1)
beta_income_shop = Beta('beta_income_shop',0,-10,10,0)
beta_income_others = Beta('beta_income_others',0,-10,10,0)

#Others
beta_workathome_work = Beta('beta_workathome_work',0,-10,10,1)
beta_workathome_edu = Beta('beta_workathome_edu',0,-10,10,1)
beta_workathome_shop = Beta('beta_workathome_shop',0,-10,10,1)
beta_workathome_others = Beta('beta_workathome_others',0,-10,10,1)

beta_caravail_work = Beta('beta_caravail_work',0,-10,10,0)
beta_caravail_edu = Beta('beta_caravail_edu',0,-10,10,1)
beta_caravail_shop = Beta('beta_caravail_shop',0,-10,10,0)
beta_caravail_others = Beta('beta_caravail_others',0,-10,10,0)

beta_motoravail_work = Beta('beta_motoravail_work',0,-10,10,0)
beta_motoravail_edu = Beta('beta_motoravail_edu',0,-10,10,1)
beta_motoravail_shop = Beta('beta_motoravail_shop',0,-10,10,0)
beta_motoravail_others = Beta('beta_motoravail_others',0,-10,10,0)


#Additional constants
beta_onetour_onestop = Beta('beta_onetour_onestop',0,-10,10,0)
beta_onetour_twostop = Beta('beta_onetour_twostop',0,-10,10,0)
beta_onetour_threestop = Beta('beta_onetour_threestop',0,-10,10,1)
beta_twotour_onestop = Beta('beta_twotour_onestop',0,-10,10,0)
beta_twotour_twostop = Beta('beta_twotour_twostop',0,-10,10,1)
beta_twotour_threestop = Beta('beta_twotour_threestop',0,-10,10,1)
beta_threetour_onestop = Beta('beta_threetour_onestop',0,-10,10,1)
beta_threetour_twostop = Beta('beta_threetour_twostop',0,-10,10,1)

beta_work_logsum=Beta('beta_work_logsum',0,-10,10,0)
beta_edu_logsum=Beta('beta_edu_logsum',0,-10,10,1)
beta_shopping_logsum=Beta('beta_shopping_logsum',0,-10,10,0)
beta_other_logsum=Beta('beta_other_logsum',0,-10,10,0)

#Choice set
counter = 0
choiceset = range(1,52)


counter = counter + 1
exec("V_%s = 0" % (counter))

for i in range(2,52):
    counter = counter + 1
    exec("V_%s = beta_tour_work * (WorkT%s) + beta_stop_work * (WorkI%s) +  beta_tour_edu * (EduT%s) + beta_stop_edu * (EduI%s) +  beta_tour_shop * (ShopT%s) + beta_stop_shop * (ShopI%s) +  beta_tour_others * (OthersT%s) + beta_stop_others * (OthersI%s) + beta_onetour_onestop * (onetour_onestop%s) + beta_onetour_twostop * (onetour_twostop%s) + beta_onetour_threestop * (onetour_threestop%s) + beta_twotour_onestop * (twotour_onestop%s) + beta_twotour_twostop * (twotour_twostop%s) + beta_twotour_threestop * (twotour_threestop%s) + beta_threetour_onestop * (threetour_onestop%s) + beta_threetour_twostop * (threetour_twostop%s)  + beta_parttime_work * (work%s * parttime) + beta_parttime_edu * (edu%s * parttime) + beta_parttime_shop * (shop%s * parttime) + beta_parttime_others * (other%s * parttime) + beta_selfemployed_work * (work%s * selfemployed) + beta_selfemployed_edu * (edu%s * selfemployed) + beta_selfemployed_shop * (shop%s * selfemployed) + beta_selfemployed_others * (other%s * selfemployed) + beta_universitystudent_work * (work%s * universitystudent) + beta_universitystudent_edu * (edu%s * universitystudent) + beta_universitystudent_shop * (shop%s * universitystudent) + beta_universitystudent_others * (other%s * universitystudent) +  beta_homemaker_work * (work%s * homemaker) + beta_homemaker_edu * (edu%s * homemaker) + beta_homemaker_shop * (shop%s * homemaker) + beta_homemaker_others * (other%s * homemaker) +  beta_retired_work * (work%s * retired) + beta_retired_edu * (edu%s * retired) + beta_retired_shop * (shop%s * retired) + beta_retired_others * (other%s * retired)  + beta_unemployed_work * (work%s * unemployed) + beta_unemployed_edu * (edu%s * unemployed) + beta_unemployed_shop * (shop%s * unemployed) + beta_unemployed_others * (other%s * unemployed) + beta_nationalservice_work * (work%s * nationalservice) + beta_nationalservice_edu * (edu%s * nationalservice) + beta_nationalservice_shop * (shop%s * nationalservice) + beta_nationalservice_others * (other%s * nationalservice) +  beta_voluntary_work * (work%s * voluntary) + beta_voluntary_edu * (edu%s * voluntary) + beta_voluntary_shop * (shop%s * voluntary) + beta_voluntary_others * (other%s * voluntary) +  beta_domestic_work * (work%s * domestic) + beta_domestic_edu * (edu%s * domestic) + beta_domestic_shop * (shop%s * domestic) + beta_domestic_others * (other%s * domestic) +  beta_otherworker_work * (work%s * otherworker) + beta_otherworker_edu * (edu%s * otherworker) + beta_otherworker_shop * (shop%s * otherworker) + beta_otherworker_others * (other%s * otherworker)  +  beta_student16_work * (work%s * student16) + beta_student16_edu * (edu%s * student16) + beta_student16_shop * (shop%s * student16) + beta_student16_others * (other%s * student16)  +  beta_student515_work * (work%s * student515) + beta_student515_edu * (edu%s * student515) + beta_student515_shop * (shop%s * student515) + beta_student515_others * (other%s * student515)  +  beta_child4_work * (work%s * child4) + beta_child4_edu * (edu%s * child4) + beta_child4_shop * (shop%s * child4) + beta_child4_others * (other%s * child4) + beta_age2025_work * (work%s * age2025) + beta_age2025_edu * (edu%s * age2025) + beta_age2025_shop * (shop%s * age2025) + beta_age2025_others * (other%s * age2025)  + beta_age2635_work * (work%s * age2635) + beta_age2635_edu * (edu%s * age2635) + beta_age2635_shop * (shop%s * age2635) + beta_age2635_others * (other%s * age2635)  + beta_age5165_work * (work%s * age5165) + beta_age5165_edu * (edu%s * age5165) + beta_age5165_shop * (shop%s * age5165) + beta_age5165_others * (other%s * age5165) + beta_maleage4_work * (work%s * maleage4) + beta_maleage4_edu * (edu%s * maleage4) + beta_maleage4_shop * (shop%s * maleage4) + beta_maleage4_others * (other%s * maleage4) + beta_maleage515_work * (work%s * maleage515) + beta_maleage515_edu * (edu%s * maleage515) + beta_maleage515_shop * (shop%s * maleage515) + beta_maleage515_others * (other%s * maleage515) + beta_femalenone_work * (work%s * femalenone) + beta_femalenone_edu * (edu%s * femalenone) + beta_femalenone_shop * (shop%s * femalenone) + beta_femalenone_others * (other%s * femalenone) + beta_femaleage4_work * (work%s * femaleage4) + beta_femaleage4_edu * (edu%s * femaleage4) + beta_femaleage4_shop * (shop%s * femaleage4) + beta_femaleage4_others * (other%s * femaleage4) + beta_femaleage515_work * (work%s * femaleage515) + beta_femaleage515_edu * (edu%s * femaleage515) + beta_femaleage515_shop * (shop%s * femaleage515) + beta_femaleage515_others * (other%s * femaleage515) + beta_onlyadults_work * (work%s * onlyadults) + beta_onlyadults_edu * (edu%s * onlyadults) + beta_onlyadults_shop * (shop%s * onlyadults) + beta_onlyadults_others * (other%s * onlyadults) + beta_onlyworkers_work * (work%s * onlyworkers) + beta_onlyworkers_edu * (edu%s * onlyworkers) + beta_onlyworkers_shop * (shop%s * onlyworkers) + beta_onlyworkers_others * (other%s * onlyworkers) +  beta_income_work * (work%s * income) + beta_income_edu * (edu%s * income) + beta_income_shop * (shop%s * income) + beta_income_others * (other%s * income) + beta_missingincome_work * (work%s * missingincome) + beta_missingincome_edu * (edu%s * missingincome) + beta_missingincome_shop * (shop%s * missingincome) + beta_missingincome_others * (other%s * missingincome) +  beta_workathome_work * (work%s * workathome) + beta_workathome_edu * (edu%s * workathome) + beta_workathome_shop * (shop%s * workathome) + beta_workathome_others * (other%s * workathome) +  beta_caravail_work * (work%s * caravail) + beta_caravail_edu * (edu%s * caravail) + beta_caravail_shop * (shop%s * caravail) + beta_caravail_others * (other%s * caravail) +  beta_motoravail_work * (work%s * motoravail) + beta_motoravail_edu * (edu%s * motoravail) + beta_motoravail_shop * (shop%s * motoravail) + beta_motoravail_others * (other%s * motoravail) + beta_work_logsum * WorkT%s * worklogsum + beta_edu_logsum * EduT%s * edulogsum + beta_shopping_logsum * ShopT%s * shoplogsum + beta_other_logsum * OthersT%s * otherlogsum" % (counter,counter,counter,counter,counter,counter,counter,counter,counter,counter,counter,counter,counter,counter,counter,counter,counter,counter,counter,counter,counter,counter,counter,counter,counter,counter,counter,counter,counter,counter,counter,counter,counter,counter,counter,counter,counter,counter,counter,counter,counter,counter,counter,counter,counter,counter,counter,counter,counter,counter,counter,counter,counter,counter,counter,counter,counter,counter,counter,counter,counter,counter,counter,counter,counter,counter,counter,counter,counter,counter,counter,counter,counter,counter,counter,counter,counter,counter,counter,counter,counter,counter,counter,counter,counter,counter,counter,counter,counter,counter,counter,counter,counter,counter,counter,counter,counter,counter,counter,counter,counter,counter,counter,counter,counter,counter,counter,counter,counter,counter,counter,counter,counter,counter,counter,counter,counter,counter,counter,counter,counter,counter,counter,counter,counter,counter,counter,counter,counter,counter,counter,counter,counter))


V =dict(zip(range(1,52),[eval('V_%s' %i) for i in choiceset]))
av=dict(zip(range(1,52),[eval('avail%s' %i) for i in choiceset]))

prob = bioLogit(V,av,oldpattern)

rowIterator('obsIter')
BIOGEME_OBJECT.ESTIMATE = Sum(log(prob),'obsIter')
exclude = ((oldpattern == 0) + (pattern_violation == 1))
BIOGEME_OBJECT.EXCLUDE = exclude
BIOGEME_OBJECT.PARAMETERS['numberOfThreads'] = '5'
BIOGEME_OBJECT.PARAMETERS['optimizationAlgorithm'] = 'DONLP2'
BIOGEME_OBJECT.PARAMETERS['checkDerivatives'] = '0'
BIOGEME_OBJECT.PARAMETERS['moreRobustToNumericalIssues'] = '0'



