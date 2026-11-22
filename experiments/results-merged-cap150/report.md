# Paraphrase-merged typed groups (cap 150)

Classes with ≥ 2 ideas: 6,621; ideas merged into another: 8,747. Settings: {'arrays': '/home/ubuntu/data/morph/graph-arrays.npz', 'emb': '/home/ubuntu/data/merge/emb-mpnet.npz', 'pairs': '/home/ubuntu/data/merge/nli-pairs.npz', 'out': '/home/ubuntu/data/merge/classes', 'keep': '/home/ubuntu/data/morph/keep-no-wiktionary.npz', 'entail': 0.6, 'contra': 0.5, 'complete': 0.75, 'low_cos': 0.55, 'max_class': 40, 'judge': '/home/ubuntu/data/merge/nli-base.npz', 'judge_entail': 0.8}.

Largest classes by typed degree (evidence = mutual NLI entailment or FormOf):

- person: human, person
- people: people, humans, folks
- water: water, watering
- examining_thing: examining_thing, see_things
- dog: dog, dogs
- read_newspaper: read_newspaper, reading_newspaper
- celebrating: celebrating, celebrate
- thinking: thinking, thought, think
- riding_bike: ride_bicycle, ride_bike, riding_bicycle, riding_bike
- buying: buy, bought, buying, purchase
- learning: learn, learned, learning
- fun: fun, enjoyable
- kill: kill, killing, murder
- having_physical_exam: having_physical_exam, having_physical_examination, have_physical_exam, have_physical_examination
- cabinet: cabinet, cupboard
- exercise: exercise, physical_activity, exercising, physical_exertion
- listening_to_music: hear_music, listening_to_music, hearing_music, enjoying_music, listening_music
- child: child, youngster, little_kid
- play_poker: poker_game, play_poker, playing_poker
- have_party: having_party, have_party
- one_impairment_person_might: one_impairment_person_might, one_impairment_person_might_have
- playing_basketball: play_basketball, playing_basketball
- play_sports: play_sport, play_sports, playing_sports, playing_sport
- painting: paint, painting, paints, painting_things
- using_computer: computer_user, use_computer, using_computer

## Real vs re-mined null graphs (both contracted with the same classes)

| | size_ge_4 | size_ge_6 | size_ge_10 | size_ge_20 | unnamed_ge_6 |
|---|---|---|---|---|---|
| real | 5050 | 2183 | 651 | 94 | 1298 |
| relation | 5584.6 [6158] | 2510.4 [2950] | 970.6 [1187] | 202.2 [257] | 1131.8 [1295] |
| strict | 4745.5 [4945] | 1470.0 [1566] | 207.6 [248] | 7.4 [14] | 888.8 [1001] |
| profile | 4916.4 [5142] | 1866.8 [2034] | 377.0 [421] | 31.6 [44] | 1139.6 [1240] |
| profile2 | 4811.5 [4942] | 1944.8 [2016] | 462.8 [508] | 51.8 [70] | 1111.5 [1175] |

Survive both profile nulls (frame support at floor, reproduced ≤ 5%): 1405; + selection control: 19. By tier: {'survives_profile': {'crosscutting': 335, 'partly_named': 400, 'uncategorised': 503, 'named': 167}, 'survives_selection': {'crosscutting': 8, 'partly_named': 2, 'uncategorised': 9}}

## What happened to previously surviving groups

| prior status | n | still survive selection | survive profile only | found, not significant | gone (no merged group with member Jaccard ≥ 0.3) |
|---|---|---|---|---|---|
| survived selection | 53 | 10 | 29 | 13 | 1 |
| survived profile only | 1306 | 8 | 708 | 428 | 162 |

Previous selection survivors, one line each (prior members → status):

- flat, stranger, war, school, theater, bank … [AtLocation> city; AtLocation> town] → **survives_selection** (members merged away 3; match J=0.97)
- chair, clutter, feet, desk_drawer, printer, carpet … [AtLocation> desk; AtLocation> office] → **survives_profile** (members merged away 2; match J=0.85)
- accordion, acoustic_guitar, balalaika, banjo, bass_baritone, bass_clarinet … [AtLocation> band; AtLocation> orchestra; UsedFor> making_music] → **survives_profile** (members merged away 1; match J=0.78)
- fair, texas, america, it's_natural_habitat, indiana, countryside … [AtLocation< cow; AtLocation< heifer] → **survives_profile** (members merged away 2; match J=0.96)
- go_to_concert, buy_ticket, open_eyes, go_to_theater, go_to_theatre, buy_tickets … [HasPrerequisite< watch_musician_perform; HasPrerequisite< see_band] → **survives_profile** (members merged away 4; match J=0.78)
- eat, cook, cook_food, prepare_food, order_food, buy_food … [HasPrerequisite< have_lunch; HasPrerequisite< eat_lunch] → **found_not_significant** (members merged away 0; match J=0.85)
- home, bar, war, school, theater, bank … [AtLocation> city; AtLocation< human] → **survives_selection** (members merged away 0; match J=0.75)
- log_on, use_computer, dial_up, turn_computer_on, turn_on_computer, connect_to_internet … [HasPrerequisite< go_on_internet; HasPrerequisite< surf_net; HasPrerequisite< get_onto_web] → **survives_selection** (members merged away 2; match J=0.64)
- death, indigestion, gas, nausea, satisfaction, feeling_full … [Causes< eating; Causes< eating_hamburger] → **survives_selection** (members merged away 0; match J=0.75)
- stretch_muscles, put_on_shoes, dress_appropriately, go_to_park, stretch_first, put_on_jogging_clothes … [HasPrerequisite< go_jogging; HasPrerequisite< go_for_jog] → **survives_profile** (members merged away 1; match J=0.31)
- friendly, go_outside, leave_house, socialize, have_party, go_to_party … [HasPrerequisite< meet_people; HasPrerequisite< meet_interesting_people] → **found_not_significant** (members merged away 0; match J=0.90)
- pain, sweat, heart_attack, sweating, sore_feet, shortness_of_breath … [Causes< running; Causes< going_for_jog] → **survives_selection** (members merged away 1; match J=0.57)
- waiter, waitress, wash_hands, get_job, become_waiter, work_in_restaurant … [HasPrerequisite< wait_tables; HasPrerequisite< wait_on_tables] → **survives_profile** (members merged away 3; match J=0.44)
- study, take_course, read_book, go_to_school, buy_book, get_book_on_subject … [HasPrerequisite< learn_new; HasPrerequisite< learn_about_subject] → **survives_profile** (members merged away 1; match J=1.00)
- light, literacy, eyes, vision, ability_to_read, knowing_how_to_read … [HasPrerequisite< reading_letter; HasPrerequisite< reading_newspaper] → **survives_profile** (members merged away 1; match J=0.67)
- wash, take_bath, take_shower, use_soap, take_off_clothes, wash_yourself … [HasPrerequisite< get_clean; HasPrerequisite< become_more_clean] → **survives_profile** (members merged away 1; match J=1.00)
- rent, turn_on_tv, rent_video, get_vcr, have_vcr, turn_on_vcr … [HasPrerequisite< view_video; HasPrerequisite< view_film_at_home] → **survives_profile** (members merged away 2; match J=1.00)
- go_to_beach, take_off_clothes, go_to_swimming_pool, go_to_pool, go_to_lake, put_on_bathing_suit … [HasPrerequisite< swim; HasPrerequisite< go_for_swim] → **survives_profile** (members merged away 1; match J=0.88)
- go_to_cinema, go_to_movie_theater, turn_on_tv, turn_on_television, rent_movie, rent_video … [HasPrerequisite< watch_movie; HasPrerequisite< see_movie; HasPrerequisite< watch_film] → **gone** (members merged away 3; match J=0.25)
- travel, plan_in_advance, decide_where_to_go, decide_where_want_to_go, choose_destination, decide_where_to_go_first … [HasPrerequisite< plan_vacation; HasPrerequisite< go_on_vacation] → **found_not_significant** (members merged away 1; match J=0.38)
- boredom, entertainment, laughter, eye_strain, falling_asleep, wasting_time … [Causes< watching_television; Causes< watching_tv] → **found_not_significant** (members merged away 0; match J=0.36)
- good_health, sweat, exhaustion, sweating, shortness_of_breath, increased_heart_rate … [Causes< running; Causes< jogging] → **found_not_significant** (members merged away 2; match J=0.40)
- start_car, fasten_seatbelt, get_driver's_license, get_keys, get_license, have_driving_license … [HasPrerequisite< drive; HasPrerequisite< drive_car] → **survives_profile** (members merged away 2; match J=0.86)
- soap_and_water, use_water, go_to_bathroom, run_water, turn_on_water, turn_on_warm_water … [HasPrerequisite< have_bath; HasPrerequisite< take_shower] → **found_not_significant** (members merged away 1; match J=0.40)
- careful, strike_match, light_match, go_outdoors, get_matches, gather_kindling … [HasPrerequisite< light_fire; HasPrerequisite< start_fire; HasPrerequisite< start_flame_or_fire] → **survives_profile** (members merged away 1; match J=0.55)
- pay_tuition, go_to_school, apply, enroll, enroll_in_one, enroll_in_school … [HasPrerequisite< take_course; HasPrerequisite< attend_class] → **survives_profile** (members merged away 0; match J=0.78)
- use_computer, connect_to_internet, buy_computer, have_computer, get_isp, log_on_to_internet … [HasPrerequisite< surf_web; HasPrerequisite< get_onto_web] → **survives_selection** (members merged away 0; match J=0.46)
- go_to_movies, make_popcorn, go_to_cinema, go_to_theater, near_tv, rent_movie … [HasPrerequisite< watch_film; HasPrerequisite< enjoy_film] → **survives_selection** (members merged away 1; match J=0.50)
- disrobe, go_to_bathroom, turn_on_water, fill_bathtub_with_water, get_in_bathtub, have_bathtub … [HasPrerequisite< bathe; HasPrerequisite< have_bath] → **survives_profile** (members merged away 0; match J=0.88)
- use_computer, boot_up_computer, connect_to_internet, buy_computer, have_computer, get_computer_modem … [HasPrerequisite< go_on_internet; HasPrerequisite< surf_web] → **survives_selection** (members merged away 0; match J=0.58)
- on_time, register, study, get_out_of_bed, enroll, matriculate … [HasPrerequisite< go_to_school; HasPrerequisite< attend_class] → **survives_profile** (members merged away 1; match J=1.00)
- soldier, join_army, get_weapons, have_enemy_to_fight, join_armed_forces, know_where_enemy … [HasPrerequisite< fight_enemy; HasPrerequisite< fight_war] → **survives_selection** (members merged away 0; match J=0.70)
- use_computer, write_code, turn_on_computer, have_computer, learn_programming_language, know_programming_language … [HasPrerequisite< program; HasPrerequisite< write_program] → **survives_profile** (members merged away 0; match J=1.00)
- use_computer, turn_on_computer, learn_how, learn_programming_language, learn_how_to, learn_computer_language … [HasPrerequisite< program; HasPrerequisite< program_computer] → **survives_profile** (members merged away 1; match J=0.44)
- take_off, use_detergent, get_water, put_in_washer, buy_washing_powder, put_clothes_in_washer … [HasPrerequisite< clean_clothing; HasPrerequisite< wash_clothes] → **survives_profile** (members merged away 0; match J=0.75)
- save_money, go_to_store, have_money, go_to_mall, go_to_shop, have_enough_money … [HasPrerequisite< buy_small; HasPrerequisite< purchase_cellular_phone; HasPrerequisite< buy_presents] → **found_not_significant** (members merged away 1; match J=0.56)
- rest, rest_feet, tired, legs_tired, rest_legs … [MotivatedByGoal< sit_down; MotivatedByGoal< sit_on_chair] → **survives_profile** (members merged away 0; match J=0.80)
- success, failure, stress, anxiety, headaches, passing_course … [Causes< taking_exam; Causes< taking_final_exams; Causes< taking_finals] → **survives_profile** (members merged away 0; match J=0.55)
- knowledge, learn, entertainment, learning, eye_strain, drowsiness … [Causes< reading; Causes< reading_magazine; Causes< reading_book] → **survives_profile** (members merged away 1; match J=0.50)
- go_to_movie, go_to_movies, go_to_cinema, go_to_movie_theater, go_to_theatre, rent_movie … [HasPrerequisite< watch_film; HasPrerequisite< take_in_film; HasPrerequisite< go_see_film] → **survives_profile** (members merged away 2; match J=0.50)
- appreciation, inspiration, enjoyment, education, learning, wonder … [Causes< seeing_exhibits; Causes< visiting_museum; UsedFor< seeing_art] → **survives_profile** (members merged away 0; match J=0.78)
- happy, gratitude, happiness, pleasure, thank, spend_money … [Causes< giving_gift; Causes< buying_for_loved_one; Causes< buying_presents_for_others] → **found_not_significant** (members merged away 0; match J=0.88)
- getting_fat, physically_fit, get_in_shape, stay_fit, loose_weight … [MotivatedByGoal< exercise; MotivatedByGoal< do_exercises] → **survives_selection** (members merged away 0; match J=0.57)
- hear_music, watch_television, watch_television_show, see_story, use_television, see_people_play_game … [CausesDesire< boredom; HasPrerequisite> turn_on; HasPrerequisite> turn_on_tv] → **found_not_significant** (members merged away 0; match J=0.38)
- anger, boredom, impatience, frustration, get_tired, getting_bored … [Causes< standing_in_line; Causes< standing_in_queue; Causes< waiting_on_line] → **survives_profile** (members merged away 0; match J=0.60)
- outside, country, a, canada, movies, detroit … [AtLocation< horse; AtLocation< apple_tree; AtLocation< heifer] → **found_not_significant** (members merged away 2; match J=0.50)
- look_different, have_shorter_hair, look_neater, new_hairstyle, shorter_hair … [Causes< cutting_hair; MotivatedByGoal< cut_hair] → **survives_profile** (members merged away 1; match J=0.43)
- open_book, take_course, read_book, read_books, go_to_school, go_to_library … [HasPrerequisite< study; HasPrerequisite< study_for_subject; HasPrerequisite< learn_about_subject] → **survives_profile** (members merged away 1; match J=0.57)
- anger, fights, pull_muscle, injuries, fatigue, becoming_tired … [Causes< getting_physical_activity; Causes< playing_soccer; Causes< playing_tennis] → **found_not_significant** (members merged away 0; match J=0.33)
- weight_loss, injury, exhaustion, heart_attack, injuries, tiredness … [Causes< running; Causes< getting_exercise; Causes< running_in_marathon] → **found_not_significant** (members merged away 1; match J=0.46)
- train, play_sport, lift_weights, work_out, stand_up, excersise … [HasPrerequisite< get_fit; HasPrerequisite< get_exercise; HasPrerequisite< get_physical_activity] → **survives_profile** (members merged away 0; match J=0.38)
- performance, singing, acting_in_play, performing … [Causes< going_on_stage; UsedFor> entertainment] → **survives_profile** (members merged away 0; match J=1.00)
- fly_kite, tie_shoes, flying_kite, tie_knot … [CapableOf< child; UsedFor< string] → **found_not_significant** (members merged away 1; match J=0.33)

## Merged groups surviving the selection control (19)

By relation types in frame: {1: 15, 2: 3, 3: 1}; by independent anchor neighbourhoods: {1: 17, 2: 1, 3: 1}

### ≥ 2 relation types and ≥ 2 independent neighbourhoods (1)

- **m1638** n=7, uncategorised, relation types 2, anchor classes 5, independent neighbourhoods 2: lose_weight(+2), staying_healthy(+1), get_fit(+2), stay_fit(+3), keeping_fit(+2), maintain_good_health(+4), stay_healthy(+3)
  - frame: HasPrerequisite> exercise (= physical_activity, exercising, physical_exertion); HasPrerequisite> do_exercises (= excercise, work_out, excersize, exercise_muscles); UsedFor< getting_exercise (= getting_physical_activity, getting_excercise, get_exercise); UsedFor< eating_healthily (= eating_well); UsedFor< going_for_run (= going_for_jog, go_for_run)
  - profile p=0.0099 sel=0.0396 rep=0.0; profile2 p=0.0099 sel=0.0297 rep=0.04

### Other selection survivors (18)

- **m1924** n=13, crosscutting, relation types 1, anchor classes 5, independent neighbourhoods 3: enjoyment(+1), sport(+1), commuter(+2), transportation(+1), leave_house(+3), getting_from_one_place_to_another(+2), going_to_work, traveling(+1), travelling(+1), passing_time(+1), test_car(+1), sightseeing(+1), going_from_one_place_to_another(+4)
  - frame: UsedFor< riding_bike (= ride_bicycle, ride_bike, riding_bicycle); UsedFor< driving_car (= moving_car, drive_car_on); UsedFor< going_for_drive (= drive_on, driving_on); UsedFor< taking_walk (= take_walk); UsedFor< taking_car_for_drive (= driving_in_car)
  - profile p=0.0099 sel=0.0099 rep=0.0; profile2 p=0.0099 sel=0.0099 rep=0.0
- **m1687** n=6, uncategorised, relation types 3, anchor classes 4, independent neighbourhoods 1: physically_fit(+1), get_in_shape(+1), losing_weight(+2), get_fit(+2), stay_fit(+3), keeping_in_shape(+2)
  - frame: HasPrerequisite< play_sports (= play_sport, playing_sports, playing_sport); MotivatedByGoal< exercise (= physical_activity, exercising, physical_exertion); MotivatedByGoal< run (= jog, go_running); MotivatedByGoal< do_exercises (= excercise, work_out, excersize, exercise_muscles); UsedFor< play_sports (= play_sport, playing_sports, playing_sport)
  - profile p=0.0099 sel=0.0198 rep=0.0; profile2 p=0.0099 sel=0.0099 rep=0.0
- **m686** n=18, crosscutting, relation types 2, anchor classes 2, independent neighbourhoods 1: fitness(+1), good_health(+1), injury(+2), sweat(+2), get_tired(+2), tiredness(+1), fatigue(+3), have_heart_attack(+3), pulling_muscle(+1), better_health(+2), shortness_of_breath(+4), become_stronger(+3), losing_weight(+2), physical_fitness(+1), get_fit(+2), increased_heart_rate(+3) …
  - frame: Causes< exercise (= physical_activity, exercising, physical_exertion); Causes< getting_exercise (= getting_physical_activity, getting_excercise, get_exercise); HasSubevent< getting_exercise (= getting_physical_activity, getting_excercise, get_exercise)
  - profile p=0.0099 sel=0.0099 rep=0.0; profile2 p=0.0099 sel=0.0099 rep=0.0
- **m1041** n=7, uncategorised, relation types 2, anchor classes 1, independent neighbourhoods 1: sit_down(+1), buy_popcorn, make_popcorn, open_eyes(+4), get_popcorn(+1), go_to_theater(+1), drive_to_theatre
  - frame: HasFirstSubevent< watch_movie (= see_movie, watch_film, go_see_film); HasPrerequisite< watch_movie (= see_movie, watch_film, go_see_film)
  - profile p=0.0099 sel=0.0198 rep=0.0; profile2 p=0.0099 sel=0.0099 rep=0.0
- **m0** n=62, crosscutting, relation types 1, anchor classes 2, independent neighbourhoods 1: flat(+1), stranger(+1), building(+1), war(+2), school(+1), street(+2), motel(+2), theater(+2), bank(+3), movies(+3), bus_stop, mall(+1), train_station(+2), sporting_goods_store(+1), church(+1), grocery_store(+1) …
  - frame: AtLocation> city; AtLocation> town (= community)
  - profile p=0.0099 sel=0.0099 rep=0.0; profile2 p=0.0099 sel=0.0198 rep=0.0
- **m73** n=24, partly_named, relation types 1, anchor classes 2, independent neighbourhoods 1: home(+1), car(+3), bar(+2), building(+1), war(+2), school(+1), motel(+2), theater(+2), bank(+3), office_building, factory, bus(+2), bus_stop, airport(+1), church(+1), department_store(+2) …
  - frame: AtLocation> city; AtLocation< person (= human)
  - profile p=0.0099 sel=0.0297 rep=0.0; profile2 p=0.0099 sel=0.0495 rep=0.0
- **m100** n=14, crosscutting, relation types 1, anchor classes 2, independent neighbourhoods 1: pain(+2), sweat(+2), fall_down(+1), get_tired(+2), fatigue(+3), have_heart_attack(+3), becoming_tired(+2), sore_feet(+2), shortness_of_breath(+4), losing_weight(+2), cramps(+5), increased_heart_rate(+3), leg_cramps, getting_out_of_breath(+1)
  - frame: Causes< running (= sprinting); Causes< going_for_run (= going_for_jog, go_for_run)
  - profile p=0.0099 sel=0.0099 rep=0.0; profile2 p=0.0099 sel=0.0099 rep=0.0
- **m138** n=14, uncategorised, relation types 1, anchor classes 2, independent neighbourhoods 1: health(+1), enjoyment(+1), lose_weight(+2), good_health(+1), staying_healthy(+1), being_healthy(+2), get_fit(+2), stay_fit(+3), improving_health(+2), keeping_fit(+2), maintain_good_health(+4), training, strengthening_heart(+1), staying_physically_fit(+1)
  - frame: UsedFor< getting_exercise (= getting_physical_activity, getting_excercise, get_exercise); UsedFor< going_for_run (= going_for_jog, go_for_run)
  - profile p=0.0099 sel=0.0099 rep=0.0; profile2 p=0.0099 sel=0.0099 rep=0.0
- **m323** n=14, crosscutting, relation types 1, anchor classes 3, independent neighbourhoods 1: fitness(+1), good_health(+1), sweat(+2), fatigue(+3), have_heart_attack(+3), better_health(+2), getting_in_shape(+1), strains, being_healthy(+2), shortness_of_breath(+4), get_fit(+2), cramps(+5), increased_heart_rate(+3), improving_health(+2)
  - frame: Causes< getting_exercise (= getting_physical_activity, getting_excercise, get_exercise); Causes< doing_exercises (= working_out); Causes< jogging
  - profile p=0.0099 sel=0.0099 rep=0.0; profile2 p=0.0099 sel=0.0099 rep=0.0
- **m1733** n=13, crosscutting, relation types 1, anchor classes 3, independent neighbourhoods 1: laugh(+1), run(+2), running(+1), sweat(+2), drink_water(+2), get_tired(+2), get_sweaty(+2), fatigue(+3), better_health(+2), eat_healthy(+1), get_fit(+2), do_exercises(+4), breathe_hard(+4)
  - frame: HasSubevent< play_sports (= play_sport, playing_sports, playing_sport); HasSubevent< getting_exercise (= getting_physical_activity, getting_excercise, get_exercise); HasSubevent< get_fit (= getting_fit, get_fitter)
  - profile p=0.0099 sel=0.0099 rep=0.0; profile2 p=0.0099 sel=0.0099 rep=0.03
- **m243** n=12, uncategorised, relation types 1, anchor classes 2, independent neighbourhoods 1: popcorn(+1), go_to_movies(+1), buy_popcorn, make_popcorn, go_to_cinema(+5), buy_ticket(+6), open_eyes(+4), go_to_theater(+1), put_on_glasses(+3), near_tv, rent_movie(+2), ability_to_see(+1)
  - frame: HasPrerequisite< watch_movie (= see_movie, watch_film, go_see_film); HasPrerequisite< enjoy_film (= enjoy_movie, enjoying_film, enjoying_movie)
  - profile p=0.0099 sel=0.0099 rep=0.0; profile2 p=0.0099 sel=0.0099 rep=0.0
- **m254** n=12, crosscutting, relation types 1, anchor classes 2, independent neighbourhoods 1: competition(+2), health(+1), fitness(+1), enjoyment(+1), recreation(+1), get_fit(+2), stay_fit(+3), keeping_fit(+2), socialising(+3), maintain_good_health(+4), body_building(+1), keeping_in_shape(+2)
  - frame: UsedFor< play_sports (= play_sport, playing_sports, playing_sport); UsedFor< getting_exercise (= getting_physical_activity, getting_excercise, get_exercise)
  - profile p=0.0099 sel=0.0099 rep=0.0; profile2 p=0.0099 sel=0.0198 rep=0.0
- **m280** n=12, uncategorised, relation types 1, anchor classes 3, independent neighbourhoods 1: log_on, using_computer(+2), dial_up, turn_on_computer(+3), connect_to_internet(+1), buy_computer, have_computer(+2), get_isp, have_modem, log_on_to_computer(+1), start_web_browser(+1), get_computer_modem
  - frame: HasPrerequisite< getting_onto_web (= get_onto_web, log_on_to_internet, accessing_internet); HasPrerequisite< go_on_internet (= use_internet); HasPrerequisite< surf_web (= surf_internet, access_internet)
  - profile p=0.0099 sel=0.0099 rep=0.0; profile2 p=0.0099 sel=0.0099 rep=0.0
- **m1013** n=12, uncategorised, relation types 1, anchor classes 3, independent neighbourhoods 1: health(+1), lose_weight(+2), good_health(+1), feeling_good(+1), staying_healthy(+1), looking_good(+1), feeling_good_about_yourself(+4), improving_health(+2), keeping_fit(+2), stay_healthy(+3), training, keeping_in_shape(+2)
  - frame: UsedFor< exercise (= physical_activity, exercising, physical_exertion); UsedFor< getting_exercise (= getting_physical_activity, getting_excercise, get_exercise); UsedFor< getting_in_shape (= getting_workout)
  - profile p=0.0099 sel=0.0099 rep=0.0; profile2 p=0.0099 sel=0.0198 rep=0.0
- **m189** n=11, partly_named, relation types 1, anchor classes 2, independent neighbourhoods 1: death(+1), indigestion, gas(+1), nausea, gain_weight(+2), feeling_full(+1), getting_full(+2), heartburn, making_less_hungry(+1), being_less_hungry(+2), sate_hunger(+9)
  - frame: Causes< eating (= ingest_food); Causes< eating_hamburger (= eat_hamburger, eat_burger)
  - profile p=0.0099 sel=0.0099 rep=0.0; profile2 p=0.0099 sel=0.0396 rep=0.02
- **m214** n=11, crosscutting, relation types 1, anchor classes 2, independent neighbourhoods 1: patience(+1), time(+1), turn_on(+1), television(+2), television_set(+1), electricity(+2), turn_on_tv(+4), switch_on_television(+2), turn_on_tv_set(+1), ability_to_see(+1), find_tv
  - frame: HasPrerequisite< watching_television (= watch_television); HasPrerequisite< watching_tv_show (= watching_television_show, watch_television_show, watch_tv_show)
  - profile p=0.0099 sel=0.0099 rep=0.0; profile2 p=0.0099 sel=0.0198 rep=0.02
- **m406** n=10, uncategorised, relation types 1, anchor classes 2, independent neighbourhoods 1: military(+1), soldier(+1), battle_enemy(+1), join_army(+1), prepare_army(+2), have_army, get_weapons(+1), know_where_enemy, make_enemy, use_weapon(+1)
  - frame: HasPrerequisite< fight_enemy (= attacking_enemy, fighting_enemy, attack_enemy); HasPrerequisite< fight_war (= wage_war)
  - profile p=0.0099 sel=0.0099 rep=0.0; profile2 p=0.0099 sel=0.0495 rep=0.0
- **m3184** n=10, uncategorised, relation types 1, anchor classes 3, independent neighbourhoods 1: health(+1), feeling_good(+1), staying_healthy(+1), losing_weight(+2), meeting_new_people(+2), stay_fit(+3), impressing_others(+2), building_muscle(+1), keeping_fit(+2), body_building(+1)
  - frame: UsedFor< play_sports (= play_sport, playing_sports, playing_sport); UsedFor< doing_exercises (= working_out); UsedFor< getting_in_shape (= getting_workout)
  - profile p=0.0099 sel=0.0297 rep=0.0; profile2 p=0.0099 sel=0.0495 rep=0.0

### Pass profile nulls but not the selection control, ≥ 2 relation types and ≥ 2 independent neighbourhoods (264; largest 25)

- **m8** n=31, partly_named, relation types 2, anchor classes 4, independent neighbourhoods 2: accordion(+1), acoustic_guitar, balalaika, banjo, bass_baritone, bass_clarinet, bass_fiddle, bassoon, piano(+1), cello, clarinet, clavichord(+1), cornet, drum(+1), fiddle(+1), flute(+1) …
  - frame: AtLocation> band; AtLocation> music_store (= music_shop, musical_instrument_store); AtLocation> orchestra; UsedFor> making_music (= make_music, create_music)
  - profile p=0.0099 sel=0.4257 rep=0.0; profile2 p=0.0099 sel=0.4356 rep=0.05
- **m4211** n=18, partly_named, relation types 2, anchor classes 5, independent neighbourhoods 3: apple(+1), egg, cake(+1), cheese, food(+1), meat, bean(+1), bread, cabbage, carrots(+1), corn, potato(+1), frozen_foods, fruit(+1), grape(+1), milk(+1) …
  - frame: AtLocation> plate; AtLocation> supermarket (= food_store); AtLocation> refrigerator (= fridge); AtLocation> market (= marketing); UsedFor> eating (= ingest_food)
  - profile p=0.0099 sel=1.0 rep=0.0; profile2 p=0.0099 sel=1.0 rep=0.0
- **m128** n=15, uncategorised, relation types 2, anchor classes 2, independent neighbourhoods 2: surprising(+5), watching_television(+1), singing(+2), fly_kite(+1), go_to_play(+1), tickling(+2), watching_movie(+3), entertaining_people(+1), going_to_party, socialising(+3), telling_story(+3), watching_tv_show(+3), see_favorite_show(+1), enjoy_film(+3), run_after_ball(+2)
  - frame: Causes> laughter (= laughing, laughs); UsedFor> fun (= enjoyable)
  - profile p=0.0099 sel=1.0 rep=0.0; profile2 p=0.0099 sel=1.0 rep=0.0
- **m274** n=13, crosscutting, relation types 2, anchor classes 3, independent neighbourhoods 3: barber_comb, blow_dryer(+2), curling_iron, gel, hairbrush(+1), hair_care_article, hair_clip, hair_dryer(+1), hair_gel, hair_roller, hair_shaping_gel, sculpting_gel, shampoo_and_conditioner
  - frame: AtLocation> bathroom (= toilet); AtLocation> beauty_salon (= beauty_parlor, beauty_shop, beauty_salons); UsedFor> styling_hair (= style_hair, making_hair_look_nice)
  - profile p=0.0099 sel=1.0 rep=0.0; profile2 p=0.0099 sel=1.0 rep=0.0
- **m601** n=13, partly_named, relation types 2, anchor classes 4, independent neighbourhoods 3: bed(+1), table, sink, bedroom(+1), bathroom(+1), closet(+1), television(+2), kitchen(+1), stove(+1), lamp(+1), computer, couch(+1), furniture
  - frame: AtLocation> house (= houses); AtLocation> neighbor's_house; AtLocation> apartment (= apartments); ReceivesAction> found_in_house (= found_in_houses)
  - profile p=0.0099 sel=1.0 rep=0.0; profile2 p=0.0099 sel=1.0 rep=0.03
- **m947** n=13, uncategorised, relation types 3, anchor classes 4, independent neighbourhoods 3: surprising(+5), watching_television(+1), go_to_play(+1), read_newspaper(+1), tickling(+2), watching_movie(+3), chatting_with_friends(+2), going_to_movie(+2), going_to_party, playing_game_with_friends(+1), watching_tv_show(+3), see_favorite_show(+1), enjoy_film(+3)
  - frame: Causes> laughter (= laughing, laughs); HasSubevent> laugh (= get_laugh); UsedFor> fun (= enjoyable); UsedFor> passing_time (= killing_time)
  - profile p=0.0099 sel=1.0 rep=0.0; profile2 p=0.0099 sel=1.0 rep=0.0
- **m2703** n=13, uncategorised, relation types 3, anchor classes 5, independent neighbourhoods 3: get_paid(+3), buying(+3), getting(+1), buying_beer(+2), buying_for_loved_one(+1), buying_presents_for_others(+1), eating_ice_cream(+1), going_to_movie(+2), going_to_performance(+1), purchasing_cellular_phone(+1), buy_christmas_presents(+1), buy_fresh_fruits_and_vegetables(+1), buy_presents(+6)
  - frame: Causes> happiness (= being_happy, being_content); Causes> pleasure (= satisfaction); HasPrerequisite> money (= currency); HasPrerequisite> go_to_store (= enter_shop, go_to_shop); HasSubevent> spend_money (= use_money, have_money_to_spend)
  - profile p=0.0099 sel=1.0 rep=0.0; profile2 p=0.0099 sel=1.0 rep=0.01
- **m542** n=11, crosscutting, relation types 2, anchor classes 2, independent neighbourhoods 2: business(+2), movies(+3), grocery_store(+1), movie_house, seafood_restaurant(+1), movie_theater(+1), bazaar, company(+1), industry, parking_area(+2), vending_stand
  - frame: AtLocation> city; UsedFor> making_money (= make_money, making_profit)
  - profile p=0.0099 sel=1.0 rep=0.0; profile2 p=0.0099 sel=1.0 rep=0.0
- **m236** n=10, uncategorised, relation types 2, anchor classes 2, independent neighbourhoods 2: run(+2), walk_dog(+1), riding_bike(+3), chopping_firewood(+1), going_for_walk(+1), playing_football(+1), playing_frisbee(+3), weeding_garden(+1), get_physical_activity(+1), go_for_jog(+2)
  - frame: HasPrerequisite> go_outside (= going_outside, step_outside); HasSubevent> sweat (= sweating, perspiration)
  - profile p=0.0099 sel=1.0 rep=0.0; profile2 p=0.0099 sel=1.0 rep=0.0
- **m268** n=10, uncategorised, relation types 2, anchor classes 2, independent neighbourhoods 2: play_game(+2), playing_games(+1), pass_course(+3), competing_against(+1), having_examination(+2), taking_examination(+1), taking_final_exams(+1), taking_midterm(+1), writing_term_paper(+1), see_people_play_game(+1)
  - frame: Causes> stress (= get_stressed); HasSubevent> cheat (= cheating, cheats)
  - profile p=0.0099 sel=1.0 rep=0.0; profile2 p=0.0099 sel=1.0 rep=0.02
- **m673** n=10, uncategorised, relation types 2, anchor classes 3, independent neighbourhoods 2: take_course(+1), get_job(+2), attending_class(+2), learning_new(+3), receiving_degree(+3), taking_exam(+3), taking_final_exams(+1), taking_finals(+1), taking_midterm(+1), improve_yourself(+2)
  - frame: Causes> stress (= get_stressed); HasPrerequisite> go_to_school (= go_to_class); HasPrerequisite> enroll_in_school (= matriculate)
  - profile p=0.0099 sel=1.0 rep=0.0; profile2 p=0.0099 sel=1.0 rep=0.01
- **m1977** n=10, partly_named, relation types 3, anchor classes 3, independent neighbourhoods 3: egg, ball, baseball(+1), basketball, beach_ball(+1), disk, football, frisbee(+1), sports_bat, tennis_ball(+1)
  - frame: AtLocation> sporting_goods_store (= sporting_goods_stores); HasProperty> round (= circle, circular); UsedFor> throwing (= throw, throw_things, toss)
  - profile p=0.0099 sel=0.0495 rep=0.0; profile2 p=0.0099 sel=0.2376 rep=0.01
- **m2005** n=10, uncategorised, relation types 2, anchor classes 3, independent neighbourhoods 2: jumping_up_and_down(+2), walk_dog(+1), riding_bike(+3), standing_in_line(+3), going_for_run(+2), going_for_walk(+1), jogging, waiting_in_line(+1), running_twenty_six_miles(+1), do_housework(+2)
  - frame: Causes> get_tired (= getting_tired, get_exhausted); Causes> fatigue (= exhaustion, being_tired, getting_exhausted); HasSubevent> whistle (= whistling); HasSubevent> get_tired (= getting_tired, get_exhausted)
  - profile p=0.0099 sel=1.0 rep=0.0; profile2 p=0.0099 sel=1.0 rep=0.01
- **m2412** n=10, crosscutting, relation types 4, anchor classes 8, independent neighbourhoods 6: act_in_play(+1), playing_violin(+1), riding_bike(+3), skiing(+2), competing_against(+1), driving_car(+2), performing(+1), playing_basketball(+1), playing_football(+1), wrestling(+1)
  - frame: Causes> injury (= injuries, injuring); HasPrerequisite> practice (= rehearse, practise); HasPrerequisite> skill (= talent); HasSubevent> sweat (= sweating, perspiration); UsedFor> pleasure (= satisfaction); UsedFor> entertainment (= amusement, being_entertained); UsedFor> fun (= enjoyable); UsedFor> earning_money (= profit)
  - profile p=0.0099 sel=1.0 rep=0.0; profile2 p=0.0099 sel=1.0 rep=0.02
- **m355** n=9, crosscutting, relation types 2, anchor classes 2, independent neighbourhoods 2: reading(+1), watching_television(+1), reading_book, watching_tv(+1), using_computer(+2), reading_to_children(+1), using_television(+1), watching_tv_show(+3), read_magazine(+3)
  - frame: Causes> eye_strain (= eyestrain, hurting_eyes); UsedFor> education (= educating)
  - profile p=0.0099 sel=1.0 rep=0.0; profile2 p=0.0099 sel=1.0 rep=0.01
- **m541** n=9, uncategorised, relation types 3, anchor classes 3, independent neighbourhoods 3: eating(+1), having_food(+1), eating_hamburger(+2), eating_apple(+4), eating_cookie(+2), eating_ice_cream(+1), go_to_restaurant(+3), open_bag_of_chips(+1), eat_lunch(+1)
  - frame: Causes> gain_weight (= weight_gain, gaining_weight); HasSubevent> swallow (= swallowing); UsedFor> sate_hunger (= ending_hunger, satisfying_hunger, reducing_hunger, relieving_hunger…)
  - profile p=0.0099 sel=1.0 rep=0.0; profile2 p=0.0099 sel=1.0 rep=0.0
- **m585** n=9, partly_named, relation types 2, anchor classes 2, independent neighbourhoods 2: dance(+1), climbing(+1), hiking(+1), ride_horse(+4), playing_violin(+1), riding_bike(+3), running_marathon(+1), going_to_store, playing_harp(+1)
  - frame: Causes> blisters (= blister); UsedFor> fun (= enjoyable)
  - profile p=0.0099 sel=1.0 rep=0.0; profile2 p=0.0099 sel=1.0 rep=0.0
- **m590** n=9, partly_named, relation types 2, anchor classes 5, independent neighbourhoods 2: action_figure(+1), ball, beanbag(+1), beanie_baby, stuffed_animal(+1), toy_ball, toy_car, toy_marble, yoyo
  - frame: AtLocation> child's_room (= kid's_room, child's_bedroom); AtLocation> toy_store (= toystore, toy_shop); AtLocation> toy_box (= toybox); UsedFor> play (= playing, played); UsedFor> play_with (= playing_with)
  - profile p=0.0099 sel=1.0 rep=0.0; profile2 p=0.0099 sel=1.0 rep=0.05
- **m641** n=9, uncategorised, relation types 4, anchor classes 6, independent neighbourhoods 4: running(+1), walk_dog(+1), jumping_rope(+2), riding_bike(+3), standing_in_line(+3), going_for_run(+2), going_for_walk(+1), running_in_marathon(+1), running_twenty_six_miles(+1)
  - frame: Causes> get_tired (= getting_tired, get_exhausted); Causes> tiredness (= crankiness); Causes> fatigue (= exhaustion, being_tired, getting_exhausted); Causes> sore_feet (= feet_hurt, getting_sore_feet); HasPrerequisite> legs (= leg, have_legs); HasSubevent> get_tired (= getting_tired, get_exhausted); UsedFor> fun (= enjoyable)
  - profile p=0.0099 sel=1.0 rep=0.0; profile2 p=0.0099 sel=1.0 rep=0.01
- **m892** n=9, partly_named, relation types 2, anchor classes 4, independent neighbourhoods 3: cake(+1), pie(+1), chicken(+1), food(+1), turkey(+1), bread, pizza(+1), cookies(+1), steak(+1)
  - frame: AtLocation> plate; AtLocation> refrigerator (= fridge); AtLocation> oven (= ovens); HasProperty> baked_in_oven (= baked_in_ovens)
  - profile p=0.0099 sel=1.0 rep=0.0; profile2 p=0.0099 sel=1.0 rep=0.0
- **m1698** n=9, crosscutting, relation types 2, anchor classes 4, independent neighbourhoods 3: table, carpet(+2), rug, beanbag_chair(+1), fireplace(+1), hide_bed_sofa(+1), love_seat, ottoman, sofabed(+2)
  - frame: AtLocation> house (= houses); AtLocation> living_room (= livingroom, living_rooms); UsedFor> decoration (= decorative); UsedFor> sitting_on (= sit_on)
  - profile p=0.0099 sel=1.0 rep=0.0; profile2 p=0.0099 sel=1.0 rep=0.01
- **m2903** n=9, partly_named, relation types 2, anchor classes 4, independent neighbourhoods 3: mall(+1), train_station(+2), pub(+1), cafe, restaurant(+1), steak_house(+1), dance_club, place_to_eat(+1), saloon(+1)
  - frame: AtLocation> city; AtLocation> town (= community); UsedFor> meeting_friend (= meeting_friends); UsedFor> socializing (= social_bonding)
  - profile p=0.0099 sel=1.0 rep=0.0; profile2 p=0.0099 sel=1.0 rep=0.0
- **m666** n=8, crosscutting, relation types 2, anchor classes 2, independent neighbourhoods 2: grocery_store(+1), greengrocer, market(+1), restaurant(+1), fast_food_restaurant_counter(+1), health_food_store, large_food_store(+1), vending_stand
  - frame: AtLocation> city; UsedFor> selling_food (= selling_groceries)
  - profile p=0.0099 sel=1.0 rep=0.0; profile2 p=0.0099 sel=1.0 rep=0.0
- **m741** n=8, crosscutting, relation types 2, anchor classes 2, independent neighbourhoods 2: stop(+1), train_station(+2), parking_lot(+1), boarding_room, dental_office(+1), bus_shelter, dentist_office(+1), subway_stop(+1)
  - frame: AtLocation> city; UsedFor> waiting (= wait)
  - profile p=0.0099 sel=1.0 rep=0.0; profile2 p=0.0099 sel=1.0 rep=0.02
- **m1640** n=8, uncategorised, relation types 2, anchor classes 4, independent neighbourhoods 2: kissing(+1), pass_course(+3), creating_idea(+2), getting_good_grade(+4), seeing_idea_become_reality(+1), winning_baseball_game(+1), see_favorite_show(+1), create_to_help_other_people(+1)
  - frame: Causes> happiness (= being_happy, being_content); Causes> pride (= proud); Causes> excitement (= delight, elation); HasSubevent> feel_good (= feel_happy)
  - profile p=0.0099 sel=1.0 rep=0.0; profile2 p=0.0099 sel=1.0 rep=0.03

## Anomaly 18 (69 merged groups with ≥ 2 of its activities; 0 survive selection, 3 survive profile)

- **m1775** n=66, uncategorised, relation types 2, anchor classes 3, independent neighbourhoods 1: dance(+1), kill(+2), watching_television(+1), singing(+2), fly_kite(+1), play_game(+2), go_to_play(+1), jumping_rope(+2), helping(+1), kissing(+1), get_paid(+3), riding_bike(+3), discovering_truth(+1), learning_new(+3), getting(+1), buying_for_loved_one(+1) …
  - frame: Causes> happiness (= being_happy, being_content); Causes> pleasure (= satisfaction); UsedFor> fun (= enjoyable)
  - profile p=0.0297 sel=0.0198 rep=0.0; profile2 p=0.0099 sel=0.0099 rep=0.02
- **m1** n=62, crosscutting, relation types 1, anchor classes 2, independent neighbourhoods 1: car(+3), dance(+1), surprising(+5), climbing(+1), swimming_pool(+1), playroom(+1), canoe(+1), discothque, singing(+2), swimming(+1), play_game(+2), play_poker(+2), getting_drunk(+2), play_guitar(+2), having_sex(+1), ride_horse(+4) …
  - frame: UsedFor> fun (= enjoyable); UsedFor> having_fun (= enjoying_yourself, having_great_time, enjoying_oneself)
  - profile p=0.0099 sel=0.4059 rep=0.3; profile2 p=0.3762 sel=0.4554 rep=1.0
- **m3** n=49, crosscutting, relation types 1, anchor classes 2, independent neighbourhoods 1: dance(+1), writing(+1), movie(+1), pot(+3), playroom(+1), baseball_stadium, vacation(+1), performance(+1), kite(+1), singing(+2), play_game(+2), climb_mountain(+3), play_poker(+2), play_piano(+1), playing_hockey(+1), playing_violin(+1) …
  - frame: UsedFor> entertainment (= amusement, being_entertained); UsedFor> fun (= enjoyable)
  - profile p=0.0099 sel=0.6634 rep=0.0; profile2 p=0.0099 sel=1.0 rep=0.41
- **m5** n=45, uncategorised, relation types 1, anchor classes 2, independent neighbourhoods 1: go_to_bed(+2), show(+1), writing(+1), fish(+2), swimming(+1), fly_kite(+1), walk_dog(+1), getting_drunk(+2), having_sex(+1), play_piano(+1), diving(+1), playing_violin(+1), read_newspaper(+1), reading_book, skiing(+2), watching_movie(+3) …
  - frame: UsedFor> fun (= enjoyable); UsedFor> relaxing (= relaxation)
  - profile p=0.099 sel=0.7723 rep=0.0; profile2 p=0.505 sel=1.0 rep=1.0
- **m1312** n=43, crosscutting, relation types 2, anchor classes 5, independent neighbourhoods 2: climbing(+1), canoe(+1), singing(+2), swimming(+1), play_lacrosse(+1), play_game(+2), go_to_play(+1), play_poker(+2), play_guitar(+2), ride_horse(+4), play_piano(+1), diving(+1), playing_violin(+1), reading_book, riding_bike(+3), skiing(+2) …
  - frame: HasPrerequisite> skill (= talent); UsedFor> enjoyment (= getting_pleasure); UsedFor> fun (= enjoyable); UsedFor> recreation (= regeneration); UsedFor> having_fun (= enjoying_yourself, having_great_time, enjoying_oneself)
  - profile p=0.0099 sel=0.8713 rep=0.0; profile2 p=0.0099 sel=1.0 rep=0.2
- **m6** n=42, uncategorised, relation types 1, anchor classes 2, independent neighbourhoods 1: show(+1), climbing(+1), oboe, singing(+2), swimming(+1), go_to_play(+1), jumping_rope(+2), play_poker(+2), ride_horse(+4), play_piano(+1), playing_violin(+1), read_newspaper(+1), reading_book, riding_bike(+3), skiing(+2), watching_movie(+3) …
  - frame: UsedFor> enjoyment (= getting_pleasure); UsedFor> fun (= enjoyable)
  - profile p=0.0099 sel=0.9307 rep=0.02; profile2 p=0.0099 sel=1.0 rep=1.0
- **m2358** n=42, crosscutting, relation types 1, anchor classes 6, independent neighbourhoods 1: dance(+1), writing(+1), reading(+1), singing(+2), swimming(+1), play_poker(+2), getting_drunk(+2), ride_horse(+4), play_piano(+1), diving(+1), playing_violin(+1), reading_book, riding_bike(+3), skiing(+2), watching_movie(+3), becoming_scuba_diver(+1) …
  - frame: UsedFor> enjoyment (= getting_pleasure); UsedFor> pleasure (= satisfaction); UsedFor> entertainment (= amusement, being_entertained); UsedFor> fun (= enjoyable); UsedFor> having_fun (= enjoying_yourself, having_great_time, enjoying_oneself); UsedFor> relaxing (= relaxation)
  - profile p=0.0099 sel=0.9307 rep=0.0; profile2 p=0.0099 sel=1.0 rep=0.71
- **m4201** n=40, partly_named, relation types 2, anchor classes 5, independent neighbourhoods 3: dance(+1), climbing(+1), running(+1), swimming(+1), play_lacrosse(+1), fly_kite(+1), play_game(+2), play_poker(+2), getting_drunk(+2), play_guitar(+2), ride_horse(+4), play_piano(+1), diving(+1), playing_games(+1), playing_hockey(+1), playing_violin(+1) …
  - frame: HasPrerequisite> skill (= talent); UsedFor> competition (= competitions, competitors); UsedFor> pleasure (= satisfaction); UsedFor> fun (= enjoyable); UsedFor> having_fun (= enjoying_yourself, having_great_time, enjoying_oneself)
  - profile p=0.0099 sel=0.9604 rep=0.0; profile2 p=0.0594 sel=1.0 rep=0.1
