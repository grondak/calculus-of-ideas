# Profile-preserving nulls, re-mined (member cap 150 typed features)

100 null graphs per mode, every one mined with the identical procedure. No edges or labels added.

| null | what is kept besides per-relation in/out counts, dataset, two-way pairs | typed incidences of the real graph still present |
|---|---|---|
| relation | nothing else (two-way pairs not kept) | 0.9% |
| strict | log2 degree class of both ends | 5.0% |
| profile | each end's dominant (relation, direction) + log2 typed degree | 15.8% |
| profile2 | each end's top-2 (relation, direction) + log2 typed degree | 35.7% |

profile: 223 endpoint classes; 3.7% of typed one-way links and 6.7% of two-way pairs sit in strata of one (cannot move).

profile2: 1879 endpoint classes; 12.1% of typed one-way links and 14.4% of two-way pairs sit in strata of one (cannot move).

## Group counts: real vs re-mined nulls (null mean [min–max])

| | real | relation | strict | profile | profile2 |
|---|---|---|---|---|---|
| size_ge_4 | 4009 | 2772.1 [2326–3186] | 1828.5 [1712–1941] | 2319.7 [2221–2399] | 2715.1 [2623–2838] |
| size_ge_6 | 1690 | 1437.0 [1145–1720] | 466.5 [414–522] | 779.9 [720–851] | 1045.3 [988–1118] |
| size_ge_10 | 459 | 663.5 [514–807] | 52.3 [39–65] | 123.2 [100–144] | 214.8 [185–237] |
| size_ge_20 | 67 | 125.7 [88–162] | 1.3 [0–4] | 10.6 [5–18] | 24.6 [17–31] |
| named_ge_6 | 124 | 65.5 [42–105] | 11.9 [3–30] | 28.9 [15–47] | 66.6 [51–85] |
| partly_named_ge_6 | 425 | 560.6 [408–699] | 135.6 [111–163] | 209.4 [173–243] | 301.8 [269–338] |
| uncategorised_ge_6 | 499 | 60.4 [35–77] | 101.4 [75–134] | 223.0 [198–269] | 279.7 [255–311] |
| crosscutting_ge_6 | 642 | 750.5 [584–866] | 217.5 [183–262] | 318.6 [266–356] | 397.2 [358–435] |
| unnamed_ge_6 | 1141 | 810.9 [650–918] | 318.9 [278–357] | 541.6 [495–592] | 676.9 [635–733] |

## Shapes: groups of size ≥ 6 (null mean) and largest group (null mean of the largest)

| shape | relation profile | real ≥6 | real unnamed ≥6 | real max | relation ≥6 / unnamed / max | strict ≥6 / unnamed / max | profile ≥6 / unnamed / max | profile2 ≥6 / unnamed / max |
|---|---|---|---|---|---|---|---|---|
| 10 | AtLocation> 93%, UsedFor> 6% | 554 | 313 | 63 | 722.9 / 285.3 / 35.1 | 184.8 / 107.1 / 15.0 | 213.9 / 118.1 / 21.3 | 312.0 / 154.2 / 22.8 |
| 2 | AtLocation< 97% | 235 | 131 | 25 | 587.9 / 422.7 / 57.3 | 104.7 / 59.2 / 13.8 | 177.3 / 107.6 / 14.9 | 238.5 / 143.6 / 18.0 |
| 26 | Causes> 68%, UsedFor> 28% | 213 | 184 | 26 | 53.3 / 49.5 / 13.5 | 90.6 / 81.7 / 18.0 | 150.3 / 128.4 / 21.1 | 156.8 / 132.8 / 23.9 |
| 28 | UsedFor> 82%, HasPrerequisite> 8% | 196 | 133 | 62 | 22.2 / 14.9 / 12.7 | 50.0 / 44.4 / 20.9 | 120.4 / 97.5 / 45.6 | 138.9 / 100.6 / 59.8 |
| 57 | Causes< 95% | 69 | 40 | 10 | 0.4 / 0.1 / 5.3 | 0.3 / 0.0 / 5.0 | 0.8 / 0.1 / 5.7 | 2.6 / 0.5 / 7.0 |
| 52 | UsedFor< 97% | 60 | 46 | 10 | 1.7 / 1.3 / 7.0 | 0.1 / 0.0 / 4.7 | 1.1 / 0.6 / 5.9 | 4.0 / 1.8 / 7.3 |
| 40 | HasPrerequisite< 96% | 59 | 59 | 13 | 0.0 / 0.0 / 3.6 | 0.0 / 0.0 / 1.0 | 0.0 / 0.0 / 3.6 | 0.4 / 0.4 / 5.3 |
| 24 | Causes> 48%, HasPrerequisite> 45% | 57 | 54 | 19 | 0.3 / 0.2 / 4.9 | 5.9 / 5.6 / 8.3 | 31.7 / 30.6 / 17.6 | 42.7 / 40.7 / 24.1 |
| 33 | HasPrerequisite> 78%, HasSubevent> 17% | 46 | 46 | 19 | 3.2 / 3.2 / 7.0 | 2.9 / 2.9 / 6.9 | 8.9 / 8.5 / 9.3 | 21.6 / 21.0 / 20.8 |
| 9 | AtLocation> 50%, AtLocation< 47% | 32 | 6 | 18 | 11.6 / 3.7 / 8.4 | 6.0 / 1.5 / 8.7 | 15.1 / 2.4 / 10.0 | 20.7 / 3.1 / 11.6 |
| 18 | HasSubevent> 48%, Causes> 48% | 31 | 28 | 15 | 5.5 / 4.8 / 7.5 | 7.2 / 6.4 / 8.0 | 11.5 / 10.4 / 8.7 | 15.8 / 14.2 / 11.0 |
| 27 | HasSubevent> 50%, UsedFor> 50% | 20 | 15 | 13 | 0.9 / 0.8 / 5.8 | 5.8 / 5.2 / 8.4 | 19.9 / 17.5 / 10.5 | 22.4 / 18.1 / 13.1 |
| 34 | MotivatedByGoal> 62%, CausesDesire< 33% | 19 | 19 | 15 | 0.8 / 0.8 / 5.8 | 0.9 / 0.9 / 5.9 | 7.7 / 7.7 / 10.7 | 15.5 / 15.0 / 12.6 |
| 21 | HasSubevent> 91%, CausesDesire< 7% | 15 | 15 | 11 | 4.4 / 3.9 / 7.3 | 1.3 / 1.2 / 6.1 | 3.8 / 3.7 / 8.1 | 7.8 / 7.8 / 10.1 |
| 43 | CapableOf< 98% | 13 | 13 | 19 | 0.2 / 0.2 / 4.3 | 0.4 / 0.4 / 5.1 | 1.8 / 1.7 / 6.7 | 6.7 / 6.6 / 16.1 |
| 8 | AtLocation> 49%, ReceivesAction> 48% | 11 | 1 | 18 | 0.1 / 0.0 / 3.3 | 1.2 / 0.2 / 6.3 | 4.0 / 0.4 / 10.4 | 6.1 / 0.5 / 18.0 |

## Survival

- frame support at the p floor under profile, profile2 and reproduced (member Jaccard ≥ 0.5) in ≤ 5% of re-mined nulls: **1359** of 4009 groups; by tier {'crosscutting': 401, 'partly_named': 287, 'uncategorised': 521, 'named': 150}
- and, in addition, larger than the largest re-mined null group of the same shape in ≥ 95% of nulls: **53**; by tier {'crosscutting': 9, 'partly_named': 7, 'uncategorised': 37}
- survives_profile by frame kind (kind, >1 relation type): {('distinct', False): 477, ('distinct', True): 270, ('paraphrase', False): 552, ('paraphrase', True): 60}
- survives_selection by frame kind (kind, >1 relation type): {('distinct', False): 13, ('distinct', True): 5, ('paraphrase', False): 33, ('paraphrase', True): 2}
- all groups by frame kind: {('distinct', False): 1642, ('distinct', True): 1200, ('paraphrase', False): 964, ('paraphrase', True): 203}
- of the 986 groups robust in the earlier run, 447 survive the profile nulls and 42 also the selection control

## Survivors of the selection control, by tier (largest size × min profile z first, ≤ 2 per shape)

### named (0)


### partly_named (7)

- **g7** n=36, partly_named, shape 10, distinct frame: accordion, acoustic_guitar, balalaika, banjo, bass_baritone, bass_clarinet, bass_drum, bass_fiddle, bassoon, clarinet, cornet, double_bass, drum, fiddle …
  - frame: AtLocation> band; AtLocation> orchestra; UsedFor> making_music
  - support 36; profile z 15.6 (null 4.87), sel p 0.0198, repro 0%, profile2 z 8.1 (null 20.23), sel p 0.0396, repro 0%; strict z 22.1
- **g217** n=10, partly_named, shape 57, paraphrase frame: death, indigestion, gas, nausea, satisfaction, feeling_full, gaining_weight, getting_full, heartburn, making_less_hungry
  - frame: Causes< eating; Causes< eating_hamburger
  - support 10; profile z 11.1 (null 0.82), sel p 0.0099, repro 0%, profile2 z 7.7 (null 2.31), sel p 0.0099, repro 2%; strict z 14.9
- **g156** n=18, partly_named, shape 9, paraphrase frame: home, bar, war, school, theater, bank, office_building, factory, bus, airport, church, department_store, prison, stadium …
  - frame: AtLocation> city; AtLocation< human
  - support 18; profile z 4.9 (null 8.55), sel p 0.0099, repro 0%, profile2 z 3.3 (null 9.83), sel p 0.0099, repro 1%; strict z 4.4
- **g1590** n=9, partly_named, shape 57, distinct frame: anger, boredom, impatience, frustration, get_tired, getting_bored, sore_feet, fidgeting, getting_to_front
  - frame: Causes< standing_in_line; Causes< standing_in_queue; Causes< waiting_on_line
  - support 9; profile z 6.8 (null 2.91), sel p 0.0099, repro 0%, profile2 z 4.3 (null 4.74), sel p 0.0099, repro 1%; strict z 11.9
- **g3513** n=4, partly_named, shape 58, distinct frame: performance, singing, acting_in_play, performing
  - frame: Causes< going_on_stage; UsedFor> entertainment
  - support 4; profile z 7.3 (null 0.36), sel p 0.0495, repro 0%, profile2 z 4.2 (null 0.83), sel p 0.0396, repro 1%; strict z 7.8

### uncategorised (37)

- **g185** n=13, uncategorised, shape 40, distinct frame: log_on, use_computer, dial_up, turn_computer_on, turn_on_computer, connect_to_internet, buy_computer, have_computer, get_computer, have_modem, log_on_to_computer, go_on_line, launch_web_browser
  - frame: HasPrerequisite< go_on_internet; HasPrerequisite< surf_net; HasPrerequisite< get_onto_web
  - support 13; profile z 19.5 (null 0.49), sel p 0.0099, repro 0%, profile2 z 10.1 (null 1.89), sel p 0.0099, repro 0%; strict z 24.3
- **g589** n=10, uncategorised, shape 40, paraphrase frame: careful, strike_match, light_match, go_outdoors, get_matches, gather_kindling, rub_two_sticks_together, use_lighter, use_match, use_matches
  - frame: HasPrerequisite< light_fire; HasPrerequisite< start_fire; HasPrerequisite< start_flame_or_fire
  - support 10; profile z 15.4 (null 0.43), sel p 0.0099, repro 0%, profile2 z 12.6 (null 0.59), sel p 0.0099, repro 0%; strict z 18.3
- **g931** n=10, uncategorised, shape 57, distinct frame: success, failure, stress, anxiety, headaches, passing_course, receiving_grade, finishing_class, getting_grade, pass_or_fail
  - frame: Causes< taking_exam; Causes< taking_final_exams; Causes< taking_finals
  - support 10; profile z 7.5 (null 1.73), sel p 0.0099, repro 0%, profile2 z 6.8 (null 3.31), sel p 0.0099, repro 0%; strict z 7.8
- **g304** n=9, uncategorised, shape 57, paraphrase frame: pain, sweat, heart_attack, sweating, sore_feet, shortness_of_breath, cramps, increased_heart_rate, leg_cramps
  - frame: Causes< running; Causes< going_for_jog
  - support 9; profile z 6.9 (null 1.61), sel p 0.0099, repro 0%, profile2 z 5.8 (null 2.65), sel p 0.0099, repro 0%; strict z 13.8
- **g1650** n=5, uncategorised, shape 51, paraphrase frame: look_different, have_shorter_hair, look_neater, new_hairstyle, shorter_hair
  - frame: Causes< cutting_hair; MotivatedByGoal< cut_hair
  - support 5; profile z 9.8 (null 0.08), sel p 0.0099, repro 0%, profile2 z 9.6 (null 0.2), sel p 0.0198, repro 0%; strict z 9.9
- **g1407** n=9, uncategorised, shape 30, distinct frame: hear_music, watch_television, watch_television_show, see_story, use_television, see_people_play_game, do_crossword_puzzle, use_vcr, view_video
  - frame: CausesDesire< boredom; HasPrerequisite> turn_on; HasPrerequisite> turn_on_tv; MotivatedByGoal> relax; MotivatedByGoal> entertained
  - support 9; profile z 8.4 (null 0.99), sel p 0.0099, repro 1%, profile2 z 3.9 (null 3.6), sel p 0.0297, repro 5%; strict z 14.1
- **g1334** n=5, uncategorised, shape 51, paraphrase frame: getting_fat, physically_fit, get_in_shape, stay_fit, loose_weight
  - frame: MotivatedByGoal< exercise; MotivatedByGoal< do_exercises
  - support 5; profile z 8.9 (null 0.28), sel p 0.0099, repro 0%, profile2 z 6.2 (null 0.65), sel p 0.0198, repro 0%; strict z 9.6
- **g3863** n=4, uncategorised, shape 44, distinct frame: fly_kite, tie_shoes, flying_kite, tie_knot
  - frame: CapableOf< child; UsedFor< string
  - support 4; profile z 6.9 (null 0.33), sel p 0.0198, repro 0%, profile2 z 4.0 (null 1.88), sel p 0.0099, repro 0%; strict z 7.9

### crosscutting (9)

- **g0** n=63, crosscutting, shape 10, paraphrase frame: flat, stranger, war, school, theater, bank, bookshop, bus_stop, mall, sporting_goods_store, church, grocery_store, pub, cafe …
  - frame: AtLocation> city; AtLocation> town
  - support 63; profile z 16.6 (null 12.75), sel p 0.0099, repro 0%, profile2 z 15.0 (null 15.29), sel p 0.0099, repro 0%; strict z 20.4
- **g5** n=43, crosscutting, shape 10, paraphrase frame: chair, clutter, feet, desk_drawer, printer, carpet, trash_can, lamp, mouse, cup_of_coffee, calculator, calendar_pad, card_case, telephone …
  - frame: AtLocation> desk; AtLocation> office
  - support 43; profile z 14.3 (null 7.86), sel p 0.0099, repro 0%, profile2 z 14.1 (null 9.07), sel p 0.0396, repro 0%; strict z 16.3
- **g13** n=25, crosscutting, shape 2, paraphrase frame: fair, texas, america, it's_natural_habitat, indiana, countryside, farm_yard, idaho, ohio, freezer, stew, barnyard, corral, county_fair …
  - frame: AtLocation< cow; AtLocation< heifer
  - support 25; profile z 12.8 (null 3.65), sel p 0.0198, repro 0%, profile2 z 9.4 (null 7.19), sel p 0.0495, repro 0%; strict z 18.2
- **g1611** n=25, crosscutting, shape 2, distinct frame: outside, country, a, canada, movies, detroit, michigan, it's_natural_habitat, woods, indiana, countryside, farm_yard, florida, idaho …
  - frame: AtLocation< horse; AtLocation< apple_tree; AtLocation< heifer
  - support 25; profile z 5.3 (null 10.79), sel p 0.0198, repro 0%, profile2 z 3.7 (null 17.21), sel p 0.0495, repro 2%; strict z 7.1
- **g714** n=7, crosscutting, shape 40, paraphrase frame: on_time, register, study, get_out_of_bed, enroll, matriculate, enroll_at_school
  - frame: HasPrerequisite< go_to_school; HasPrerequisite< attend_class
  - support 7; profile z 8.4 (null 0.87), sel p 0.0099, repro 0%, profile2 z 7.4 (null 2.51), sel p 0.0396, repro 0%; strict z 13.6
- **g351** n=7, crosscutting, shape 40, paraphrase frame: light, literacy, eyes, vision, ability_to_read, knowing_how_to_read, understanding_of_language
  - frame: HasPrerequisite< reading_letter; HasPrerequisite< reading_newspaper
  - support 7; profile z 9.9 (null 0.5), sel p 0.0099, repro 0%, profile2 z 6.4 (null 2.05), sel p 0.0396, repro 2%; strict z 13.6
- **g472** n=8, crosscutting, shape 57, paraphrase frame: good_health, sweat, exhaustion, sweating, shortness_of_breath, increased_heart_rate, getting_out_of_breath, running_out_of_breath
  - frame: Causes< running; Causes< jogging
  - support 8; profile z 6.6 (null 1.39), sel p 0.0099, repro 0%, profile2 z 5.0 (null 1.92), sel p 0.0198, repro 0%; strict z 10.4
- **g1957** n=9, crosscutting, shape 57, distinct frame: weight_loss, injury, exhaustion, heart_attack, injuries, tiredness, becoming_tired, getting_in_shape, shortness_of_breath
  - frame: Causes< running; Causes< getting_exercise; Causes< running_in_marathon
  - support 9; profile z 4.5 (null 3.15), sel p 0.0099, repro 0%, profile2 z 3.0 (null 4.78), sel p 0.0099, repro 0%; strict z 8.4

## Selection survivors with distinct (non-paraphrase) frame neighbours

18 groups.

- **g7** n=36, partly_named, shape 10, distinct frame: accordion, acoustic_guitar, balalaika, banjo, bass_baritone, bass_clarinet, bass_drum, bass_fiddle, bassoon, clarinet, cornet, double_bass, drum, fiddle …
  - frame: AtLocation> band; AtLocation> orchestra; UsedFor> making_music
  - support 36; profile z 15.6 (null 4.87), sel p 0.0198, repro 0%, profile2 z 8.1 (null 20.23), sel p 0.0396, repro 0%; strict z 22.1
- **g185** n=13, uncategorised, shape 40, distinct frame: log_on, use_computer, dial_up, turn_computer_on, turn_on_computer, connect_to_internet, buy_computer, have_computer, get_computer, have_modem, log_on_to_computer, go_on_line, launch_web_browser
  - frame: HasPrerequisite< go_on_internet; HasPrerequisite< surf_net; HasPrerequisite< get_onto_web
  - support 13; profile z 19.5 (null 0.49), sel p 0.0099, repro 0%, profile2 z 10.1 (null 1.89), sel p 0.0099, repro 0%; strict z 24.3
- **g126** n=11, uncategorised, shape 40, distinct frame: go_to_concert, buy_ticket, open_eyes, go_to_theater, go_to_theatre, buy_tickets, buy_tickets_to_concert, buy_ticket_to_concert, go_to_club, buy_concert_ticket, attend_concert
  - frame: HasPrerequisite< watch_musician_perform; HasPrerequisite< see_band
  - support 11; profile z 15.0 (null 0.5), sel p 0.0099, repro 0%, profile2 z 10.7 (null 1.09), sel p 0.0099, repro 0%; strict z 21.5
- **g1611** n=25, crosscutting, shape 2, distinct frame: outside, country, a, canada, movies, detroit, michigan, it's_natural_habitat, woods, indiana, countryside, farm_yard, florida, idaho …
  - frame: AtLocation< horse; AtLocation< apple_tree; AtLocation< heifer
  - support 25; profile z 5.3 (null 10.79), sel p 0.0198, repro 0%, profile2 z 3.7 (null 17.21), sel p 0.0495, repro 2%; strict z 7.1
- **g590** n=7, uncategorised, shape 40, distinct frame: pay_tuition, go_to_school, apply, enroll, enroll_in_one, enroll_in_school, register_for
  - frame: HasPrerequisite< take_course; HasPrerequisite< attend_class
  - support 7; profile z 13.9 (null 0.06), sel p 0.0099, repro 0%, profile2 z 11.8 (null 1.09), sel p 0.0396, repro 0%; strict z 13.8
- **g931** n=10, uncategorised, shape 57, distinct frame: success, failure, stress, anxiety, headaches, passing_course, receiving_grade, finishing_class, getting_grade, pass_or_fail
  - frame: Causes< taking_exam; Causes< taking_final_exams; Causes< taking_finals
  - support 10; profile z 7.5 (null 1.73), sel p 0.0099, repro 0%, profile2 z 6.8 (null 3.31), sel p 0.0099, repro 0%; strict z 7.8
- **g563** n=7, uncategorised, shape 40, distinct frame: soap_and_water, use_water, go_to_bathroom, run_water, turn_on_water, turn_on_warm_water, undress_first
  - frame: HasPrerequisite< have_bath; HasPrerequisite< take_shower
  - support 7; profile z 13.7 (null 0.16), sel p 0.0099, repro 0%, profile2 z 9.7 (null 0.61), sel p 0.0396, repro 0%; strict z 13.8
- **g395** n=7, uncategorised, shape 40, distinct frame: go_to_cinema, go_to_movie_theater, turn_on_tv, turn_on_television, rent_movie, rent_video, rent_one
  - frame: HasPrerequisite< watch_movie; HasPrerequisite< see_movie; HasPrerequisite< watch_film; HasPrerequisite< view_film_at_home
  - support 7; profile z 13.9 (null 0.06), sel p 0.0099, repro 0%, profile2 z 8.6 (null 1.06), sel p 0.0396, repro 0%; strict z 14.0
- **g811** n=8, uncategorised, shape 40, distinct frame: save_money, go_to_store, have_money, go_to_mall, go_to_shop, have_enough_money, go_to_department_store, make_sure_have_money
  - frame: HasPrerequisite< buy_small; HasPrerequisite< purchase_cellular_phone; HasPrerequisite< buy_presents
  - support 8; profile z 6.1 (null 1.79), sel p 0.0099, repro 0%, profile2 z 5.2 (null 3.73), sel p 0.0099, repro 1%; strict z 15.4
- **g1590** n=9, partly_named, shape 57, distinct frame: anger, boredom, impatience, frustration, get_tired, getting_bored, sore_feet, fidgeting, getting_to_front
  - frame: Causes< standing_in_line; Causes< standing_in_queue; Causes< waiting_on_line
  - support 9; profile z 6.8 (null 2.91), sel p 0.0099, repro 0%, profile2 z 4.3 (null 4.74), sel p 0.0099, repro 1%; strict z 11.9
- **g1407** n=9, uncategorised, shape 30, distinct frame: hear_music, watch_television, watch_television_show, see_story, use_television, see_people_play_game, do_crossword_puzzle, use_vcr, view_video
  - frame: CausesDesire< boredom; HasPrerequisite> turn_on; HasPrerequisite> turn_on_tv; MotivatedByGoal> relax; MotivatedByGoal> entertained
  - support 9; profile z 8.4 (null 0.99), sel p 0.0099, repro 1%, profile2 z 3.9 (null 3.6), sel p 0.0297, repro 5%; strict z 14.1
- **g1029** n=8, partly_named, shape 57, distinct frame: appreciation, inspiration, enjoyment, education, learning, wonder, insight, learning_about_art
  - frame: Causes< seeing_exhibits; Causes< visiting_museum; UsedFor< seeing_art
  - support 8; profile z 4.8 (null 2.83), sel p 0.0099, repro 0%, profile2 z 4.0 (null 3.44), sel p 0.0198, repro 0%; strict z 6.5
- **g1108** n=8, partly_named, shape 57, distinct frame: happy, gratitude, happiness, pleasure, thank, spend_money, make_happy, making_happy
  - frame: Causes< giving_gift; Causes< buying_for_loved_one; Causes< buying_presents_for_others
  - support 8; profile z 4.6 (null 2.78), sel p 0.0099, repro 1%, profile2 z 4.0 (null 4.3), sel p 0.0198, repro 5%; strict z 6.5
- **g2882** n=7, crosscutting, shape 40, distinct frame: train, play_sport, lift_weights, work_out, stand_up, excersise, go_to_gym
  - frame: HasPrerequisite< get_fit; HasPrerequisite< get_exercise; HasPrerequisite< get_physical_activity
  - support 7; profile z 6.9 (null 0.93), sel p 0.0099, repro 0%, profile2 z 4.5 (null 2.61), sel p 0.0396, repro 1%; strict z 8.1
- **g1955** n=8, uncategorised, shape 57, distinct frame: anger, fights, pull_muscle, injuries, fatigue, becoming_tired, sweating, will_get_tired
  - frame: Causes< getting_physical_activity; Causes< playing_soccer; Causes< playing_tennis
  - support 8; profile z 5.9 (null 1.68), sel p 0.0099, repro 0%, profile2 z 3.7 (null 3.19), sel p 0.0198, repro 0%; strict z 6.4
- **g1957** n=9, crosscutting, shape 57, distinct frame: weight_loss, injury, exhaustion, heart_attack, injuries, tiredness, becoming_tired, getting_in_shape, shortness_of_breath
  - frame: Causes< running; Causes< getting_exercise; Causes< running_in_marathon
  - support 9; profile z 4.5 (null 3.15), sel p 0.0099, repro 0%, profile2 z 3.0 (null 4.78), sel p 0.0099, repro 0%; strict z 8.4
- **g3513** n=4, partly_named, shape 58, distinct frame: performance, singing, acting_in_play, performing
  - frame: Causes< going_on_stage; UsedFor> entertainment
  - support 4; profile z 7.3 (null 0.36), sel p 0.0495, repro 0%, profile2 z 4.2 (null 0.83), sel p 0.0396, repro 1%; strict z 7.8
- **g3863** n=4, uncategorised, shape 44, distinct frame: fly_kite, tie_shoes, flying_kite, tie_knot
  - frame: CapableOf< child; UsedFor< string
  - support 4; profile z 6.9 (null 0.33), sel p 0.0198, repro 0%, profile2 z 4.0 (null 1.88), sel p 0.0099, repro 0%; strict z 7.9

## Disappeared: earlier robust unnamed groups that the profile nulls explain

310 groups. Largest:

- **g2** n=59, uncategorised, shape 28, paraphrase frame: car, surprising, climbing, swimming_pool, playroom, canoe, discothque, singing, swimming, diving, playing_hockey, playing_sports, riding_bike, tickling …
  - frame: UsedFor> fun; UsedFor> having_fun
  - support 59; profile z 7.7 (null 28.19), sel p 0.2376, repro 37%, profile2 z 0.0 (null 59.0), sel p 1.0, repro 100%; strict z 11.9
- **g3** n=47, crosscutting, shape 28, paraphrase frame: writing, thinking, movie, playroom, baseball_stadium, dancing, vacation, performance, kite, marijuana, singing, playing_hockey, playing_sports, playing_violin …
  - frame: UsedFor> entertainment; UsedFor> fun
  - support 47; profile z 4.7 (null 29.98), sel p 0.505, repro 0%, profile2 z 2.5 (null 40.13), sel p 1.0, repro 23%; strict z 8.8
- **g4** n=41, uncategorised, shape 28, paraphrase frame: show, climbing, oboe, singing, swimming, riding_bicycle, playing_sports, playing_violin, reading_book, skiing, becoming_scuba_diver, getting_exercise, copulating, eating_cookie …
  - frame: UsedFor> enjoyment; UsedFor> fun
  - support 41; profile z 5.1 (null 25.57), sel p 0.5347, repro 1%, profile2 z 2.9 (null 33.89), sel p 1.0, repro 95%; strict z 7.6
- **g6** n=36, uncategorised, shape 28, distinct frame: show, writing, fishing, swimming, diving, reading_book, skiing, becoming_inebriated, becoming_scuba_diver, getting_exercise, creating_art, enjoying_film, going_for_drive, going_for_walk …
  - frame: UsedFor> fun; UsedFor> relaxation
  - support 36; profile z 3.8 (null 23.18), sel p 0.6634, repro 0%, profile2 z 1.2 (null 32.42), sel p 1.0, repro 2%; strict z 8.4
- **g8** n=32, crosscutting, shape 28, paraphrase frame: writing, running, dancing, marijuana, swimming, flying_kite, riding_bicycle, getting_drunk, diving, playing_violin, reading_book, skiing, becoming_scuba_diver, driving_car …
  - frame: UsedFor> pleasure; UsedFor> fun
  - support 32; profile z 2.3 (null 23.97), sel p 0.8614, repro 0%, profile2 z 0.1 (null 31.84), sel p 1.0, repro 2%; strict z 6.2
- **g11** n=25, crosscutting, shape 28, paraphrase frame: reading, swimming, riding_bicycle, drinking, playing_violin, reading_book, skiing, spending_money, becoming_scuba_diver, cooking_meal, relaxing, getting_physical_activity, going_fishing, going_for_drive …
  - frame: UsedFor> enjoyment; UsedFor> pleasure
  - support 25; profile z 3.4 (null 15.62), sel p 1.0, repro 0%, profile2 z 1.9 (null 19.52), sel p 1.0, repro 0%; strict z 7.6
- **g14** n=24, uncategorised, shape 26, paraphrase frame: flying_kite, riding_bike, hearing_music, learning_new, celebrating, enjoying_film, entertaining_people, going_for_spin, going_for_walk, going_see_film, going_to_baseball_game, going_to_concert, going_to_film, going_to_opera …
  - frame: Causes> enjoyment; UsedFor> fun
  - support 24; profile z 3.2 (null 17.66), sel p 0.1782, repro 89%, profile2 z 2.2 (null 21.19), sel p 0.3168, repro 87%; strict z 7.5
- **g23** n=23, crosscutting, shape 28, paraphrase frame: climbing, gymnasium, baseball_stadium, dancing, swimming, tennis_game, flying_kite, jumping_rope, riding_bicycle, hiking, diving, playing_hockey, playing_sports, riding_bike …
  - frame: UsedFor> exercise; UsedFor> fun
  - support 23; profile z 3.2 (null 15.3), sel p 1.0, repro 0%, profile2 z 1.4 (null 21.27), sel p 1.0, repro 100%; strict z 6.6
- **g44** n=22, crosscutting, shape 10, paraphrase frame: food, goods, paint, handbag, clerk, mouse, candy, cash_register, clothing, clerks, clothes, jeans, display_cabinet, label_maker …
  - frame: AtLocation> store; AtLocation> shop
  - support 22; profile z 7.0 (null 5.23), sel p 0.3366, repro 0%, profile2 z 4.9 (null 14.46), sel p 0.4851, repro 100%; strict z 9.3
- **g726** n=22, uncategorised, shape 28, distinct frame: show, writing, reading, reading_book, skiing, becoming_scuba_diver, creating_art, enjoying_film, getting_onto_web, going_outside_for_evening, traveling, going_to_zoo, playing_basketball, seeing_art …
  - frame: UsedFor> education; UsedFor> entertainment; UsedFor> fun; UsedFor> relaxation
  - support 22; profile z 2.9 (null 14.74), sel p 1.0, repro 1%, profile2 z 0.5 (null 20.73), sel p 1.0, repro 8%; strict z 8.4

## Anomaly 18 family (groups with ≥ 2 of swimming, surfing, skating, skiing, dancing, singing, playing_cards)

58 groups.

| g | n | anomaly-18 members | frame | tier | relation z / sel p / repro | strict z / sel p / repro | profile z / sel p / repro | profile2 z / sel p / repro | survives profile | + selection |
|---|---|---|---|---|---|---|---|---|---|---|
| 1439 | 62 | singing, skating, skiing, surfing, swimming | UsedFor> enjoyment; UsedFor> entertainment; UsedFor> fun; UsedFor> relaxation | uncategorised | 30.6 / 0.0099 / 0% | 17.3 / 0.0099 / 0% | 8.5 / 0.1683 / 0% | 3.6 / 0.099 / 28% | False | False |
| 2 | 59 | singing, skating, surfing, swimming | UsedFor> fun; UsedFor> having_fun | uncategorised | 15.6 / 0.0099 / 0% | 11.9 / 0.0099 / 0% | 7.7 / 0.2376 / 37% | 0.0 / 1.0 / 100% | False | False |
| 1745 | 57 | dancing, playing_cards, singing, skating, skiing, surfing, swimming | UsedFor> enjoyment; UsedFor> pleasure; UsedFor> entertainment | crosscutting | 14.4 / 0.0099 / 0% | 9.1 / 0.0099 / 0% | 6.3 / 0.2871 / 0% | 4.6 / 1.0 / 7% | False | False |
| 3 | 47 | dancing, singing, skating, skiing, surfing | UsedFor> entertainment; UsedFor> fun | crosscutting | 12.8 / 0.0099 / 0% | 8.8 / 0.0099 / 0% | 4.7 / 0.505 / 0% | 2.5 / 1.0 / 23% | False | False |
| 3403 | 43 | skating, skiing, swimming | UsedFor> pleasure; UsedFor> relaxation; UsedFor> relaxing | crosscutting | 15.0 / 0.0099 / 0% | 9.5 / 0.0198 / 0% | 5.2 / 0.5248 / 0% | 4.1 / 1.0 / 1% | True | False |
| 4 | 41 | singing, skating, skiing, swimming | UsedFor> enjoyment; UsedFor> fun | uncategorised | 12.8 / 0.0099 / 0% | 7.6 / 0.0198 / 0% | 5.1 / 0.5347 / 1% | 2.9 / 1.0 / 95% | False | False |
| 2221 | 39 | playing_cards, skating, skiing, swimming | UsedFor> pleasure; UsedFor> relaxation; UsedFor> passing_time | crosscutting | 14.8 / 0.0099 / 0% | 11.0 / 0.0297 / 0% | 4.2 / 0.5446 / 0% | 4.6 / 1.0 / 0% | True | False |
| 6 | 36 | skating, skiing, swimming | UsedFor> fun; UsedFor> relaxation | uncategorised | 12.8 / 0.0099 / 0% | 8.4 / 0.0297 / 0% | 3.8 / 0.6634 / 0% | 1.2 / 1.0 / 2% | False | False |
| 1232 | 36 | skating, skiing, swimming | UsedFor> enjoyment; UsedFor> education; UsedFor> relaxation | uncategorised | 11.1 / 0.0099 / 0% | 6.7 / 0.0297 / 0% | 3.7 / 0.6634 / 0% | 1.2 / 1.0 / 3% | False | False |
| 8 | 32 | dancing, skating, skiing, surfing, swimming | UsedFor> pleasure; UsedFor> fun | crosscutting | 8.6 / 0.0099 / 0% | 6.2 / 0.0297 / 0% | 2.3 / 0.8614 / 0% | 0.1 / 1.0 / 2% | False | False |
| 3062 | 32 | dancing, skating, skiing, surfing, swimming | Causes> injury; UsedFor> exercise; UsedFor> pleasure; UsedFor> entertainment | partly_named | 18.0 / 0.0099 / 0% | 11.1 / 0.0297 / 0% | 5.1 / 0.8614 / 0% | 2.1 / 1.0 / 11% | False | False |
| 1296 | 31 | dancing, skating, skiing, surfing, swimming | UsedFor> exercise; UsedFor> pleasure; UsedFor> fun; UsedFor> recreation | crosscutting | 17.1 / 0.0099 / 0% | 9.2 / 0.0297 / 0% | 3.4 / 0.8911 / 0% | -1.4 / 1.0 / 22% | False | False |
| 20 | 26 | dancing, singing | Causes> happiness; UsedFor> fun | uncategorised | 5.1 / 0.0099 / 0% | 3.2 / 0.0297 / 0% | 2.1 / 0.0495 / 3% | 2.3 / 0.1683 / 79% | False | False |
| 11 | 25 | playing_cards, skating, skiing, swimming | UsedFor> enjoyment; UsedFor> pleasure | crosscutting | 11.7 / 0.0099 / 0% | 7.6 / 0.099 / 0% | 3.4 / 1.0 / 0% | 1.9 / 1.0 / 0% | False | False |
| 1301 | 25 | singing, skating, skiing, swimming | Causes> fatigue; UsedFor> enjoyment; UsedFor> entertainment; UsedFor> fun | uncategorised | 32.8 / 0.0099 / 0% | 17.0 / 0.099 / 0% | 7.2 / 1.0 / 0% | 3.3 / 1.0 / 1% | True | False |
| 1819 | 25 | dancing, playing_cards, skating, skiing, surfing | HasPrerequisite> skill; UsedFor> pleasure; UsedFor> entertainment; UsedFor> fun | crosscutting | 22.8 / 0.0099 / 0% | 12.5 / 0.099 / 0% | 5.8 / 1.0 / 0% | 2.0 / 1.0 / 3% | False | False |
| 3242 | 25 | skating, skiing, swimming | UsedFor> enjoyment; UsedFor> pleasure; UsedFor> fun; UsedFor> recreation | uncategorised | 19.6 / 0.0099 / 0% | 11.8 / 0.099 / 0% | 4.8 / 1.0 / 0% | 1.4 / 1.0 / 18% | False | False |
| 3075 | 24 | playing_cards, singing, skating | HasPrerequisite> skill; UsedFor> enjoyment; UsedFor> entertainment; UsedFor> fun | partly_named | 29.4 / 0.0099 / 0% | 22.2 / 0.1584 / 0% | 7.2 / 1.0 / 0% | 2.8 / 1.0 / 3% | False | False |
| 16 | 23 | dancing, playing_cards, skating, skiing, surfing | UsedFor> pleasure; UsedFor> entertainment | partly_named | 9.4 / 0.0099 / 0% | 5.6 / 0.2376 / 0% | 4.2 / 1.0 / 0% | 2.9 / 1.0 / 0% | False | False |
| 23 | 23 | dancing, skating, skiing, surfing, swimming | UsedFor> exercise; UsedFor> fun | crosscutting | 9.1 / 0.0099 / 0% | 6.6 / 0.2376 / 0% | 3.2 / 1.0 / 0% | 1.4 / 1.0 / 100% | False | False |
| 726 | 22 | skating, skiing | UsedFor> education; UsedFor> entertainment; UsedFor> fun; UsedFor> relaxation | uncategorised | 16.3 / 0.0099 / 0% | 8.4 / 0.3465 / 0% | 2.9 / 1.0 / 1% | 0.5 / 1.0 / 8% | False | False |
| 39 | 21 | skiing, swimming | UsedFor> fun; UsedFor> recreation | uncategorised | 8.3 / 0.0099 / 0% | 5.3 / 0.4752 / 0% | 3.5 / 1.0 / 0% | 0.0 / 1.0 / 100% | False | False |
| 721 | 20 | skating, skiing, surfing, swimming | UsedFor> competition; UsedFor> exercise; UsedFor> fun; UsedFor> having_fun | partly_named | 18.4 / 0.0099 / 0% | 11.8 / 0.6238 / 0% | 5.6 / 1.0 / 0% | 2.8 / 1.0 / 4% | False | False |
| 42 | 19 | skating, skiing, swimming | UsedFor> pleasure; UsedFor> relaxation | crosscutting | 11.6 / 0.0099 / 0% | 6.5 / 0.7624 / 0% | 3.4 / 1.0 / 0% | 2.8 / 1.0 / 1% | True | False |
| 1395 | 19 | playing_cards, skating, skiing | UsedFor> enjoyment; UsedFor> pleasure; UsedFor> entertainment; UsedFor> fun | crosscutting | 21.4 / 0.0099 / 0% | 13.0 / 0.7624 / 0% | 4.2 / 1.0 / 0% | 2.4 / 1.0 / 0% | False | False |
| 51 | 16 | dancing, skating, skiing, surfing | Causes> injury; UsedFor> exercise | partly_named | 14.4 / 0.1188 / 0% | 10.2 / 0.8713 / 0% | 9.3 / 1.0 / 0% | 4.0 / 1.0 / 62% | False | False |
| 113 | 16 | dancing, skating, skiing, surfing | Causes> injury; UsedFor> fun | partly_named | 6.0 / 0.1188 / 0% | 3.9 / 0.8713 / 0% | 3.3 / 1.0 / 0% | 1.1 / 1.0 / 57% | False | False |
| 59 | 15 | skiing, swimming | UsedFor> competition; UsedFor> exercise; UsedFor> fun; UsedFor> recreation | crosscutting | 20.7 / 0.2772 / 0% | 12.3 / 1.0 / 0% | 6.5 / 1.0 / 0% | 5.3 / 1.0 / 33% | False | False |
| 2000 | 14 | skiing, swimming | HasPrerequisite> skill; UsedFor> competition; UsedFor> pleasure; UsedFor> fun | crosscutting | 26.3 / 0.3366 / 0% | 14.7 / 1.0 / 0% | 5.6 / 1.0 / 0% | 0.6 / 1.0 / 6% | False | False |
| 171 | 13 | surfing, swimming | Causes> get_wet; Causes> getting_wet; HasPrerequisite> water | crosscutting | 16.8 / 0.0099 / 0% | 10.2 / 0.0198 / 0% | 6.3 / 0.9802 / 0% | 6.4 / 1.0 / 0% | True | False |
| 255 | 12 | skiing, swimming | Causes> getting_tired; UsedFor> competition; UsedFor> exercise; UsedFor> enjoyment | crosscutting | 23.8 / 0.6337 / 0% | 23.6 / 1.0 / 0% | 10.7 / 1.0 / 0% | 9.3 / 1.0 / 0% | True | False |
| 345 | 11 | playing_cards, singing | Causes> happiness; UsedFor> enjoyment | uncategorised | 3.7 / 0.9703 / 0% | 1.5 / 1.0 / 0% | 1.7 / 1.0 / 5% | 1.5 / 1.0 / 12% | False | False |
| 1212 | 11 | skating, skiing, surfing, swimming | HasPrerequisite> balance; UsedFor> exercise; UsedFor> pleasure; UsedFor> fun | partly_named | 18.5 / 0.8119 / 0% | 13.2 / 1.0 / 0% | 4.7 / 1.0 / 0% | 0.4 / 1.0 / 50% | False | False |
| 3094 | 11 | dancing, playing_cards, singing, skiing | Causes> happiness; Causes> having_fun; UsedFor> entertainment; UsedFor> fun | crosscutting | 7.3 / 0.9703 / 0% | 3.8 / 1.0 / 0% | 2.7 / 1.0 / 0% | 0.8 / 1.0 / 11% | False | False |
| 402 | 10 | dancing, skiing | Causes> having_fun; UsedFor> fun | crosscutting | 5.0 / 1.0 / 0% | 3.6 / 1.0 / 0% | 3.6 / 1.0 / 8% | 0.0 / 1.0 / 98% | False | False |
| 418 | 10 | skating, skiing | HasSubevent> fall_down; UsedFor> fun | crosscutting | 7.4 / 0.0198 / 0% | 5.0 / 0.198 / 0% | 3.1 / 0.7327 / 0% | 2.5 / 1.0 / 34% | False | False |
| 480 | 10 | dancing, playing_cards | Causes> happiness; UsedFor> pleasure | crosscutting | 4.0 / 1.0 / 0% | 1.6 / 1.0 / 0% | 1.3 / 1.0 / 1% | 0.9 / 1.0 / 11% | False | False |
| 2347 | 10 | skating, skiing | Causes> having_fun; UsedFor> relaxation; UsedFor> social_interaction | uncategorised | 6.3 / 0.9505 / 0% | 4.0 / 1.0 / 0% | 1.4 / 1.0 / 0% | 0.8 / 1.0 / 0% | False | False |
| 3207 | 10 | skiing, swimming | Causes> sweat; UsedFor> competition; UsedFor> enjoyment; UsedFor> fun | partly_named | 14.7 / 0.9505 / 0% | 8.2 / 1.0 / 0% | 3.5 / 1.0 / 0% | 2.7 / 1.0 / 0% | True | False |
| 191 | 9 | dancing, skiing | Causes> injury; Causes> having_fun; UsedFor> exercise; UsedFor> passing_time | partly_named | 17.7 / 1.0 / 0% | 15.9 / 1.0 / 0% | 3.9 / 1.0 / 14% | 0.9 / 1.0 / 93% | False | False |
| 500 | 9 | skating, swimming | UsedFor> fun; UsedFor> keeping_fit | partly_named | 5.1 / 1.0 / 0% | 4.0 / 1.0 / 0% | 2.5 / 1.0 / 0% | 1.2 / 1.0 / 4% | False | False |
| 949 | 9 | skating, skiing, swimming | Causes> injury; Causes> injuries; UsedFor> competition; UsedFor> exercise | partly_named | 18.0 / 1.0 / 0% | 18.0 / 1.0 / 0% | 12.2 / 1.0 / 0% | 5.8 / 1.0 / 71% | False | False |
| 1742 | 9 | dancing, playing_cards | Causes> happiness; Causes> laughter; Causes> having_fun; UsedFor> pleasure | uncategorised | 10.2 / 1.0 / 0% | 5.7 / 1.0 / 0% | 2.9 / 1.0 / 1% | 2.0 / 1.0 / 7% | False | False |
| 2883 | 9 | dancing, skiing, surfing | Causes> enjoyment; Causes> having_fun; UsedFor> exercise; UsedFor> fun | partly_named | 13.6 / 1.0 / 0% | 7.2 / 1.0 / 0% | 2.9 / 1.0 / 1% | 1.0 / 1.0 / 43% | False | False |
| 383 | 8 | dancing, playing_cards | Causes> having_fun; UsedFor> socializing | uncategorised | 10.4 / 1.0 / 0% | 7.5 / 1.0 / 0% | 3.9 / 1.0 / 0% | 0.6 / 1.0 / 100% | False | False |
| 514 | 8 | skating, skiing | Causes> injury; Causes> injuries; Causes> getting_injured; UsedFor> competition | named | 16.0 / 1.0 / 0% | 15.9 / 1.0 / 1% | 15.8 / 1.0 / 0% | 5.2 / 1.0 / 8% | False | False |
| 1912 | 8 | skating, skiing, swimming | UsedFor> competition; UsedFor> exercise; UsedFor> enjoyment; UsedFor> pleasure | named | 15.8 / 1.0 / 0% | 15.8 / 1.0 / 0% | 6.4 / 1.0 / 0% | 2.7 / 1.0 / 12% | False | False |
| 3071 | 8 | skating, swimming | Causes> getting_exercise; Causes> sore_muscles; UsedFor> exercise; UsedFor> enjoyment | partly_named | 15.7 / 1.0 / 0% | 10.7 / 1.0 / 0% | 3.7 / 1.0 / 0% | 2.8 / 1.0 / 0% | False | False |
| 178 | 7 | surfing, swimming | Causes> drowning; Causes> get_wet; Causes> getting_wet; HasPrerequisite> water | partly_named | 14.0 / 1.0 / 0% | 13.9 / 1.0 / 0% | 12.5 / 1.0 / 5% | 3.6 / 1.0 / 85% | False | False |
| 836 | 7 | playing_cards, skiing | Causes> having_fun; UsedFor> enjoyment | crosscutting | 5.2 / 1.0 / 0% | 4.1 / 1.0 / 1% | 1.1 / 1.0 / 16% | 2.3 / 1.0 / 39% | False | False |
| 968 | 7 | dancing, playing_cards, skiing | Causes> having_fun; UsedFor> entertainment | crosscutting | 5.6 / 1.0 / 0% | 3.4 / 1.0 / 0% | 1.1 / 1.0 / 4% | 0.5 / 1.0 / 31% | False | False |
| 1090 | 7 | playing_cards, singing | Causes> anger; UsedFor> enjoyment | uncategorised | 3.6 / 1.0 / 0% | 2.0 / 1.0 / 0% | 2.2 / 1.0 / 0% | 1.4 / 1.0 / 11% | False | False |
| 3008 | 6 | dancing, skiing | Causes> happiness; Causes> injury; Causes> having_fun; UsedFor> competition | crosscutting | 12.0 / 1.0 / 0% | 11.8 / 1.0 / 0% | 9.0 / 1.0 / 4% | 3.2 / 1.0 / 37% | False | False |
| 787 | 5 | dancing, skating, skiing | Causes> injury; Causes> having_fun; Causes> injuries; HasPrerequisite> coordination | named | 10.0 / 1.0 / 0% | 10.0 / 1.0 / 0% | 9.9 / 1.0 / 3% | 3.7 / 1.0 / 52% | False | False |
| 1690 | 5 | dancing, skiing | Causes> injury; Causes> sweat; Causes> exhaustion; Causes> becoming_tired | partly_named | 10.0 / 1.0 / 0% | 10.0 / 1.0 / 0% | 10.0 / 1.0 / 3% | 9.9 / 1.0 / 8% | False | False |
| 2226 | 5 | skating, swimming | Causes> fatigue; UsedFor> enjoyment; UsedFor> pleasure; UsedFor> fun | partly_named | 9.9 / 1.0 / 0% | 9.7 / 1.0 / 1% | 4.6 / 1.0 / 1% | 1.3 / 1.0 / 1% | False | False |
| 860 | 4 | skating, skiing, swimming | Causes> injury; Causes> falling; Causes> increased_heart_rate; HasSubevent> fall_down | named | 8.0 / 1.0 / 0% | 8.0 / 1.0 / 0% | 8.0 / 1.0 / 2% | 7.6 / 1.0 / 1% | True | False |
| 3167 | 4 | skating, skiing | UsedFor> enjoyment; UsedFor> social_interaction | named | 3.7 / 1.0 / 0% | 2.5 / 1.0 / 0% | 1.8 / 1.0 / 0% | 1.3 / 1.0 / 4% | False | False |

## What construction alone produces: largest unnamed groups mined from profile nulls (seeds 0–2)

- n=52, crosscutting, shape 28: car, thinking, baseball_stadium, frisbee, watching_television, singing, swimming, toy_ball, flying_kite, jumping_rope, riding_bicycle, drinking_alcohol …
  - frame: UsedFor> fun; UsedFor> having_fun; UsedFor> relaxing
- n=37, crosscutting, shape 28: writing, baseball_stadium, bass, dancing, discothque, vacation, fishing, jumping_rope, hiking, playing_sports, playing_violin, riding_bike …
  - frame: UsedFor> entertainment; UsedFor> fun
- n=35, uncategorised, shape 28: show, running, toy_marble, riding_bicycle, listening_to_music, planning_vacation, reading_book, skiing, cooking_meal, creating_art, getting_onto_web, going_for_drive …
  - frame: UsedFor> enjoyment; UsedFor> relaxation; UsedFor> having_fun
- n=32, uncategorised, shape 28: living, writing, climbing, acoustic_guitar, singing, swimming, playing_sports, reading_book, learning_new, chatting_with_friends, getting_exercise, copulating …
  - frame: UsedFor> enjoyment; UsedFor> fun
- n=30, uncategorised, shape 28: car, surprising, climbing, canoe, singing, swimming, playing_sports, becoming_inebriated, celebrating, creating_art, dreaming, fencing …
  - frame: UsedFor> fun; UsedFor> having_fun
- n=30, crosscutting, shape 10: beer, gun, book, automobile, bag, steak_house, basketball, books, satchel, bread, lamp, computer …
  - frame: AtLocation> desk; AtLocation> office; AtLocation> store
- n=25, crosscutting, shape 28: living, writing, painting, nightclub, watching_television, killing, swimming, flying_kite, riding_bicycle, having_sex, doing_crossword_puzzle, driving_car …
  - frame: UsedFor> pleasure; UsedFor> fun
- n=24, uncategorised, shape 26: living, diving, making_friends, attending_classical_concert, buying_christmas_presents, eating_hamburger, buying_presents, buying_presents_for_others, celebrating, chatting_with_friends, eating_cookie, enjoying_day …
  - frame: Causes> happiness; UsedFor> fun
