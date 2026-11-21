# Paraphrase-merged typed groups (cap 30)

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
| real | 1166 | 420 | 122 | 13 | 266 |
| relation | 818.7 [898] | 195.7 [243] | 14.4 [27] | 0.0 [1] | 127.1 [169] |
| strict | 529.1 [582] | 107.4 [127] | 7.3 [14] | 0.3 [1] | 68.6 [95] |
| profile | 702.8 [748] | 205.6 [236] | 23.3 [35] | 1.1 [3] | 130.7 [165] |
| profile2 | 772.2 [828] | 254.8 [280] | 40.7 [52] | 2.2 [5] | 147.7 [169] |

Survive both profile nulls (frame support at floor, reproduced ≤ 5%): 580; + selection control: 32. By tier: {'survives_profile': {'crosscutting': 158, 'partly_named': 139, 'uncategorised': 216, 'named': 67}, 'survives_selection': {'crosscutting': 10, 'partly_named': 4, 'uncategorised': 18}}

## What happened to previously surviving groups

| prior status | n | still survive selection | survive profile only | found, not significant | gone (no merged group with member Jaccard ≥ 0.3) |
|---|---|---|---|---|---|
| survived selection | 89 | 25 | 46 | 3 | 15 |
| survived profile only | 660 | 16 | 336 | 84 | 224 |

Previous selection survivors, one line each (prior members → status):

- flat, stranger, bank, bookshop, sporting_goods_store, pub … [AtLocation> city; AtLocation> town] → **survives_selection** (members merged away 2; match J=0.79)
- clutter, feet, printer, trash_can, lamp, cup_of_coffee … [AtLocation> desk; AtLocation> office] → **survives_selection** (members merged away 2; match J=0.79)
- accordion, acoustic_guitar, balalaika, banjo, bass_baritone, bass_clarinet … [AtLocation> band; AtLocation> orchestra; UsedFor> making_music] → **survives_selection** (members merged away 1; match J=0.78)
- dollar, return_ticket, comb, car_keys, cash_coin, coin_purse … [AtLocation> purse; AtLocation> pocket] → **survives_profile** (members merged away 3; match J=0.91)
- seat, backdrop, balcony, balcony_railing, balcony_seat, seats … [AtLocation> theater; AtLocation> theatre] → **gone** (members merged away 2; match J=0.20)
- fair, texas, america, it's_natural_habitat, indiana, farm_yard … [AtLocation< cow; AtLocation< heifer] → **survives_selection** (members merged away 2; match J=0.90)
- bank, bookshop, movie_house, bookstore, movie_theater, parking_lot … [AtLocation> city; AtLocation> mall] → **survives_selection** (members merged away 1; match J=0.66)
- apple, pie, cheese, turkey, bad_smell, butter … [AtLocation> fridge; AtLocation> refrigerator] → **gone** (members merged away 0; match J=0.22)
- ceiling, air_conditioner, balcony, beam, lamp, parlor … [AtLocation> building; AtLocation> house] → **survives_profile** (members merged away 1; match J=0.79)
- telephone_book, envelope, gun, ballpoint_pen, card_case, checkbook … [AtLocation> desk; AtLocation> drawer] → **survives_profile** (members merged away 1; match J=0.92)
- wild, pants, group, dictionary, it's_natural_habitat, woods … [AtLocation< lemur; AtLocation< marmoset] → **survives_profile** (members merged away 1; match J=0.94)
- go_to_concert, buy_ticket, open_eyes, go_to_theater, go_to_theatre, buy_tickets … [HasPrerequisite< watch_musician_perform; HasPrerequisite< see_band] → **survives_profile** (members merged away 4; match J=0.57)
- stretch_muscles, put_on_shoes, dress_appropriately, go_to_park, stretch_first, put_on_jogging_clothes … [HasPrerequisite< go_jogging; HasPrerequisite< go_for_jog] → **survives_profile** (members merged away 1; match J=0.36)
- log_on, dial_up, turn_computer_on, turn_on_computer, connect_to_internet, buy_computer … [HasPrerequisite< go_on_internet; HasPrerequisite< get_onto_web] → **survives_selection** (members merged away 1; match J=0.89)
- watch_television_show, see_favorite_show, see_story, use_television, see_people_play_game, see_particular_program … [HasPrerequisite> turn_on_tv; MotivatedByGoal> entertained] → **gone** (members merged away 0; match J=0.00)
- rent, turn_on_tv, rent_video, get_vcr, have_vcr, turn_on_vcr … [HasPrerequisite< view_video; HasPrerequisite< view_film_at_home] → **survives_profile** (members merged away 2; match J=1.00)
- go_to_cinema, go_to_movie_theater, turn_on_tv, turn_on_television, rent_movie, rent_video … [HasPrerequisite< watch_movie; HasPrerequisite< see_movie; HasPrerequisite< watch_film] → **gone** (members merged away 3; match J=0.25)
- go_to_beach, take_off_clothes, go_to_swimming_pool, go_to_pool, go_to_lake, put_on_bathing_suit … [HasPrerequisite< swim; HasPrerequisite< go_for_swim] → **survives_selection** (members merged away 1; match J=0.88)
- indigestion, gas, nausea, feeling_full, full_stomach, gaining_energy … [Causes< eating; Causes< eating_hamburger; Causes< eating_breakfast] → **survives_selection** (members merged away 0; match J=0.67)
- cook_food, prepare_food, order_food, hungry, get_food, find_restaurant … [HasPrerequisite< have_lunch; HasPrerequisite< eat_lunch] → **survives_profile** (members merged away 0; match J=0.71)
- start_car, fasten_seatbelt, get_driver's_license, get_keys, get_license, have_driving_license … [HasPrerequisite< drive; HasPrerequisite< drive_car] → **survives_profile** (members merged away 2; match J=0.86)
- soap_and_water, use_water, go_to_bathroom, run_water, turn_on_water, turn_on_warm_water … [HasPrerequisite< have_bath; HasPrerequisite< take_shower] → **survives_selection** (members merged away 1; match J=0.42)
- baking_bread, baking_cookies, bread, cakes, pizza, cookies … [AtLocation> oven; UsedFor< baking_oven] → **survives_profile** (members merged away 0; match J=0.71)
- careful, strike_match, light_match, go_outdoors, get_matches, gather_kindling … [HasPrerequisite< light_fire; HasPrerequisite< start_fire; HasPrerequisite< start_flame_or_fire] → **survives_profile** (members merged away 1; match J=0.45)
- rolling, throwing, bouncing, catching, kicking, play_with_dog … [UsedFor< ball; UsedFor< toy_ball] → **survives_selection** (members merged away 0; match J=1.00)
- go_to_movies, make_popcorn, go_to_cinema, go_to_theater, near_tv, rent_movie … [HasPrerequisite< watch_film; HasPrerequisite< enjoy_film] → **survives_selection** (members merged away 1; match J=0.60)
- waiter, waitress, become_waiter, work_in_restaurant, get_job_as_waiter, get_job_at_restaurant … [HasPrerequisite< wait_tables; HasPrerequisite< wait_on_tables] → **survives_profile** (members merged away 3; match J=0.67)
- disrobe, go_to_bathroom, turn_on_water, fill_bathtub_with_water, get_in_bathtub, have_bathtub … [HasPrerequisite< bathe; HasPrerequisite< have_bath] → **survives_profile** (members merged away 0; match J=0.86)
- plan_in_advance, decide_where_to_go, decide_where_want_to_go, choose_destination, decide_where_to_go_first, get_travel_brochures … [HasPrerequisite< plan_vacation; HasPrerequisite< go_on_vacation] → **gone** (members merged away 1; match J=0.25)
- go_to_doctor, go_see_doctor, make_doctor's_appointment, see_doctor, schedule_appointment_with_doctor, wear_clean_underwear … [HasPrerequisite< have_examination; HasPrerequisite< have_physical_exam] → **survives_selection** (members merged away 0; match J=0.55)
- better_health, living_longer, being_healthy, long_life, longer_life, longevity … [Causes< eating_healthily; Causes< staying_fit] → **survives_profile** (members merged away 1; match J=0.80)
- soldier, join_army, get_weapons, have_enemy_to_fight, join_armed_forces, know_where_enemy … [HasPrerequisite< fight_enemy; HasPrerequisite< fight_war] → **survives_selection** (members merged away 0; match J=0.60)
- having_hair_cut, getting_haircut, getting_hair_colored, getting_manicure, getting_perm, having_hair_styled … [UsedFor< salon; UsedFor< hairdressing_salon] → **survives_profile** (members merged away 0; match J=0.57)
- go_to_doctor, go_see_doctor, make_appointment_with_doctor, call_doctor, see_doctor, go_to_doctors … [HasPrerequisite< have_checkup; HasPrerequisite< have_physical_exam] → **survives_profile** (members merged away 2; match J=0.60)
- take_off, use_detergent, get_water, put_in_washer, buy_washing_powder, put_clothes_in_washer … [HasPrerequisite< clean_clothing; HasPrerequisite< wash_clothes] → **survives_profile** (members merged away 0; match J=0.75)
- graduate, celebration, relief, elation, graduating, graduation … [Causes< passing_class; Causes< passing_university_exams] → **gone** (members merged away 2; match J=0.14)
- accomplishment, sore_muscles, falling_down, get_higher, getting_to_top, loss_of_breath … [Causes< climbing; Causes< climbing_mountain] → **survives_profile** (members merged away 0; match J=0.67)
- wash, use_soap, take_off_clothes, wash_yourself, take_shower_or_bath, take_bath_or_shower … [HasPrerequisite< get_clean; HasPrerequisite< become_more_clean] → **survives_profile** (members merged away 1; match J=1.00)
- buy_hardware, buy_nails, buying_hardware, buying_nails, buying_screws, buying_tools … [UsedFor< hardware_store; UsedFor< hardware_shop] → **gone** (members merged away 2; match J=0.00)
- pay_tuition, apply, enroll, enroll_in_one, enroll_in_school, register_for … [HasPrerequisite< take_course; HasPrerequisite< attend_class] → **survives_selection** (members merged away 0; match J=0.75)
- find_newspaper, learn_to_read, know_how_to_read, get_paper, get_newspaper, have_newspaper … [HasPrerequisite< read_newspaper; HasPrerequisite< read_news] → **survives_profile** (members merged away 2; match J=1.00)
- use_money, go_to_hairdresser, go_to_barber, go_to_hair_salon, go_to_hairdressers, have_hair … [HasPrerequisite< have_haircut; HasPrerequisite< go_to_get_haircut] → **survives_selection** (members merged away 1; match J=0.30)
- open_mouth, not_drive, go_to_bar, have_id, buy_alcohol, not_drive_car … [HasPrerequisite< drink; HasPrerequisite< drink_alcohol] → **survives_profile** (members merged away 0; match J=0.67)
- connect_to_internet, buy_computer, have_computer, get_isp, log_on_to_internet, start_web_browser … [HasPrerequisite< surf_web; HasPrerequisite< get_onto_web] → **survives_selection** (members merged away 0; match J=0.36)
- heart_attack, sore_feet, shortness_of_breath, cramps, increased_heart_rate, leg_cramps … [Causes< running; Causes< going_for_jog] → **survives_selection** (members merged away 0; match J=0.62)
- able_to_see, go_to_cinema, buy_ticket, buy_tickets, rent_movie, rent_video … [HasPrerequisite< watch_movie; HasPrerequisite< enjoy_film] → **gone** (members merged away 2; match J=0.27)
- styling_hair, holding_hair_in_place, style_hair, arranging_hair, shape_hair … [UsedFor< hair_gel; UsedFor< hair_shaping_gel] → **survives_profile** (members merged away 1; match J=1.00)
- on_time, register, get_out_of_bed, enroll, matriculate, sign_up … [HasPrerequisite< go_to_school; HasPrerequisite< attend_school; HasPrerequisite< attend_class] → **survives_profile** (members merged away 2; match J=0.88)
- buy_car, get_in_car, steal_car, get_car, get_keys, have_car … [HasPrerequisite< drive; HasPrerequisite< go_for_drive] → **survives_selection** (members merged away 1; match J=0.44)
- go_to_bathroom, turn_on_water, fill_bathtub_with_water, fill_bathtub, fill_tub_with_water, use_bubbles … [HasPrerequisite< have_bath; HasPrerequisite< take_bath] → **survives_profile** (members merged away 1; match J=0.80)
- bad_breath, indigestion, feeling_full, heartburn, satisfying_hunger, late_for_work … [Causes< eating_breakfast; Causes< eating_lunch] → **survives_profile** (members merged away 0; match J=0.38)
- get_dirty, mop_floor, get_broom, get_cleaning_supplies, have_chemicals, sweep_floor … [HasPrerequisite< clean; HasPrerequisite< clean_house] → **survives_profile** (members merged away 0; match J=1.00)
- hanging, drying_towels, hang_towels, hanging_towel, hanging_towels_on … [UsedFor< towel_bar; UsedFor< towel_rack] → **gone** (members merged away 1; match J=0.00)
- boot_up_computer, connect_to_internet, buy_computer, have_computer, get_computer_modem, open_browser … [HasPrerequisite< go_on_internet; HasPrerequisite< surf_web] → **survives_selection** (members merged away 0; match J=0.50)
- criminals, murderers, revenge, ending_life, getting_rid_of_enemy, making_die … [UsedFor< killing; UsedFor< committing_murder] → **survives_profile** (members merged away 0; match J=0.83)
- carry_water, holding_water, carrying_things, bail_water, carrying_liquids … [UsedFor< bucket; UsedFor< pail] → **survives_profile** (members merged away 1; match J=1.00)
- take_course, buy_book, get_book_on_subject, go_to_library, read_book_about, use_search_engine … [HasPrerequisite< learn_new; HasPrerequisite< learn_about_subject; HasSubevent< finding_information] → **gone** (members merged away 1; match J=0.12)
- write_code, turn_on_computer, have_computer, learn_programming_language, know_programming_language, learn_to_code … [HasPrerequisite< program; HasPrerequisite< write_program] → **survives_profile** (members merged away 0; match J=1.00)
- turn_on_computer, learn_how, learn_programming_language, learn_how_to, learn_computer_language, learn_programming … [HasPrerequisite< program; HasPrerequisite< program_computer] → **survives_profile** (members merged away 1; match J=0.38)
- patient, stand, get_in_line, line_up, wear_comfortable_shoes, find_line … [HasPrerequisite< wait_turn; HasPrerequisite< stand_in_queue; HasPrerequisite< stand_in_line] → **survives_profile** (members merged away 0; match J=0.43)
- plug_in, turn_on, buy_one, turn_on_tv, turn_on_television, read_instruction_manual … [HasPrerequisite< watch_television; HasPrerequisite< use_television; HasPrerequisite< use_vcr] → **found_not_significant** (members merged away 1; match J=1.00)
- start_car, put_in_gear, start_motor, turn_car_on, turn_on_ignition, use_steering_wheel … [HasPrerequisite< drive_car; HasPrerequisite< move_car] → **survives_profile** (members merged away 1; match J=0.71)
- safety, avoiding_accident, not_moving, obeying_traffic_laws, stopping_at_intersection … [UsedFor< stopping_bicycle; UsedFor< stopping_car] → **survives_selection** (members merged away 0; match J=0.83)
- keep_things_cold, keeping_things_cold, storing_ice, storing_ice_cream, storing_meat … [UsedFor< icebox; UsedFor< refrigerator_freezer] → **survives_profile** (members merged away 1; match J=1.00)
- being_mean, revenge, causing_pain, getting_revenge, inflicting_pain … [UsedFor< hurting_else; UsedFor< punching] → **survives_profile** (members merged away 1; match J=1.00)
- cleanliness, removing_stains, sanitation, removing_dirt, hygiene, keeping_clean … [UsedFor< cleaning; UsedFor< washing_clothes; UsedFor< washing_hands] → **survives_profile** (members merged away 2; match J=0.80)
- eating_food, doing_homework, eat_dinner_on, eating_dinner_on, serving_dinner … [UsedFor< dining_room_table; UsedFor< dining_table] → **survives_profile** (members merged away 1; match J=0.80)
- lighting_fire, lighting_cigarette, lighting_candle, seeing_in_dark, creating_light … [UsedFor< lighting_match; UsedFor< striking_match] → **survives_profile** (members merged away 0; match J=0.80)
- find_partner, find_to_play_with, find_opponent, learn_rules, have_chess_board, have_oppenant … [HasPrerequisite< play_games; HasPrerequisite< play_chess; HasPrerequisite< play_game_of_chess] → **survives_profile** (members merged away 0; match J=0.86)
- clean_teeth, brush_teeth, brushing_teeth, removing_plaque, cleaning_teeth … [UsedFor< electric_toothbrush; UsedFor< gel_toothpaste; UsedFor< toothbrush] → **survives_profile** (members merged away 1; match J=1.00)
- order, hungry, go_to_burger_king, go_to_fast_food_restaurant, go_to_macdonalds, go_to_mcdonalds … [HasPrerequisite< buy_hamburger; HasPrerequisite< eat_hamburger; HasPrerequisite< eat_in_fast_food_restaurant] → **survives_profile** (members merged away 0; match J=0.83)
- selling_food, buying_milk, purchasing_food, selling_groceries, purchasing_groceries … [UsedFor< grocery_store; UsedFor< grocer] → **gone** (members merged away 1; match J=0.12)
- feeling_better, feeling_refreshed, dreaming, rejuvination, not_being_tired, renewed_energy … [Causes< having_rest; Causes< resting; UsedFor< sleeping] → **found_not_significant** (members merged away 0; match J=0.33)
- washing_hair, washing, keeping_clean, removing_dirt_from_body, relaxing_after_busy_day … [UsedFor< taking_bath; UsedFor< having_shower] → **survives_profile** (members merged away 0; match J=1.00)
- look_different, have_shorter_hair, look_neater, new_hairstyle, shorter_hair … [Causes< cutting_hair; MotivatedByGoal< cut_hair] → **survives_profile** (members merged away 1; match J=0.50)
- grooming, comb_hair, combing_hair, styling_hair, remove_tangles_from_hair … [UsedFor< barber_comb; UsedFor< comb; UsedFor< hairbrush] → **survives_profile** (members merged away 1; match J=0.60)
- exchanging_information, good_time, catching_up, keeping_in_touch, relaying_information … [UsedFor< chatting_with_friends; UsedFor< talking_with_far_away] → **survives_profile** (members merged away 0; match J=1.00)
- sport, going_someplace, racing, sightseeing, getting_out_of_house … [UsedFor< riding_bicycle; UsedFor< taking_car_for_drive] → **survives_profile** (members merged away 0; match J=0.50)
- hungry_people, satisfying_craving, filling_stomach, satisfying_hunger, nourishment … [UsedFor< eating_hamburger; UsedFor< having_lunch] → **gone** (members merged away 0; match J=0.00)
- feeling_good_about_yourself, improving_health, keeping_fit, training, keeping_in_shape … [UsedFor< getting_exercise; UsedFor< exercising] → **survives_selection** (members merged away 0; match J=0.33)
- ballpoint_pen, lamp, calculator, calendar_pad, telephone, clip … [AtLocation> desk; AtLocation> backpack; AtLocation> desk_drawer] → **survives_selection** (members merged away 1; match J=0.58)
- warmth, cooking_food, keeping_warm, burning_wood, creating_light, making_light … [UsedFor< starting_fire; UsedFor< lighting_fire; UsedFor< starting_flame_or_fire] → **survives_selection** (members merged away 0; match J=0.71)
- birthday, christmas, showing_affection, showing_love, celebrating_birthday … [UsedFor< giving_gift; UsedFor< buying_presents_for_others] → **survives_selection** (members merged away 1; match J=0.44)
- surprising, showing_love, saying_thankyou, making_yourself_happy, celebrating_birthday … [UsedFor< buying_for_loved_one; UsedFor< buying_presents_for_others] → **survives_selection** (members merged away 0; match J=0.40)
- prayer, weddings, praying, worship, worshipping, get_married_in … [UsedFor< church; UsedFor< temple; UsedFor< chapel] → **gone** (members merged away 2; match J=0.00)
- guilt, grief, guilty_conscience, going_to_jail, remorse, feelings_of_guilt … [Causes< killing; Causes< killing_people; Causes< getting_away_with_crime] → **found_not_significant** (members merged away 1; match J=0.50)
- make_clothes, make_clothing, making_clothing, making_clothes, making_curtains, making_cloth … [UsedFor< textile; UsedFor< cloth; UsedFor< fabric] → **gone** (members merged away 3; match J=0.00)
- indigestion, gas, illness, heartburn, upset_stomach, flatulence … [Causes< eating_dinner; Causes< eating_in_fast_food_restaurant; Causes< eating_quickly] → **survives_profile** (members merged away 1; match J=0.57)
- fly_kite, tie_shoes, flying_kite, tie_knot … [CapableOf< child; UsedFor< string] → **gone** (members merged away 1; match J=0.00)

## Merged groups surviving the selection control (32)

By relation types in frame: {1: 28, 2: 4}; by independent anchor neighbourhoods: {1: 24, 2: 7, 3: 1}

### ≥ 2 relation types and ≥ 2 independent neighbourhoods (1)

- **m3** n=31, partly_named, relation types 2, anchor classes 4, independent neighbourhoods 2: accordion(+1), acoustic_guitar, balalaika, banjo, bass_baritone, bass_clarinet, bass_fiddle, bassoon, piano(+1), cello, clarinet, clavichord(+1), cornet, drum(+1), fiddle(+1), flute(+1) …
  - frame: AtLocation> band; AtLocation> music_store (= music_shop, musical_instrument_store); AtLocation> orchestra; UsedFor> making_music (= make_music, create_music)
  - profile p=0.0099 sel=0.0099 rep=0.0; profile2 p=0.0099 sel=0.0198 rep=0.05

### Other selection survivors (31)

- **m652** n=7, uncategorised, relation types 1, anchor classes 3, independent neighbourhoods 3: commuter(+2), go_fast(+2), getting_from_one_place_to_another(+2), getting_somewhere(+1), getting_from_to_b, getting_somewhere_fast(+2), going_from_one_place_to_another(+4)
  - frame: UsedFor< freeway (= highway, motorway); UsedFor< riding_bike (= ride_bicycle, ride_bike, riding_bicycle); UsedFor< driving_car (= moving_car, drive_car_on)
  - profile p=0.0099 sel=0.0099 rep=0.0; profile2 p=0.0099 sel=0.0099 rep=0.0
- **m1039** n=25, crosscutting, relation types 1, anchor classes 4, independent neighbourhoods 2: address_label(+1), calculator(+1), calendar_book(+1), calendar_pad, clip, correction_fluid, desk_tray, electric_pencil_sharpener, eraser(+1), glue_stick, highlighter(+1), highlighter_pen, label_maker(+1), staples(+1), notepad(+1), paper_clip(+2) …
  - frame: AtLocation> desk; AtLocation> desk_drawer; AtLocation> office; AtLocation> office_supply_store (= stationary_store)
  - profile p=0.0099 sel=0.0198 rep=0.0; profile2 p=0.0099 sel=0.0297 rep=0.0
- **m75** n=9, uncategorised, relation types 1, anchor classes 2, independent neighbourhoods 2: log_on, dial_up, turn_on_computer(+3), connect_to_internet(+1), buy_computer, have_computer(+2), have_modem, log_on_to_computer(+1), start_web_browser(+1)
  - frame: HasPrerequisite< getting_onto_web (= get_onto_web, log_on_to_internet, accessing_internet); HasPrerequisite< go_on_internet (= use_internet)
  - profile p=0.0099 sel=0.0099 rep=0.0; profile2 p=0.0099 sel=0.0198 rep=0.0
- **m88** n=8, crosscutting, relation types 1, anchor classes 2, independent neighbourhoods 2: register(+3), pay_tuition, apply(+2), registration(+1), sign_up_for_class(+1), enroll_in_one, enroll_in_school(+1), go_to_university(+1)
  - frame: HasPrerequisite< take_course (= take_classes); HasPrerequisite< attending_class (= attend_classes, attend_class)
  - profile p=0.0099 sel=0.0099 rep=0.0; profile2 p=0.0099 sel=0.0495 rep=0.0
- **m393** n=8, uncategorised, relation types 1, anchor classes 3, independent neighbourhoods 2: start_car(+2), turn_key(+2), buy_car(+1), find_car_keys, steal_car, get_keys(+1), have_car(+1), stay_sober
  - frame: HasPrerequisite< drive (= motor); HasPrerequisite< drive_to_work (= driving_to_work); HasPrerequisite< go_for_drive (= drive_away)
  - profile p=0.0099 sel=0.0099 rep=0.0; profile2 p=0.0099 sel=0.0495 rep=0.0
- **m191** n=6, crosscutting, relation types 1, anchor classes 2, independent neighbourhoods 2: appearance(+2), smell(+3), cleanliness(+3), looking_nice(+2), hygeine(+1), good_hygene
  - frame: UsedFor< clean_clothes (= cleaning_clothes, clothes_cleaned, cleaning_clothing, getting_clothes_clean); UsedFor< getting_clean (= being_clean)
  - profile p=0.0099 sel=0.0099 rep=0.0; profile2 p=0.0099 sel=0.0099 rep=0.0
- **m408** n=6, uncategorised, relation types 1, anchor classes 3, independent neighbourhoods 2: improving_health(+2), keeping_fit(+2), getting_into_shape(+1), maintaining_health(+3), getting_cardiovascular_exercise(+1), preparing_for_race
  - frame: UsedFor< going_for_run (= going_for_jog, go_for_run); UsedFor< jogging; UsedFor< playing_tennis (= tennis_game, play_tennis)
  - profile p=0.0099 sel=0.0099 rep=0.0; profile2 p=0.0099 sel=0.0099 rep=0.0
- **m268** n=9, uncategorised, relation types 2, anchor classes 2, independent neighbourhoods 1: dreams, refreshing(+2), dreaming, feeling_rested(+3), no_longer_tired, refreshment(+1), becoming_less_tired, healing(+1), restoring_energy(+2)
  - frame: Causes< sleeping (= falling_asleep, napping, taking_nap); Causes< resting (= getting_rest, having_rest); UsedFor< resting (= getting_rest, having_rest)
  - profile p=0.0099 sel=0.0099 rep=0.0; profile2 p=0.0099 sel=0.0099 rep=0.01
- **m420** n=9, uncategorised, relation types 2, anchor classes 2, independent neighbourhoods 1: fitness(+1), good_health(+1), pulling_muscle(+1), better_health(+2), shortness_of_breath(+4), become_stronger(+3), physical_fitness(+1), increased_heart_rate(+3), thirsty(+2)
  - frame: Causes< exercise (= physical_activity, exercising, physical_exertion); Causes< getting_exercise (= getting_physical_activity, getting_excercise, get_exercise); HasSubevent< getting_exercise (= getting_physical_activity, getting_excercise, get_exercise)
  - profile p=0.0099 sel=0.0099 rep=0.0; profile2 p=0.0099 sel=0.0099 rep=0.0
- **m200** n=8, crosscutting, relation types 2, anchor classes 3, independent neighbourhoods 1: warmth(+1), destruction(+1), burning(+2), heat_source(+4), burn(+3), getting_warm(+1), burning_fuel(+1), keeping_warm(+2)
  - frame: Causes< starting_fire (= make_fire, start_fire, creating_fire, build_fire…); Causes< lighting_fire (= light_fire, ignite); UsedFor< starting_flame_or_fire (= creating_flame)
  - profile p=0.0099 sel=0.0099 rep=0.0; profile2 p=0.0099 sel=0.0099 rep=0.0
- **m2** n=40, crosscutting, relation types 1, anchor classes 2, independent neighbourhoods 1: mess(+1), printer(+1), waste_bin(+4), trash_can(+4), lamp(+1), cup_of_coffee(+1), calculator(+1), calendar_book(+1), calendar_pad, card_case, chairs(+1), clip, correction_fluid, desk_tray, notebook, file_cabinet(+1) …
  - frame: AtLocation> desk; AtLocation> office
  - profile p=0.0099 sel=0.0099 rep=0.0; profile2 p=0.0099 sel=0.0099 rep=0.0
- **m1** n=38, crosscutting, relation types 1, anchor classes 2, independent neighbourhoods 1: flat(+1), stranger(+1), pub(+1), cafe, court(+1), movie_theater(+1), parking_lot(+1), avenue, dentist(+1), barber_shop(+1), graveyard(+1), boulevard(+1), dental_office(+1), diner(+1), circular_route, city_hall …
  - frame: AtLocation> city; AtLocation> town (= community)
  - profile p=0.0099 sel=0.0099 rep=0.0; profile2 p=0.0099 sel=0.0198 rep=0.0
- **m18** n=24, crosscutting, relation types 1, anchor classes 3, independent neighbourhoods 1: movie_house, waste_bin(+4), movie_theater(+1), parking_lot(+1), barber_shop(+1), beauty_salon(+3), salon, booking_office, deli_store(+1), jeans(+1), electronics_store, fast_food_restaurant_counter(+1), five_and_ten_store, gourmet_shop, health_food_store, large_food_store(+1) …
  - frame: AtLocation> city; AtLocation> mall (= malls); AtLocation> shopping_mall (= shopping_center, shopping_centre)
  - profile p=0.0099 sel=0.0198 rep=0.0; profile2 p=0.0099 sel=0.0396 rep=0.0
- **m12** n=19, crosscutting, relation types 1, anchor classes 2, independent neighbourhoods 1: texas, it's_natural_habitat, indiana, farm_yard(+3), idaho, ohio, barn(+1), stew, corral, county_fair, cow_barn(+1), cow_pasture, cowshed, dairy_farm, farmer's_pasture, feed_lot …
  - frame: AtLocation< cow (= cattle, cows); AtLocation< heifer
  - profile p=0.0099 sel=0.0099 rep=0.0; profile2 p=0.0099 sel=0.0099 rep=0.0
- **m28** n=17, crosscutting, relation types 1, anchor classes 2, independent neighbourhoods 1: wild(+1), it's_natural_habitat, pet_shop(+3), forrest, nature(+2), new_mexico, louisiana(+1), cage, tropics(+1), africa(+1), dessert(+2), creek, tropical_forest(+1), amazon, herpetarium, warm_room(+1) …
  - frame: AtLocation< lizard (= lizards); AtLocation< snake (= snakes)
  - profile p=0.0099 sel=0.0099 rep=0.0; profile2 p=0.0099 sel=0.0099 rep=0.0
- **m91** n=11, uncategorised, relation types 1, anchor classes 3, independent neighbourhoods 1: health_insurance(+1), visit_doctor(+3), make_appointment(+1), going_to_doctor(+3), go_to_doctor(+2), go_see_doctor(+2), take_off_clothes(+5), call_doctor, see_doctor(+1), schedule_appointment_with_doctor, wear_clean_underwear
  - frame: HasPrerequisite< having_physical_exam (= having_physical_examination, have_physical_exam, have_physical_examination); HasPrerequisite< having_checkup (= have_checkup, get_checkup, getting_checkup); HasPrerequisite< have_examination (= examination)
  - profile p=0.0099 sel=0.0099 rep=0.0; profile2 p=0.0099 sel=0.0099 rep=0.0
- **m111** n=11, uncategorised, relation types 1, anchor classes 3, independent neighbourhoods 1: heat_water(+2), hot_water(+1), soap_and_water(+1), use_soap(+1), use_water(+1), get_naked(+1), turn_on_water(+1), take_clothes_off(+3), water_and_soap(+2), enter_bathroom(+1), undress_first
  - frame: HasPrerequisite< take_shower (= taking_shower, go_to_shower); HasPrerequisite< having_bath (= bath, have_bath); HasPrerequisite< have_shower (= having_shower, get_shower)
  - profile p=0.0099 sel=0.0099 rep=0.0; profile2 p=0.0099 sel=0.0099 rep=0.0
- **m80** n=10, uncategorised, relation types 1, anchor classes 2, independent neighbourhoods 1: popcorn(+1), go_to_movies(+1), buy_popcorn, make_popcorn, go_to_cinema(+5), go_to_theater(+1), put_on_glasses(+3), near_tv, rent_movie(+2), ability_to_see(+1)
  - frame: HasPrerequisite< watch_movie (= see_movie, watch_film, go_see_film); HasPrerequisite< enjoy_film (= enjoy_movie, enjoying_film, enjoying_movie)
  - profile p=0.0099 sel=0.0099 rep=0.0; profile2 p=0.0099 sel=0.0099 rep=0.0
- **m70** n=9, partly_named, relation types 1, anchor classes 2, independent neighbourhoods 1: indigestion, gas(+1), nausea, gain_weight(+2), feeling_full(+1), getting_full(+2), heartburn, making_less_hungry(+1), being_less_hungry(+2)
  - frame: Causes< eating (= ingest_food); Causes< eating_hamburger (= eat_hamburger, eat_burger)
  - profile p=0.0099 sel=0.0099 rep=0.0; profile2 p=0.0099 sel=0.0099 rep=0.03
- **m98** n=9, uncategorised, relation types 1, anchor classes 2, independent neighbourhoods 1: military(+1), soldier(+1), battle_enemy(+1), prepare_army(+2), have_army, get_weapons(+1), know_where_enemy, make_enemy, use_weapon(+1)
  - frame: HasPrerequisite< fight_enemy (= attacking_enemy, fighting_enemy, attack_enemy); HasPrerequisite< fight_war (= wage_war)
  - profile p=0.0099 sel=0.0099 rep=0.0; profile2 p=0.0099 sel=0.0198 rep=0.0
- **m233** n=9, uncategorised, relation types 1, anchor classes 3, independent neighbourhoods 1: birthday(+1), christmas, express_love(+5), kindness(+2), make_people_happy(+2), saying_thankyou(+4), celebrating_anniversary, celebrating_birthday(+1), celebrating_special_occasion(+2)
  - frame: UsedFor< giving_gift (= bring_gift); UsedFor< buying_for_loved_one (= buy_for_loved_one); UsedFor< buying_presents_for_others (= buy_presents_for_others)
  - profile p=0.0099 sel=0.0099 rep=0.0; profile2 p=0.0099 sel=0.0099 rep=0.0
- **m96** n=8, uncategorised, relation types 1, anchor classes 2, independent neighbourhoods 1: bathing_suit(+3), go_to_beach(+1), take_off_clothes(+5), go_to_swimming_pool, go_to_pool(+2), go_to_lake, put_on_bathing_suit(+2), stay_away_from_sharks
  - frame: HasPrerequisite< swim (= go_swimming, swiming); HasPrerequisite< going_for_swim (= go_for_swim)
  - profile p=0.0099 sel=0.0099 rep=0.0; profile2 p=0.0099 sel=0.0495 rep=0.0
- **m199** n=8, uncategorised, relation types 1, anchor classes 3, independent neighbourhoods 1: scissors(+1), go_to_hairdresser(+2), decide_how_want_cut, go_to_barber(+1), go_to_barber_shop, sharpen_scissors, visit_barber(+1), go_to_hair_salon
  - frame: HasPrerequisite< cut_hair (= trim_hair, trimming_hair); HasPrerequisite< have_haircut (= haircut, get_haircut); HasPrerequisite< go_to_get_haircut (= going_to_get_haircut)
  - profile p=0.0099 sel=0.0099 rep=0.0; profile2 p=0.0099 sel=0.0495 rep=0.0
- **m156** n=7, uncategorised, relation types 1, anchor classes 2, independent neighbourhoods 1: becoming_tired(+2), sore_feet(+2), shortness_of_breath(+4), cramps(+5), increased_heart_rate(+3), leg_cramps, getting_out_of_breath(+1)
  - frame: Causes< running (= sprinting); Causes< going_for_run (= going_for_jog, go_for_run)
  - profile p=0.0099 sel=0.0099 rep=0.0; profile2 p=0.0099 sel=0.0495 rep=0.0
- **m195** n=7, uncategorised, relation types 1, anchor classes 2, independent neighbourhoods 1: good_health(+1), being_healthy(+2), improving_health(+2), keeping_fit(+2), training, strengthening_heart(+1), staying_physically_fit(+1)
  - frame: UsedFor< getting_exercise (= getting_physical_activity, getting_excercise, get_exercise); UsedFor< going_for_run (= going_for_jog, go_for_run)
  - profile p=0.0099 sel=0.0099 rep=0.0; profile2 p=0.0099 sel=0.0099 rep=0.0
- **m240** n=7, uncategorised, relation types 1, anchor classes 2, independent neighbourhoods 1: cleanliness(+3), smell_nice(+4), removing_stains(+1), impressing_others(+2), getting_rid_of_dirt(+1), making_clothes_look_nicer, making_clothes_smell_better
  - frame: UsedFor< clean_clothes (= cleaning_clothes, clothes_cleaned, cleaning_clothing, getting_clothes_clean); UsedFor< washing_clothes (= clean_laundry, making_clothes_clean)
  - profile p=0.0099 sel=0.0099 rep=0.0; profile2 p=0.0099 sel=0.0099 rep=0.0
- **m140** n=6, partly_named, relation types 1, anchor classes 2, independent neighbourhoods 1: catch(+1), roll(+2), kick(+2), throwing(+3), bouncing(+1), play_with_dog(+1)
  - frame: UsedFor< ball; UsedFor< toy_ball
  - profile p=0.0099 sel=0.0099 rep=0.0; profile2 p=0.0099 sel=0.0099 rep=0.0
- **m164** n=6, uncategorised, relation types 1, anchor classes 2, independent neighbourhoods 1: safety(+1), arrive_at_destination(+3), avoiding_accident(+3), not_moving, obeying_traffic_laws, stopping_at_intersection
  - frame: UsedFor< stopping_bicycle (= stop_bicycle, get_off_bicycle); UsedFor< stopping_car
  - profile p=0.0099 sel=0.0099 rep=0.0; profile2 p=0.0099 sel=0.0099 rep=0.0
- **m227** n=6, crosscutting, relation types 1, anchor classes 2, independent neighbourhoods 1: destruction(+1), illumination(+1), wood_burns(+2), cooking_food(+1), keeping_warm(+2), creating_light(+1)
  - frame: UsedFor< starting_fire (= make_fire, start_fire, creating_fire, build_fire…); UsedFor< starting_flame_or_fire (= creating_flame)
  - profile p=0.0099 sel=0.0099 rep=0.0; profile2 p=0.0099 sel=0.0099 rep=0.0
- **m273** n=6, uncategorised, relation types 1, anchor classes 2, independent neighbourhoods 1: heal(+2), feeling_rested(+3), recover(+1), rejuvenating(+1), taking_break_from_work(+1), letting_body_recover(+2)
  - frame: UsedFor< sleeping (= falling_asleep, napping, taking_nap); UsedFor< resting (= getting_rest, having_rest)
  - profile p=0.0099 sel=0.0099 rep=0.0; profile2 p=0.0099 sel=0.0099 rep=0.0
- **m653** n=6, partly_named, relation types 1, anchor classes 4, independent neighbourhoods 1: cleanliness(+3), feeling_clean(+1), washing, washing_body(+2), keeping_clean(+1), removing_dirt_from_body
  - frame: UsedFor< take_shower (= taking_shower, go_to_shower); UsedFor< taking_bath (= go_for_bath); UsedFor< bathing (= baths); UsedFor< have_shower (= having_shower, get_shower)
  - profile p=0.0099 sel=0.0099 rep=0.0; profile2 p=0.0099 sel=0.0099 rep=0.0

### Pass profile nulls but not the selection control, ≥ 2 relation types and ≥ 2 independent neighbourhoods (61; largest 25)

- **m52** n=13, crosscutting, relation types 2, anchor classes 3, independent neighbourhoods 3: barber_comb, blow_dryer(+2), curling_iron, gel, hairbrush(+1), hair_care_article, hair_clip, hair_dryer(+1), hair_gel, hair_roller, hair_shaping_gel, sculpting_gel, shampoo_and_conditioner
  - frame: AtLocation> bathroom (= toilet); AtLocation> beauty_salon (= beauty_parlor, beauty_shop, beauty_salons); UsedFor> styling_hair (= style_hair, making_hair_look_nice)
  - profile p=0.0099 sel=1.0 rep=0.0; profile2 p=0.0099 sel=1.0 rep=0.0
- **m247** n=11, crosscutting, relation types 2, anchor classes 3, independent neighbourhoods 2: family_room, beanbag(+1), chess_set, cards, chess_board(+1), chess_pawn, kite(+1), sports_ball, toy_ball, toy_car, toy_marble
  - frame: AtLocation> toy_store (= toystore, toy_shop); UsedFor> play_game (= play_games, playing_game); UsedFor> playing_games (= game_playing)
  - profile p=0.0099 sel=0.6832 rep=0.0; profile2 p=0.0099 sel=1.0 rep=0.0
- **m100** n=7, uncategorised, relation types 2, anchor classes 2, independent neighbourhoods 2: calendar_pad, mechanical_pencil, memo_pad(+1), pocket_notebook(+2), pocket_sized_notebook, self_adhesive_label, tear_off_calendar
  - frame: AtLocation> office_supply_store (= stationary_store); UsedFor> making_notes (= scribbling_notes, writing_note, jotting_notes, writing_notes)
  - profile p=0.0099 sel=1.0 rep=0.0; profile2 p=0.0099 sel=1.0 rep=0.0
- **m151** n=7, crosscutting, relation types 2, anchor classes 2, independent neighbourhoods 2: stop(+1), parking_lot(+1), boarding_room, dental_office(+1), bus_shelter, dentist_office(+1), subway_stop(+1)
  - frame: AtLocation> city; UsedFor> waiting (= wait)
  - profile p=0.0099 sel=1.0 rep=0.0; profile2 p=0.0099 sel=1.0 rep=0.02
- **m203** n=7, crosscutting, relation types 2, anchor classes 2, independent neighbourhoods 2: movie_house, seafood_restaurant(+1), movie_theater(+1), bazaar, industry, parking_area(+2), vending_stand
  - frame: AtLocation> city; UsedFor> making_money (= make_money, making_profit)
  - profile p=0.0099 sel=1.0 rep=0.0; profile2 p=0.0099 sel=1.0 rep=0.01
- **m206** n=7, crosscutting, relation types 2, anchor classes 2, independent neighbourhoods 2: envelope, printer(+1), ballpoint_pen, lead_pencil, quill_brush, typewriter(+1), steel_pen
  - frame: AtLocation> desk; UsedFor> writing_letter (= write_letter, send_letter)
  - profile p=0.0099 sel=1.0 rep=0.0; profile2 p=0.0099 sel=1.0 rep=0.0
- **m246** n=7, named, relation types 2, anchor classes 4, independent neighbourhoods 3: pie(+1), chicken(+1), turkey(+1), bread, pizza(+1), cookies(+1), steak(+1)
  - frame: AtLocation> plate; AtLocation> refrigerator (= fridge); AtLocation> oven (= ovens); HasProperty> baked_in_oven (= baked_in_ovens)
  - profile p=0.0099 sel=1.0 rep=0.0; profile2 p=0.0099 sel=1.0 rep=0.0
- **m317** n=7, named, relation types 2, anchor classes 4, independent neighbourhoods 4: dental_floss(+1), fluoride_mouthwash, gel_toothpaste, hair_care_article, mouthwash, toothbrush(+1), toothpaste(+1)
  - frame: AtLocation> bathroom (= toilet); AtLocation> drug_store (= drugstore, pharmacy); AtLocation> bathroom_cabinet; UsedFor> breathe_fresh_air (= fresh_breath, freshen_breath)
  - profile p=0.0099 sel=1.0 rep=0.0; profile2 p=0.0099 sel=1.0 rep=0.0
- **m89** n=6, named, relation types 2, anchor classes 4, independent neighbourhoods 2: bureau(+1), chest, clothing_shelf, wardrobe(+1), chest_of_drawers, closet_for_clothes
  - frame: AtLocation> bedroom (= bedrooms); UsedFor> clothing_closet (= clothes_closet, store_clothing); UsedFor> storing_clothes (= store_cloths); UsedFor> storing_clothing (= holding_clothes)
  - profile p=0.0099 sel=1.0 rep=0.0; profile2 p=0.0099 sel=1.0 rep=0.0
- **m160** n=6, partly_named, relation types 2, anchor classes 5, independent neighbourhoods 3: drill(+1), hammer(+1), phillips_head_screwdriver, phillips_screwdriver, power_screwdriver, tool
  - frame: AtLocation> garage (= garages); AtLocation> hardware_store (= hardware_shop); AtLocation> tool_box (= toolbox, toolkit); AtLocation> toolbelt (= tool_chest); UsedFor> removing_screws (= unscrew)
  - profile p=0.0099 sel=1.0 rep=0.0; profile2 p=0.0099 sel=1.0 rep=0.0
- **m281** n=6, named, relation types 2, anchor classes 2, independent neighbourhoods 2: hat, shirt, jeans(+1), linen(+1), shirts, t_shirt(+1)
  - frame: AtLocation> closet (= closets); UsedFor> wearing (= wearer)
  - profile p=0.0099 sel=1.0 rep=0.0; profile2 p=0.0099 sel=1.0 rep=0.0
- **m453** n=6, partly_named, relation types 2, anchor classes 2, independent neighbourhoods 2: baseball(+1), puck, rod, sports_bat, tennis_ball(+1), arrow(+1)
  - frame: AtLocation> sporting_goods_store (= sporting_goods_stores); UsedFor> hit (= hitting)
  - profile p=0.0099 sel=1.0 rep=0.0; profile2 p=0.0099 sel=1.0 rep=0.0
- **m508** n=6, partly_named, relation types 2, anchor classes 4, independent neighbourhoods 3: notebook, index_card(+1), notepad(+1), pad, pocket_notebook(+2), ring_binder
  - frame: AtLocation> backpack (= backpacks); AtLocation> office; UsedFor> take_notes (= taking_notes, keeping_notes); UsedFor> write_note (= write_notes_on)
  - profile p=0.0099 sel=1.0 rep=0.0; profile2 p=0.0099 sel=1.0 rep=0.0
- **m526** n=6, partly_named, relation types 2, anchor classes 5, independent neighbourhoods 2: ballpoint_pen, marker(+1), mechanical_pencil, paper_punch, quill_brush, tape_dispenser
  - frame: AtLocation> desk; AtLocation> drawer; AtLocation> office_supply_store (= stationary_store); UsedFor> writing (= literacy); UsedFor> drawing (= draw, make_drawings)
  - profile p=0.0099 sel=1.0 rep=0.0; profile2 p=0.0099 sel=1.0 rep=0.0
- **m155** n=5, partly_named, relation types 2, anchor classes 4, independent neighbourhoods 3: birth_control_pill, condom(+1), contraceptive(+2), pill(+1), rubber
  - frame: AtLocation> medicine_chest (= medicine_cabinet); AtLocation> drug_store (= drugstore, pharmacy); UsedFor> prevent_pregnancy (= avoid_pregnancy, avoiding_pregnancy, preventing_pregnancy); UsedFor> prevent_conception (= prevent_unwanted_pregnancy)
  - profile p=0.0099 sel=1.0 rep=0.0; profile2 p=0.0099 sel=1.0 rep=0.0
- **m213** n=5, partly_named, relation types 2, anchor classes 6, independent neighbourhoods 3: check(+1), cash_token(+1), credit_card(+1), dollar_bill, penny
  - frame: AtLocation> wallet; AtLocation> purse (= handbag); AtLocation> bank (= banking, banks, bankers); AtLocation> pocket (= pockets); UsedFor> pay (= make_payments); UsedFor> paying (= payment)
  - profile p=0.0099 sel=1.0 rep=0.0; profile2 p=0.0099 sel=1.0 rep=0.01
- **m263** n=5, partly_named, relation types 2, anchor classes 2, independent neighbourhoods 2: duvet, hide_bed(+1), mat, ottoman, sofabed(+2)
  - frame: AtLocation> living_room (= livingroom, living_rooms); UsedFor> sleep (= take_nap)
  - profile p=0.0099 sel=1.0 rep=0.0; profile2 p=0.0099 sel=1.0 rep=0.01
- **m364** n=5, partly_named, relation types 2, anchor classes 6, independent neighbourhoods 2: box_office, ticket_booth(+2), movie_ticket(+1), theater_seat(+2), ticket_office(+1)
  - frame: AtLocation> theater (= theatre, theatres); AtLocation> movies (= cinema, motion_pictures, films); AtLocation> movie_theatre (= theaters); AtLocation> movie_theater (= movie_theaters); UsedFor> selling_tickets; UsedFor> buy_ticket (= book_tickets, buying_tickets, buy_tickets, purchase_tickets…)
  - profile p=0.0099 sel=1.0 rep=0.0; profile2 p=0.0099 sel=1.0 rep=0.03
- **m426** n=5, crosscutting, relation types 2, anchor classes 2, independent neighbourhoods 2: cafeteria(+1), chalk(+1), janitor, pencil_sharpener(+2), principal
  - frame: AtLocation> school (= schools); ReceivesAction> found_in_school (= found_at_school, found_in_classroom)
  - profile p=0.0099 sel=0.6931 rep=0.0; profile2 p=0.0099 sel=1.0 rep=0.0
- **m495** n=5, partly_named, relation types 2, anchor classes 3, independent neighbourhoods 2: blanket(+1), comforter, matress(+1), pillow_case(+1), sheet
  - frame: AtLocation> bedroom (= bedrooms); AtLocation> linen_closet (= linen_cupboard); ReceivesAction> found_on_bed
  - profile p=0.0099 sel=0.6931 rep=0.0; profile2 p=0.0099 sel=1.0 rep=0.0
- **m728** n=5, uncategorised, relation types 2, anchor classes 5, independent neighbourhoods 4: becoming_tired(+2), become_tired(+1), getting_tired_legs(+3), sore_feet(+2), sore_legs
  - frame: Causes< dance (= dancing); Causes< hiking (= hikers); Causes< standing_in_line (= take_place_in_line, standing_in_queue, standing_on_line); Causes< going_for_run (= going_for_jog, go_for_run); Causes< going_for_walk (= take_walk_outside); HasSubevent< going_for_run (= going_for_jog, go_for_run)
  - profile p=0.0099 sel=0.1782 rep=0.0; profile2 p=0.0099 sel=0.8911 rep=0.04
- **m914** n=5, partly_named, relation types 2, anchor classes 3, independent neighbourhoods 2: hockey_puck(+1), hockey_stick(+1), puck, skates(+1), ice_skater(+2)
  - frame: AtLocation> sporting_goods_store (= sporting_goods_stores); AtLocation> hockey_game; HasPrerequisite< playing_hockey (= play_hockey)
  - profile p=0.0099 sel=1.0 rep=0.0; profile2 p=0.0099 sel=1.0 rep=0.0
- **m217** n=4, crosscutting, relation types 2, anchor classes 4, independent neighbourhoods 2: electric_toothbrush(+1), gel_toothpaste, tartar_control_toothpaste, toothbrush_head
  - frame: AtLocation> medicine_chest (= medicine_cabinet); UsedFor> toothbrush (= brushing_teeth); UsedFor> clean_teeth (= getting_teeth_cleaned, cleaning_teeth); UsedFor> brush_teeth
  - profile p=0.0099 sel=1.0 rep=0.0; profile2 p=0.0099 sel=1.0 rep=0.0
- **m239** n=4, crosscutting, relation types 2, anchor classes 4, independent neighbourhoods 2: better_health(+2), living_longer(+1), being_healthy(+2), long_life(+2)
  - frame: Causes< eating_healthily (= eating_well); Causes< stay_fit (= staying_in_shape, staying_fit, keeps_fit); Causes< making_sure_re_healthy (= knowing_if_re_healthy); UsedFor< losing_weight (= weight_loss, loose_weight)
  - profile p=0.0099 sel=0.7624 rep=0.0; profile2 p=0.0099 sel=1.0 rep=0.0
- **m265** n=4, uncategorised, relation types 2, anchor classes 2, independent neighbourhoods 2: barber_comb, razor(+1), haircutting_scissors, hairdresser_chair
  - frame: AtLocation> barber_shop (= barbershop); UsedFor> cutting_hair (= get_hair_cut, having_hair_cut, hair_cut)
  - profile p=0.0099 sel=1.0 rep=0.0; profile2 p=0.0099 sel=1.0 rep=0.0

## Anomaly 18 (0 merged groups with ≥ 2 of its activities; 0 survive selection, 0 survive profile)

