# Profile-preserving nulls, re-mined (member cap 30 typed features)

100 null graphs per mode, every one mined with the identical procedure. No edges or labels added.

| null | what is kept besides per-relation in/out counts, dataset, two-way pairs | typed incidences of the real graph still present |
|---|---|---|
| relation | nothing else (two-way pairs not kept) | 0.6% |
| strict | log2 degree class of both ends | 4.3% |
| profile | each end's dominant (relation, direction) + log2 typed degree | 13.3% |
| profile2 | each end's top-2 (relation, direction) + log2 typed degree | 31.7% |

profile: 223 endpoint classes; 3.7% of typed one-way links and 6.7% of two-way pairs sit in strata of one (cannot move).

profile2: 1879 endpoint classes; 12.1% of typed one-way links and 14.4% of two-way pairs sit in strata of one (cannot move).

## Group counts: real vs re-mined nulls (null mean [min–max])

| | real | relation | strict | profile | profile2 |
|---|---|---|---|---|---|
| size_ge_4 | 1511 | 751.7 [658–834] | 355.0 [300–415] | 569.8 [532–613] | 772.4 [730–820] |
| size_ge_6 | 571 | 200.2 [148–255] | 59.9 [46–81] | 145.7 [126–168] | 244.6 [222–269] |
| size_ge_10 | 155 | 15.3 [4–31] | 4.2 [1–9] | 14.2 [8–21] | 38.0 [29–50] |
| size_ge_20 | 18 | 0.0 [0–1] | 0.2 [0–1] | 1.1 [1–2] | 2.3 [2–4] |
| named_ge_6 | 42 | 0.3 [0–2] | 1.4 [0–4] | 3.6 [0–9] | 20.2 [14–28] |
| partly_named_ge_6 | 106 | 34.6 [18–56] | 10.6 [5–16] | 26.4 [15–41] | 50.3 [34–73] |
| uncategorised_ge_6 | 147 | 14.7 [5–26] | 10.5 [3–23] | 34.5 [24–48] | 54.8 [46–66] |
| crosscutting_ge_6 | 276 | 150.6 [104–192] | 37.5 [26–51] | 81.2 [61–106] | 119.3 [102–139] |
| unnamed_ge_6 | 423 | 165.3 [118–209] | 48.0 [33–66] | 115.7 [95–144] | 174.1 [154–199] |

## Shapes: groups of size ≥ 6 (null mean) and largest group (null mean of the largest)

| shape | relation profile | real ≥6 | real unnamed ≥6 | real max | relation ≥6 / unnamed / max | strict ≥6 / unnamed / max | profile ≥6 / unnamed / max | profile2 ≥6 / unnamed / max |
|---|---|---|---|---|---|---|---|---|
| 30 | AtLocation> 99% | 272 | 196 | 50 | 69.2 / 52.8 / 11.7 | 33.4 / 27.0 / 11.0 | 60.0 / 47.0 / 15.8 | 83.0 / 60.6 / 15.9 |
| 18 | AtLocation< 94%, AtLocation> 5% | 81 | 62 | 23 | 103.3 / 89.0 / 14.2 | 6.1 / 5.0 / 7.3 | 42.6 / 31.9 / 9.9 | 72.5 / 52.6 / 12.8 |
| 26 | UsedFor> 75%, AtLocation> 24% | 67 | 29 | 27 | 14.1 / 9.8 / 9.8 | 10.6 / 8.4 / 10.6 | 17.1 / 12.8 / 14.2 | 38.9 / 19.1 / 27.0 |
| 2 | HasPrerequisite< 98% | 40 | 40 | 11 | 0.0 / 0.0 / 0.4 | 0.0 / 0.0 / 0.2 | 0.0 / 0.0 / 1.4 | 0.0 / 0.0 / 4.3 |
| 4 | Causes> 75%, UsedFor> 23% | 24 | 24 | 12 | 8.8 / 8.8 / 8.7 | 5.5 / 5.4 / 8.1 | 11.5 / 11.3 / 9.8 | 14.8 / 14.7 / 10.0 |
| 7 | HasPrerequisite> 51%, Causes> 49% | 11 | 11 | 11 | 0.0 / 0.0 / 1.8 | 0.3 / 0.3 / 4.9 | 5.2 / 5.2 / 8.3 | 6.4 / 6.4 / 11.0 |
| 31 | CapableOf< 96% | 9 | 9 | 16 | 0.1 / 0.1 / 3.9 | 0.1 / 0.1 / 4.2 | 0.4 / 0.4 / 5.1 | 4.8 / 4.6 / 13.7 |
| 32 | UsedFor< 98% | 9 | 8 | 7 | 0.1 / 0.0 / 2.0 | 0.0 / 0.0 / 0.2 | 0.0 / 0.0 / 0.9 | 0.0 / 0.0 / 2.8 |
| 36 | Causes< 94%, HasSubevent< 5% | 9 | 8 | 11 | 0.0 / 0.0 / 0.5 | 0.0 / 0.0 / 0.2 | 0.0 / 0.0 / 0.5 | 0.0 / 0.0 / 3.8 |
| 10 | HasPrerequisite> 87%, HasLastSubevent> 6% | 8 | 8 | 13 | 0.6 / 0.6 / 5.5 | 0.1 / 0.1 / 3.7 | 0.6 / 0.6 / 5.8 | 2.2 / 2.2 / 11.0 |
| 14 | MotivatedByGoal> 68%, CausesDesire< 32% | 7 | 7 | 8 | 0.2 / 0.2 / 4.5 | 0.1 / 0.1 / 4.3 | 1.5 / 1.5 / 7.5 | 2.7 / 2.7 / 6.2 |
| 16 | HasA< 96% | 5 | 5 | 9 | 1.3 / 1.3 / 9.2 | 0.8 / 0.5 / 5.7 | 1.2 / 1.0 / 6.2 | 3.7 / 2.9 / 8.3 |
| 25 | HasPrerequisite> 50%, UsedFor> 50% | 4 | 4 | 11 | 0.0 / 0.0 / 0.5 | 0.3 / 0.3 / 4.5 | 2.5 / 2.5 / 8.5 | 4.3 / 4.3 / 11.0 |
| 27 | HasProperty> 49%, AtLocation> 48% | 4 | 2 | 8 | 0.0 / 0.0 / 1.5 | 0.0 / 0.0 / 1.2 | 0.0 / 0.0 / 2.9 | 0.9 / 0.0 / 6.1 |
| 29 | AtLocation> 49%, ReceivesAction> 48% | 4 | 0 | 11 | 0.0 / 0.0 / 0.6 | 0.1 / 0.0 / 4.0 | 0.8 / 0.2 / 6.2 | 2.1 / 0.0 / 11.0 |
| 8 | HasPrerequisite> 48%, MotivatedByGoal> 43%, HasSubevent> 6% | 3 | 2 | 8 | 0.1 / 0.1 / 4.4 | 0.0 / 0.0 / 1.4 | 0.0 / 0.0 / 3.3 | 0.0 / 0.0 / 3.8 |

## Survival

- frame support at the p floor under profile, profile2 and reproduced (member Jaccard ≥ 0.5) in ≤ 5% of re-mined nulls: **749** of 1511 groups; by tier {'crosscutting': 236, 'partly_named': 119, 'named': 79, 'uncategorised': 315}
- and, in addition, larger than the largest re-mined null group of the same shape in ≥ 95% of nulls: **89**; by tier {'crosscutting': 17, 'partly_named': 4, 'uncategorised': 68}
- survives_profile by frame kind (kind, >1 relation type): {('distinct', False): 240, ('distinct', True): 91, ('paraphrase', False): 386, ('paraphrase', True): 32}
- survives_selection by frame kind (kind, >1 relation type): {('distinct', False): 21, ('distinct', True): 5, ('paraphrase', False): 61, ('paraphrase', True): 2}
- all groups by frame kind: {('distinct', False): 575, ('distinct', True): 272, ('paraphrase', False): 576, ('paraphrase', True): 88}
- of the 434 groups robust in the earlier run, 282 survive the profile nulls and 58 also the selection control

## Survivors of the selection control, by tier (largest size × min profile z first, ≤ 2 per shape)

### named (0)


### partly_named (4)

- **g11** n=23, partly_named, shape 30, paraphrase frame: apple, pie, cheese, turkey, bad_smell, butter, carrots, carton_of_milk, fresh_vegetables, frozen_foods, fruit, ham, juice, ketchup …
  - frame: AtLocation> fridge; AtLocation> refrigerator
  - support 23; profile z 16.0 (null 2.52), sel p 0.0297, repro 0%, profile2 z 12.8 (null 4.62), sel p 0.0396, repro 0%; strict z 22.3
- **g3** n=36, partly_named, shape 30, distinct frame: accordion, acoustic_guitar, balalaika, banjo, bass_baritone, bass_clarinet, bass_drum, bass_fiddle, bassoon, clarinet, cornet, double_bass, drum, fiddle …
  - frame: AtLocation> band; AtLocation> orchestra; UsedFor> making_music
  - support 36; profile z 15.6 (null 4.87), sel p 0.0099, repro 0%, profile2 z 8.1 (null 20.23), sel p 0.0099, repro 0%; strict z 23.1
- **g208** n=6, partly_named, shape 32, paraphrase frame: rolling, throwing, bouncing, catching, kicking, play_with_dog
  - frame: UsedFor< ball; UsedFor< toy_ball
  - support 6; profile z 11.5 (null 0.25), sel p 0.0099, repro 0%, profile2 z 8.6 (null 0.48), sel p 0.0099, repro 0%; strict z 11.7
- **g397** n=6, partly_named, shape 36, paraphrase frame: bad_breath, indigestion, feeling_full, heartburn, satisfying_hunger, late_for_work
  - frame: Causes< eating_breakfast; Causes< eating_lunch
  - support 6; profile z 10.3 (null 0.29), sel p 0.0099, repro 0%, profile2 z 5.8 (null 1.61), sel p 0.0099, repro 1%; strict z 11.8

### uncategorised (68)

- **g203** n=10, uncategorised, shape 2, paraphrase frame: careful, strike_match, light_match, go_outdoors, get_matches, gather_kindling, rub_two_sticks_together, use_lighter, use_match, use_matches
  - frame: HasPrerequisite< light_fire; HasPrerequisite< start_fire; HasPrerequisite< start_flame_or_fire
  - support 10; profile z 19.4 (null 0.3), sel p 0.0099, repro 0%, profile2 z 12.8 (null 0.56), sel p 0.0099, repro 0%; strict z 19.7
- **g45** n=11, uncategorised, shape 2, distinct frame: go_to_concert, buy_ticket, open_eyes, go_to_theater, go_to_theatre, buy_tickets, buy_tickets_to_concert, buy_ticket_to_concert, go_to_club, buy_concert_ticket, attend_concert
  - frame: HasPrerequisite< watch_musician_perform; HasPrerequisite< see_band
  - support 11; profile z 17.6 (null 0.41), sel p 0.0099, repro 0%, profile2 z 10.8 (null 1.05), sel p 0.0099, repro 0%; strict z 21.6
- **g150** n=11, uncategorised, shape 36, paraphrase frame: indigestion, gas, nausea, feeling_full, full_stomach, gaining_energy, gaining_weight, getting_full, heartburn, making_less_hungry, not_being_hungry
  - frame: Causes< eating; Causes< eating_hamburger; Causes< eating_breakfast
  - support 11; profile z 12.3 (null 1.1), sel p 0.0099, repro 0%, profile2 z 7.4 (null 2.92), sel p 0.0099, repro 0%; strict z 13.2
- **g292** n=6, uncategorised, shape 32, paraphrase frame: buy_hardware, buy_nails, buying_hardware, buying_nails, buying_screws, buying_tools
  - frame: UsedFor< hardware_store; UsedFor< hardware_shop
  - support 6; profile z 12.0 (null 0.0), sel p 0.0099, repro 0%, profile2 z 12.0 (null 0.02), sel p 0.0099, repro 0%; strict z 12.0
- **g246** n=6, uncategorised, shape 32, paraphrase frame: having_hair_cut, getting_haircut, getting_hair_colored, getting_manicure, getting_perm, having_hair_styled
  - frame: UsedFor< salon; UsedFor< hairdressing_salon
  - support 6; profile z 11.8 (null 0.08), sel p 0.0099, repro 0%, profile2 z 11.8 (null 0.11), sel p 0.0099, repro 0%; strict z 11.9
- **g288** n=6, uncategorised, shape 36, paraphrase frame: accomplishment, sore_muscles, falling_down, get_higher, getting_to_top, loss_of_breath
  - frame: Causes< climbing; Causes< climbing_mountain
  - support 6; profile z 11.6 (null 0.22), sel p 0.0099, repro 0%, profile2 z 10.4 (null 0.32), sel p 0.0099, repro 0%; strict z 11.7
- **g607** n=5, uncategorised, shape 34, paraphrase frame: look_different, have_shorter_hair, look_neater, new_hairstyle, shorter_hair
  - frame: Causes< cutting_hair; MotivatedByGoal< cut_hair
  - support 5; profile z 9.8 (null 0.08), sel p 0.0099, repro 0%, profile2 z 9.6 (null 0.2), sel p 0.0198, repro 0%; strict z 9.9
- **g101** n=7, uncategorised, shape 8, distinct frame: watch_television_show, see_favorite_show, see_story, use_television, see_people_play_game, see_particular_program, view_video
  - frame: HasPrerequisite> turn_on_tv; MotivatedByGoal> entertained
  - support 7; profile z 9.6 (null 0.46), sel p 0.0198, repro 0%, profile2 z 5.5 (null 1.36), sel p 0.0297, repro 1%; strict z 13.5

### crosscutting (17)

- **g1** n=50, crosscutting, shape 30, paraphrase frame: flat, stranger, bank, bookshop, sporting_goods_store, pub, cafe, bookstore, court, movie_theater, parking_lot, avenue, back_garden, dentist …
  - frame: AtLocation> city; AtLocation> town
  - support 50; profile z 16.0 (null 7.87), sel p 0.0099, repro 0%, profile2 z 14.3 (null 10.19), sel p 0.0099, repro 0%; strict z 20.0
- **g674** n=25, crosscutting, shape 30, distinct frame: ballpoint_pen, lamp, calculator, calendar_pad, telephone, clip, correction_fluid, desk_tray, notebook, pencil, glue_stick, highlighter, highlighter_pen, keyboard …
  - frame: AtLocation> desk; AtLocation> backpack; AtLocation> desk_drawer; AtLocation> office; AtLocation> desktop
  - support 25; profile z 31.2 (null 0.64), sel p 0.0198, repro 0%, profile2 z 22.3 (null 1.55), sel p 0.0198, repro 0%; strict z 40.3
- **g8** n=23, crosscutting, shape 18, paraphrase frame: fair, texas, america, it's_natural_habitat, indiana, farm_yard, idaho, ohio, stew, barnyard, corral, county_fair, cow_barn, cow_pasture …
  - frame: AtLocation< cow; AtLocation< heifer
  - support 23; profile z 13.5 (null 3.0), sel p 0.0099, repro 0%, profile2 z 9.1 (null 6.34), sel p 0.0198, repro 0%; strict z 19.3
- **g21** n=17, crosscutting, shape 18, distinct frame: wild, pants, group, dictionary, it's_natural_habitat, woods, detroit_zoo, great_outdoors, captivity, wilderness, cage, tropics, rain_forest, possession_of_zoo …
  - frame: AtLocation< lemur; AtLocation< marmoset
  - support 17; profile z 7.6 (null 3.93), sel p 0.0099, repro 0%, profile2 z 6.9 (null 6.17), sel p 0.0495, repro 0%; strict z 14.5
- **g465** n=6, crosscutting, shape 2, paraphrase frame: patient, stand, get_in_line, line_up, wear_comfortable_shoes, find_line
  - frame: HasPrerequisite< wait_turn; HasPrerequisite< stand_in_queue; HasPrerequisite< stand_in_line
  - support 6; profile z 9.9 (null 0.49), sel p 0.0099, repro 0%, profile2 z 8.2 (null 1.89), sel p 0.0297, repro 0%; strict z 11.8
- **g721** n=6, crosscutting, shape 32, paraphrase frame: prayer, weddings, praying, worship, worshipping, get_married_in
  - frame: UsedFor< church; UsedFor< temple; UsedFor< chapel
  - support 6; profile z 11.9 (null 0.07), sel p 0.0099, repro 0%, profile2 z 7.8 (null 0.52), sel p 0.0099, repro 0%; strict z 11.9
- **g234** n=6, crosscutting, shape 36, paraphrase frame: better_health, living_longer, being_healthy, long_life, longer_life, longevity
  - frame: Causes< eating_healthily; Causes< staying_fit
  - support 6; profile z 11.5 (null 0.23), sel p 0.0099, repro 0%, profile2 z 7.7 (null 1.4), sel p 0.0099, repro 0%; strict z 11.7
- **g200** n=7, crosscutting, shape 32, paraphrase frame: baking_bread, baking_cookies, bread, cakes, pizza, cookies, pot_roast
  - frame: AtLocation> oven; UsedFor< baking_oven
  - support 7; profile z 13.7 (null 0.14), sel p 0.0099, repro 0%, profile2 z 6.5 (null 1.12), sel p 0.0099, repro 0%; strict z 13.9

## Selection survivors with distinct (non-paraphrase) frame neighbours

26 groups.

- **g674** n=25, crosscutting, shape 30, distinct frame: ballpoint_pen, lamp, calculator, calendar_pad, telephone, clip, correction_fluid, desk_tray, notebook, pencil, glue_stick, highlighter, highlighter_pen, keyboard …
  - frame: AtLocation> desk; AtLocation> backpack; AtLocation> desk_drawer; AtLocation> office; AtLocation> desktop
  - support 25; profile z 31.2 (null 0.64), sel p 0.0198, repro 0%, profile2 z 22.3 (null 1.55), sel p 0.0198, repro 0%; strict z 40.3
- **g3** n=36, partly_named, shape 30, distinct frame: accordion, acoustic_guitar, balalaika, banjo, bass_baritone, bass_clarinet, bass_drum, bass_fiddle, bassoon, clarinet, cornet, double_bass, drum, fiddle …
  - frame: AtLocation> band; AtLocation> orchestra; UsedFor> making_music
  - support 36; profile z 15.6 (null 4.87), sel p 0.0099, repro 0%, profile2 z 8.1 (null 20.23), sel p 0.0099, repro 0%; strict z 23.1
- **g45** n=11, uncategorised, shape 2, distinct frame: go_to_concert, buy_ticket, open_eyes, go_to_theater, go_to_theatre, buy_tickets, buy_tickets_to_concert, buy_ticket_to_concert, go_to_club, buy_concert_ticket, attend_concert
  - frame: HasPrerequisite< watch_musician_perform; HasPrerequisite< see_band
  - support 11; profile z 17.6 (null 0.41), sel p 0.0099, repro 0%, profile2 z 10.8 (null 1.05), sel p 0.0099, repro 0%; strict z 21.6
- **g21** n=17, crosscutting, shape 18, distinct frame: wild, pants, group, dictionary, it's_natural_habitat, woods, detroit_zoo, great_outdoors, captivity, wilderness, cage, tropics, rain_forest, possession_of_zoo …
  - frame: AtLocation< lemur; AtLocation< marmoset
  - support 17; profile z 7.6 (null 3.93), sel p 0.0099, repro 0%, profile2 z 6.9 (null 6.17), sel p 0.0495, repro 0%; strict z 14.5
- **g98** n=9, uncategorised, shape 2, distinct frame: log_on, dial_up, turn_computer_on, turn_on_computer, connect_to_internet, buy_computer, have_computer, have_modem, log_on_to_computer
  - frame: HasPrerequisite< go_on_internet; HasPrerequisite< get_onto_web
  - support 9; profile z 17.7 (null 0.16), sel p 0.0099, repro 0%, profile2 z 11.5 (null 0.48), sel p 0.0099, repro 0%; strict z 17.8
- **g191** n=7, uncategorised, shape 2, distinct frame: soap_and_water, use_water, go_to_bathroom, run_water, turn_on_water, turn_on_warm_water, undress_first
  - frame: HasPrerequisite< have_bath; HasPrerequisite< take_shower
  - support 7; profile z 13.7 (null 0.16), sel p 0.0099, repro 0%, profile2 z 9.7 (null 0.61), sel p 0.0099, repro 0%; strict z 13.8
- **g131** n=7, uncategorised, shape 2, distinct frame: go_to_cinema, go_to_movie_theater, turn_on_tv, turn_on_television, rent_movie, rent_video, rent_one
  - frame: HasPrerequisite< watch_movie; HasPrerequisite< see_movie; HasPrerequisite< watch_film; HasPrerequisite< view_film_at_home
  - support 7; profile z 13.9 (null 0.06), sel p 0.0099, repro 0%, profile2 z 8.6 (null 1.06), sel p 0.0099, repro 0%; strict z 14.0
- **g314** n=6, uncategorised, shape 2, distinct frame: pay_tuition, apply, enroll, enroll_in_one, enroll_in_school, register_for
  - frame: HasPrerequisite< take_course; HasPrerequisite< attend_class
  - support 6; profile z 11.9 (null 0.06), sel p 0.0099, repro 0%, profile2 z 9.9 (null 1.04), sel p 0.0297, repro 0%; strict z 11.8
- **g451** n=6, uncategorised, shape 2, distinct frame: take_course, buy_book, get_book_on_subject, go_to_library, read_book_about, use_search_engine
  - frame: HasPrerequisite< learn_new; HasPrerequisite< learn_about_subject; HasSubevent< finding_information
  - support 6; profile z 9.6 (null 0.4), sel p 0.0099, repro 0%, profile2 z 9.2 (null 1.32), sel p 0.0297, repro 0%; strict z 11.9
- **g251** n=6, uncategorised, shape 2, distinct frame: go_to_doctor, go_see_doctor, make_appointment_with_doctor, call_doctor, see_doctor, go_to_doctors
  - frame: HasPrerequisite< have_checkup; HasPrerequisite< have_physical_exam
  - support 6; profile z 11.7 (null 0.16), sel p 0.0099, repro 0%, profile2 z 8.5 (null 0.56), sel p 0.0297, repro 0%; strict z 12.0
- **g493** n=5, uncategorised, shape 32, distinct frame: keep_things_cold, keeping_things_cold, storing_ice, storing_ice_cream, storing_meat
  - frame: UsedFor< icebox; UsedFor< refrigerator_freezer
  - support 5; profile z 10.0 (null 0.02), sel p 0.0297, repro 0%, profile2 z 10.0 (null 0.01), sel p 0.0297, repro 0%; strict z 10.0
- **g622** n=5, uncategorised, shape 32, distinct frame: exchanging_information, good_time, catching_up, keeping_in_touch, relaying_information
  - frame: UsedFor< chatting_with_friends; UsedFor< talking_with_far_away
  - support 5; profile z 9.9 (null 0.07), sel p 0.0297, repro 0%, profile2 z 9.7 (null 0.14), sel p 0.0297, repro 0%; strict z 10.0
- **g602** n=5, uncategorised, shape 32, distinct frame: washing_hair, washing, keeping_clean, removing_dirt_from_body, relaxing_after_busy_day
  - frame: UsedFor< taking_bath; UsedFor< having_shower
  - support 5; profile z 9.7 (null 0.14), sel p 0.0297, repro 0%, profile2 z 9.4 (null 0.29), sel p 0.0297, repro 0%; strict z 9.9
- **g101** n=7, uncategorised, shape 8, distinct frame: watch_television_show, see_favorite_show, see_story, use_television, see_people_play_game, see_particular_program, view_video
  - frame: HasPrerequisite> turn_on_tv; MotivatedByGoal> entertained
  - support 7; profile z 9.6 (null 0.46), sel p 0.0198, repro 0%, profile2 z 5.5 (null 1.36), sel p 0.0297, repro 1%; strict z 13.5
- **g502** n=5, uncategorised, shape 32, distinct frame: being_mean, revenge, causing_pain, getting_revenge, inflicting_pain
  - frame: UsedFor< hurting_else; UsedFor< punching
  - support 5; profile z 8.6 (null 0.37), sel p 0.0297, repro 0%, profile2 z 7.7 (null 1.15), sel p 0.0297, repro 0%; strict z 10.0
- **g574** n=6, uncategorised, shape 2, distinct frame: order, hungry, go_to_burger_king, go_to_fast_food_restaurant, go_to_macdonalds, go_to_mcdonalds
  - frame: HasPrerequisite< buy_hamburger; HasPrerequisite< eat_hamburger; HasPrerequisite< eat_in_fast_food_restaurant
  - support 6; profile z 9.2 (null 0.44), sel p 0.0099, repro 0%, profile2 z 6.3 (null 1.68), sel p 0.0297, repro 0%; strict z 11.6
- **g780** n=7, uncategorised, shape 36, distinct frame: guilt, grief, guilty_conscience, going_to_jail, remorse, feelings_of_guilt, guilty_conscious
  - frame: Causes< killing; Causes< killing_people; Causes< getting_away_with_crime
  - support 7; profile z 5.9 (null 1.26), sel p 0.0099, repro 0%, profile2 z 5.1 (null 2.17), sel p 0.0099, repro 0%; strict z 12.2
- **g471** n=6, uncategorised, shape 2, distinct frame: plug_in, turn_on, buy_one, turn_on_tv, turn_on_television, read_instruction_manual
  - frame: HasPrerequisite< watch_television; HasPrerequisite< use_television; HasPrerequisite< use_vcr
  - support 6; profile z 9.7 (null 0.45), sel p 0.0099, repro 0%, profile2 z 5.0 (null 2.69), sel p 0.0297, repro 0%; strict z 11.1
- **g632** n=5, crosscutting, shape 32, distinct frame: sport, going_someplace, racing, sightseeing, getting_out_of_house
  - frame: UsedFor< riding_bicycle; UsedFor< taking_car_for_drive
  - support 5; profile z 9.6 (null 0.18), sel p 0.0297, repro 0%, profile2 z 6.0 (null 1.04), sel p 0.0297, repro 0%; strict z 9.9
- **g706** n=5, uncategorised, shape 32, distinct frame: surprising, showing_love, saying_thankyou, making_yourself_happy, celebrating_birthday
  - frame: UsedFor< buying_for_loved_one; UsedFor< buying_presents_for_others
  - support 5; profile z 9.7 (null 0.14), sel p 0.0297, repro 0%, profile2 z 5.5 (null 0.73), sel p 0.0297, repro 0%; strict z 9.8
- **g651** n=5, uncategorised, shape 32, distinct frame: hungry_people, satisfying_craving, filling_stomach, satisfying_hunger, nourishment
  - frame: UsedFor< eating_hamburger; UsedFor< having_lunch
  - support 5; profile z 9.2 (null 0.25), sel p 0.0297, repro 0%, profile2 z 5.2 (null 1.47), sel p 0.0297, repro 0%; strict z 9.8
- **g697** n=5, uncategorised, shape 32, distinct frame: birthday, christmas, showing_affection, showing_love, celebrating_birthday
  - frame: UsedFor< giving_gift; UsedFor< buying_presents_for_others
  - support 5; profile z 9.4 (null 0.28), sel p 0.0297, repro 0%, profile2 z 5.2 (null 0.78), sel p 0.0297, repro 0%; strict z 9.9
- **g614** n=5, uncategorised, shape 32, distinct frame: grooming, comb_hair, combing_hair, styling_hair, remove_tangles_from_hair
  - frame: UsedFor< barber_comb; UsedFor< comb; UsedFor< hairbrush
  - support 5; profile z 9.5 (null 0.27), sel p 0.0297, repro 0%, profile2 z 4.9 (null 0.99), sel p 0.0297, repro 0%; strict z 9.9
- **g595** n=6, uncategorised, shape 36, distinct frame: feeling_better, feeling_refreshed, dreaming, rejuvination, not_being_tired, renewed_energy
  - frame: Causes< having_rest; Causes< resting; UsedFor< sleeping
  - support 6; profile z 8.6 (null 0.41), sel p 0.0099, repro 0%, profile2 z 3.7 (null 2.29), sel p 0.0099, repro 0%; strict z 11.8
- **g354** n=6, uncategorised, shape 2, distinct frame: able_to_see, go_to_cinema, buy_ticket, buy_tickets, rent_movie, rent_video
  - frame: HasPrerequisite< watch_movie; HasPrerequisite< enjoy_film
  - support 6; profile z 8.0 (null 0.57), sel p 0.0099, repro 0%, profile2 z 3.5 (null 2.04), sel p 0.0297, repro 0%; strict z 10.0

## Disappeared: earlier robust unnamed groups that the profile nulls explain

104 groups. Largest:

- **g4** n=27, uncategorised, shape 26, paraphrase frame: surprising, swimming_pool, playroom, canoe, discothque, playing_hockey, tickling, creating_art, dreaming, fencing, going_on_internet, going_outside_for_evening, going_see_film, going_to_play …
  - frame: UsedFor> fun; UsedFor> having_fun
  - support 27; profile z 5.4 (null 12.64), sel p 0.0099, repro 33%, profile2 z 0.0 (null 27.0), sel p 1.0, repro 100%; strict z 6.6
- **g16** n=19, crosscutting, shape 26, paraphrase frame: playroom, baseball_stadium, vacation, performance, kite, marijuana, playing_hockey, becoming_scuba_diver, creating_art, fencing, getting_onto_web, going_outside_for_evening, going_to_zoo, having_friends_over …
  - frame: UsedFor> entertainment; UsedFor> fun
  - support 19; profile z 2.4 (null 11.85), sel p 0.0693, repro 0%, profile2 z 1.0 (null 16.75), sel p 1.0, repro 53%; strict z 4.8
- **g42** n=16, crosscutting, shape 30, paraphrase frame: goods, handbag, clerk, candy, cash_register, clerks, jeans, display_cabinet, label_maker, merchant, neighborhood_map, products, service_counter, shopping_bag …
  - frame: AtLocation> store; AtLocation> shop
  - support 16; profile z 6.8 (null 3.32), sel p 0.5446, repro 0%, profile2 z 4.8 (null 9.67), sel p 0.4653, repro 97%; strict z 9.7
- **g127** n=16, uncategorised, shape 31, paraphrase frame: tie_shoes, butter_bread, bicycle_to_school, fear_dark, fear_imaginary_monsters, need_mother, play_tag, play_video_games, set_table, share_toys, thank_parents, trade_pokemon_cards, visit_grandparents, watch_cartoons …
  - frame: CapableOf< child; CapableOf< children
  - support 16; profile z 7.2 (null 3.37), sel p 0.0099, repro 0%, profile2 z 1.3 (null 13.66), sel p 0.1683, repro 100%; strict z 9.0
- **g29** n=15, uncategorised, shape 26, paraphrase frame: oboe, becoming_scuba_diver, copulating, eating_cookie, going_for_swim, going_outside_for_evening, playing_poker, riding_horse, seeing_band, seeing_people_play_game, seeing_story, soaking_in_hotspring, visiting_art_gallery, walking_around_lake …
  - frame: UsedFor> enjoyment; UsedFor> fun
  - support 15; profile z 1.6 (null 11.2), sel p 0.3762, repro 11%, profile2 z 0.7 (null 13.87), sel p 1.0, repro 95%; strict z 3.5
- **g71** n=15, crosscutting, shape 30, paraphrase frame: flat, loft, cafe, auditorium, boarding_room, booking_office, college, dental_office, parlor, deli, dentist_office, record_library, registry_office, restaurant_entrance …
  - frame: AtLocation> city; AtLocation> building
  - support 15; profile z 3.1 (null 7.53), sel p 0.6832, repro 0%, profile2 z 2.9 (null 7.98), sel p 0.6832, repro 0%; strict z 4.2
- **g103** n=15, crosscutting, shape 30, paraphrase frame: shoe, beanbag, lamp, clock, dandruff_shampoo, jeans, television_set, fans, stuff, flooring, furniture, linoleum, mat, pliers …
  - frame: AtLocation> house; AtLocation> store
  - support 15; profile z 0.9 (null 12.01), sel p 0.6832, repro 0%, profile2 z 2.0 (null 12.76), sel p 0.6832, repro 100%; strict z 3.4
- **g22** n=14, crosscutting, shape 26, paraphrase frame: cake, meat, seafood_restaurant, steak_house, bass, dining_room, diner, dish, spoon, fork, fruit, kosher_delicatessen, kosher_restaurant, cooking_dinner
  - frame: UsedFor> eat; UsedFor> eating
  - support 14; profile z 8.6 (null 2.68), sel p 0.5743, repro 1%, profile2 z 3.6 (null 8.58), sel p 1.0, repro 92%; strict z 17.9
- **g44** n=13, uncategorised, shape 26, distinct frame: becoming_scuba_diver, creating_art, going_outside_for_evening, going_to_baseball_game, going_to_bed, going_to_zoo, making_patchwork_quilt, playing_harp, seeing_band, seeing_exhibits, visiting_art_gallery, walking_around_lake, walking_dog
  - frame: UsedFor> fun; UsedFor> relaxation
  - support 13; profile z 2.2 (null 8.26), sel p 0.7723, repro 0%, profile2 z 0.9 (null 10.91), sel p 1.0, repro 5%; strict z 3.7
- **g92** n=13, crosscutting, shape 18, paraphrase frame: mexico, circus, ass, own_house, cage, lap, petshop, barbeque, vet's_office, grandma's_house, animal_shelter, obedience_school, owner's_house
  - frame: AtLocation< small_dog; AtLocation< wiener_dog
  - support 13; profile z 5.8 (null 4.13), sel p 0.0594, repro 0%, profile2 z 4.7 (null 6.43), sel p 0.5248, repro 14%; strict z 8.4

## Anomaly 18 family (groups with ≥ 2 of swimming, surfing, skating, skiing, dancing, singing, playing_cards)

0 groups.

| g | n | anomaly-18 members | frame | tier | relation z / sel p / repro | strict z / sel p / repro | profile z / sel p / repro | profile2 z / sel p / repro | survives profile | + selection |
|---|---|---|---|---|---|---|---|---|---|---|

## What construction alone produces: largest unnamed groups mined from profile nulls (seeds 0–2)

- n=17, crosscutting, shape 30: apple, acoustic_guitar, beanbag, clock, clothes_closet, jeans, duvet_cover, fire_extinguisher, john, phone, mat, mini_bar …
  - frame: AtLocation> city; AtLocation> house
- n=14, crosscutting, shape 26: gymnasium, baseball_stadium, vacation, performance, kite, tickling, fencing, getting_onto_web, going_to_baseball_game, going_to_zoo, growing_vegetables, seeing_exhibits …
  - frame: UsedFor> entertainment; UsedFor> fun
- n=14, uncategorised, shape 26: back_courtyard, copulating, eating_cookie, going_for_swim, going_see_film, going_to_zoo, playing_poker, reading_to_children, seeing_artifacts, seeing_exciting_story, seeing_people_play_game, soaking_in_hotspring …
  - frame: UsedFor> enjoyment; UsedFor> fun
- n=14, uncategorised, shape 26: surprising, canoe, creating_art, dreaming, fencing, going_on_internet, going_outside_for_evening, going_to_zoo, laughing_at_joke, playing_guitar, playing_poker, seeing_people_play_game …
  - frame: UsedFor> fun; UsedFor> having_fun
- n=14, crosscutting, shape 30: acoustic_guitar, air_conditioner, beam, cardboard_box, parlor, dining_area, fire_extinguisher, furnace, linen, linen_chest, mat, staples …
  - frame: AtLocation> house; AtLocation> store
- n=13, crosscutting, shape 30: broom, parlor, desk_tray, gloves, glue, heater, phone, shelter, linen, mat, pencil_sharpener, pill …
  - frame: AtLocation> school; AtLocation> house
- n=13, uncategorised, shape 4: attending_classical_concert, buying_christmas_presents, buying_presents, eating_cookie, enjoying_day, going_see_film, howling_with_laughter, laughing_at_joke, living_life, making_people_laugh, seeing_band, sleighing_ride …
  - frame: Causes> happiness; UsedFor> fun
- n=13, crosscutting, shape 30: newspaper, pub, court, satchel, booking_office, clippers, computer_user, correction_fluid, garbage_can, five_and_ten_store, letters, sideboard …
  - frame: AtLocation> city; AtLocation> town
