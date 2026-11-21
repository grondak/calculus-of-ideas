# Typed-relation groups (Wiktionary-only links removed)

Variant: 689,944 of 4,341,307 links; datasets {'/d/wiktionary': 27365, '/d/verbosity': 45512, '/d/conceptnet': 220555, '/d/dbpedia': 45038, '/d/wordnet': 296711, '/d/opencyc': 86828}. Typed features 19,369 columns / 209,681 incidences.
Groups mined 4,009; significant under all nulls (global, relation, reciprocal, strict) 2,503; robust (all nulls + recovered in ≥60% of 80% edge subsamples + still present with Wiktionary restored) 986.
Robust tiers: {'crosscutting': 267, 'partly_named': 203, 'uncategorised': 379, 'named': 137}. Subsample re-mining group counts: [2119, 2178, 2220, 2166, 2194].
Selection control (re-mining null graphs): {"real": {"groups": 4009, "size_ge_6": 1690, "size_ge_10": 459}, "global": {"groups": [241, 262, 273, 313], "size_ge_6": [92, 122, 122, 151], "size_ge_10": [9, 14, 15, 19]}, "relation": {"groups": [2849, 2774, 2740, 2597], "size_ge_6": [1492, 1438, 1372, 1309], "size_ge_10": [613, 620, 598, 543]}, "reciprocal": {"groups": [2802, 2742, 2790, 2626], "size_ge_6": [1475, 1373, 1379, 1315], "size_ge_10": [676, 643, 602, 625]}, "strict": {"groups": [1777, 1788, 1841, 1867], "size_ge_6": [453, 458, 466, 460], "size_ge_10": [60, 51, 48, 57]}}

## Shapes (clusters of relation profiles)

| shape | relation profile (share of member–frame incidences) | groups | robust | robust tiers |
|---|---|---|---|---|
| 10 | AtLocation> 0.93, UsedFor> 0.06 | 1037 | 233 | {'crosscutting': 126, 'partly_named': 60, 'named': 43, 'uncategorised': 4} |
| 28 | UsedFor> 0.82, HasPrerequisite> 0.08 | 398 | 130 | {'uncategorised': 45, 'crosscutting': 33, 'named': 22, 'partly_named': 30} |
| 26 | Causes> 0.68, UsedFor> 0.28 | 397 | 101 | {'uncategorised': 57, 'partly_named': 11, 'named': 12, 'crosscutting': 21} |
| 52 | UsedFor< 0.97 | 299 | 80 | {'partly_named': 15, 'crosscutting': 26, 'uncategorised': 33, 'named': 6} |
| 40 | HasPrerequisite< 0.96 | 228 | 79 | {'uncategorised': 73, 'crosscutting': 4, 'partly_named': 1, 'named': 1} |
| 2 | AtLocation< 0.97 | 479 | 66 | {'crosscutting': 10, 'partly_named': 36, 'named': 20} |
| 57 | Causes< 0.95 | 225 | 66 | {'partly_named': 19, 'uncategorised': 16, 'crosscutting': 20, 'named': 11} |
| 33 | HasPrerequisite> 0.78, HasSubevent> 0.17 | 146 | 43 | {'uncategorised': 40, 'crosscutting': 2, 'partly_named': 1} |
| 24 | Causes> 0.48, HasPrerequisite> 0.45 | 101 | 36 | {'uncategorised': 21, 'crosscutting': 10, 'partly_named': 2, 'named': 3} |
| 9 | AtLocation> 0.5, AtLocation< 0.47 | 103 | 24 | {'partly_named': 12, 'named': 8, 'crosscutting': 4} |
| 34 | MotivatedByGoal> 0.62, CausesDesire< 0.33 | 38 | 16 | {'uncategorised': 16} |
| 18 | HasSubevent> 0.48, Causes> 0.48 | 67 | 14 | {'uncategorised': 10, 'crosscutting': 2, 'named': 1, 'partly_named': 1} |
| 21 | HasSubevent> 0.91, CausesDesire< 0.07 | 67 | 14 | {'uncategorised': 13, 'partly_named': 1} |
| 43 | CapableOf< 0.98 | 29 | 11 | {'uncategorised': 10, 'crosscutting': 1} |
| 3 | HasA< 0.94, AtLocation> 0.06 | 17 | 9 | {'uncategorised': 4, 'crosscutting': 4, 'named': 1} |

## Easy to name: an existing category covers ≥50% of members

### group 19 — 18 members, shape 28, tier named
members: acoustic_guitar, bagpipes, bass_fiddle, clavichord, cornet, french_horn, harmonica, keyboard, mandolin, symphony_hall, organ, string_bass, stringed_instrument, trombone, trumpet, viola, violin, woodwind
frame: UsedFor> play_music; UsedFor> playing_music
density 1.0; support 18 (with Wiktionary 18); nulls global p=0.0099 z=36.0 (null mean 0.01), relation p=0.0099 z=23.1 (null mean 0.66), reciprocal p=0.0099 z=21.5 (null mean 0.8), strict p=0.0099 z=17.0 (null mean 1.06); BH q 0.0159; subsample recovery 1.0
category: best direct musical_instrument (0.72), best within 2 IsA-steps musical_instrument (0.94), members with any category 1.0
member categories: acoustic_guitar→guitar,acoustic_instrument,larger_than_violin; bagpipes→best,musical_instrument,musical_instruments,from_scotland; bass_fiddle→bass,instrument,stringed_instrument,bowed_stringed_instrument; clavichord→keyboard_instrument,musical_instrument,stringed_instrument,archaic_musical_instrument; cornet→brass,brass_instrument,musical_instrument; french_horn→brass,brass_instrument,instrument,musical_instrument; harmonica→instrument,musical_instrument,reed,wind_instrument; keyboard→terminal,piano,computer,organ; mandolin→instrument,musical_instrument,stringed_instrument,chordophone; symphony_hall→where_orchestras_play
internal links among members 9 (configuration expectation 0.19); relative weight of member–frame links {'original': 1.251, 'wiki_half0': 1.266, 'wiki_half1': 1.265}
WikiText (obs/exp): wiki_half0 member–frame 0/0.1, member–member 176/2.8; wiki_half1 member–frame 1/0.1, member–member 113/2.9

### group 61 — 17 members, shape 10, tier named
members: cow, anemone, apple_tree, bald_eagle, beaver, blowfish, ficus, fox, gazelle, kitten, koala, lemur, lizard, mammoth, marmoset, monkey, shark
frame: AtLocation> outside; AtLocation> book; AtLocation> it's_natural_habitat; AtLocation> great_outdoors
density 0.809; support 17 (with Wiktionary 17); nulls global p=0.0099 z=34.0 (null mean 0.0), relation p=0.0099 z=33.7 (null mean 0.17), reciprocal p=0.0099 z=33.6 (null mean 0.2), strict p=0.0099 z=15.2 (null mean 1.46); BH q 0.0159; subsample recovery 0.8
category: best direct animal (0.53), best within 2 IsA-steps animal (0.82), members with any category 1.0
member categories: cow→adult,cattle,living_creature,heard; anemone→plant,flower; apple_tree→tree,fruit_tree,blooming; bald_eagle→bird,eagle,raptor,accipitridae; beaver→animal,person,work,mammal; blowfish→animal,saltwater_fish; ficus→plant,woody_plant,dicot_genus,spatial_thing; fox→animal,mammal,television_station,fur; gazelle→animal,mammal,automobile,company; kitten→animal,cat,give_birth,young_mammal
internal links among members 0 (configuration expectation 1.78); relative weight of member–frame links {'original': 0.934, 'wiki_half0': 0.946, 'wiki_half1': 0.941}
WikiText (obs/exp): wiki_half0 member–frame 40/99.8, member–member 17/13.1; wiki_half1 member–frame 43/91.1, member–member 11/11.2

### group 52 — 14 members, shape 10, tier named
members: bass_drum, brass, brass_family, cornet, crash_cymbal, drum, flute, percussion_instrument, saxophone, snare_drum, string_bass, trombone, trumpet, tuba
frame: AtLocation> marching_band; AtLocation> orchestra
density 1.0; support 14 (with Wiktionary 14); nulls global p=0.0099 z=28.0 (null mean 0.0), relation p=0.0099 z=21.5 (null mean 0.4), reciprocal p=0.0099 z=17.5 (null mean 0.53), strict p=0.0099 z=27.1 (null mean 0.37); BH q 0.0159; subsample recovery 0.6
category: best direct musical_instrument (0.64), best within 2 IsA-steps musical_instrument (0.86), members with any category 1.0
member categories: bass_drum→drum,instrument,musical_instrument,percussion_instrument; brass→conductor,album,memorial,wind_instrument; brass_family→class; cornet→brass,brass_instrument,musical_instrument; crash_cymbal→drum_set; drum→can,play,sound,container; flute→crimp,instrument,wind_instrument,woodwind; percussion_instrument→instrument,musical_instrument,music_instrument,acoustic_instrument; saxophone→instrument,musical_instrument,tool,woodwind; snare_drum→drum,musical_instrument,percussion_instrument,percussion
internal links among members 10 (configuration expectation 0.09); relative weight of member–frame links {'original': 1.058, 'wiki_half0': 1.026, 'wiki_half1': 1.071}
WikiText (obs/exp): wiki_half0 member–frame 43/2.9, member–member 108/1.6; wiki_half1 member–frame 24/2.9, member–member 70/1.6

### group 502 — 9 members, shape 28, tier named
members: accordion, guitar, instrument_triangle, oboe, percussion_instrument, tuba, wind_instrument, woodwind, playing_harp
frame: UsedFor> make_music; UsedFor> making_music; UsedFor> playing_in_orchestra; UsedFor> playing_in_band
density 0.833; support 9 (with Wiktionary 9); nulls global p=0.0099 z=18.0 (null mean 0.0), relation p=0.0099 z=17.9 (null mean 0.04), reciprocal p=0.0099 z=17.8 (null mean 0.08), strict p=0.0099 z=18.0 (null mean 0.01); BH q 0.0159; subsample recovery 0.6
category: best direct musical_instrument (0.78), best within 2 IsA-steps musical_instrument (0.89), members with any category 0.89
member categories: accordion→instrument,keyboard_instrument,musical_instrument,man_made_object; guitar→instrument,stringed_instrument,lute,chordophone; instrument_triangle→musical_instrument; oboe→instrument,musical_instrument,wind_instrument,woodwind; percussion_instrument→instrument,musical_instrument,music_instrument,acoustic_instrument; tuba→brass_instrument,musical_instrument,large_musical_instrument,instrument_in_band; wind_instrument→musical_instrument,acoustic_instrument,single_user_device,member_of_orchestra; woodwind→instrument,musical_instrument,wind_instrument,musical_instriment; playing_harp→–
internal links among members 3 (configuration expectation 0.06); relative weight of member–frame links {'original': 1.126, 'wiki_half0': 1.139, 'wiki_half1': 1.139}
WikiText (obs/exp): wiki_half0 member–frame 1/0.3, member–member 9/0.9; wiki_half1 member–frame 1/0.2, member–member 13/1.0

### group 820 — 8 members, shape 26, tier named
members: riding_bicycle, playing_sports, getting_physical_activity, playing, playing_sport, playing_baseball, playing_basketball, playing_lacrosse
frame: Causes> fun; Causes> injury; Causes> injuries; Causes> getting_tired; HasSubevent> running; UsedFor> competition; UsedFor> exercise; UsedFor> enjoyment; UsedFor> recreation
density 0.764; support 8 (with Wiktionary 8); nulls global p=0.0099 z=16.0 (null mean 0.0), relation p=0.0099 z=16.0 (null mean 0.0), reciprocal p=0.0099 z=16.0 (null mean 0.0), strict p=0.0099 z=16.0 (null mean 0.0); BH q 0.0159; subsample recovery 1.0
category: best direct intelligent_agent_activity (0.5), best within 2 IsA-steps action (0.5), members with any category 0.75
member categories: riding_bicycle→form_of_exercise; playing_sports→about_competition,fun_and_good_exercise; getting_physical_activity→–; playing→action,musical_performance,making_music,information_transfer; playing_sport→–; playing_baseball→play,playing_game,intelligent_agent_activity,playing_of_sports_event; playing_basketball→event,playing_game,form_of_exercise,intelligent_agent_activity; playing_lacrosse→playing_game,intelligent_agent_activity,playing_of_sports_event
internal links among members 1 (configuration expectation 0.4); relative weight of member–frame links {'original': 1.225, 'wiki_half0': 1.192, 'wiki_half1': 1.191}
WikiText (obs/exp): wiki_half0 member–frame 129/81.7, member–member 0/0.3; wiki_half1 member–frame 120/80.5, member–member 0/0.4

### group 686 — 8 members, shape 10, tier named
members: cat, bee, ferret, ficus, fox, marmot, rosebush, snake
frame: AtLocation> outside; AtLocation> wild; AtLocation> park; AtLocation> field; AtLocation> outdoors; AtLocation> canada; AtLocation> nature
density 0.786; support 8 (with Wiktionary 8); nulls global p=0.0099 z=16.0 (null mean 0.0), relation p=0.0099 z=15.9 (null mean 0.05), reciprocal p=0.0099 z=15.9 (null mean 0.05), strict p=0.0099 z=15.8 (null mean 0.09); BH q 0.0159; subsample recovery 1.0
category: best direct animal (0.5), best within 2 IsA-steps animal (0.62), members with any category 0.88
member categories: cat→animal,woman,book,gossip; bee→colony,insect,hive,hymenoptera; ferret→animal,mammal,hunt,wild_animal; ficus→plant,woody_plant,dicot_genus,spatial_thing; fox→animal,mammal,television_station,fur; marmot→animal,squirrel,mammal,rodent; rosebush→–; snake→idaho,oregon,washington,wyoming
internal links among members 0 (configuration expectation 0.72); relative weight of member–frame links {'original': 1.073, 'wiki_half0': 1.032, 'wiki_half1': 1.074}
WikiText (obs/exp): wiki_half0 member–frame 71/154.5, member–member 10/6.7; wiki_half1 member–frame 45/150.2, member–member 6/6.6


## Hard to name: partial category (33–50%, or ≥50% only at 2 IsA-steps), or members mostly uncategorised

### group 7 — 36 members, shape 10, tier partly_named
members: accordion, acoustic_guitar, balalaika, banjo, bass_baritone, bass_clarinet, bass_drum, bass_fiddle, bassoon, clarinet, cornet, double_bass, drum, fiddle, flute, gong, guitar, harpsichord, instrument, instrument_triangle, keyboard_instrument, mandolin, music_stand, musical_instrument …
frame: AtLocation> band; AtLocation> orchestra; UsedFor> making_music
density 0.824; support 36 (with Wiktionary 36); nulls global p=0.0099 z=72.0 (null mean 0.02), relation p=0.0099 z=29.8 (null mean 1.42), reciprocal p=0.0099 z=28.0 (null mean 1.65), strict p=0.0099 z=25.7 (null mean 2.27); BH q 0.0159; subsample recovery 0.6
category: best direct stringed_instrument (0.17), best within 2 IsA-steps device (0.72), members with any category 0.97
member categories: accordion→instrument,keyboard_instrument,musical_instrument,man_made_object; acoustic_guitar→guitar,acoustic_instrument,larger_than_violin; balalaika→stringed_instrument,chordophone,stringed_music_instrument; banjo→musical_instrument,stringed_instrument,string_instrument,acoustic_instrument; bass_baritone→–; bass_clarinet→clarinet,reed_instrument; bass_drum→drum,instrument,musical_instrument,percussion_instrument; bass_fiddle→bass,instrument,stringed_instrument,bowed_stringed_instrument; bassoon→musical_instrument,wind_instrument,woodwind,woodwind_instrument; clarinet→instrument,musical_instrument,woodwind_instrument,horn_musical_instrument
internal links among members 53 (configuration expectation 0.84); relative weight of member–frame links {'original': 1.185, 'wiki_half0': 1.131, 'wiki_half1': 1.12}
WikiText (obs/exp): wiki_half0 member–frame 499/123.7, member–member 599/22.1; wiki_half1 member–frame 350/114.8, member–member 611/20.4

### group 2 — 59 members, shape 28, tier uncategorised
members: car, surprising, climbing, swimming_pool, playroom, canoe, discothque, singing, swimming, diving, playing_hockey, playing_sports, riding_bike, tickling, watching_movie, learning_new, becoming_inebriated, celebrating, getting_exercise, creating_art, dreaming, driving_car, enjoying_film, entertaining_people …
frame: UsedFor> fun; UsedFor> having_fun
density 1.0; support 59 (with Wiktionary 59); nulls global p=0.0099 z=117.8 (null mean 0.08), relation p=0.0099 z=16.3 (null mean 9.98), reciprocal p=0.0099 z=17.0 (null mean 9.95), strict p=0.0099 z=13.6 (null mean 18.1); BH q 0.0159; subsample recovery 1.0
category: best direct intelligent_agent_activity (0.19), best within 2 IsA-steps action (0.27), members with any category 0.49
member categories: car→artifact,vehicle,train,elevator; surprising→–; climbing→performing,locomotion,recreational_activity; swimming_pool→pond,pool,artificial_pond,lido; playroom→where_children_play; canoe→vehicle,boat,ship,user_powered_device; discothque→–; singing→activity,performance,musical_performance,making_music; swimming→sport,another_activity,good_exercise,locomotion; diving→match,sport,simple_whole_body_movement,olympic_sport
internal links among members 26 (configuration expectation 18.1); relative weight of member–frame links {'original': 1.181, 'wiki_half0': 1.192, 'wiki_half1': 1.179}
WikiText (obs/exp): wiki_half0 member–frame 15/13.4, member–member 119/35.6; wiki_half1 member–frame 21/13.6, member–member 93/33.4

### group 1 — 53 members, shape 14, tier partly_named
members: rich, bill, chase, john, milan, andrew, bob, charles, chris, harry, henry, jeff, jim, joe, larry, mary, mike, robert, terry, tim, jill, gene, bobby, brent …
frame: Desires> sex; HasA> kids; HasProperty> nuts
density 0.943; support 53 (with Wiktionary 53); nulls global p=0.0099 z=106.0 (null mean 0.0), relation p=0.0099 z=50.4 (null mean 1.59), reciprocal p=0.0099 z=43.1 (null mean 1.37), strict p=0.0099 z=10.8 (null mean 24.47); BH q 0.0159; subsample recovery 1.0
category: best direct washing_car (0.45), best within 2 IsA-steps washing_car (0.45), members with any category 0.83
member categories: rich→name_for_male,not_at_work; bill→list,paper_money,money,statement; chase→cut,bank,frame,washing_car; john→person,student,college_student,crying; milan→lombardy,in_italy; andrew→person,goof,in_fourth_grade; bob→dog,person,dress,move; charles→person,massachusetts,standing_up; chris→violinist,welder,programmer,given_name; harry→destroy,washing_car,given_name,moving_quickly
internal links among members 0 (configuration expectation 0.26); relative weight of member–frame links {'original': 0.917, 'wiki_half0': 0.918, 'wiki_half1': 0.93}
WikiText (obs/exp): wiki_half0 member–frame 132/216.4, member–member 6635/3781.8; wiki_half1 member–frame 108/227.3, member–member 6328/3796.2

### group 185 — 13 members, shape 40, tier uncategorised
members: log_on, use_computer, dial_up, turn_computer_on, turn_on_computer, connect_to_internet, buy_computer, have_computer, get_computer, have_modem, log_on_to_computer, go_on_line, launch_web_browser
frame: HasPrerequisite< go_on_internet; HasPrerequisite< surf_net; HasPrerequisite< get_onto_web
density 0.821; support 13 (with Wiktionary 13); nulls global p=0.0099 z=22.6 (null mean 0.37), relation p=0.0099 z=21.5 (null mean 0.35), reciprocal p=0.0099 z=20.6 (null mean 0.38), strict p=0.0099 z=25.7 (null mean 0.14); BH q 0.0159; subsample recovery 0.6
category: best direct 0 (0.0), best within 2 IsA-steps 0 (0.0), members with any category 0.0
member categories: log_on→–; use_computer→–; dial_up→–; turn_computer_on→–; turn_on_computer→–; connect_to_internet→–; buy_computer→–; have_computer→–; get_computer→–; have_modem→–
internal links among members 3 (configuration expectation 0.01); relative weight of member–frame links {'original': 1.161, 'wiki_half0': 1.161, 'wiki_half1': 1.161}
WikiText (obs/exp): wiki_half0 member–frame 0/0.0, member–member 0/0.0; wiki_half1 member–frame 0/0.0, member–member 0/0.0

### group 73 — 19 members, shape 33, tier uncategorised
members: buy, shop, spend_money, buy_house, buy_food, buy_hamburger, buy_small, buy_products, purchase_cellular_phone, buy_for_loved_one, buy_beer, buy_presents_for_others, buy_fresh_fruits_and_vegetables, go_to_market, go_to_restaurant, grocery_shop, buy_presents, christmas_shop, holiday_shop
frame: HasPrerequisite> get_money; HasPrerequisite> go_to_store; HasPrerequisite> have_money
density 0.825; support 19 (with Wiktionary 19); nulls global p=0.0099 z=38.0 (null mean 0.0), relation p=0.0099 z=13.6 (null mean 1.77), reciprocal p=0.0099 z=13.7 (null mean 2.01), strict p=0.0099 z=12.8 (null mean 1.82); BH q 0.0159; subsample recovery 0.8
category: best direct be (0.05), best within 2 IsA-steps get (0.11), members with any category 0.11
member categories: buy→be,get,believe; shop→search,obtain,service_organization,mercantile_establishment; spend_money→–; buy_house→–; buy_food→–; buy_hamburger→–; buy_small→–; buy_products→–; purchase_cellular_phone→–; buy_for_loved_one→–
internal links among members 21 (configuration expectation 1.68); relative weight of member–frame links {'original': 1.205, 'wiki_half0': 1.206, 'wiki_half1': 1.206}
WikiText (obs/exp): wiki_half0 member–frame 1/0.0, member–member 5/0.7; wiki_half1 member–frame 0/0.0, member–member 1/0.6

### group 126 — 11 members, shape 40, tier uncategorised
members: go_to_concert, buy_ticket, open_eyes, go_to_theater, go_to_theatre, buy_tickets, buy_tickets_to_concert, buy_ticket_to_concert, go_to_club, buy_concert_ticket, attend_concert
frame: HasPrerequisite< watch_musician_perform; HasPrerequisite< see_band
density 1.0; support 11 (with Wiktionary 11); nulls global p=0.0099 z=21.9 (null mean 0.05), relation p=0.0099 z=21.8 (null mean 0.12), reciprocal p=0.0099 z=21.7 (null mean 0.13), strict p=0.0099 z=21.9 (null mean 0.07); BH q 0.0159; subsample recovery 1.0
category: best direct 0 (0.0), best within 2 IsA-steps 0 (0.0), members with any category 0.0
member categories: go_to_concert→–; buy_ticket→–; open_eyes→–; go_to_theater→–; go_to_theatre→–; buy_tickets→–; buy_tickets_to_concert→–; buy_ticket_to_concert→–; go_to_club→–; buy_concert_ticket→–
internal links among members 1 (configuration expectation 0.01); relative weight of member–frame links {'original': 1.182, 'wiki_half0': 1.182, 'wiki_half1': 1.182}
WikiText (obs/exp): wiki_half0 member–frame 0/0.0, member–member 0/0.0; wiki_half1 member–frame 0/0.0, member–member 0/0.0

### group 131 — 11 members, shape 40, tier uncategorised
members: eat, cook, cook_food, prepare_food, order_food, buy_food, hungry, get_food, go_to_restaurant, find_restaurant, go_to_cafeteria
frame: HasPrerequisite< have_lunch; HasPrerequisite< eat_lunch
density 1.0; support 11 (with Wiktionary 11); nulls global p=0.0099 z=21.8 (null mean 0.09), relation p=0.0099 z=21.7 (null mean 0.16), reciprocal p=0.0099 z=21.8 (null mean 0.12), strict p=0.0099 z=21.7 (null mean 0.17); BH q 0.0159; subsample recovery 0.8
category: best direct change (0.09), best within 2 IsA-steps action (0.09), members with any category 0.18
member categories: eat→worry; cook→change,concoct,skilled_worker,food_because_tastes_better; cook_food→–; prepare_food→–; order_food→–; buy_food→–; hungry→–; get_food→–; go_to_restaurant→–; find_restaurant→–
internal links among members 13 (configuration expectation 0.32); relative weight of member–frame links {'original': 1.118, 'wiki_half0': 1.119, 'wiki_half1': 1.119}
WikiText (obs/exp): wiki_half0 member–frame 0/0.0, member–member 6/0.8; wiki_half1 member–frame 0/0.0, member–member 3/1.0

### group 65 — 12 members, shape 33, tier uncategorised
members: watch_movie, fly_in_airplane, go_to_movie, attend_classical_concert, go_see_play, see_favorite_show, enjoy_film, go_to_opera, watch_musician_perform, go_to_sporting_event, see_particular_program, see_band
frame: HasPrerequisite> buy_ticket; HasPrerequisite> buy_tickets
density 1.0; support 12 (with Wiktionary 12); nulls global p=0.0099 z=24.0 (null mean 0.0), relation p=0.0099 z=22.0 (null mean 0.33), reciprocal p=0.0099 z=19.3 (null mean 0.34), strict p=0.0099 z=20.6 (null mean 0.33); BH q 0.0159; subsample recovery 1.0
category: best direct 0 (0.0), best within 2 IsA-steps 0 (0.0), members with any category 0.0
member categories: watch_movie→–; fly_in_airplane→–; go_to_movie→–; attend_classical_concert→–; go_see_play→–; see_favorite_show→–; enjoy_film→–; go_to_opera→–; watch_musician_perform→–; go_to_sporting_event→–
internal links among members 1 (configuration expectation 0.37); relative weight of member–frame links {'original': 1.335, 'wiki_half0': 1.335, 'wiki_half1': 1.335}
WikiText (obs/exp): wiki_half0 member–frame 0/0.0, member–member 0/0.0; wiki_half1 member–frame 0/0.0, member–member 0/0.0

### group 1985 — 12 members, shape 9, tier partly_named
members: flat, building, war, school, theater, bus_stop, mall, bookstore, apartment, hospital, hotel, buildings
frame: AtLocation> city; AtLocation> town; AtLocation< people; AtLocation< bathroom
density 0.812; support 12 (with Wiktionary 12); nulls global p=0.0099 z=23.9 (null mean 0.03), relation p=0.0099 z=23.5 (null mean 0.23), reciprocal p=0.0099 z=23.6 (null mean 0.19), strict p=0.0099 z=18.6 (null mean 0.43); BH q 0.0159; subsample recovery 0.6
category: best direct organization (0.17), best within 2 IsA-steps real_estate (0.67), members with any category 1.0
member categories: flat→box,plain,house,scenery; building→creation,real_estate,becoming,condominium; war→hostility,hell,collective,violence; school→body,organization,building,place; theater→building,public_place,large_building,playing_game; bus_stop→stop,port,bus_route,outdoor_location; mall→building,place_for_shopping; bookstore→shop,retail_store,facility,good_place_to_steal_books; apartment→building,accomodation,apartment_building,film; hospital→organization,building,large_building,medical_building
internal links among members 11 (configuration expectation 1.52); relative weight of member–frame links {'original': 1.187, 'wiki_half0': 0.791, 'wiki_half1': 0.877}
WikiText (obs/exp): wiki_half0 member–frame 1623/2205.4, member–member 984/906.6; wiki_half1 member–frame 1622/2180.0, member–member 1001/900.4

### group 111 — 11 members, shape 26, tier uncategorised
members: reading, reading_magazine, reading_book, attending_meeting, communicating, finding_information, traveling, seeing_new, hearing_news, meeting_interesting_people, taking_course
frame: Causes> learning; UsedFor> learning_new_things
density 1.0; support 11 (with Wiktionary 11); nulls global p=0.0099 z=22.0 (null mean 0.0), relation p=0.0099 z=19.5 (null mean 0.28), reciprocal p=0.0099 z=21.4 (null mean 0.28), strict p=0.0099 z=19.7 (null mean 0.44); BH q 0.0159; subsample recovery 0.8
category: best direct action (0.09), best within 2 IsA-steps action (0.18), members with any category 0.45
member categories: reading→activity,england,berkshire,datum; reading_magazine→–; reading_book→form_of_entertainment; attending_meeting→–; communicating→social_event,physical_event; finding_information→–; traveling→action,major_human_industry; seeing_new→–; hearing_news→–; meeting_interesting_people→–
internal links among members 3 (configuration expectation 0.76); relative weight of member–frame links {'original': 1.113, 'wiki_half0': 1.084, 'wiki_half1': 1.084}
WikiText (obs/exp): wiki_half0 member–frame 9/4.0, member–member 1/2.3; wiki_half1 member–frame 13/3.9, member–member 0/2.2

### group 55 — 13 members, shape 28, tier partly_named
members: home, apartment_building, town, brick_row_house, brownstone, bungalow, condominium, cottage, ranch_house, rented_apartment, row_house, terraced_house, townhouse
frame: UsedFor> living_in; UsedFor> live_in
density 1.0; support 13 (with Wiktionary 13); nulls global p=0.0099 z=26.0 (null mean 0.0), relation p=0.0099 z=25.5 (null mean 0.24), reciprocal p=0.0099 z=25.5 (null mean 0.24), strict p=0.0099 z=16.0 (null mean 0.76); BH q 0.0159; subsample recovery 0.8
category: best direct house (0.46), best within 2 IsA-steps building (0.69), members with any category 0.92
member categories: home→beginning,house,castle,residence; apartment_building→building,modern_residence; town→city,community,place,settlement; brick_row_house→often_in_clusters_of_five; brownstone→home,real_estate,row_house,sandstone; bungalow→building,house,one_storeyed_house,small_house_or_home; condominium→home,dwelling,housing,where_people_live; cottage→home,house,small_home,small_house; ranch_house→house,where_farmers_live,where_rancher_lives; rented_apartment→–
internal links among members 12 (configuration expectation 0.35); relative weight of member–frame links {'original': 1.281, 'wiki_half0': 1.234, 'wiki_half1': 1.204}
WikiText (obs/exp): wiki_half0 member–frame 58/51.7, member–member 138/104.6; wiki_half1 member–frame 71/51.9, member–member 184/118.4

### group 30 — 19 members, shape 26, tier uncategorised
members: sitting_on_chair, sleeping, flying_kite, listening_to_music, planning_vacation, playing_games, playing_violin, watching_movie, going_to_sleep, hearing_music, breathing_fresh_air, buying_beer, cooling_off, going_fishing, taking_walk, playing, resting, soaking_in_hotspring, staying_in_bed
frame: Causes> relaxation; UsedFor> relaxing
density 1.0; support 19 (with Wiktionary 19); nulls global p=0.0099 z=38.0 (null mean 0.02), relation p=0.0099 z=13.6 (null mean 1.74), reciprocal p=0.0099 z=12.5 (null mean 1.92), strict p=0.0099 z=10.3 (null mean 3.03); BH q 0.0159; subsample recovery 1.0
category: best direct intelligent_agent_activity (0.11), best within 2 IsA-steps intelligent_agent_activity (0.21), members with any category 0.47
member categories: sitting_on_chair→–; sleeping→sleep,bodily_process,involuntary_bodily_function,most_often; flying_kite→–; listening_to_music→listening,human_activity,form_of_entertainment,common_activity; planning_vacation→–; playing_games→activity,way_to_waste_time; playing_violin→playing,intelligent_agent_activity,playing_stringed_instrument; watching_movie→recreational_activity,entertainment_event_watching; going_to_sleep→becoming,action_performed_by_animals; hearing_music→–
internal links among members 9 (configuration expectation 1.69); relative weight of member–frame links {'original': 1.195, 'wiki_half0': 1.207, 'wiki_half1': 1.206}
WikiText (obs/exp): wiki_half0 member–frame 2/0.8, member–member 14/2.9; wiki_half1 member–frame 2/0.9, member–member 7/2.9


## Coherent but resisting: members are categorised, but no category within 2 steps covers ≥33%

### group 0 — 63 members, shape 10, tier crosscutting
members: flat, stranger, war, school, theater, bank, bookshop, bus_stop, mall, sporting_goods_store, church, grocery_store, pub, cafe, post_office, bookstore, market, hospital, court, movie_theater, parking_lot, avenue, back_garden, dentist …
frame: AtLocation> city; AtLocation> town
density 1.0; support 63 (with Wiktionary 63); nulls global p=0.0099 z=82.9 (null mean 0.55), relation p=0.0099 z=21.2 (null mean 9.67), reciprocal p=0.0099 z=21.2 (null mean 9.14), strict p=0.0099 z=21.2 (null mean 8.16); BH q 0.0159; subsample recovery 1.0
category: best direct building (0.14), best within 2 IsA-steps building (0.32), members with any category 0.86
member categories: flat→box,plain,house,scenery; stranger→person,book,being,intruder; war→hostility,hell,collective,violence; school→body,organization,building,place; theater→building,public_place,large_building,playing_game; bank→reserve,array,cover,depository; bookshop→shop,fun_place_to_spend_time; bus_stop→stop,port,bus_route,outdoor_location; mall→building,place_for_shopping; sporting_goods_store→retail_store
internal links among members 36 (configuration expectation 8.91); relative weight of member–frame links {'original': 1.121, 'wiki_half0': 0.934, 'wiki_half1': 0.948}
WikiText (obs/exp): wiki_half0 member–frame 2366/2236.5, member–member 2371/2539.7; wiki_half1 member–frame 2468/2260.5, member–member 2574/2549.6

### group 3 — 47 members, shape 28, tier crosscutting
members: writing, thinking, movie, playroom, baseball_stadium, dancing, vacation, performance, kite, marijuana, singing, playing_hockey, playing_sports, playing_violin, riding_bike, skiing, becoming_scuba_diver, climbing_mountain, creating_art, driving_car, enjoying_film, fencing, getting_onto_web, going_outside_for_evening …
frame: UsedFor> entertainment; UsedFor> fun
density 1.0; support 47 (with Wiktionary 47); nulls global p=0.0099 z=93.7 (null mean 0.14), relation p=0.0099 z=12.3 (null mean 11.49), reciprocal p=0.0099 z=11.6 (null mean 10.72), strict p=0.0099 z=8.7 (null mean 17.1); BH q 0.0159; subsample recovery 1.0
category: best direct intelligent_agent_activity (0.23), best within 2 IsA-steps intelligent_agent_activity (0.3), members with any category 0.6
member categories: writing→activity,skill,oeuvre,human_activity; thinking→reading,being_human,higher_cognitive_process,intentional_mental_event; movie→show,product,video,conceptual_work; playroom→where_children_play; baseball_stadium→stadium,tangible_thing; dancing→motion,rhythmic_movement,diversion,pastime; vacation→trip,leisure,spend,abrogation; performance→action,show,presentation,accomplishment; kite→check,increase,hawk,word; marijuana→drug,drugs,plant_kingdom,medicine
internal links among members 21 (configuration expectation 12.8); relative weight of member–frame links {'original': 1.103, 'wiki_half0': 1.075, 'wiki_half1': 1.067}
WikiText (obs/exp): wiki_half0 member–frame 426/161.2, member–member 573/382.6; wiki_half1 member–frame 443/169.5, member–member 573/370.8

### group 9 — 27 members, shape 10, tier crosscutting
members: human, show, play, seat, movie, backdrop, balcony, balcony_railing, balcony_seat, seats, candy, catwalk, chairs, ticket_booth, costumes, curtain, curtains, makeup, movie_theater_seat, orchestra_seat, rehearsing_room, rows_of_seats, theater_box, stage_entrance …
frame: AtLocation> theater; AtLocation> theatre
density 1.0; support 27 (with Wiktionary 27); nulls global p=0.0099 z=54.0 (null mean 0.01), relation p=0.0099 z=16.5 (null mean 2.95), reciprocal p=0.0099 z=14.0 (null mean 3.21), strict p=0.0099 z=23.7 (null mean 1.68); BH q 0.0159; subsample recovery 1.0
category: best direct person (0.07), best within 2 IsA-steps artifact (0.15), members with any category 0.7
member categories: human→person,nature,ecology,primate; show→appear,entertainment,race,social_event; play→action,compete,move,show; seat→accommodate,chair,center,support; movie→show,product,video,conceptual_work; backdrop→curtain,scenery; balcony→artwork,structure,level_of_construction,fixed_structure_platform; balcony_railing→–; balcony_seat→above_other_seats; seats→baseball_stadium,in_cars
internal links among members 25 (configuration expectation 2.04); relative weight of member–frame links {'original': 1.114, 'wiki_half0': 1.024, 'wiki_half1': 1.025}
WikiText (obs/exp): wiki_half0 member–frame 500/203.6, member–member 438/638.7; wiki_half1 member–frame 396/193.8, member–member 439/626.4

### group 5 — 43 members, shape 10, tier crosscutting
members: chair, clutter, feet, desk_drawer, printer, carpet, trash_can, lamp, mouse, cup_of_coffee, calculator, calendar_pad, card_case, telephone, chairs, clip, clock, correction_fluid, desk_tray, notebook, electric_pencil_sharpener, glue_stick, highlighter, highlighter_pen …
frame: AtLocation> desk; AtLocation> office
density 1.0; support 43 (with Wiktionary 43); nulls global p=0.0099 z=85.9 (null mean 0.07), relation p=0.0099 z=8.4 (null mean 13.98), reciprocal p=0.0099 z=8.9 (null mean 13.4), strict p=0.0099 z=16.1 (null mean 5.74); BH q 0.0159; subsample recovery 1.0
category: best direct machine (0.09), best within 2 IsA-steps device (0.28), members with any category 0.79
member categories: chair→head,place,seat,funiture; clutter→fill,software,noise,mess; feet→–; desk_drawer→drawer,opaque_thing; printer→machine,device,peripheral,skilled_worker; carpet→cover,luxury,natural_object,household_furnishings; trash_can→garbage_container; lamp→electrical_device,furniture,source_of_illumination; mouse→animal,person,mammal,computer; cup_of_coffee→pleasant_way_to_relax
internal links among members 23 (configuration expectation 1.71); relative weight of member–frame links {'original': 1.211, 'wiki_half0': 1.189, 'wiki_half1': 1.216}
WikiText (obs/exp): wiki_half0 member–frame 74/91.1, member–member 67/63.3; wiki_half1 member–frame 56/94.0, member–member 71/65.2

### group 10 — 26 members, shape 10, tier crosscutting
members: dollar, return_ticket, pen, wallet, comb, car_keys, cash_coin, coin_purse, change, checkbook_holder, cheque_book_holder, condom, credit_card_wallet, dollar_bill, eyeglasses_case, glasses_case, key, key_case, keys, kleenex, lint, movie_ticket, penny, subway_pass …
frame: AtLocation> purse; AtLocation> pocket
density 1.0; support 26 (with Wiktionary 26); nulls global p=0.0099 z=52.0 (null mean 0.02), relation p=0.0099 z=12.8 (null mean 4.2), reciprocal p=0.0099 z=12.4 (null mean 3.67), strict p=0.0099 z=19.8 (null mean 1.81); BH q 0.0159; subsample recovery 1.0
category: best direct coin (0.12), best within 2 IsA-steps artifact (0.19), members with any category 0.69
member categories: dollar→money,currency,bill,coin; return_ticket→–; pen→enclosure,object,writing_instrument,swan; wallet→case,software,gear,transport_container; comb→groom,straighten,plate,tool; car_keys→–; cash_coin→always_less_dollar; coin_purse→small_bag_in,small_purse; change→action,dress,money,cash; checkbook_holder→–
internal links among members 15 (configuration expectation 1.02); relative weight of member–frame links {'original': 1.211, 'wiki_half0': 1.26, 'wiki_half1': 1.231}
WikiText (obs/exp): wiki_half0 member–frame 9/6.0, member–member 61/48.9; wiki_half1 member–frame 11/7.2, member–member 57/42.6

### group 164 — 12 members, shape 28, tier crosscutting
members: tennis_game, riding_bicycle, playing_hockey, playing_sports, riding_bike, climbing_mountain, driving_car, playing_sport, playing_basketball, playing_lacrosse, playing_soccer, running_twenty_six_miles
frame: Causes> getting_tired; UsedFor> competition; UsedFor> exercise; UsedFor> sport
density 0.833; support 12 (with Wiktionary 12); nulls global p=0.0099 z=24.0 (null mean 0.0), relation p=0.0099 z=23.9 (null mean 0.03), reciprocal p=0.0099 z=23.8 (null mean 0.09), strict p=0.0099 z=23.7 (null mean 0.14); BH q 0.0159; subsample recovery 0.6
category: best direct playing_game (0.25), best within 2 IsA-steps action (0.25), members with any category 0.75
member categories: tennis_game→good_exercise; riding_bicycle→form_of_exercise; playing_hockey→playing_game,intelligent_agent_activity,playing_of_sports_event; playing_sports→about_competition,fun_and_good_exercise; riding_bike→good_way_to_exercise,fun_sort_of_exercise,good_exerise,good_source_of_exercise; climbing_mountain→dangerous_activity; driving_car→dangerous_activity,privilege_not_right; playing_sport→–; playing_basketball→event,playing_game,form_of_exercise,intelligent_agent_activity; playing_lacrosse→playing_game,intelligent_agent_activity,playing_of_sports_event
internal links among members 1 (configuration expectation 0.78); relative weight of member–frame links {'original': 1.118, 'wiki_half0': 1.129, 'wiki_half1': 1.129}
WikiText (obs/exp): wiki_half0 member–frame 2/0.3, member–member 1/0.0; wiki_half1 member–frame 2/0.4, member–member 0/0.0


## Earlier groups 18–20, located

### group 1439 — 62 members, shape 28, tier uncategorised
members: show, writing, climbing, reading, playroom, singing, swimming, diving, playing_hockey, playing_sports, playing_violin, reading_book, riding_bike, skiing, becoming_inebriated, becoming_scuba_diver, getting_exercise, creating_art, doing_crossword_puzzle, driving_car, enjoying_film, fencing, going_for_drive, going_for_walk …
frame: UsedFor> enjoyment; UsedFor> entertainment; UsedFor> fun; UsedFor> relaxation; UsedFor> having_fun
density 0.677; support 62 (with Wiktionary 62); nulls global p=0.0099 z=124.0 (null mean 0.01), relation p=0.0099 z=30.5 (null mean 4.93), reciprocal p=0.0099 z=31.0 (null mean 4.79), strict p=0.0099 z=17.8 (null mean 13.94); BH q 0.0159; subsample recovery 0.2
category: best direct intelligent_agent_activity (0.26), best within 2 IsA-steps action (0.29), members with any category 0.47
member categories: show→appear,entertainment,race,social_event; writing→activity,skill,oeuvre,human_activity; climbing→performing,locomotion,recreational_activity; reading→activity,england,berkshire,datum; playroom→where_children_play; singing→activity,performance,musical_performance,making_music; swimming→sport,another_activity,good_exercise,locomotion; diving→match,sport,simple_whole_body_movement,olympic_sport; playing_hockey→playing_game,intelligent_agent_activity,playing_of_sports_event; playing_sports→about_competition,fun_and_good_exercise
internal links among members 24 (configuration expectation 21.98); relative weight of member–frame links {'original': 1.117, 'wiki_half0': 1.12, 'wiki_half1': 1.113}
WikiText (obs/exp): wiki_half0 member–frame 464/198.3, member–member 647/457.4; wiki_half1 member–frame 491/203.9, member–member 510/427.9

### group 2 — 59 members, shape 28, tier uncategorised
members: car, surprising, climbing, swimming_pool, playroom, canoe, discothque, singing, swimming, diving, playing_hockey, playing_sports, riding_bike, tickling, watching_movie, learning_new, becoming_inebriated, celebrating, getting_exercise, creating_art, dreaming, driving_car, enjoying_film, entertaining_people …
frame: UsedFor> fun; UsedFor> having_fun
density 1.0; support 59 (with Wiktionary 59); nulls global p=0.0099 z=117.8 (null mean 0.08), relation p=0.0099 z=16.3 (null mean 9.98), reciprocal p=0.0099 z=17.0 (null mean 9.95), strict p=0.0099 z=13.6 (null mean 18.1); BH q 0.0159; subsample recovery 1.0
category: best direct intelligent_agent_activity (0.19), best within 2 IsA-steps action (0.27), members with any category 0.49
member categories: car→artifact,vehicle,train,elevator; surprising→–; climbing→performing,locomotion,recreational_activity; swimming_pool→pond,pool,artificial_pond,lido; playroom→where_children_play; canoe→vehicle,boat,ship,user_powered_device; discothque→–; singing→activity,performance,musical_performance,making_music; swimming→sport,another_activity,good_exercise,locomotion; diving→match,sport,simple_whole_body_movement,olympic_sport
internal links among members 26 (configuration expectation 18.1); relative weight of member–frame links {'original': 1.181, 'wiki_half0': 1.192, 'wiki_half1': 1.179}
WikiText (obs/exp): wiki_half0 member–frame 15/13.4, member–member 119/35.6; wiki_half1 member–frame 21/13.6, member–member 93/33.4

### group 1439 — 62 members, shape 28, tier uncategorised
members: show, writing, climbing, reading, playroom, singing, swimming, diving, playing_hockey, playing_sports, playing_violin, reading_book, riding_bike, skiing, becoming_inebriated, becoming_scuba_diver, getting_exercise, creating_art, doing_crossword_puzzle, driving_car, enjoying_film, fencing, going_for_drive, going_for_walk …
frame: UsedFor> enjoyment; UsedFor> entertainment; UsedFor> fun; UsedFor> relaxation; UsedFor> having_fun
density 0.677; support 62 (with Wiktionary 62); nulls global p=0.0099 z=124.0 (null mean 0.01), relation p=0.0099 z=30.5 (null mean 4.93), reciprocal p=0.0099 z=31.0 (null mean 4.79), strict p=0.0099 z=17.8 (null mean 13.94); BH q 0.0159; subsample recovery 0.2
category: best direct intelligent_agent_activity (0.26), best within 2 IsA-steps action (0.29), members with any category 0.47
member categories: show→appear,entertainment,race,social_event; writing→activity,skill,oeuvre,human_activity; climbing→performing,locomotion,recreational_activity; reading→activity,england,berkshire,datum; playroom→where_children_play; singing→activity,performance,musical_performance,making_music; swimming→sport,another_activity,good_exercise,locomotion; diving→match,sport,simple_whole_body_movement,olympic_sport; playing_hockey→playing_game,intelligent_agent_activity,playing_of_sports_event; playing_sports→about_competition,fun_and_good_exercise
internal links among members 24 (configuration expectation 21.98); relative weight of member–frame links {'original': 1.117, 'wiki_half0': 1.12, 'wiki_half1': 1.113}
WikiText (obs/exp): wiki_half0 member–frame 464/198.3, member–member 647/457.4; wiki_half1 member–frame 491/203.9, member–member 510/427.9

### group 1745 — 57 members, shape 28, tier crosscutting
members: writing, reading, dancing, literature, marijuana, singing, swimming, viola, yoyo, riding_bicycle, drinking, playing_sports, playing_violin, reading_book, skiing, acting_in_play, attending_classical_concert, spending_money, becoming_scuba_diver, cooking_meal, buying, doing_crossword_puzzle, relaxing, driving_car …
frame: UsedFor> enjoyment; UsedFor> pleasure; UsedFor> entertainment
density 0.725; support 57 (with Wiktionary 57); nulls global p=0.0099 z=113.8 (null mean 0.08), relation p=0.0099 z=14.8 (null mean 11.54), reciprocal p=0.0099 z=14.9 (null mean 11.24), strict p=0.0099 z=10.2 (null mean 20.51); BH q 0.0159; subsample recovery 0.2
category: best direct intelligent_agent_activity (0.21), best within 2 IsA-steps intelligent_agent_activity (0.26), members with any category 0.54
member categories: writing→activity,skill,oeuvre,human_activity; reading→activity,england,berkshire,datum; dancing→motion,rhythmic_movement,diversion,pastime; literature→writing,written_text,profession,literary_study; marijuana→drug,drugs,plant_kingdom,medicine; singing→activity,performance,musical_performance,making_music; swimming→sport,another_activity,good_exercise,locomotion; viola→plant,string_quartet,instrument,musical_instrument; yoyo→toy; riding_bicycle→form_of_exercise
internal links among members 36 (configuration expectation 20.16); relative weight of member–frame links {'original': 1.044, 'wiki_half0': 1.039, 'wiki_half1': 1.03}
WikiText (obs/exp): wiki_half0 member–frame 297/99.3, member–member 318/193.7; wiki_half1 member–frame 316/105.0, member–member 274/189.7

### group 5 — 43 members, shape 10, tier crosscutting
members: chair, clutter, feet, desk_drawer, printer, carpet, trash_can, lamp, mouse, cup_of_coffee, calculator, calendar_pad, card_case, telephone, chairs, clip, clock, correction_fluid, desk_tray, notebook, electric_pencil_sharpener, glue_stick, highlighter, highlighter_pen …
frame: AtLocation> desk; AtLocation> office
density 1.0; support 43 (with Wiktionary 43); nulls global p=0.0099 z=85.9 (null mean 0.07), relation p=0.0099 z=8.4 (null mean 13.98), reciprocal p=0.0099 z=8.9 (null mean 13.4), strict p=0.0099 z=16.1 (null mean 5.74); BH q 0.0159; subsample recovery 1.0
category: best direct machine (0.09), best within 2 IsA-steps device (0.28), members with any category 0.79
member categories: chair→head,place,seat,funiture; clutter→fill,software,noise,mess; feet→–; desk_drawer→drawer,opaque_thing; printer→machine,device,peripheral,skilled_worker; carpet→cover,luxury,natural_object,household_furnishings; trash_can→garbage_container; lamp→electrical_device,furniture,source_of_illumination; mouse→animal,person,mammal,computer; cup_of_coffee→pleasant_way_to_relax
internal links among members 23 (configuration expectation 1.71); relative weight of member–frame links {'original': 1.211, 'wiki_half0': 1.189, 'wiki_half1': 1.216}
WikiText (obs/exp): wiki_half0 member–frame 74/91.1, member–member 67/63.3; wiki_half1 member–frame 56/94.0, member–member 71/65.2

### group 56 — 17 members, shape 10, tier crosscutting
members: window, chair, table, fan, carpet, doorway, shelf, beanbag, carpeting, candle, wardrobe, dust, electricity, pillow, hairbrush, on_off_switch, side_chair
frame: AtLocation> bedroom; AtLocation> room
density 1.0; support 17 (with Wiktionary 17); nulls global p=0.0099 z=33.9 (null mean 0.03), relation p=0.0099 z=10.9 (null mean 2.23), reciprocal p=0.0099 z=9.9 (null mean 2.51), strict p=0.0099 z=12.5 (null mean 1.59); BH q 0.0159; subsample recovery 0.8
category: best direct furniture (0.18), best within 2 IsA-steps artifact (0.41), members with any category 0.94
member categories: window→car,opening,portal,building; chair→head,place,seat,funiture; table→array,furniture,platform,piece_of_furniture; fan→person,intensify,follower,shake; carpet→cover,luxury,natural_object,household_furnishings; doorway→wall,entrance,portal,walled_cavity; shelf→support,cabinet,closet,grocery_store; beanbag→bag; carpeting→floor_covering,one_type_of_surface,soft_floor_covering; candle→smoothness,lamp,fuel,examine
internal links among members 9 (configuration expectation 0.93); relative weight of member–frame links {'original': 1.089, 'wiki_half0': 1.012, 'wiki_half1': 1.019}
WikiText (obs/exp): wiki_half0 member–frame 101/28.4, member–member 50/28.8; wiki_half1 member–frame 91/25.6, member–member 50/25.5
