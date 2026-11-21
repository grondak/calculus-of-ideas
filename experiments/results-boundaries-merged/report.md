# Sparse boundaries between structured neighbourhoods

A candidate pair is two typed groups with disjoint cores whose member neighbourhoods (outside both cores) are in the top 1% of context similarity among all core-disjoint group pairs of the same graph. It is a *boundary* when the two cores (members + frame anchors) have no conceptual link at all while comparable candidate pairs (same similarity, size, degree and dominant-relation bins) have a median of at least 2 links. Every null graph is generated at the original-id level, contracted with the same class map, re-mined, and scored the same way. No edges are proposed.

## unmerged

| graph | groups | candidate pairs | boundaries | boundary rate | p (rate real ≥ null) | candidate pairs linked | p (real unlinked share ≥ null) |
|---|---|---|---|---|---|---|---|
| real | 1511 | 6347 | 183 | 0.029 | | 0.64 | |
| relation null (mean) | 748 | 2381 | 46.4 [max 167] | 0.019 [0.004–0.065] | 0.1386 | 0.98 | 0.0099 |
| strict null (mean) | 359 | 508 | 21.7 [max 46] | 0.043 [0.005–0.084] | 0.8317 | 0.78 | 0.0099 |
| profile null (mean) | 573 | 1240 | 73.6 [max 142] | 0.059 [0.031–0.105] | 1.0 | 0.93 | 0.0099 |
| profile2 null (mean) | 771 | 2179 | 116.1 [max 173] | 0.053 [0.033–0.080] | 1.0 | 0.93 | 0.0099 |

Sparse regions: candidate pairs grouped by the two groups' dominant frame relations. Linked share in the real graph vs re-mined nulls (strata with ≥ 20 real pairs; null graphs where the stratum has ≥ 5 pairs).

| dominant relations | real pairs | real linked | relation linked [p real ≤ null, graphs] | strict linked [p real ≤ null, graphs] | profile linked [p real ≤ null, graphs] | profile2 linked [p real ≤ null, graphs] |
|---|---|---|---|---|---|---|
| AtLocation x AtLocation | 1713 | 0.95 | 0.98 [0.0396, 100] | 0.802 [1.0, 100] | 0.932 [0.901, 100] | 0.941 [0.8713, 100] |
| HasPrerequisite x HasPrerequisite | 1428 | 0.43 | — | — | — | 0.422 [0.5, 13] |
| AtLocation x UsedFor | 717 | 0.79 | 0.661 [0.8, 4] | 0.655 [0.7391, 91] | 0.458 [0.963, 26] | 0.85 [0.2871, 100] |
| HasPrerequisite x UsedFor | 391 | 0.32 | — | — | — | — |
| Causes x HasPrerequisite | 275 | 0.44 | — | 0.8 [0.5, 1] | — | 0.571 [0.5, 1] |
| Causes x UsedFor | 269 | 0.61 | — | 0.861 [0.15, 19] | — | 1.0 [0.5, 1] |
| AtLocation x HasPrerequisite | 267 | 0.50 | — | — | — | 0.216 [0.75, 3] |
| UsedFor x UsedFor | 258 | 0.55 | — | 1.0 [0.5, 1] | 1.0 [0.125, 7] | 0.982 [0.0263, 37] |
| HasPrerequisite x HasSubevent | 138 | 0.51 | — | — | — | 0.5 [0.6667, 2] |
| Causes x Causes | 112 | 0.73 | — | 0.86 [0.122, 40] | — | 0.933 [0.25, 3] |
| CapableOf x HasPrerequisite | 107 | 0.28 | — | — | — | 0.309 [0.4167, 23] |
| HasSubevent x UsedFor | 67 | 0.49 | — | — | — | — |
| HasPrerequisite x MotivatedByGoal | 56 | 0.61 | — | — | — | — |
| AtLocation x ReceivesAction | 44 | 0.93 | 1.0 [0.5, 1] | 0.721 [0.88, 24] | 0.678 [0.8667, 14] | 0.921 [0.4824, 84] |
| AtLocation x HasProperty | 41 | 0.93 | — | 0.715 [0.8537, 40] | — | 0.679 [0.8269, 51] |
| ReceivesAction x UsedFor | 37 | 0.51 | — | — | — | 0.429 [1.0, 1] |
| Causes x HasSubevent | 34 | 0.62 | — | 0.733 [0.3333, 2] | — | — |
| HasLastSubevent x HasPrerequisite | 34 | 0.50 | — | — | — | — |
| CapableOf x UsedFor | 32 | 0.16 | — | 0.6 [0.5, 1] | — | 0.8 [0.25, 3] |
| CapableOf x Causes | 26 | 0.50 | 0.5 [1.0, 1] | — | — | — |
| AtLocation x Causes | 25 | 0.80 | — | 0.141 [1.0, 9] | — | — |
| CausesDesire x HasPrerequisite | 22 | 0.95 | — | — | — | — |

Same real group pairs re-checked in every null graph (cores fixed). Unlinked real candidate pairs: 2269; unlinked in ≤ 5% of graphs of both profile nulls: 3; BH q ≤ 0.10: 0.

| dominant relations | real pairs | real linked | relation linked [p real ≤ null] | strict linked [p real ≤ null] | profile linked [p real ≤ null] | profile2 linked [p real ≤ null] |
|---|---|---|---|---|---|---|
| AtLocation x AtLocation | 1713 | 0.95 | 0.71 [1.0] | 0.82 [1.0] | 0.89 [1.0] | 0.93 [1.0] |
| HasPrerequisite x HasPrerequisite | 1428 | 0.43 | 0.33 [1.0] | 0.36 [1.0] | 0.51 [0.0099] | 0.52 [0.0099] |
| AtLocation x UsedFor | 717 | 0.79 | 0.37 [1.0] | 0.51 [1.0] | 0.62 [1.0] | 0.71 [1.0] |
| HasPrerequisite x UsedFor | 391 | 0.32 | 0.12 [1.0] | 0.14 [1.0] | 0.23 [1.0] | 0.28 [1.0] |
| Causes x HasPrerequisite | 275 | 0.44 | 0.18 [1.0] | 0.20 [1.0] | 0.31 [1.0] | 0.36 [1.0] |
| Causes x UsedFor | 269 | 0.61 | 0.25 [1.0] | 0.35 [1.0] | 0.50 [1.0] | 0.57 [0.9604] |
| AtLocation x HasPrerequisite | 267 | 0.50 | 0.14 [1.0] | 0.22 [1.0] | 0.28 [1.0] | 0.35 [1.0] |
| UsedFor x UsedFor | 258 | 0.55 | 0.23 [1.0] | 0.36 [1.0] | 0.49 [0.9802] | 0.54 [0.6832] |
| HasPrerequisite x HasSubevent | 138 | 0.51 | 0.23 [1.0] | 0.26 [1.0] | 0.37 [1.0] | 0.44 [0.9901] |
| Causes x Causes | 112 | 0.73 | 0.40 [1.0] | 0.46 [1.0] | 0.62 [0.9901] | 0.71 [0.7723] |
| CapableOf x HasPrerequisite | 107 | 0.28 | 0.13 [1.0] | 0.19 [0.9901] | 0.23 [0.9802] | 0.25 [1.0] |
| HasSubevent x UsedFor | 67 | 0.49 | 0.15 [1.0] | 0.19 [1.0] | 0.36 [1.0] | 0.45 [0.9901] |
| HasPrerequisite x MotivatedByGoal | 56 | 0.61 | 0.27 [1.0] | 0.29 [1.0] | 0.39 [1.0] | 0.46 [1.0] |
| AtLocation x ReceivesAction | 44 | 0.93 | 0.69 [1.0] | 0.82 [1.0] | 0.89 [1.0] | 0.92 [0.8911] |
| AtLocation x HasProperty | 41 | 0.93 | 0.73 [0.9604] | 0.80 [0.8812] | 0.75 [1.0] | 0.79 [1.0] |
| ReceivesAction x UsedFor | 37 | 0.51 | 0.28 [1.0] | 0.31 [0.9901] | 0.41 [0.9406] | 0.41 [0.9307] |
| Causes x HasSubevent | 34 | 0.62 | 0.33 [1.0] | 0.41 [1.0] | 0.46 [0.9901] | 0.55 [0.9703] |
| HasLastSubevent x HasPrerequisite | 34 | 0.50 | 0.40 [0.8713] | 0.42 [0.8614] | 0.49 [0.7327] | 0.54 [0.3663] |
| CapableOf x UsedFor | 32 | 0.16 | 0.08 [0.9703] | 0.12 [0.8911] | 0.17 [0.6238] | 0.17 [0.6931] |
| CapableOf x Causes | 26 | 0.50 | 0.13 [1.0] | 0.19 [1.0] | 0.30 [1.0] | 0.36 [1.0] |
| AtLocation x Causes | 25 | 0.80 | 0.08 [1.0] | 0.21 [1.0] | 0.50 [1.0] | 0.73 [1.0] |
| CausesDesire x HasPrerequisite | 22 | 0.95 | 0.61 [1.0] | 0.65 [1.0] | 0.77 [1.0] | 0.79 [0.9901] |

### Sparse region HasPrerequisite x HasPrerequisite: unlinked real pairs that both profile nulls link most often

- linked in ≥ 96% of graphs of each profile null; context 0.017; relation null mean links 1.07; strict null mean links 1.65; profile null mean links 3.33; profile2 null mean links 3.84
  - A (9): fly_in_airplane, attend_classical_concert, go_see_play, see_favorite_show, go_to_opera, watch_musician_perform, go_to_sporting_event, see_particular_program, see_band — frame HasPrerequisite> buy_ticket; HasPrerequisite> buy_tickets
  - B (9): stretch_muscles, put_on_shoes, dress_appropriately, go_to_park, stretch_first, put_on_jogging_clothes, put_on_jogging_suit, wear_good_shoes, wear_jogging_shoes — frame HasPrerequisite< go_jogging; HasPrerequisite< go_for_jog
  - shared surroundings: listen_to_music, go_home, open_eyes, go_to_performance, go_out, dance, leave_house, put_on_pants, go_somewhere
  - A→surroundings [['HasSubevent>', 6], ['HasPrerequisite>', 5], ['HasLastSubevent>', 2], ['HasFirstSubevent<', 1], ['HasPrerequisite<', 1]]; B→surroundings [['HasPrerequisite>', 3], ['HasFirstSubevent>', 2], ['HasLastSubevent>', 2], ['HasSubevent>', 2], ['HasPrerequisite<', 2]]
- linked in ≥ 96% of graphs of each profile null; context 0.032; relation null mean links 1.51; strict null mean links 2.53; profile null mean links 3.09; profile2 null mean links 2.95
  - A (4): buy_ticket, go_to_theater, go_to_theatre, buy_tickets — frame HasPrerequisite< watch_movie; HasPrerequisite< attend_classical_concert; HasPrerequisite< go_see_play; HasPrerequisite< enjoy_film; HasPrerequisite< watch_musician_perform …
  - B (4): use_water, go_to_bathroom, turn_on_water, take_clothes_off — frame HasPrerequisite< bathe; HasPrerequisite< have_bath; HasPrerequisite< take_shower; HasPrerequisite< wash_hands; HasPrerequisite< have_shower
  - shared surroundings: child, go_to_movie, stand_in_line, visit_art_gallery, getting_married, going_to_movie, have_sex
  - A→surroundings [['HasPrerequisite<', 2], ['HasPrerequisite>', 1], ['MotivatedByGoal>', 1], ['CausesDesire<', 1], ['HasFirstSubevent<', 1]]; B→surroundings [['CapableOf<', 2], ['HasPrerequisite<', 2], ['HasPrerequisite>', 1], ['CausesDesire<', 1], ['HasLastSubevent<', 1]]
- linked in ≥ 94% of graphs of each profile null; context 0.021; relation null mean links 0.98; strict null mean links 1.82; profile null mean links 2.89; profile2 null mean links 3.58
  - A (5): go_to_cinema, go_to_movie_theater, go_to_theatre, rent_movie, go_to_movie_theatre — frame HasPrerequisite< watch_movie; HasPrerequisite< watch_film; HasPrerequisite< take_in_film; HasPrerequisite< go_see_film
  - B (4): use_water, go_to_bathroom, turn_on_water, take_clothes_off — frame HasPrerequisite< bathe; HasPrerequisite< have_bath; HasPrerequisite< take_shower; HasPrerequisite< wash_hands; HasPrerequisite< have_shower
  - shared surroundings: go_to_film, go_to_movie, going_to_movie, eat_ice_cream, sit
  - A→surroundings [['HasPrerequisite>', 2], ['HasSubevent>', 2], ['HasPrerequisite<', 2], ['HasSubevent<', 2]]; B→surroundings [['HasLastSubevent<', 3], ['HasPrerequisite>', 1], ['HasSubevent<', 1]]
- linked in ≥ 93% of graphs of each profile null; context 0.03; relation null mean links 0.59; strict null mean links 1.18; profile null mean links 2.25; profile2 null mean links 2.32
  - A (9): stretch_muscles, put_on_shoes, dress_appropriately, go_to_park, stretch_first, put_on_jogging_clothes, put_on_jogging_suit, wear_good_shoes, wear_jogging_shoes — frame HasPrerequisite< go_jogging; HasPrerequisite< go_for_jog
  - B (5): buy_ticket, buy_tickets, drive_there, find_one, use_ticket — frame HasPrerequisite< go_to_movie; HasPrerequisite< attend_classical_concert; HasPrerequisite< go_to_opera; HasPrerequisite< see_band
  - shared surroundings: listen_to_music, go_to_pub, leave_house, go_to_performance, go_out, go_home, open_eyes, go_on_vacation, dance
  - A→surroundings [['HasPrerequisite<', 3], ['HasFirstSubevent>', 2], ['HasLastSubevent>', 2], ['HasPrerequisite>', 2], ['HasSubevent>', 2]]; B→surroundings [['HasPrerequisite>', 3], ['HasSubevent>', 3], ['HasPrerequisite<', 3], ['HasFirstSubevent>', 1], ['HasLastSubevent>', 1]]
- linked in ≥ 92% of graphs of each profile null; context 0.029; relation null mean links 0.75; strict null mean links 1.18; profile null mean links 2.36; profile2 null mean links 2.66
  - A (9): stretch_muscles, put_on_shoes, dress_appropriately, go_to_park, stretch_first, put_on_jogging_clothes, put_on_jogging_suit, wear_good_shoes, wear_jogging_shoes — frame HasPrerequisite< go_jogging; HasPrerequisite< go_for_jog
  - B (4): buy_ticket, turn_on_tv, buy_tickets, turn_on_television — frame HasPrerequisite< watch_movie; HasPrerequisite< see_movie; HasPrerequisite< see_favorite_show; HasPrerequisite< see_particular_program
  - shared surroundings: open_eyes, go_to_performance, see_people_play_game, get_fit
  - A→surroundings [['HasPrerequisite<', 2], ['HasPrerequisite>', 1], ['HasSubevent>', 1]]; B→surroundings [['HasFirstSubevent<', 2], ['HasPrerequisite<', 2], ['HasFirstSubevent>', 1], ['HasPrerequisite>', 1]]
- linked in ≥ 92% of graphs of each profile null; context 0.018; relation null mean links 1.16; strict null mean links 1.92; profile null mean links 2.79; profile2 null mean links 1.92
  - A (7): go_to_cinema, go_to_movie_theater, turn_on_tv, turn_on_television, rent_movie, rent_video, rent_one — frame HasPrerequisite< watch_movie; HasPrerequisite< see_movie; HasPrerequisite< watch_film; HasPrerequisite< view_film_at_home
  - B (4): use_water, go_to_bathroom, turn_on_water, take_clothes_off — frame HasPrerequisite< bathe; HasPrerequisite< have_bath; HasPrerequisite< take_shower; HasPrerequisite< wash_hands; HasPrerequisite< have_shower
  - shared surroundings: go_to_film, going_to_movie, go_to_movie, eat_ice_cream
  - A→surroundings [['HasPrerequisite<', 2], ['HasSubevent<', 2], ['HasPrerequisite>', 1], ['HasSubevent>', 1], ['MotivatedByGoal<', 1]]; B→surroundings [['HasLastSubevent<', 3], ['HasSubevent<', 1]]
- linked in ≥ 90% of graphs of each profile null; context 0.031; relation null mean links 1.21; strict null mean links 1.99; profile null mean links 2.52; profile2 null mean links 2.22
  - A (11): go_to_concert, buy_ticket, open_eyes, go_to_theater, go_to_theatre, buy_tickets, buy_tickets_to_concert, buy_ticket_to_concert, go_to_club, buy_concert_ticket … — frame HasPrerequisite< watch_musician_perform; HasPrerequisite< see_band
  - B (4): use_water, go_to_bathroom, turn_on_water, take_clothes_off — frame HasPrerequisite< bathe; HasPrerequisite< have_bath; HasPrerequisite< take_shower; HasPrerequisite< wash_hands; HasPrerequisite< have_shower
  - shared surroundings: get_dressed, take_bath, go_to_movie, waking_up_in_morning, awake, run_in_marathon, visit_art_gallery, stand_in_line, getting_married, socialize
  - A→surroundings [['HasPrerequisite<', 7], ['HasPrerequisite>', 1], ['MotivatedByGoal>', 1], ['HasFirstSubevent<', 1], ['HasLastSubevent<', 1]]; B→surroundings [['HasPrerequisite<', 6], ['HasLastSubevent<', 3], ['HasLastSubevent>', 2], ['HasFirstSubevent<', 2], ['HasSubevent<', 2]]
- linked in ≥ 89% of graphs of each profile null; context 0.02; relation null mean links 0.98; strict null mean links 2.68; profile null mean links 1.55; profile2 null mean links 1.25
  - A (6): open_mouth, not_drive, go_to_bar, have_id, buy_alcohol, not_drive_car — frame HasPrerequisite< drink; HasPrerequisite< drink_alcohol
  - B (4): tie_shoes, put_on_shoes, go_to_park, wear_good_shoes — frame HasPrerequisite< walk; HasPrerequisite< run; HasPrerequisite< go_jogging; HasPrerequisite< go_for_jog
  - shared surroundings: go_to_pub, person, action, activity, pour, jump_up_and_down, breathe_fresh_air, escape, stumble, energy
  - A→surroundings [['RelatedTo>', 4], ['RelatedTo<', 4], ['HasFirstSubevent<', 3], ['HasFirstSubevent>', 1], ['HasSubevent>', 1]]; B→surroundings [['RelatedTo>', 5], ['RelatedTo<', 5], ['HasPrerequisite<', 3], ['Synonym>', 2], ['Synonym<', 2]]
- linked in ≥ 89% of graphs of each profile null; context 0.045; relation null mean links 0.8; strict null mean links 1.38; profile null mean links 2.26; profile2 null mean links 2.17
  - A (4): buy_ticket, turn_on_tv, buy_tickets, turn_on_television — frame HasPrerequisite< watch_movie; HasPrerequisite< see_movie; HasPrerequisite< see_favorite_show; HasPrerequisite< see_particular_program
  - B (5): bring_money, leave_house, get_dressed, put_on_shoes, get_car_keys — frame HasPrerequisite< go_to_store; HasPrerequisite< go_to_pub
  - shared surroundings: turn_off_tv, go_to_sporting_event, go_to_opera, go_to_performance, go_to_zoo, go_to_movie, find_seat, get_in_car, visit_art_gallery, go_to_film
  - A→surroundings [['HasPrerequisite<', 8], ['HasLastSubevent>', 2], ['HasPrerequisite>', 2], ['HasFirstSubevent<', 2], ['HasSubevent>', 1]]; B→surroundings [['HasPrerequisite<', 5], ['HasPrerequisite>', 3], ['HasFirstSubevent<', 3], ['HasFirstSubevent>', 1]]
- linked in ≥ 88% of graphs of each profile null; context 0.041; relation null mean links 0.3; strict null mean links 0.62; profile null mean links 1.69; profile2 null mean links 2.35
  - A (8): start_car, fasten_seatbelt, get_driver's_license, get_keys, get_license, have_driving_license, have_license, learn_how_to_drive — frame HasPrerequisite< drive; HasPrerequisite< drive_car
  - B (4): get_broom, use_hands, use_vacuum_cleaner, vacuum_floor — frame HasPrerequisite< clean_room; HasPrerequisite< do_housework
  - shared surroundings: test_car, find_keys, go_home, person
  - A→surroundings [['HasPrerequisite<', 3], ['HasPrerequisite>', 1], ['MotivatedByGoal>', 1], ['Desires<', 1]]; B→surroundings [['HasLastSubevent>', 1], ['HasPrerequisite>', 1], ['HasPrerequisite<', 1], ['NotDesires<', 1]]
- linked in ≥ 88% of graphs of each profile null; context 0.041; relation null mean links 0.49; strict null mean links 0.83; profile null mean links 1.78; profile2 null mean links 2.24
  - A (5): get_dressed, get_in_car, go_to_museum, choose_one_of_ytour_liking, go_to_major_city — frame HasPrerequisite< visit_museum; HasPrerequisite< visit_art_gallery
  - B (5): friendly, leave_house, brush_teeth, take_class, go_to_bar — frame HasPrerequisite< meet_people; HasPrerequisite< meet_interesting_people
  - shared surroundings: going_out_at_night, go_to_party, go_to_store, go_to_work, go_outside_for_evening, attend_school, go_to_laundromat, go_to_pub, go_to_market, go_to_mall
  - A→surroundings [['HasPrerequisite<', 13], ['HasSubevent>', 2], ['MotivatedByGoal>', 2], ['HasFirstSubevent<', 2], ['CapableOf<', 1]]; B→surroundings [['HasPrerequisite<', 9], ['HasPrerequisite>', 4], ['HasFirstSubevent<', 3], ['HasSubevent<', 2], ['HasFirstSubevent>', 1]]
- linked in ≥ 87% of graphs of each profile null; context 0.018; relation null mean links 0.44; strict null mean links 0.86; profile null mean links 1.72; profile2 null mean links 1.85
  - A (4): buy_ticket, turn_on_tv, buy_tickets, turn_on_television — frame HasPrerequisite< watch_movie; HasPrerequisite< see_movie; HasPrerequisite< see_favorite_show; HasPrerequisite< see_particular_program
  - B (4): go_outdoors, go_to_swimming_pool, learn_how_to_swim, go_to_pool — frame HasPrerequisite< dive; HasPrerequisite< go_for_swim
  - shared surroundings: get_fit, take_bus
  - A→surroundings [['HasFirstSubevent<', 1], ['HasSubevent<', 1]]; B→surroundings [['MotivatedByGoal>', 1], ['HasPrerequisite<', 1]]

### Unlinked context-similar group pairs least expected under both profile nulls (top 15)

- p_absent (worst profile) 0.0495, q=1.0, context 0.032; relation null mean links 1.51; strict null mean links 2.53; profile null mean links 3.09; profile2 null mean links 2.95
  - A (4): buy_ticket, go_to_theater, go_to_theatre, buy_tickets — frame HasPrerequisite< watch_movie; HasPrerequisite< attend_classical_concert; HasPrerequisite< go_see_play; HasPrerequisite< enjoy_film; HasPrerequisite< watch_musician_perform …
  - B (4): use_water, go_to_bathroom, turn_on_water, take_clothes_off — frame HasPrerequisite< bathe; HasPrerequisite< have_bath; HasPrerequisite< take_shower; HasPrerequisite< wash_hands; HasPrerequisite< have_shower
  - shared surroundings: child, go_to_movie, stand_in_line, visit_art_gallery, getting_married, going_to_movie, have_sex
  - A→surroundings [['HasPrerequisite<', 2], ['HasPrerequisite>', 1], ['MotivatedByGoal>', 1], ['CausesDesire<', 1], ['HasFirstSubevent<', 1]]; B→surroundings [['CapableOf<', 2], ['HasPrerequisite<', 2], ['HasPrerequisite>', 1], ['CausesDesire<', 1], ['HasLastSubevent<', 1]]
- p_absent (worst profile) 0.0495, q=1.0, context 0.019; relation null mean links 1.28; strict null mean links 1.45; profile null mean links 2.89; profile2 null mean links 2.22
  - A (7): saltwater, atlantic_ocean, gulf_of_mexico, it's_natural_habitat, reef, salt_water, south_pacific — frame AtLocation< anemone; AtLocation< shark
  - B (6): a, detroit, circus, florida, washington, parade — frame AtLocation< horse; AtLocation< wiener_dog
  - shared surroundings: outside, jellyfish, michigan, apple_tree, monkey, lemur, sloth, tampa_bay, ficus, beaver
  - A→surroundings [['AtLocation>', 15], ['AtLocation<', 12], ['RelatedTo>', 1], ['PartOf<', 1], ['RelatedTo<', 1]]; B→surroundings [['AtLocation>', 13], ['AtLocation<', 11], ['RelatedTo>', 2], ['PartOf<', 2], ['RelatedTo<', 2]]
- p_absent (worst profile) 0.0495, q=1.0, context 0.017; relation null mean links 1.07; strict null mean links 1.65; profile null mean links 3.33; profile2 null mean links 3.84
  - A (9): fly_in_airplane, attend_classical_concert, go_see_play, see_favorite_show, go_to_opera, watch_musician_perform, go_to_sporting_event, see_particular_program, see_band — frame HasPrerequisite> buy_ticket; HasPrerequisite> buy_tickets
  - B (9): stretch_muscles, put_on_shoes, dress_appropriately, go_to_park, stretch_first, put_on_jogging_clothes, put_on_jogging_suit, wear_good_shoes, wear_jogging_shoes — frame HasPrerequisite< go_jogging; HasPrerequisite< go_for_jog
  - shared surroundings: listen_to_music, go_home, open_eyes, go_to_performance, go_out, dance, leave_house, put_on_pants, go_somewhere
  - A→surroundings [['HasSubevent>', 6], ['HasPrerequisite>', 5], ['HasLastSubevent>', 2], ['HasFirstSubevent<', 1], ['HasPrerequisite<', 1]]; B→surroundings [['HasPrerequisite>', 3], ['HasFirstSubevent>', 2], ['HasLastSubevent>', 2], ['HasSubevent>', 2], ['HasPrerequisite<', 2]]
- p_absent (worst profile) 0.0594, q=1.0, context 0.02; relation null mean links 0.83; strict null mean links 1.21; profile null mean links 2.4; profile2 null mean links 2.05
  - A (7): wild, india, hole, south_carolina, petshop, petstore, cat's_mouth — frame AtLocation< mouse; AtLocation< lizard
  - B (4): meadow, biology_book, cartoon, field_of_flowers — frame AtLocation< anemone; AtLocation< bee
  - shared surroundings: cat, outside, water, lemur, nature, forest, garden, kitten, michigan, fox
  - A→surroundings [['AtLocation>', 24], ['AtLocation<', 18], ['RelatedTo>', 2], ['IsA>', 1], ['PartOf>', 1]]; B→surroundings [['AtLocation>', 22], ['AtLocation<', 16], ['IsA>', 2], ['PartOf>', 1], ['RelatedTo>', 1]]
- p_absent (worst profile) 0.0594, q=1.0, context 0.018; relation null mean links 1.31; strict null mean links 2.57; profile null mean links 3.69; profile2 null mean links 2.11
  - A (9): outdoors, it's_natural_habitat, den, forrest, great_britain, hole_in_ground, out_of_doors, wolf's_belly, wood_pile — frame AtLocation< ferret; AtLocation< weasel
  - B (6): a, detroit, circus, florida, washington, parade — frame AtLocation< horse; AtLocation< wiener_dog
  - shared surroundings: snake, mammal, outside, michigan, beaver, mouse, lemur, pocket, apple_tree, cow
  - A→surroundings [['AtLocation<', 23], ['AtLocation>', 18], ['IsA>', 5], ['CapableOf>', 1], ['Synonym>', 1]]; B→surroundings [['AtLocation>', 16], ['AtLocation<', 12], ['RelatedTo<', 5], ['IsA>', 4], ['PartOf>', 3]]
- p_absent (worst profile) 0.0693, q=1.0, context 0.021; relation null mean links 0.98; strict null mean links 1.82; profile null mean links 2.89; profile2 null mean links 3.58
  - A (5): go_to_cinema, go_to_movie_theater, go_to_theatre, rent_movie, go_to_movie_theatre — frame HasPrerequisite< watch_movie; HasPrerequisite< watch_film; HasPrerequisite< take_in_film; HasPrerequisite< go_see_film
  - B (4): use_water, go_to_bathroom, turn_on_water, take_clothes_off — frame HasPrerequisite< bathe; HasPrerequisite< have_bath; HasPrerequisite< take_shower; HasPrerequisite< wash_hands; HasPrerequisite< have_shower
  - shared surroundings: go_to_film, go_to_movie, going_to_movie, eat_ice_cream, sit
  - A→surroundings [['HasPrerequisite>', 2], ['HasSubevent>', 2], ['HasPrerequisite<', 2], ['HasSubevent<', 2]]; B→surroundings [['HasLastSubevent<', 3], ['HasPrerequisite>', 1], ['HasSubevent<', 1]]
- p_absent (worst profile) 0.0792, q=1.0, context 0.03; relation null mean links 0.59; strict null mean links 1.18; profile null mean links 2.25; profile2 null mean links 2.32
  - A (9): stretch_muscles, put_on_shoes, dress_appropriately, go_to_park, stretch_first, put_on_jogging_clothes, put_on_jogging_suit, wear_good_shoes, wear_jogging_shoes — frame HasPrerequisite< go_jogging; HasPrerequisite< go_for_jog
  - B (5): buy_ticket, buy_tickets, drive_there, find_one, use_ticket — frame HasPrerequisite< go_to_movie; HasPrerequisite< attend_classical_concert; HasPrerequisite< go_to_opera; HasPrerequisite< see_band
  - shared surroundings: listen_to_music, go_to_pub, leave_house, go_to_performance, go_out, go_home, open_eyes, go_on_vacation, dance
  - A→surroundings [['HasPrerequisite<', 3], ['HasFirstSubevent>', 2], ['HasLastSubevent>', 2], ['HasPrerequisite>', 2], ['HasSubevent>', 2]]; B→surroundings [['HasPrerequisite>', 3], ['HasSubevent>', 3], ['HasPrerequisite<', 3], ['HasFirstSubevent>', 1], ['HasLastSubevent>', 1]]
- p_absent (worst profile) 0.0792, q=1.0, context 0.019; relation null mean links 0.77; strict null mean links 1.08; profile null mean links 2.78; profile2 null mean links 2.4
  - A (7): guilt, grief, guilty_conscience, going_to_jail, remorse, feelings_of_guilt, guilty_conscious — frame Causes< killing; Causes< killing_people; Causes< getting_away_with_crime
  - B (4): eye_strain, drowsiness, gaining_knowledge, learn_things — frame Causes< reading; Causes< reading_book
  - shared surroundings: fun, pleasure, hearing_news, using_television, determining_truth, laugh
  - A→surroundings [['Causes<', 3], ['Causes>', 1], ['HasProperty>', 1], ['HasSubevent>', 1], ['UsedFor>', 1]]; B→surroundings [['UsedFor>', 3], ['Causes<', 3], ['HasProperty>', 1], ['HasSubevent>', 1]]
- p_absent (worst profile) 0.0891, q=1.0, context 0.029; relation null mean links 0.75; strict null mean links 1.18; profile null mean links 2.36; profile2 null mean links 2.66
  - A (9): stretch_muscles, put_on_shoes, dress_appropriately, go_to_park, stretch_first, put_on_jogging_clothes, put_on_jogging_suit, wear_good_shoes, wear_jogging_shoes — frame HasPrerequisite< go_jogging; HasPrerequisite< go_for_jog
  - B (4): buy_ticket, turn_on_tv, buy_tickets, turn_on_television — frame HasPrerequisite< watch_movie; HasPrerequisite< see_movie; HasPrerequisite< see_favorite_show; HasPrerequisite< see_particular_program
  - shared surroundings: open_eyes, go_to_performance, see_people_play_game, get_fit
  - A→surroundings [['HasPrerequisite<', 2], ['HasPrerequisite>', 1], ['HasSubevent>', 1]]; B→surroundings [['HasFirstSubevent<', 2], ['HasPrerequisite<', 2], ['HasFirstSubevent>', 1], ['HasPrerequisite>', 1]]
- p_absent (worst profile) 0.0891, q=1.0, context 0.018; relation null mean links 1.16; strict null mean links 1.92; profile null mean links 2.79; profile2 null mean links 1.92
  - A (7): go_to_cinema, go_to_movie_theater, turn_on_tv, turn_on_television, rent_movie, rent_video, rent_one — frame HasPrerequisite< watch_movie; HasPrerequisite< see_movie; HasPrerequisite< watch_film; HasPrerequisite< view_film_at_home
  - B (4): use_water, go_to_bathroom, turn_on_water, take_clothes_off — frame HasPrerequisite< bathe; HasPrerequisite< have_bath; HasPrerequisite< take_shower; HasPrerequisite< wash_hands; HasPrerequisite< have_shower
  - shared surroundings: go_to_film, going_to_movie, go_to_movie, eat_ice_cream
  - A→surroundings [['HasPrerequisite<', 2], ['HasSubevent<', 2], ['HasPrerequisite>', 1], ['HasSubevent>', 1], ['MotivatedByGoal<', 1]]; B→surroundings [['HasLastSubevent<', 3], ['HasSubevent<', 1]]
- p_absent (worst profile) 0.099, q=1.0, context 0.021; relation null mean links 1.47; strict null mean links 3.31; profile null mean links 5.68; profile2 null mean links 1.68
  - A (13): mexico, circus, ass, own_house, cage, lap, petshop, barbeque, vet's_office, grandma's_house … — frame AtLocation< small_dog; AtLocation< wiener_dog
  - B (9): outdoors, it's_natural_habitat, den, forrest, great_britain, hole_in_ground, out_of_doors, wolf's_belly, wood_pile — frame AtLocation< ferret; AtLocation< weasel
  - shared surroundings: marmoset, lizard, snake, kitten, outside, marmot, fox, sloth, canada, own_home
  - A→surroundings [['AtLocation<', 21], ['AtLocation>', 18], ['RelatedTo>', 3], ['RelatedTo<', 3], ['IsA>', 2]]; B→surroundings [['AtLocation<', 26], ['AtLocation>', 22], ['IsA>', 4], ['CapableOf>', 1], ['RelatedTo>', 1]]
- p_absent (worst profile) 0.1089, q=1.0, context 0.031; relation null mean links 1.21; strict null mean links 1.99; profile null mean links 2.52; profile2 null mean links 2.22
  - A (11): go_to_concert, buy_ticket, open_eyes, go_to_theater, go_to_theatre, buy_tickets, buy_tickets_to_concert, buy_ticket_to_concert, go_to_club, buy_concert_ticket … — frame HasPrerequisite< watch_musician_perform; HasPrerequisite< see_band
  - B (4): use_water, go_to_bathroom, turn_on_water, take_clothes_off — frame HasPrerequisite< bathe; HasPrerequisite< have_bath; HasPrerequisite< take_shower; HasPrerequisite< wash_hands; HasPrerequisite< have_shower
  - shared surroundings: get_dressed, take_bath, go_to_movie, waking_up_in_morning, awake, run_in_marathon, visit_art_gallery, stand_in_line, getting_married, socialize
  - A→surroundings [['HasPrerequisite<', 7], ['HasPrerequisite>', 1], ['MotivatedByGoal>', 1], ['HasFirstSubevent<', 1], ['HasLastSubevent<', 1]]; B→surroundings [['HasPrerequisite<', 6], ['HasLastSubevent<', 3], ['HasLastSubevent>', 2], ['HasFirstSubevent<', 2], ['HasSubevent<', 2]]
- p_absent (worst profile) 0.1188, q=1.0, context 0.045; relation null mean links 0.8; strict null mean links 1.38; profile null mean links 2.26; profile2 null mean links 2.17
  - A (4): buy_ticket, turn_on_tv, buy_tickets, turn_on_television — frame HasPrerequisite< watch_movie; HasPrerequisite< see_movie; HasPrerequisite< see_favorite_show; HasPrerequisite< see_particular_program
  - B (5): bring_money, leave_house, get_dressed, put_on_shoes, get_car_keys — frame HasPrerequisite< go_to_store; HasPrerequisite< go_to_pub
  - shared surroundings: turn_off_tv, go_to_sporting_event, go_to_opera, go_to_performance, go_to_zoo, go_to_movie, find_seat, get_in_car, visit_art_gallery, go_to_film
  - A→surroundings [['HasPrerequisite<', 8], ['HasLastSubevent>', 2], ['HasPrerequisite>', 2], ['HasFirstSubevent<', 2], ['HasSubevent>', 1]]; B→surroundings [['HasPrerequisite<', 5], ['HasPrerequisite>', 3], ['HasFirstSubevent<', 3], ['HasFirstSubevent>', 1]]
- p_absent (worst profile) 0.1188, q=1.0, context 0.02; relation null mean links 0.66; strict null mean links 1.76; profile null mean links 2.73; profile2 null mean links 1.92
  - A (7): woods, great_outdoors, cage_at_zoo, captivity, colorado, treetop, wilderness — frame AtLocation< bald_eagle; AtLocation< marmoset
  - B (5): pet_shop, couch, petshop, dog_house, doghouse — frame AtLocation< dog; AtLocation< wiener_dog
  - shared surroundings: lizard, outside, animal, book, crab, mouse, shark, weasel, cage, washington
  - A→surroundings [['AtLocation>', 11], ['AtLocation<', 8], ['IsA>', 2], ['PartOf>', 1]]; B→surroundings [['AtLocation>', 11], ['AtLocation<', 8], ['RelatedTo>', 2], ['RelatedTo<', 2], ['IsA>', 1]]
- p_absent (worst profile) 0.1188, q=1.0, context 0.02; relation null mean links 0.98; strict null mean links 2.68; profile null mean links 1.55; profile2 null mean links 1.25
  - A (6): open_mouth, not_drive, go_to_bar, have_id, buy_alcohol, not_drive_car — frame HasPrerequisite< drink; HasPrerequisite< drink_alcohol
  - B (4): tie_shoes, put_on_shoes, go_to_park, wear_good_shoes — frame HasPrerequisite< walk; HasPrerequisite< run; HasPrerequisite< go_jogging; HasPrerequisite< go_for_jog
  - shared surroundings: go_to_pub, person, action, activity, pour, jump_up_and_down, breathe_fresh_air, escape, stumble, energy
  - A→surroundings [['RelatedTo>', 4], ['RelatedTo<', 4], ['HasFirstSubevent<', 3], ['HasFirstSubevent>', 1], ['HasSubevent>', 1]]; B→surroundings [['RelatedTo>', 5], ['RelatedTo<', 5], ['HasPrerequisite<', 3], ['Synonym>', 2], ['Synonym<', 2]]

Boundaries by frame kind: {'location-only': 48, 'different relation types': 120, 'same relation types': 15}. Fixed-pair test (both profile nulls leave the pair unlinked in ≤ 5% of graphs): 1 of 183; BH q ≤ 0.10: 0.

### Most unexpected boundaries (smallest worst-case profile p; ties by context similarity), top 15

- **location-only**, context 0.019, comparable pairs 292 with median 5 links (97% linked); relation p_absent=0.2574 (null mean links 1.28); strict p_absent=0.1881 (null mean links 1.45); profile p_absent=0.0495 (null mean links 2.89); profile2 p_absent=0.0495 (null mean links 2.22); q=1.00
  - A (7): saltwater, atlantic_ocean, gulf_of_mexico, it's_natural_habitat, reef, salt_water, south_pacific — frame AtLocation< anemone; AtLocation< shark
  - B (6): a, detroit, circus, florida, washington, parade — frame AtLocation< horse; AtLocation< wiener_dog
  - shared surroundings: outside, jellyfish, michigan, apple_tree, monkey, lemur, sloth, tampa_bay, ficus, beaver
  - A→surroundings [['AtLocation>', 15], ['AtLocation<', 12], ['RelatedTo>', 1], ['PartOf<', 1], ['RelatedTo<', 1]]; B→surroundings [['AtLocation>', 13], ['AtLocation<', 11], ['RelatedTo>', 2], ['PartOf<', 2], ['RelatedTo<', 2]]; links between comparable linked pairs are mostly [['AtLocation<', 0.334], ['AtLocation>', 0.318], ['RelatedTo>', 0.096], ['RelatedTo<', 0.084]]
- **location-only**, context 0.02, comparable pairs 94 with median 3 links (97% linked); relation p_absent=0.4455 (null mean links 0.83); strict p_absent=0.3564 (null mean links 1.21); profile p_absent=0.0594 (null mean links 2.4); profile2 p_absent=0.0594 (null mean links 2.05); q=1.00
  - A (7): wild, india, hole, south_carolina, petshop, petstore, cat's_mouth — frame AtLocation< mouse; AtLocation< lizard
  - B (4): meadow, biology_book, cartoon, field_of_flowers — frame AtLocation< anemone; AtLocation< bee
  - shared surroundings: cat, outside, water, lemur, nature, forest, garden, kitten, michigan, fox
  - A→surroundings [['AtLocation>', 24], ['AtLocation<', 18], ['RelatedTo>', 2], ['IsA>', 1], ['PartOf>', 1]]; B→surroundings [['AtLocation>', 22], ['AtLocation<', 16], ['IsA>', 2], ['PartOf>', 1], ['RelatedTo>', 1]]; links between comparable linked pairs are mostly [['AtLocation>', 0.292], ['AtLocation<', 0.255], ['RelatedTo<', 0.123], ['RelatedTo>', 0.094]]
- **location-only**, context 0.018, comparable pairs 292 with median 5 links (97% linked); relation p_absent=0.2772 (null mean links 1.31); strict p_absent=0.0495 (null mean links 2.57); profile p_absent=0.0198 (null mean links 3.69); profile2 p_absent=0.0594 (null mean links 2.11); q=1.00
  - A (9): outdoors, it's_natural_habitat, den, forrest, great_britain, hole_in_ground, out_of_doors, wolf's_belly, wood_pile — frame AtLocation< ferret; AtLocation< weasel
  - B (6): a, detroit, circus, florida, washington, parade — frame AtLocation< horse; AtLocation< wiener_dog
  - shared surroundings: snake, mammal, outside, michigan, beaver, mouse, lemur, pocket, apple_tree, cow
  - A→surroundings [['AtLocation<', 23], ['AtLocation>', 18], ['IsA>', 5], ['CapableOf>', 1], ['Synonym>', 1]]; B→surroundings [['AtLocation>', 16], ['AtLocation<', 12], ['RelatedTo<', 5], ['IsA>', 4], ['PartOf>', 3]]; links between comparable linked pairs are mostly [['AtLocation<', 0.334], ['AtLocation>', 0.318], ['RelatedTo>', 0.096], ['RelatedTo<', 0.084]]
- **location-only**, context 0.021, comparable pairs 59 with median 3 links (91% linked); relation p_absent=0.2178 (null mean links 1.47); strict p_absent=0.0495 (null mean links 3.31); profile p_absent=0.0198 (null mean links 5.68); profile2 p_absent=0.099 (null mean links 1.68); q=1.00
  - A (13): mexico, circus, ass, own_house, cage, lap, petshop, barbeque, vet's_office, grandma's_house … — frame AtLocation< small_dog; AtLocation< wiener_dog
  - B (9): outdoors, it's_natural_habitat, den, forrest, great_britain, hole_in_ground, out_of_doors, wolf's_belly, wood_pile — frame AtLocation< ferret; AtLocation< weasel
  - shared surroundings: marmoset, lizard, snake, kitten, outside, marmot, fox, sloth, canada, own_home
  - A→surroundings [['AtLocation<', 21], ['AtLocation>', 18], ['RelatedTo>', 3], ['RelatedTo<', 3], ['IsA>', 2]]; B→surroundings [['AtLocation<', 26], ['AtLocation>', 22], ['IsA>', 4], ['CapableOf>', 1], ['RelatedTo>', 1]]; links between comparable linked pairs are mostly [['AtLocation<', 0.498], ['AtLocation>', 0.391], ['IsA<', 0.029], ['RelatedTo>', 0.021]]
- **location-only**, context 0.02, comparable pairs 292 with median 5 links (97% linked); relation p_absent=0.4851 (null mean links 0.66); strict p_absent=0.1386 (null mean links 1.76); profile p_absent=0.0198 (null mean links 2.73); profile2 p_absent=0.1188 (null mean links 1.92); q=1.00
  - A (7): woods, great_outdoors, cage_at_zoo, captivity, colorado, treetop, wilderness — frame AtLocation< bald_eagle; AtLocation< marmoset
  - B (5): pet_shop, couch, petshop, dog_house, doghouse — frame AtLocation< dog; AtLocation< wiener_dog
  - shared surroundings: lizard, outside, animal, book, crab, mouse, shark, weasel, cage, washington
  - A→surroundings [['AtLocation>', 11], ['AtLocation<', 8], ['IsA>', 2], ['PartOf>', 1]]; B→surroundings [['AtLocation>', 11], ['AtLocation<', 8], ['RelatedTo>', 2], ['RelatedTo<', 2], ['IsA>', 1]]; links between comparable linked pairs are mostly [['AtLocation<', 0.334], ['AtLocation>', 0.318], ['RelatedTo>', 0.096], ['RelatedTo<', 0.084]]
- **same relation types**, context 0.024, comparable pairs 5 with median 2 links (71% linked); relation p_absent=0.5347 (null mean links 0.58); strict p_absent=0.4158 (null mean links 0.88); profile p_absent=0.1782 (null mean links 1.71); profile2 p_absent=0.1089 (null mean links 2.07); q=1.00
  - A (7): cleanliness, removing_stains, sanitation, removing_dirt, hygiene, keeping_clean, getting_rid_of_dirt — frame UsedFor< cleaning; UsedFor< washing_clothes; UsedFor< washing_hands
  - B (4): feeling_better_about_yourself, looking_good, improving_health, keeping_fit — frame UsedFor< getting_in_shape; UsedFor< exercising
  - shared surroundings: health, doing_housework, staying_healthy, grooming, energy, good_health, maintaining_good_health, taking_care_of, getting_tired, becoming_more_clean
  - A→surroundings [['Causes>', 5], ['UsedFor<', 4], ['UsedFor>', 3], ['HasPrerequisite>', 2], ['Causes<', 2]]; B→surroundings [['UsedFor>', 6], ['UsedFor<', 4], ['Causes>', 3], ['HasPrerequisite>', 2], ['HasSubevent>', 1]]; links between comparable linked pairs are mostly [['UsedFor<', 0.5], ['UsedFor>', 0.25], ['AtLocation>', 0.083], ['AtLocation<', 0.083]]
- **location-only**, context 0.021, comparable pairs 44 with median 2 links (96% linked); relation p_absent=0.505 (null mean links 0.65); strict p_absent=0.396 (null mean links 0.94); profile p_absent=0.2376 (null mean links 1.49); profile2 p_absent=0.2475 (null mean links 1.17); q=1.00
  - A (5): boxes, junk, spiders, stairs, water_heater — frame AtLocation> garage; AtLocation> cellar
  - B (4): computer_user, fastener_binder, second_floor, staple_remover — frame AtLocation> school; AtLocation> office_building
  - shared surroundings: house, mouse, building, basement, desk, closet, computer, staircase, room, trash
  - A→surroundings [['AtLocation>', 15], ['AtLocation<', 9], ['IsA>', 2], ['RelatedTo>', 2], ['Synonym>', 2]]; B→surroundings [['AtLocation<', 17], ['AtLocation>', 8], ['IsA>', 3], ['RelatedTo<', 2], ['RelatedTo>', 1]]; links between comparable linked pairs are mostly [['AtLocation>', 0.416], ['AtLocation<', 0.365], ['RelatedTo>', 0.036], ['RelatedTo<', 0.036]]
- **location-only**, context 0.019, comparable pairs 53 with median 2 links (88% linked); relation p_absent=0.5545 (null mean links 0.56); strict p_absent=0.2178 (null mean links 1.28); profile p_absent=0.1089 (null mean links 2.02); profile2 p_absent=0.2673 (null mean links 1.07); q=1.00
  - A (5): pet_shop, couch, petshop, dog_house, doghouse — frame AtLocation< dog; AtLocation< wiener_dog
  - B (4): encyclopedia, cartoon, detroit_zoo, jungle — frame AtLocation< jellyfish; AtLocation< marmot
  - shared surroundings: cat, animal, kitten, weasel, store, book, outside, lizard, cage, blowfish
  - A→surroundings [['AtLocation<', 11], ['AtLocation>', 9], ['IsA>', 2], ['RelatedTo<', 2], ['Antonym>', 1]]; B→surroundings [['AtLocation<', 10], ['AtLocation>', 7], ['IsA>', 3], ['IsA<', 1], ['NotDesires<', 1]]; links between comparable linked pairs are mostly [['AtLocation<', 0.431], ['AtLocation>', 0.359], ['IsA>', 0.046], ['UsedFor>', 0.033]]
- **location-only**, context 0.02, comparable pairs 292 with median 5 links (97% linked); relation p_absent=0.0495 (null mean links 2.15); strict p_absent=0.0693 (null mean links 2.3); profile p_absent=0.2079 (null mean links 1.55); profile2 p_absent=0.2871 (null mean links 1.14); q=1.00
  - A (16): oil, cup, pot, bar_stool, candle, chef_special, cold_tap, grape, grill, large_container … — frame AtLocation> kitchen; AtLocation> restaurant
  - B (4): darkness, coal, dust_mites, junk — frame AtLocation> bed; AtLocation> cellar
  - shared surroundings: table, trash, room, potato, drawer, place, find_inside, find_downstairs, neighbor's_house, person
  - A→surroundings [['AtLocation>', 19], ['AtLocation<', 16], ['RelatedTo>', 14], ['RelatedTo<', 13], ['IsA>', 8]]; B→surroundings [['RelatedTo<', 24], ['RelatedTo>', 16], ['AtLocation<', 14], ['AtLocation>', 7], ['UsedFor>', 4]]; links between comparable linked pairs are mostly [['AtLocation<', 0.334], ['AtLocation>', 0.318], ['RelatedTo>', 0.096], ['RelatedTo<', 0.084]]
- **location-only**, context 0.019, comparable pairs 54 with median 3 links (92% linked); relation p_absent=0.5446 (null mean links 0.59); strict p_absent=0.2871 (null mean links 1.24); profile p_absent=0.2079 (null mean links 1.52); profile2 p_absent=0.3861 (null mean links 0.95); q=1.00
  - A (4): soccer_game, sporting_event, stadium, hockey_game — frame AtLocation< fan; AtLocation< beer; AtLocation< audience; AtLocation< bleachers; AtLocation< coach …
  - B (6): bench, benches, vending_machines, seating, tired_people, travellers — frame AtLocation> rest_area; AtLocation> bus_depot
  - shared surroundings: people, seats, team, sit_down_on, penalty_box, judge, tiered_seats, sit_on, grass, food_vendor
  - A→surroundings [['AtLocation<', 8], ['RelatedTo>', 4], ['RelatedTo<', 4], ['AtLocation>', 3], ['UsedFor>', 2]]; B→surroundings [['AtLocation<', 5], ['AtLocation>', 3], ['IsA<', 3], ['IsA>', 2], ['RelatedTo>', 2]]; links between comparable linked pairs are mostly [['AtLocation<', 0.467], ['AtLocation>', 0.41], ['PartOf<', 0.031], ['RelatedTo<', 0.026]]
- **location-only**, context 0.032, comparable pairs 72 with median 4 links (96% linked); relation p_absent=0.3564 (null mean links 1.05); strict p_absent=0.297 (null mean links 1.05); profile p_absent=0.198 (null mean links 1.58); profile2 p_absent=0.4059 (null mean links 0.76); q=1.00
  - A (4): utah, new_mexico, california, nevada — frame AtLocation< lizard; HasA> deserts
  - B (5): art, texas, cartoon, jungle, weirdest_places — frame AtLocation< cat; AtLocation< jellyfish
  - shared surroundings: administrative_region, state, united_states, book, southwest, colorado, nature, state_in_united_states, brazos, sun_itself
  - A→surroundings [['AtLocation>', 19], ['AtLocation<', 14], ['IsA>', 11], ['PartOf<', 9], ['PartOf>', 8]]; B→surroundings [['AtLocation>', 22], ['AtLocation<', 9], ['IsA>', 8], ['PartOf<', 7], ['PartOf>', 4]]; links between comparable linked pairs are mostly [['AtLocation>', 0.265], ['AtLocation<', 0.22], ['RelatedTo>', 0.143], ['RelatedTo<', 0.143]]
- **location-only**, context 0.029, comparable pairs 20 with median 4 links (95% linked); relation p_absent=0.1683 (null mean links 1.37); strict p_absent=0.0495 (null mean links 2.14); profile p_absent=0.4059 (null mean links 0.89); profile2 p_absent=0.3267 (null mean links 0.88); q=1.00
  - A (4): mess, cup, cloth, shoes — frame AtLocation> table; AtLocation> closet
  - B (4): mug, glasses, liquor, vodka — frame AtLocation> bar; AtLocation> cabinet
  - shared surroundings: container, drink, store, cupboard, kitchen, drinking, counter, cleaning, plate, house
  - A→surroundings [['AtLocation<', 26], ['AtLocation>', 17], ['RelatedTo>', 12], ['RelatedTo<', 10], ['IsA>', 8]]; B→surroundings [['AtLocation<', 25], ['RelatedTo<', 15], ['RelatedTo>', 13], ['IsA>', 11], ['UsedFor>', 8]]; links between comparable linked pairs are mostly [['RelatedTo>', 0.194], ['AtLocation>', 0.177], ['AtLocation<', 0.161], ['RelatedTo<', 0.137]]
- **same relation types**, context 0.021, comparable pairs 5 with median 2 links (71% linked); relation p_absent=0.5941 (null mean links 0.49); strict p_absent=0.4158 (null mean links 0.95); profile p_absent=0.1881 (null mean links 1.89); profile2 p_absent=0.4158 (null mean links 0.84); q=1.00
  - A (7): cleanliness, removing_stains, sanitation, removing_dirt, hygiene, keeping_clean, getting_rid_of_dirt — frame UsedFor< cleaning; UsedFor< washing_clothes; UsedFor< washing_hands
  - B (4): clearing_mind, being_healthy, keeping_fit, relieving_stress — frame UsedFor< getting_exercise; UsedFor< going_for_walk
  - shared surroundings: health, staying_healthy, tiredness, becoming_more_clean, taking_bath, energy, effort, getting_tired, good_health, time
  - A→surroundings [['Causes>', 4], ['HasPrerequisite>', 3], ['UsedFor>', 2], ['UsedFor<', 2]]; B→surroundings [['UsedFor>', 4], ['HasPrerequisite>', 3], ['UsedFor<', 3], ['Causes>', 2], ['HasSubevent>', 1]]; links between comparable linked pairs are mostly [['UsedFor<', 0.5], ['UsedFor>', 0.25], ['AtLocation>', 0.083], ['AtLocation<', 0.083]]
- **different relation types**, context 0.019, comparable pairs 21 with median 2 links (78% linked); relation p_absent=0.4356 (null mean links 0.7); strict p_absent=0.4653 (null mean links 0.72); profile p_absent=0.4257 (null mean links 0.79); profile2 p_absent=0.3168 (null mean links 1.05); q=1.00
  - A (15): printer, chairs, clipboard, eraser, glue, lunch, homework, instrument_triangle, keyboard, lead_pencil … — frame AtLocation> desk; AtLocation> school
  - B (4): sending_packages, receiving_letters, sending_letters, storing_mail — frame UsedFor< post_office; UsedFor< mailbox
  - shared surroundings: building, facility, stationery, tape_dispenser, sloth, computers, town, stamp_pad, address_label, city
  - A→surroundings [['AtLocation<', 5], ['RelatedTo<', 4], ['AtLocation>', 3], ['RelatedTo>', 3], ['IsA>', 1]]; B→surroundings [['AtLocation<', 5], ['AtLocation>', 3], ['IsA>', 2], ['UsedFor<', 1]]; links between comparable linked pairs are mostly [['UsedFor>', 0.237], ['AtLocation>', 0.197], ['AtLocation<', 0.158], ['RelatedTo<', 0.105]]
- **different relation types**, context 0.025, comparable pairs 22 with median 2 links (79% linked); relation p_absent=0.6238 (null mean links 0.51); strict p_absent=0.6733 (null mean links 0.36); profile p_absent=0.4356 (null mean links 0.79); profile2 p_absent=0.3861 (null mean links 0.93); q=1.00
  - A (4): store_clothes, store_clothing, storing_clothes, storing_clothing — frame UsedFor< closet; UsedFor< dresser; UsedFor< clothing_shelf; UsedFor< chest_of_drawers; UsedFor< closet_for_clothes
  - B (4): stationary, junk, staples, paperclips — frame AtLocation> desk; UsedFor< desk_drawer
  - shared surroundings: drawer, box, bedroom, storage, cabinet, school, furniture, found_in_house, shoes, pantry
  - A→surroundings [['AtLocation<', 13], ['IsA>', 6], ['AtLocation>', 5], ['RelatedTo<', 5], ['UsedFor>', 3]]; B→surroundings [['AtLocation<', 12], ['AtLocation>', 10], ['UsedFor>', 3], ['IsA>', 2], ['RelatedTo<', 2]]; links between comparable linked pairs are mostly [['UsedFor<', 0.242], ['UsedFor>', 0.165], ['AtLocation>', 0.132], ['AtLocation<', 0.132]]

## merged

| graph | groups | candidate pairs | boundaries | boundary rate | p (rate real ≥ null) | candidate pairs linked | p (real unlinked share ≥ null) |
|---|---|---|---|---|---|---|---|
| real | 1166 | 4667 | 227 | 0.049 | | 0.65 | |
| relation null (mean) | 819 | 3010 | 92.2 [max 169] | 0.031 [0.012–0.050] | 0.0297 | 0.96 | 0.0099 |
| strict null (mean) | 526 | 1226 | 63.3 [max 139] | 0.051 [0.019–0.101] | 0.5347 | 0.85 | 0.0099 |
| profile null (mean) | 706 | 2191 | 85.5 [max 134] | 0.039 [0.018–0.064] | 0.1782 | 0.95 | 0.0099 |
| profile2 null (mean) | 771 | 2554 | 118.6 [max 181] | 0.046 [0.021–0.066] | 0.4059 | 0.93 | 0.0099 |

Sparse regions: candidate pairs grouped by the two groups' dominant frame relations. Linked share in the real graph vs re-mined nulls (strata with ≥ 20 real pairs; null graphs where the stratum has ≥ 5 pairs).

| dominant relations | real pairs | real linked | relation linked [p real ≤ null, graphs] | strict linked [p real ≤ null, graphs] | profile linked [p real ≤ null, graphs] | profile2 linked [p real ≤ null, graphs] |
|---|---|---|---|---|---|---|
| AtLocation x AtLocation | 877 | 0.95 | 0.968 [0.0594, 100] | 0.869 [1.0, 100] | 0.959 [0.2079, 100] | 0.949 [0.5149, 100] |
| Causes x HasPrerequisite | 548 | 0.59 | 0.0 [1.0, 1] | 0.667 [0.5, 1] | 0.428 [0.75, 19] | 0.349 [0.875, 71] |
| HasPrerequisite x HasPrerequisite | 543 | 0.46 | — | — | 0.728 [0.1212, 32] | 0.693 [0.1316, 75] |
| HasPrerequisite x UsedFor | 412 | 0.61 | — | — | 0.318 [0.8333, 5] | 0.403 [0.8571, 20] |
| HasPrerequisite x HasSubevent | 371 | 0.48 | 0.479 [0.5862, 28] | 0.686 [0.3333, 2] | 0.523 [0.55, 19] | 0.448 [0.5063, 78] |
| Causes x UsedFor | 256 | 0.71 | — | — | — | 0.917 [0.3333, 2] |
| AtLocation x UsedFor | 236 | 0.84 | 0.736 [0.6984, 62] | 0.684 [0.7789, 94] | 0.774 [0.5733, 74] | 0.838 [0.4949, 98] |
| Causes x HasSubevent | 217 | 0.65 | 0.675 [0.4231, 25] | — | — | 0.491 [0.7647, 16] |
| HasSubevent x UsedFor | 190 | 0.54 | 0.435 [0.6154, 25] | — | — | 0.6 [0.5, 3] |
| Causes x Causes | 164 | 0.60 | — | — | — | 0.77 [0.1429, 6] |
| UsedFor x UsedFor | 142 | 0.63 | 0.8 [0.6667, 2] | — | 0.981 [0.04, 24] | 0.951 [0.0476, 20] |
| AtLocation x HasPrerequisite | 99 | 0.59 | 0.716 [0.6, 4] | 0.272 [0.8947, 18] | 0.026 [1.0, 6] | 0.187 [0.973, 36] |
| CapableOf x HasPrerequisite | 75 | 0.49 | — | 0.667 [0.5, 1] | 0.267 [0.8621, 28] | 0.292 [0.8889, 98] |
| HasSubevent x HasSubevent | 52 | 0.52 | 0.825 [0.0337, 88] | — | — | 0.295 [1.0, 3] |
| AtLocation x Causes | 45 | 0.44 | 0.377 [0.8, 4] | 0.375 [0.6, 4] | 0.1 [1.0, 2] | 0.75 [0.3333, 2] |
| CapableOf x Causes | 44 | 0.48 | — | — | — | 0.224 [0.9167, 23] |
| CapableOf x UsedFor | 44 | 0.50 | — | — | 0.386 [0.6667, 2] | 0.38 [0.7273, 10] |
| HasPrerequisite x MotivatedByGoal | 44 | 0.48 | — | — | — | 0.333 [1.0, 1] |
| MotivatedByGoal x UsedFor | 37 | 0.51 | — | — | — | — |
| Causes x MotivatedByGoal | 31 | 0.29 | — | — | — | — |
| CapableOf x HasSubevent | 29 | 0.52 | 0.424 [0.8125, 31] | 0.574 [0.5, 5] | — | 0.499 [0.625, 23] |
| AtLocation x HasSubevent | 21 | 0.43 | 0.295 [0.7761, 66] | 0.345 [0.6458, 47] | 0.125 [1.0, 1] | 0.338 [0.7273, 10] |
| HasLastSubevent x HasPrerequisite | 20 | 0.45 | — | — | — | 0.428 [0.7, 9] |

Same real group pairs re-checked in every null graph (cores fixed). Unlinked real candidate pairs: 1643; unlinked in ≤ 5% of graphs of both profile nulls: 5; BH q ≤ 0.10: 0.

| dominant relations | real pairs | real linked | relation linked [p real ≤ null] | strict linked [p real ≤ null] | profile linked [p real ≤ null] | profile2 linked [p real ≤ null] |
|---|---|---|---|---|---|---|
| AtLocation x AtLocation | 877 | 0.95 | 0.75 [1.0] | 0.87 [1.0] | 0.93 [0.9703] | 0.94 [0.8119] |
| Causes x HasPrerequisite | 548 | 0.59 | 0.48 [1.0] | 0.53 [1.0] | 0.58 [0.604] | 0.62 [0.0693] |
| HasPrerequisite x HasPrerequisite | 543 | 0.46 | 0.52 [0.0099] | 0.54 [0.0099] | 0.59 [0.0099] | 0.56 [0.0099] |
| HasPrerequisite x UsedFor | 412 | 0.61 | 0.36 [1.0] | 0.41 [1.0] | 0.53 [1.0] | 0.59 [0.7723] |
| HasPrerequisite x HasSubevent | 371 | 0.48 | 0.46 [0.7426] | 0.47 [0.6238] | 0.52 [0.0792] | 0.52 [0.0297] |
| Causes x UsedFor | 256 | 0.71 | 0.49 [1.0] | 0.58 [1.0] | 0.68 [0.8614] | 0.74 [0.1287] |
| AtLocation x UsedFor | 236 | 0.84 | 0.50 [1.0] | 0.57 [1.0] | 0.69 [1.0] | 0.75 [1.0] |
| Causes x HasSubevent | 217 | 0.65 | 0.51 [1.0] | 0.58 [0.9604] | 0.62 [0.7822] | 0.65 [0.3762] |
| HasSubevent x UsedFor | 190 | 0.54 | 0.34 [1.0] | 0.38 [1.0] | 0.49 [0.9703] | 0.56 [0.3366] |
| Causes x Causes | 164 | 0.60 | 0.58 [0.6535] | 0.66 [0.0693] | 0.69 [0.0297] | 0.72 [0.0099] |
| UsedFor x UsedFor | 142 | 0.63 | 0.37 [1.0] | 0.47 [1.0] | 0.54 [0.9703] | 0.59 [0.9406] |
| AtLocation x HasPrerequisite | 99 | 0.59 | 0.20 [1.0] | 0.27 [1.0] | 0.43 [1.0] | 0.50 [1.0] |
| CapableOf x HasPrerequisite | 75 | 0.49 | 0.28 [1.0] | 0.33 [1.0] | 0.47 [0.7723] | 0.48 [0.8218] |
| HasSubevent x HasSubevent | 52 | 0.52 | 0.53 [0.5248] | 0.55 [0.3564] | 0.62 [0.0396] | 0.61 [0.0594] |
| AtLocation x Causes | 45 | 0.44 | 0.21 [1.0] | 0.22 [1.0] | 0.30 [1.0] | 0.37 [0.9901] |
| CapableOf x Causes | 44 | 0.48 | 0.27 [0.9802] | 0.36 [0.9604] | 0.48 [0.5545] | 0.45 [0.9406] |
| CapableOf x UsedFor | 44 | 0.50 | 0.28 [1.0] | 0.34 [0.9901] | 0.46 [0.8812] | 0.49 [0.7822] |
| HasPrerequisite x MotivatedByGoal | 44 | 0.48 | 0.46 [0.6337] | 0.50 [0.4554] | 0.54 [0.2475] | 0.50 [0.4059] |
| MotivatedByGoal x UsedFor | 37 | 0.51 | 0.31 [0.9703] | 0.41 [0.8515] | 0.48 [0.6832] | 0.52 [0.6634] |
| Causes x MotivatedByGoal | 31 | 0.29 | 0.36 [0.4059] | 0.43 [0.198] | 0.39 [0.297] | 0.32 [0.5248] |
| CapableOf x HasSubevent | 29 | 0.52 | 0.26 [1.0] | 0.29 [1.0] | 0.45 [0.8812] | 0.55 [0.4059] |
| AtLocation x HasSubevent | 21 | 0.43 | 0.22 [0.9901] | 0.18 [1.0] | 0.27 [1.0] | 0.34 [1.0] |
| HasLastSubevent x HasPrerequisite | 20 | 0.45 | 0.57 [0.2376] | 0.51 [0.396] | 0.56 [0.2079] | 0.56 [0.1881] |

### Sparse region HasPrerequisite x HasPrerequisite: unlinked real pairs that both profile nulls link most often

- linked in ≥ 99% of graphs of each profile null; context 0.022; relation null mean links 1.05; strict null mean links 1.7; profile null mean links 3.14; profile2 null mean links 4.22
  - A (7): driver's_license (= get_driver's_license, have_driving_license), start_engine (= start_motor), start_car (= turn_car_on, turn_on_car), fasten_seatbelt (= seat_belt, put_seatbelt), get_keys (= get_key), get_license (= get_licence, have_license), learn_how_to_drive — frame HasPrerequisite< drive (= motor); HasPrerequisite< drive_car (= car_to_drive)
  - B (7): get_weapon (= have_weapon), see_psychiatrist (= seek_psychiatric_help, consult_psychiatrist), get_gun (= buy_weapon), buy_gun, have_gun, get_weapons (= have_weapons), use_weapon (= use_weapons) — frame HasPrerequisite< kill (= killing, murder); HasPrerequisite< kill_people (= killing_humans); HasPrerequisite< fight_enemy (= attacking_enemy, fighting_enemy, attack_enemy)
  - shared surroundings: panic, people, involved_in_accident, manufacture, machine, mean, hit, hunting, car, take
  - A→surroundings [['RelatedTo>', 6], ['RelatedTo<', 5], ['MannerOf>', 4], ['HasSubevent>', 1], ['IsA>', 1]]; B→surroundings [['RelatedTo>', 4], ['RelatedTo<', 4], ['CapableOf<', 3], ['UsedFor<', 2], ['Causes>', 1]]
- linked in ≥ 95% of graphs of each profile null; context 0.021; relation null mean links 1.5; strict null mean links 1.86; profile null mean links 3.03; profile2 null mean links 2.64
  - A (10): popcorn (= pop_corn), go_to_movies (= watch_movies), buy_popcorn, make_popcorn, go_to_cinema (= go_to_movie_theater, take_to_movies, go_to_movie_theatre, visit_cinema, enter_movie_theater), go_to_theater (= theatre_goers), put_on_glasses (= put_glasses_on, put_on_eyeglasses, wear_glasses), near_tv, rent_movie (= rent_video, rent_film), ability_to_see (= able_to_see) — frame HasPrerequisite< watch_movie (= see_movie, watch_film, go_see_film); HasPrerequisite< enjoy_film (= enjoy_movie, enjoying_film, enjoying_movie)
  - B (4): go_out (= going_out), put_on_shoes (= wear_shoes, put_shoes_on, put_on_footwear), go_outdoors (= do_outside, get_outside), check_weather (= finding_out_weather) — frame HasPrerequisite< walk_dog (= walking_dog); HasPrerequisite< walk_in_rain (= walking_in_rain); HasPrerequisite< go_for_jog (= start_running, go_jogging)
  - shared surroundings: relaxing, using_television, fun, open_eyes, cry, leave, watching_movie, seeing_band, go_home, couple
  - A→surroundings [['HasPrerequisite>', 6], ['HasSubevent>', 5], ['HasPrerequisite<', 4], ['Causes>', 3], ['HasLastSubevent>', 3]]; B→surroundings [['UsedFor>', 6], ['CapableOf<', 4], ['Causes>', 2], ['HasLastSubevent>', 2], ['HasPrerequisite>', 2]]
- linked in ≥ 90% of graphs of each profile null; context 0.019; relation null mean links 1.1; strict null mean links 1.56; profile null mean links 2.19; profile2 null mean links 2.19
  - A (7): enemy (= opponent), chess_board (= have_chess_board), find_partner (= finding_mate), find_to_play_with, find_opponent (= find_enemy), learn_rules (= understand_rules, read_rules, know_rules, knowing_rules), have_oppenant — frame HasPrerequisite< play_chess (= chess_game, game_of_chess); HasPrerequisite< play_game (= play_games, playing_game); HasPrerequisite< play_game_of_chess (= playing_game_of_chess)
  - B (4): take_music_lessons (= learning_music, learn_music), learn_to_read_music, take_lessons, use_fingers (= move_hands, move_fingers) — frame HasPrerequisite< play_guitar (= playing_guitar, strumming_guitar); HasPrerequisite< play_piano (= playing_piano); HasPrerequisite< playing_violin (= play_violin); HasPrerequisite< playing_harp (= play_harp)
  - shared surroundings: fun, play, having_fun, intelligent_agent_activity, entertainment, challenge, skill, musician, have_fun, relax
  - A→surroundings [['MotivatedByGoal>', 14], ['UsedFor>', 11], ['HasSubevent>', 8], ['HasPrerequisite<', 7], ['Causes>', 5]]; B→surroundings [['UsedFor>', 18], ['HasPrerequisite>', 7], ['MotivatedByGoal>', 7], ['IsA>', 6], ['HasSubevent>', 5]]
- linked in ≥ 84% of graphs of each profile null; context 0.049; relation null mean links 0.58; strict null mean links 0.93; profile null mean links 1.51; profile2 null mean links 1.67
  - A (7): take_off (= go_off), sort_laundry (= sort_clothes, sort_clothing), use_detergent (= add_detergent), get_water (= have_water), put_in_washer (= put_in_washing_machine), buy_washing_powder, use_washing_machine — frame HasPrerequisite< clean_clothing (= wash_clothing); HasPrerequisite< wash_clothes (= put_clothes_in_washer)
  - B (7): start, start_engine (= start_motor), start_car (= turn_car_on, turn_on_car), shift_gears (= put_in_gear), start_car_engine (= turn_on_ignition), press_accelerator (= pressing_accelerator), turn_steering_wheel (= use_steering_wheel) — frame HasPrerequisite< drive_car (= car_to_drive); HasPrerequisite< move_car; HasSubevent< driving_car (= moving_car, drive_car_on)
  - shared surroundings: get_off_ground, press, turn, depart
  - A→surroundings [['Synonym>', 2], ['Synonym<', 2], ['HasFirstSubevent>', 1], ['HasLastSubevent>', 1]]; B→surroundings [['HasPrerequisite>', 1], ['IsA>', 1], ['Synonym>', 1], ['MannerOf<', 1], ['Synonym<', 1]]
- linked in ≥ 83% of graphs of each profile null; context 0.02; relation null mean links 0.86; strict null mean links 1.3; profile null mean links 1.9; profile2 null mean links 1.41
  - A (6): take_music_lessons (= learning_music, learn_music), take_lessons, use_fingers (= move_hands, move_fingers), take_lesson (= learn_lesson), learning_about_music (= knowledge_of_music), lots_of_practice (= practice_lot) — frame HasPrerequisite< play_piano (= playing_piano); HasPrerequisite< playing_violin (= play_violin)
  - B (7): enemy (= opponent), chess_board (= have_chess_board), find_partner (= finding_mate), find_to_play_with, find_opponent (= find_enemy), learn_rules (= understand_rules, read_rules, know_rules, knowing_rules), have_oppenant — frame HasPrerequisite< play_chess (= chess_game, game_of_chess); HasPrerequisite< play_game (= play_games, playing_game); HasPrerequisite< play_game_of_chess (= playing_game_of_chess)
  - shared surroundings: play, fun, entertainment, intelligent_agent_activity, wrestling, having_fun, play_ball, pleasure, person, people
  - A→surroundings [['UsedFor>', 11], ['HasPrerequisite<', 6], ['IsA>', 4], ['CapableOf<', 4], ['HasPrerequisite>', 3]]; B→surroundings [['UsedFor>', 8], ['MotivatedByGoal>', 7], ['HasPrerequisite<', 7], ['IsA>', 4], ['Causes>', 3]]
- linked in ≥ 82% of graphs of each profile null; context 0.042; relation null mean links 0.63; strict null mean links 0.89; profile null mean links 1.58; profile2 null mean links 1.61
  - A (5): shave (= shaving), get_out_of_bed (= getting_out_of_bed), find_job, go_to_office, get_up_and_get_dressed — frame HasPrerequisite< begin_work (= beginning_work); HasPrerequisite< go_to_work (= report_to_work)
  - B (4): go_out (= going_out), put_on_shoes (= wear_shoes, put_shoes_on, put_on_footwear), go_outdoors (= do_outside, get_outside), check_weather (= finding_out_weather) — frame HasPrerequisite< walk_dog (= walking_dog); HasPrerequisite< walk_in_rain (= walking_in_rain); HasPrerequisite< go_for_jog (= start_running, go_jogging)
  - shared surroundings: get_dressed, get_tired, dress_nice, get_up_in_morning, go_to_school, person, leave_house, waking_up_in_morning, run, tiredness
  - A→surroundings [['HasPrerequisite>', 5], ['HasPrerequisite<', 5], ['HasSubevent>', 3], ['HasFirstSubevent<', 3], ['Causes>', 2]]; B→surroundings [['HasPrerequisite>', 5], ['HasPrerequisite<', 5], ['HasSubevent>', 3], ['CapableOf<', 3], ['HasFirstSubevent<', 3]]
- linked in ≥ 81% of graphs of each profile null; context 0.019; relation null mean links 1.22; strict null mean links 1.31; profile null mean links 1.73; profile2 null mean links 1.57
  - A (7): turn_on (= turn_things_on), television_set (= tv_set), turn_on_tv (= turning_on_television, turn_on_television, switch_tv_on, turn_on_t.v), switch_on_television (= turn_television_on, switch_on_tv), turn_on_tv_set (= turn_on_television_set), ability_to_see (= able_to_see), find_tv — frame HasPrerequisite< watching_television (= watch_television); HasPrerequisite< watching_tv_show (= watching_television_show, watch_television_show, watch_tv_show)
  - B (4): visit_doctor (= make_doctor_appointment, find_doctor, visit_to_doctor), go_to_doctor (= make_appointment_with_doctor, go_to_doctors), go_see_doctor (= go_to_see_doctor, go_to_doctor's_office), see_doctor (= check_with_doctor) — frame Causes< making_sure_re_healthy (= knowing_if_re_healthy); HasPrerequisite< having_physical_exam (= having_physical_examination, have_physical_exam, have_physical_examination); HasPrerequisite< having_checkup (= have_checkup, get_checkup, getting_checkup); HasPrerequisite< make_sure_you're_healthy (= have_good_health); HasPrerequisite< have_examination (= examination) …
  - shared surroundings: get_bored, patience, time, relaxing, doctor_office, fun, stress, cough, have_fun
  - A→surroundings [['HasPrerequisite>', 4], ['HasSubevent>', 4], ['UsedFor>', 4], ['Causes>', 3], ['MotivatedByGoal>', 2]]; B→surroundings [['HasPrerequisite>', 4], ['HasSubevent>', 4], ['Causes>', 3], ['UsedFor<', 2], ['MotivatedByGoal>', 1]]
- linked in ≥ 81% of graphs of each profile null; context 0.035; relation null mean links 0.76; strict null mean links 0.64; profile null mean links 1.45; profile2 null mean links 1.48
  - A (7): learn_to_read (= know_how_to_read), turn_on_light (= turn_on_lights, turning_on_light), learn_how_to_read (= knowing_how_to_read), put_on_glasses (= put_glasses_on, put_on_eyeglasses, wear_glasses), get_one, have_light (= have_lighter), make_sure_have_enough_light — frame HasPrerequisite< read_book (= read_books, reading_books); HasPrerequisite< read_newspaper (= reading_newspaper)
  - B (4): inspired (= get_inspired), creativity (= innovation), use_imagination (= think_creatively), choose_subject (= decide_on_topic, choose_topic, decide_on_subject) — frame HasPrerequisite< creating_art (= make_art, create_art); HasPrerequisite< writing_poem (= write_poem)
  - shared surroundings: person, wait_for, learning, fun, write, thinking, knowledge, relaxing, relax, people
  - A→surroundings [['HasPrerequisite<', 7], ['HasSubevent<', 6], ['HasPrerequisite>', 5], ['HasSubevent>', 5], ['UsedFor>', 4]]; B→surroundings [['HasSubevent<', 5], ['HasSubevent>', 4], ['UsedFor>', 4], ['CapableOf<', 3], ['Causes>', 2]]
- linked in ≥ 79% of graphs of each profile null; context 0.037; relation null mean links 1.23; strict null mean links 1.38; profile null mean links 1.58; profile2 null mean links 1.72
  - A (9): log_on, dial_up, turn_on_computer (= start_computer, boot_up_computer, turn_computer_on), connect_to_internet (= get_on_internet), buy_computer, have_computer (= having_computer, get_computer), have_modem, log_on_to_computer (= logon), start_web_browser (= open_browser) — frame HasPrerequisite< getting_onto_web (= get_onto_web, log_on_to_internet, accessing_internet); HasPrerequisite< go_on_internet (= use_internet)
  - B (5): use_pen, get_paper (= have_paper), find_paper (= get_piece_of_paper), get_pen (= have_pen), get_paper_and_pen (= get_pen_and_paper, have_paper_and_pen, pen_and_paper) — frame HasPrerequisite< write (= written); HasPrerequisite< writing_letter (= write_letter, send_letter); HasPrerequisite< writing_story (= write_stories, write_story); HasPrerequisite< writing_poem (= write_poem); HasPrerequisite< make_shopping_list (= making_shopping_list)
  - shared surroundings: typing, using_computer, entertainment, write_program, research, information, read_news, talking_to_friends, fun, lose_track_of_time
  - A→surroundings [['HasPrerequisite<', 10], ['UsedFor>', 5], ['HasPrerequisite>', 4], ['MotivatedByGoal>', 4], ['Causes>', 2]]; B→surroundings [['UsedFor>', 5], ['UsedFor<', 4], ['HasPrerequisite<', 3], ['Causes>', 2], ['MotivatedByGoal<', 2]]
- linked in ≥ 79% of graphs of each profile null; context 0.047; relation null mean links 1.02; strict null mean links 1.45; profile null mean links 2.51; profile2 null mean links 1.32
  - A (7): learn_to_read (= know_how_to_read), turn_on_light (= turn_on_lights, turning_on_light), learn_how_to_read (= knowing_how_to_read), put_on_glasses (= put_glasses_on, put_on_eyeglasses, wear_glasses), get_one, have_light (= have_lighter), make_sure_have_enough_light — frame HasPrerequisite< read_book (= read_books, reading_books); HasPrerequisite< read_newspaper (= reading_newspaper)
  - B (5): settle_down (= try_to_calm_down), get_weapon (= have_weapon), change_mind (= change_opinion, changing_mind), lack_of_conscience, lack_of_empathy — frame HasPrerequisite< kill (= killing, murder); HasPrerequisite< hurting_else (= hurt_else)
  - shared surroundings: handle_proposals, having_lunch, fun, person, study_for_subject, making_angry, going_fishing, eat_breakfast, panic, fighting_war
  - A→surroundings [['HasPrerequisite<', 8], ['HasSubevent<', 8], ['Causes>', 4], ['HasSubevent>', 3], ['HasPrerequisite>', 2]]; B→surroundings [['MotivatedByGoal>', 3], ['Causes<', 3], ['HasSubevent<', 3], ['Causes>', 2], ['HasPrerequisite>', 2]]
- linked in ≥ 78% of graphs of each profile null; context 0.027; relation null mean links 0.55; strict null mean links 0.68; profile null mean links 1.47; profile2 null mean links 1.56
  - A (5): full_bladder (= having_full_bladder, bladder_full), having_pee (= peeing, urination), pull_down_pants (= unzip_pants, drop_pants), do_in_private (= do_privately), enter_bathroom (= find_restroom) — frame HasPrerequisite< urinate (= urinating); HasPrerequisite< empty_bladder (= emptying_bladder, emptying_of_bladder)
  - B (4): find_water (= go_to_water), take_off_clothes (= taking_clothes_off, remove_clothes, take_off_clothing, taking_off_clothes, remove_clothing), turn_on_water (= run_water), adjust_water_temperature — frame HasPrerequisite< bathe (= bather); HasPrerequisite< get_wet (= getting_wet)
  - shared surroundings: wash_hands, have_shower, take_shower, having_bath, having_physical_exam, go_to_bathroom, grooming, copulate, liquid, relax
  - A→surroundings [['HasPrerequisite>', 7], ['HasPrerequisite<', 6], ['HasLastSubevent>', 2], ['Causes>', 1], ['HasSubevent<', 1]]; B→surroundings [['HasPrerequisite<', 14], ['HasSubevent<', 7], ['Causes<', 5], ['HasFirstSubevent<', 4], ['HasPrerequisite>', 3]]
- linked in ≥ 78% of graphs of each profile null; context 0.03; relation null mean links 0.61; strict null mean links 0.65; profile null mean links 1.33; profile2 null mean links 1.75
  - A (5): order_food (= order_meal, ordering_meal, ordering_food), make_appointment (= make_reservation), make_reservations (= book_ticket), make_sure_have_money, finding_restaurant (= pick_restaurant) — frame HasPrerequisite< eating_in_restaurant (= eat_in_restaurant); HasPrerequisite< go_to_restaurant (= eat_in_restaurants, going_to_restaurant, go_to_diner)
  - B (4): take_music_lessons (= learning_music, learn_music), learn_to_read_music, take_lessons, use_fingers (= move_hands, move_fingers) — frame HasPrerequisite< play_guitar (= playing_guitar, strumming_guitar); HasPrerequisite< play_piano (= playing_piano); HasPrerequisite< playing_violin (= play_violin); HasPrerequisite< playing_harp (= play_harp)
  - shared surroundings: fun, entertainment, people, having_good_time, fly_in_airplane, eating_in_fast_food_restaurant, sit_down, eat
  - A→surroundings [['UsedFor>', 3], ['HasSubevent>', 2], ['CapableOf<', 2], ['HasPrerequisite<', 2], ['HasSubevent<', 1]]; B→surroundings [['UsedFor>', 7], ['HasSubevent>', 2], ['HasPrerequisite<', 2], ['HasLastSubevent>', 1], ['HasProperty>', 1]]

### Sparse region Causes x Causes: unlinked real pairs that both profile nulls link most often

- linked in ≥ 95% of graphs of each profile null; context 0.038; relation null mean links 1.61; strict null mean links 2.0; profile null mean links 3.08; profile2 null mean links 2.68
  - A (7): becoming_tired (= feeling_tired, becomming_tired), sore_feet (= feet_hurt, getting_sore_feet), shortness_of_breath (= loss_of_breath, breathlessness, running_out_of_breath, getting_short_of_breath), cramps (= cramp, cramping, getting_cramp, crampy, get_cramp), increased_heart_rate (= increase_heart_rate, increased_heartrate, heart_rate_increases), leg_cramps, getting_out_of_breath (= get_winded) — frame Causes< running (= sprinting); Causes< going_for_run (= going_for_jog, go_for_run)
  - B (4): increase_knowledge (= better_knowledge, increased_understanding, increased_knowledge, enhanced_knowledge), insight (= insights), become_smarter (= increase_intelligence, becoming_smarter), improved_performance (= improve_performance) — frame Causes< learning_new (= learn_new, know_new_things, gaining_new_knowledge); HasSubevent< learning (= learn, learned)
  - shared surroundings: fun, visit_art_gallery, reading_book, seeing_exhibits, study, effort, going_to_school, visiting_museum, thinking, play
  - A→surroundings [['Causes<', 8], ['HasSubevent<', 6], ['UsedFor>', 5], ['Causes>', 2], ['CausesDesire>', 1]]; B→surroundings [['Causes<', 14], ['HasSubevent<', 9], ['HasPrerequisite>', 7], ['HasSubevent>', 3], ['UsedFor<', 3]]
- linked in ≥ 93% of graphs of each profile null; context 0.022; relation null mean links 1.48; strict null mean links 1.74; profile null mean links 2.11; profile2 null mean links 2.36
  - A (5): good_health (= healthy_living), better_health (= improved_health, being_more_healthy), shortness_of_breath (= loss_of_breath, breathlessness, running_out_of_breath, getting_short_of_breath), cramps (= cramp, cramping, getting_cramp, crampy, get_cramp), increased_heart_rate (= increase_heart_rate, increased_heartrate, heart_rate_increases) — frame Causes< running (= sprinting); Causes< getting_exercise (= getting_physical_activity, getting_excercise, get_exercise); Causes< doing_exercises (= working_out); Causes< going_for_run (= going_for_jog, go_for_run); Causes< jogging …
  - B (4): cleanliness (= sanitation, hygiene, being_sanitary), wet_person (= wet_skin), clean_skin (= cleaning_body), getting_cleaner (= cleaning_things) — frame Causes< bathing (= baths); Causes< having_bath (= bath, have_bath)
  - shared surroundings: pleasure, have_shower, relaxing, cleaning, getting_clean, fun, feeling_good, grooming, have_fun, take_shower
  - A→surroundings [['UsedFor>', 9], ['Causes>', 4], ['UsedFor<', 3], ['CausesDesire>', 2], ['HasLastSubevent>', 2]]; B→surroundings [['UsedFor<', 12], ['UsedFor>', 10], ['Causes>', 6], ['HasSubevent>', 5], ['Causes<', 4]]
- linked in ≥ 90% of graphs of each profile null; context 0.028; relation null mean links 1.08; strict null mean links 1.32; profile null mean links 1.58; profile2 null mean links 2.57
  - A (6): fitness (= being_fit), good_health (= healthy_living), better_health (= improved_health, being_more_healthy), being_healthy (= being_healthier, getting_healthier), shortness_of_breath (= loss_of_breath, breathlessness, running_out_of_breath, getting_short_of_breath), improving_health (= becoming_more_healthy, improvement_in_health) — frame Causes< getting_exercise (= getting_physical_activity, getting_excercise, get_exercise); Causes< doing_exercises (= working_out); Causes< jogging; UsedFor< getting_exercise (= getting_physical_activity, getting_excercise, get_exercise)
  - B (4): cleanliness (= sanitation, hygiene, being_sanitary), wet_person (= wet_skin), clean_skin (= cleaning_body), getting_cleaner (= cleaning_things) — frame Causes< bathing (= baths); Causes< having_bath (= bath, have_bath)
  - shared surroundings: relaxing, cleaning, feeling_good, getting_clean, grooming, pleasure, take_shower, have_shower, becoming_more_clean, look_better
  - A→surroundings [['UsedFor>', 5], ['UsedFor<', 4], ['Causes>', 3], ['Causes<', 3], ['CausesDesire>', 1]]; B→surroundings [['UsedFor<', 14], ['UsedFor>', 10], ['Causes>', 6], ['HasSubevent>', 4], ['Causes<', 4]]
- linked in ≥ 83% of graphs of each profile null; context 0.018; relation null mean links 1.34; strict null mean links 1.71; profile null mean links 2.42; profile2 null mean links 1.8
  - A (4): increase_knowledge (= better_knowledge, increased_understanding, increased_knowledge, enhanced_knowledge), insight (= insights), become_smarter (= increase_intelligence, becoming_smarter), improved_performance (= improve_performance) — frame Causes< learning_new (= learn_new, know_new_things, gaining_new_knowledge); HasSubevent< learning (= learn, learned)
  - B (4): trip (= tripping), becoming_tired (= feeling_tired, becomming_tired), increased_heart_rate (= increase_heart_rate, increased_heartrate, heart_rate_increases), trip_and_fall (= tripping_and_falling) — frame Causes< jumping_rope (= jump_rope, have_jump_rope); Causes< going_for_run (= going_for_jog, go_for_run)
  - shared surroundings: fun, person, reading_book, enjoyment, thinking, study, effort, going_to_school, experience, dance
  - A→surroundings [['HasPrerequisite>', 8], ['Causes<', 8], ['HasSubevent<', 5], ['Causes>', 3], ['HasSubevent>', 3]]; B→surroundings [['UsedFor>', 9], ['HasSubevent<', 8], ['Causes>', 3], ['MotivatedByGoal>', 3], ['Causes<', 3]]
- linked in ≥ 79% of graphs of each profile null; context 0.02; relation null mean links 1.49; strict null mean links 1.5; profile null mean links 1.49; profile2 null mean links 1.57
  - A (4): getting_hurt (= getting_wounded, being_injured, being_hurt), get_hurt (= getting_injured, get_injured), bruises (= bruise), victory_or_defeat — frame Causes< playing_football (= play_football); Causes< wrestling (= wrestle)
  - B (5): becoming_tired (= feeling_tired, becomming_tired), become_tired (= make_tired), getting_tired_legs (= tired_legs, legs_get_tired, legs_tired), sore_feet (= feet_hurt, getting_sore_feet), sore_legs — frame Causes< dance (= dancing); Causes< hiking (= hikers); Causes< standing_in_line (= take_place_in_line, standing_in_queue, standing_on_line); Causes< going_for_run (= going_for_jog, go_for_run); Causes< going_for_walk (= take_walk_outside) …
  - shared surroundings: fun, exercise, sweat, having_fun, injury, foot, pleasure, fall, entertainment, stretch
  - A→surroundings [['UsedFor>', 13], ['HasPrerequisite>', 9], ['HasSubevent>', 6], ['HasSubevent<', 6], ['Causes>', 5]]; B→surroundings [['Causes>', 18], ['UsedFor>', 16], ['RelatedTo<', 13], ['RelatedTo>', 12], ['HasPrerequisite>', 11]]
- linked in ≥ 78% of graphs of each profile null; context 0.027; relation null mean links 1.2; strict null mean links 1.65; profile null mean links 1.66; profile2 null mean links 1.4
  - A (5): good_health (= healthy_living), better_health (= improved_health, being_more_healthy), shortness_of_breath (= loss_of_breath, breathlessness, running_out_of_breath, getting_short_of_breath), cramps (= cramp, cramping, getting_cramp, crampy, get_cramp), increased_heart_rate (= increase_heart_rate, increased_heartrate, heart_rate_increases) — frame Causes< running (= sprinting); Causes< getting_exercise (= getting_physical_activity, getting_excercise, get_exercise); Causes< doing_exercises (= working_out); Causes< going_for_run (= going_for_jog, go_for_run); Causes< jogging …
  - B (4): smell_nice (= smell_good, wonderful_smell, smelling_good, smelling_nice), not_smelling_bad, smell_better (= smelling_better), getting_rid_of_dirt (= washing_away_dirt) — frame Causes< becoming_more_clean (= get_cleaner); UsedFor< clean_clothes (= cleaning_clothes, clothes_cleaned, cleaning_clothing, getting_clothes_clean)
  - shared surroundings: health, feel_better, staying_healthy, being_healthy, feeling_good, stay_healthy, look_better, have_shower, wash_hands, take_shower
  - A→surroundings [['UsedFor>', 18], ['Causes>', 9], ['HasSubevent>', 4], ['UsedFor<', 3], ['Causes<', 2]]; B→surroundings [['Causes<', 8], ['UsedFor>', 5], ['Causes>', 4], ['HasSubevent>', 3], ['MotivatedByGoal<', 2]]
- linked in ≥ 75% of graphs of each profile null; context 0.026; relation null mean links 0.9; strict null mean links 0.97; profile null mean links 1.79; profile2 null mean links 1.18
  - A (4): overeating (= eat_too_much, eating_too_much), feeling_full (= becoming_full), feeling_satisfied (= feeling_of_accomplishment), heartburn — frame Causes< diminishing_own_hunger (= becoming_less_hungry, diminish_own_hunger); Causes< having_lunch (= lunch, have_lunch, getting_lunch); Causes< sating_hunger (= satisfying_craving, satisfying_appetite); Causes< eat_breakfast (= eating_breakfast)
  - B (4): hangover, drunkenness (= drunk_people), nausea, pass_out (= passing_out) — frame Causes< getting_drunk (= becoming_inebriated, getting_wasted); Causes< hit_bottle (= hitting_bottle)
  - shared surroundings: drink, eating, eating_hamburger, go_to_restaurant, celebrating, feel_better, illness, pleasure, relaxing, being_sick
  - A→surroundings [['Causes<', 9], ['HasSubevent>', 8], ['Causes>', 5], ['HasPrerequisite>', 4], ['UsedFor>', 4]]; B→surroundings [['UsedFor>', 9], ['Causes<', 7], ['HasSubevent<', 4], ['Causes>', 3], ['Synonym>', 3]]
- linked in ≥ 71% of graphs of each profile null; context 0.027; relation null mean links 0.94; strict null mean links 1.8; profile null mean links 1.13; profile2 null mean links 1.54
  - A (7): becoming_tired (= feeling_tired, becomming_tired), sore_feet (= feet_hurt, getting_sore_feet), shortness_of_breath (= loss_of_breath, breathlessness, running_out_of_breath, getting_short_of_breath), cramps (= cramp, cramping, getting_cramp, crampy, get_cramp), increased_heart_rate (= increase_heart_rate, increased_heartrate, heart_rate_increases), leg_cramps, getting_out_of_breath (= get_winded) — frame Causes< running (= sprinting); Causes< going_for_run (= going_for_jog, go_for_run)
  - B (4): hangover, drunkenness (= drunk_people), nausea, pass_out (= passing_out) — frame Causes< getting_drunk (= becoming_inebriated, getting_wasted); Causes< hit_bottle (= hitting_bottle)
  - shared surroundings: jogging, getting_exercise, celebrating, running_twenty_six_miles, running_marathon, pleasure, fun, fall_down, illness, feel_better
  - A→surroundings [['Causes<', 14], ['HasSubevent<', 8], ['Causes>', 7], ['UsedFor>', 7], ['HasSubevent>', 4]]; B→surroundings [['UsedFor>', 7], ['HasSubevent<', 5], ['Causes>', 4], ['Causes<', 4], ['HasSubevent>', 2]]
- linked in ≥ 68% of graphs of each profile null; context 0.019; relation null mean links 1.05; strict null mean links 1.53; profile null mean links 1.15; profile2 null mean links 1.1
  - A (6): get_sweaty (= getting_sweaty, working_up_sweat), sore_muscles (= muscle_pain, getting_sore_muscles), getting_tired_legs (= tired_legs, legs_get_tired, legs_tired), better_health (= improved_health, being_more_healthy), cramps (= cramp, cramping, getting_cramp, crampy, get_cramp), sore_legs — frame Causes< hiking (= hikers); Causes< riding_bike (= ride_bicycle, ride_bike, riding_bicycle); Causes< going_for_run (= going_for_jog, go_for_run); Causes< going_for_walk (= take_walk_outside)
  - B (5): wetness (= moist_place, wet_area), drowning (= drown), exfoliation, wrinkled_skin, will_get_wet (= becoming_wet, would_get_wet) — frame Causes< taking_bath (= go_for_bath); Causes< having_bath (= bath, have_bath)
  - shared surroundings: fun, pleasure, have_shower, get_clean, getting_clean, person, relaxing, going_for_swim, have_fun, take_bath
  - A→surroundings [['UsedFor>', 12], ['Causes<', 4], ['CausesDesire>', 3], ['HasSubevent<', 3], ['Causes>', 2]]; B→surroundings [['UsedFor>', 6], ['HasSubevent>', 5], ['Causes>', 4], ['Causes<', 4], ['HasSubevent<', 4]]
- linked in ≥ 68% of graphs of each profile null; context 0.022; relation null mean links 1.32; strict null mean links 1.29; profile null mean links 1.42; profile2 null mean links 1.1
  - A (9): fitness (= being_fit), good_health (= healthy_living), pulling_muscle (= pull_muscle), better_health (= improved_health, being_more_healthy), shortness_of_breath (= loss_of_breath, breathlessness, running_out_of_breath, getting_short_of_breath), become_stronger (= becoming_stronger, get_strong, increasing_strength), physical_fitness (= physical_exercise), increased_heart_rate (= increase_heart_rate, increased_heartrate, heart_rate_increases), thirsty (= thirst, being_thirsty) — frame Causes< exercise (= physical_activity, exercising, physical_exertion); Causes< getting_exercise (= getting_physical_activity, getting_excercise, get_exercise); HasSubevent< getting_exercise (= getting_physical_activity, getting_excercise, get_exercise)
  - B (4): smell_nice (= smell_good, wonderful_smell, smelling_good, smelling_nice), not_smelling_bad, smell_better (= smelling_better), getting_rid_of_dirt (= washing_away_dirt) — frame Causes< becoming_more_clean (= get_cleaner); UsedFor< clean_clothes (= cleaning_clothes, clothes_cleaned, cleaning_clothing, getting_clothes_clean)
  - shared surroundings: health, stay_healthy, look_better, feel_better, person, staying_healthy, feeling_good, getting_clean, take_shower, wash_hands
  - A→surroundings [['UsedFor>', 13], ['Causes>', 5], ['HasPrerequisite<', 5], ['HasSubevent<', 4], ['HasSubevent>', 3]]; B→surroundings [['Causes<', 8], ['UsedFor>', 6], ['Causes>', 4], ['HasPrerequisite>', 3], ['HasSubevent>', 3]]
- linked in ≥ 68% of graphs of each profile null; context 0.038; relation null mean links 0.69; strict null mean links 0.69; profile null mean links 1.05; profile2 null mean links 0.97
  - A (4): increase_knowledge (= better_knowledge, increased_understanding, increased_knowledge, enhanced_knowledge), eye_strain (= eyestrain, hurting_eyes), drowsiness (= sleepiness, sleepyness, getting_sleepy, being_sleepy), learning_things (= learn_things) — frame Causes< reading (= literature); Causes< reading_book
  - B (4): no_longer_hungry (= no_longer_being_hungry), feeling_full (= becoming_full), being_less_hungry (= decreasing_hunger, getting_less_hungry), will_no_longer_hungry — frame Causes< eating_apple (= eat_apple, eating_apples, eat_apples, bite_into_apple); Causes< having_lunch (= lunch, have_lunch, getting_lunch)
  - shared surroundings: eat_lunch, eat_dinner, school, pleasure, read_book, read, drink, good
  - A→surroundings [['UsedFor>', 4], ['RelatedTo<', 4], ['RelatedTo>', 3], ['Causes<', 3], ['HasSubevent<', 3]]; B→surroundings [['HasSubevent>', 4], ['Causes<', 4], ['AtLocation>', 1], ['HasPrerequisite>', 1], ['HasProperty>', 1]]
- linked in ≥ 67% of graphs of each profile null; context 0.025; relation null mean links 1.13; strict null mean links 1.55; profile null mean links 0.98; profile2 null mean links 1.25
  - A (7): becoming_tired (= feeling_tired, becomming_tired), sore_feet (= feet_hurt, getting_sore_feet), shortness_of_breath (= loss_of_breath, breathlessness, running_out_of_breath, getting_short_of_breath), cramps (= cramp, cramping, getting_cramp, crampy, get_cramp), increased_heart_rate (= increase_heart_rate, increased_heartrate, heart_rate_increases), leg_cramps, getting_out_of_breath (= get_winded) — frame Causes< running (= sprinting); Causes< going_for_run (= going_for_jog, go_for_run)
  - B (4): car_accident (= car_wreck, when_car_crashes, automobile_accidents, car_accidents, have_car_accident), pass_out (= passing_out), drunk_driving (= drunk_drivers, drink_and_drive), being_sick (= being_ill, getting_sick) — frame Causes< getting_drunk (= becoming_inebriated, getting_wasted); HasPrerequisite< go_into_coma (= going_into_coma)
  - shared surroundings: jogging, getting_exercise, fun, injury, pleasure, fall_down, running_marathon, running_twenty_six_miles, dance, celebrating
  - A→surroundings [['Causes<', 16], ['Causes>', 8], ['HasSubevent<', 8], ['UsedFor>', 7], ['HasSubevent>', 3]]; B→surroundings [['UsedFor>', 7], ['Causes>', 5], ['HasSubevent<', 5], ['HasSubevent>', 2], ['Causes<', 2]]

### Unlinked context-similar group pairs least expected under both profile nulls (top 15)

- p_absent (worst profile) 0.0198, q=1.0, context 0.032; relation null mean links 1.82; strict null mean links 2.39; profile null mean links 3.65; profile2 null mean links 3.99
  - A (7): cleanliness (= sanitation, hygiene, being_sanitary), smell_nice (= smell_good, wonderful_smell, smelling_good, smelling_nice), removing_stains (= remove_spots), impressing_others (= impressing_people, impress_other_people), getting_rid_of_dirt (= washing_away_dirt), making_clothes_look_nicer, making_clothes_smell_better — frame UsedFor< clean_clothes (= cleaning_clothes, clothes_cleaned, cleaning_clothing, getting_clothes_clean); UsedFor< washing_clothes (= clean_laundry, making_clothes_clean)
  - B (5): good_health (= healthy_living), better_health (= improved_health, being_more_healthy), shortness_of_breath (= loss_of_breath, breathlessness, running_out_of_breath, getting_short_of_breath), cramps (= cramp, cramping, getting_cramp, crampy, get_cramp), increased_heart_rate (= increase_heart_rate, increased_heartrate, heart_rate_increases) — frame Causes< running (= sprinting); Causes< getting_exercise (= getting_physical_activity, getting_excercise, get_exercise); Causes< doing_exercises (= working_out); Causes< going_for_run (= going_for_jog, go_for_run); Causes< jogging …
  - shared surroundings: get_fit, getting_in_shape, cleaning, have_shower, health, play_sports, getting_clean, effort, get_sweaty, tiredness
  - A→surroundings [['UsedFor<', 19], ['Causes<', 7], ['UsedFor>', 4], ['Causes>', 3], ['HasPrerequisite>', 3]]; B→surroundings [['Causes>', 15], ['UsedFor>', 14], ['Causes<', 9], ['HasSubevent<', 9], ['HasPrerequisite>', 7]]
- p_absent (worst profile) 0.0198, q=1.0, context 0.022; relation null mean links 1.05; strict null mean links 1.7; profile null mean links 3.14; profile2 null mean links 4.22
  - A (7): driver's_license (= get_driver's_license, have_driving_license), start_engine (= start_motor), start_car (= turn_car_on, turn_on_car), fasten_seatbelt (= seat_belt, put_seatbelt), get_keys (= get_key), get_license (= get_licence, have_license), learn_how_to_drive — frame HasPrerequisite< drive (= motor); HasPrerequisite< drive_car (= car_to_drive)
  - B (7): get_weapon (= have_weapon), see_psychiatrist (= seek_psychiatric_help, consult_psychiatrist), get_gun (= buy_weapon), buy_gun, have_gun, get_weapons (= have_weapons), use_weapon (= use_weapons) — frame HasPrerequisite< kill (= killing, murder); HasPrerequisite< kill_people (= killing_humans); HasPrerequisite< fight_enemy (= attacking_enemy, fighting_enemy, attack_enemy)
  - shared surroundings: panic, people, involved_in_accident, manufacture, machine, mean, hit, hunting, car, take
  - A→surroundings [['RelatedTo>', 6], ['RelatedTo<', 5], ['MannerOf>', 4], ['HasSubevent>', 1], ['IsA>', 1]]; B→surroundings [['RelatedTo>', 4], ['RelatedTo<', 4], ['CapableOf<', 3], ['UsedFor<', 2], ['Causes>', 1]]
- p_absent (worst profile) 0.0198, q=1.0, context 0.022; relation null mean links 1.21; strict null mean links 2.57; profile null mean links 6.07; profile2 null mean links 3.63
  - A (9): it's_natural_habitat, indiana, farm_yard (= farm_area, farmer's_field, farmyard), farmland (= farm_field, farm_land), idaho, new_hampshire, new_jersey, ohio, oregon — frame AtLocation< apple_tree; AtLocation< heifer
  - B (4): encyclopedia (= encyclopedias), cartoon, detroit_zoo, jungle (= jungles) — frame AtLocation< jellyfish (= jelly); AtLocation< marmot
  - shared surroundings: united_states, beaver, cow, snake, monkey, field, country, weasel, gazelle, kitten
  - A→surroundings [['AtLocation<', 35], ['AtLocation>', 15], ['PartOf>', 6], ['IsA>', 4], ['PartOf<', 2]]; B→surroundings [['AtLocation<', 23], ['AtLocation>', 15], ['NotDesires<', 1]]
- p_absent (worst profile) 0.0198, q=1.0, context 0.022; relation null mean links 1.54; strict null mean links 2.54; profile null mean links 3.4; profile2 null mean links 2.25
  - A (7): landscape (= landscaping, landscapes), nature (= natural_habitat, natural_habitats), california, arboretum, botanical_garden, flower_garden (= field_of_flowers, flower_bed), garden_store (= garden_shop, garden_center, garden_nursery) — frame AtLocation< ficus; AtLocation< rosebush
  - B (5): maine, cartoon, pet_shop (= pet_store, petshop, petstore), spain, cave — frame AtLocation< crab (= crabs); AtLocation< weasel
  - shared surroundings: outside, anemone, trees, garden, forest, lizard, lemur, snake, bee, front_yard
  - A→surroundings [['AtLocation<', 25], ['AtLocation>', 23], ['IsA>', 9], ['RelatedTo>', 7], ['RelatedTo<', 7]]; B→surroundings [['AtLocation<', 32], ['AtLocation>', 22], ['IsA>', 11], ['PartOf>', 1], ['RelatedTo>', 1]]
- p_absent (worst profile) 0.0297, q=1.0, context 0.022; relation null mean links 1.13; strict null mean links 1.66; profile null mean links 3.16; profile2 null mean links 2.65
  - A (7): wild (= wilderness), india (= indian_subcontinent), pet_shop (= pet_store, petshop, petstore), hole (= cavity), south_carolina, dark_place (= shady_spot), cat's_mouth — frame AtLocation< mouse (= mice); AtLocation< lizard (= lizards)
  - B (4): meadow, biology_book, cartoon, flower_garden (= field_of_flowers, flower_bed) — frame AtLocation< anemone; AtLocation< bee (= bees)
  - shared surroundings: country, lemur, forest, garden, water, outside, animals, cat, michigan, nature
  - A→surroundings [['AtLocation<', 34], ['AtLocation>', 31], ['IsA>', 5], ['RelatedTo>', 3], ['IsA<', 2]]; B→surroundings [['AtLocation>', 31], ['AtLocation<', 21], ['IsA>', 5], ['RelatedTo>', 2], ['RelatedTo<', 2]]
- p_absent (worst profile) 0.0594, q=1.0, context 0.038; relation null mean links 1.61; strict null mean links 2.0; profile null mean links 3.08; profile2 null mean links 2.68
  - A (7): becoming_tired (= feeling_tired, becomming_tired), sore_feet (= feet_hurt, getting_sore_feet), shortness_of_breath (= loss_of_breath, breathlessness, running_out_of_breath, getting_short_of_breath), cramps (= cramp, cramping, getting_cramp, crampy, get_cramp), increased_heart_rate (= increase_heart_rate, increased_heartrate, heart_rate_increases), leg_cramps, getting_out_of_breath (= get_winded) — frame Causes< running (= sprinting); Causes< going_for_run (= going_for_jog, go_for_run)
  - B (4): increase_knowledge (= better_knowledge, increased_understanding, increased_knowledge, enhanced_knowledge), insight (= insights), become_smarter (= increase_intelligence, becoming_smarter), improved_performance (= improve_performance) — frame Causes< learning_new (= learn_new, know_new_things, gaining_new_knowledge); HasSubevent< learning (= learn, learned)
  - shared surroundings: fun, visit_art_gallery, reading_book, seeing_exhibits, study, effort, going_to_school, visiting_museum, thinking, play
  - A→surroundings [['Causes<', 8], ['HasSubevent<', 6], ['UsedFor>', 5], ['Causes>', 2], ['CausesDesire>', 1]]; B→surroundings [['Causes<', 14], ['HasSubevent<', 9], ['HasPrerequisite>', 7], ['HasSubevent>', 3], ['UsedFor<', 3]]
- p_absent (worst profile) 0.0594, q=1.0, context 0.021; relation null mean links 1.5; strict null mean links 1.86; profile null mean links 3.03; profile2 null mean links 2.64
  - A (10): popcorn (= pop_corn), go_to_movies (= watch_movies), buy_popcorn, make_popcorn, go_to_cinema (= go_to_movie_theater, take_to_movies, go_to_movie_theatre, visit_cinema, enter_movie_theater), go_to_theater (= theatre_goers), put_on_glasses (= put_glasses_on, put_on_eyeglasses, wear_glasses), near_tv, rent_movie (= rent_video, rent_film), ability_to_see (= able_to_see) — frame HasPrerequisite< watch_movie (= see_movie, watch_film, go_see_film); HasPrerequisite< enjoy_film (= enjoy_movie, enjoying_film, enjoying_movie)
  - B (4): go_out (= going_out), put_on_shoes (= wear_shoes, put_shoes_on, put_on_footwear), go_outdoors (= do_outside, get_outside), check_weather (= finding_out_weather) — frame HasPrerequisite< walk_dog (= walking_dog); HasPrerequisite< walk_in_rain (= walking_in_rain); HasPrerequisite< go_for_jog (= start_running, go_jogging)
  - shared surroundings: relaxing, using_television, fun, open_eyes, cry, leave, watching_movie, seeing_band, go_home, couple
  - A→surroundings [['HasPrerequisite>', 6], ['HasSubevent>', 5], ['HasPrerequisite<', 4], ['Causes>', 3], ['HasLastSubevent>', 3]]; B→surroundings [['UsedFor>', 6], ['CapableOf<', 4], ['Causes>', 2], ['HasLastSubevent>', 2], ['HasPrerequisite>', 2]]
- p_absent (worst profile) 0.0792, q=1.0, context 0.042; relation null mean links 1.22; strict null mean links 1.74; profile null mean links 2.6; profile2 null mean links 3.07
  - A (6): fitness (= being_fit), good_health (= healthy_living), better_health (= improved_health, being_more_healthy), being_healthy (= being_healthier, getting_healthier), shortness_of_breath (= loss_of_breath, breathlessness, running_out_of_breath, getting_short_of_breath), improving_health (= becoming_more_healthy, improvement_in_health) — frame Causes< getting_exercise (= getting_physical_activity, getting_excercise, get_exercise); Causes< doing_exercises (= working_out); Causes< jogging; UsedFor< getting_exercise (= getting_physical_activity, getting_excercise, get_exercise)
  - B (7): cleanliness (= sanitation, hygiene, being_sanitary), smell_nice (= smell_good, wonderful_smell, smelling_good, smelling_nice), removing_stains (= remove_spots), impressing_others (= impressing_people, impress_other_people), getting_rid_of_dirt (= washing_away_dirt), making_clothes_look_nicer, making_clothes_smell_better — frame UsedFor< clean_clothes (= cleaning_clothes, clothes_cleaned, cleaning_clothing, getting_clothes_clean); UsedFor< washing_clothes (= clean_laundry, making_clothes_clean)
  - shared surroundings: get_fit, getting_in_shape, becoming_more_clean, cleaning, play_sports, health, getting_clean, grooming, cleaning_house, look_better
  - A→surroundings [['UsedFor<', 14], ['Causes>', 12], ['UsedFor>', 9], ['Causes<', 9], ['HasPrerequisite>', 6]]; B→surroundings [['UsedFor<', 21], ['Causes<', 10], ['UsedFor>', 4], ['Causes>', 3], ['HasPrerequisite>', 3]]
- p_absent (worst profile) 0.0792, q=1.0, context 0.024; relation null mean links 0.77; strict null mean links 0.97; profile null mean links 2.07; profile2 null mean links 2.19
  - A (7): get_weapon (= have_weapon), see_psychiatrist (= seek_psychiatric_help, consult_psychiatrist), get_gun (= buy_weapon), buy_gun, have_gun, get_weapons (= have_weapons), use_weapon (= use_weapons) — frame HasPrerequisite< kill (= killing, murder); HasPrerequisite< kill_people (= killing_humans); HasPrerequisite< fight_enemy (= attacking_enemy, fighting_enemy, attack_enemy)
  - B (4): trip (= tripping), shortness_of_breath (= loss_of_breath, breathlessness, running_out_of_breath, getting_short_of_breath), trip_and_fall (= tripping_and_falling), getting_out_of_breath (= get_winded) — frame Causes< going_for_run (= going_for_jog, go_for_run); Causes< run_after_ball (= chase_ball, running_after_ball)
  - shared surroundings: run, advancing_into_battle, death, fun, laughter, falling, bus, having_asthma_attack, pain, pleasure
  - A→surroundings [['Causes>', 5], ['HasSubevent>', 5], ['UsedFor<', 3], ['IsA<', 2], ['HasLastSubevent>', 1]]; B→surroundings [['Causes>', 4], ['HasSubevent<', 4], ['HasSubevent>', 3], ['UsedFor>', 3], ['Causes<', 3]]
- p_absent (worst profile) 0.0792, q=1.0, context 0.022; relation null mean links 1.48; strict null mean links 1.74; profile null mean links 2.11; profile2 null mean links 2.36
  - A (5): good_health (= healthy_living), better_health (= improved_health, being_more_healthy), shortness_of_breath (= loss_of_breath, breathlessness, running_out_of_breath, getting_short_of_breath), cramps (= cramp, cramping, getting_cramp, crampy, get_cramp), increased_heart_rate (= increase_heart_rate, increased_heartrate, heart_rate_increases) — frame Causes< running (= sprinting); Causes< getting_exercise (= getting_physical_activity, getting_excercise, get_exercise); Causes< doing_exercises (= working_out); Causes< going_for_run (= going_for_jog, go_for_run); Causes< jogging …
  - B (4): cleanliness (= sanitation, hygiene, being_sanitary), wet_person (= wet_skin), clean_skin (= cleaning_body), getting_cleaner (= cleaning_things) — frame Causes< bathing (= baths); Causes< having_bath (= bath, have_bath)
  - shared surroundings: pleasure, have_shower, relaxing, cleaning, getting_clean, fun, feeling_good, grooming, have_fun, take_shower
  - A→surroundings [['UsedFor>', 9], ['Causes>', 4], ['UsedFor<', 3], ['CausesDesire>', 2], ['HasLastSubevent>', 2]]; B→surroundings [['UsedFor<', 12], ['UsedFor>', 10], ['Causes>', 6], ['HasSubevent>', 5], ['Causes<', 4]]
- p_absent (worst profile) 0.0891, q=1.0, context 0.025; relation null mean links 1.21; strict null mean links 1.54; profile null mean links 2.01; profile2 null mean links 2.49
  - A (7): good_health (= healthy_living), being_healthy (= being_healthier, getting_healthier), improving_health (= becoming_more_healthy, improvement_in_health), keeping_fit (= becoming_fit, keeping_active), training, strengthening_heart (= strengthen_heart), staying_physically_fit (= build_stamina) — frame UsedFor< getting_exercise (= getting_physical_activity, getting_excercise, get_exercise); UsedFor< going_for_run (= going_for_jog, go_for_run)
  - B (7): cleanliness (= sanitation, hygiene, being_sanitary), smell_nice (= smell_good, wonderful_smell, smelling_good, smelling_nice), removing_stains (= remove_spots), impressing_others (= impressing_people, impress_other_people), getting_rid_of_dirt (= washing_away_dirt), making_clothes_look_nicer, making_clothes_smell_better — frame UsedFor< clean_clothes (= cleaning_clothes, clothes_cleaned, cleaning_clothing, getting_clothes_clean); UsedFor< washing_clothes (= clean_laundry, making_clothes_clean)
  - shared surroundings: getting_in_shape, grooming, get_fit, cleaning, becoming_more_clean, play_sports, running_in_marathon, feel_better, cleaning_house, take_shower
  - A→surroundings [['UsedFor>', 12], ['UsedFor<', 12], ['Causes>', 9], ['HasPrerequisite>', 5], ['HasSubevent>', 5]]; B→surroundings [['UsedFor<', 18], ['Causes<', 8], ['HasPrerequisite>', 3], ['HasSubevent>', 3], ['UsedFor>', 3]]
- p_absent (worst profile) 0.0891, q=1.0, context 0.019; relation null mean links 1.79; strict null mean links 3.09; profile null mean links 2.64; profile2 null mean links 1.93
  - A (8): indiana, great_outdoors (= enjoy_outdoors), idaho, pennsylvania (= pennslyvania), rural_area (= rural_areas), story_book (= storybook), california, tennessee — frame AtLocation< cow (= cattle, cows); AtLocation< fox
  - B (4): maine, pet_shop (= pet_store, petshop, petstore), basket, chinese_restaurant — frame AtLocation< crab (= crabs); AtLocation< small_dog
  - shared surroundings: united_states, administrative_region, state, apple_tree, animals, outside, ficus, weasel, bald_eagle, beaver
  - A→surroundings [['AtLocation<', 29], ['AtLocation>', 19], ['IsA>', 14], ['PartOf>', 5], ['RelatedTo<', 4]]; B→surroundings [['AtLocation<', 26], ['AtLocation>', 24], ['IsA>', 6], ['MannerOf>', 2], ['PartOf>', 1]]
- p_absent (worst profile) 0.099, q=1.0, context 0.019; relation null mean links 0.34; strict null mean links 2.12; profile null mean links 2.15; profile2 null mean links 3.35
  - A (17): agent_provocateur, pub (= pubs), aon (= aol), den (= lair), capita, french_connection, harrods, lonsdale, mi5, piccadilly_circus … — frame AtLocation> london; AtLocation> england (= united_kingdom, great_britain)
  - B (4): exploratorium, ign, macromedia, uber — frame AtLocation> san_francisco; AtLocation> california
  - shared surroundings: company, city, fox, subsidiary, corner_grocery, museum, beach, freeway, cow, bridge
  - A→surroundings [['IsA>', 11], ['AtLocation<', 5], ['AtLocation>', 3], ['RelatedTo<', 2], ['HasA>', 1]]; B→surroundings [['IsA>', 5], ['AtLocation<', 5], ['HasA>', 1], ['InstanceOf>', 1]]
- p_absent (worst profile) 0.1089, q=1.0, context 0.028; relation null mean links 1.08; strict null mean links 1.32; profile null mean links 1.58; profile2 null mean links 2.57
  - A (6): fitness (= being_fit), good_health (= healthy_living), better_health (= improved_health, being_more_healthy), being_healthy (= being_healthier, getting_healthier), shortness_of_breath (= loss_of_breath, breathlessness, running_out_of_breath, getting_short_of_breath), improving_health (= becoming_more_healthy, improvement_in_health) — frame Causes< getting_exercise (= getting_physical_activity, getting_excercise, get_exercise); Causes< doing_exercises (= working_out); Causes< jogging; UsedFor< getting_exercise (= getting_physical_activity, getting_excercise, get_exercise)
  - B (4): cleanliness (= sanitation, hygiene, being_sanitary), wet_person (= wet_skin), clean_skin (= cleaning_body), getting_cleaner (= cleaning_things) — frame Causes< bathing (= baths); Causes< having_bath (= bath, have_bath)
  - shared surroundings: relaxing, cleaning, feeling_good, getting_clean, grooming, pleasure, take_shower, have_shower, becoming_more_clean, look_better
  - A→surroundings [['UsedFor>', 5], ['UsedFor<', 4], ['Causes>', 3], ['Causes<', 3], ['CausesDesire>', 1]]; B→surroundings [['UsedFor<', 14], ['UsedFor>', 10], ['Causes>', 6], ['HasSubevent>', 4], ['Causes<', 4]]
- p_absent (worst profile) 0.1089, q=1.0, context 0.024; relation null mean links 0.46; strict null mean links 0.87; profile null mean links 2.01; profile2 null mean links 1.33
  - A (5): catalog, gardening_catalog (= garden_catalog), flower_garden (= field_of_flowers, flower_bed), garden_store (= garden_shop, garden_center, garden_nursery), flower_shops (= flower_shop) — frame AtLocation< anemone; AtLocation< rosebush
  - B (5): great_outdoors (= enjoy_outdoors), ohio, iowa, northern_california, rural_area (= rural_areas) — frame AtLocation< cow (= cattle, cows); AtLocation< bald_eagle (= bald_eagles)
  - shared surroundings: book, trees, outside, apple_tree, canada, field, ficus, garden, nature, picture
  - A→surroundings [['AtLocation>', 19], ['AtLocation<', 8], ['IsA>', 2], ['RelatedTo>', 1], ['RelatedTo<', 1]]; B→surroundings [['AtLocation>', 16], ['AtLocation<', 10], ['RelatedTo>', 2], ['RelatedTo<', 2]]

Boundaries by frame kind: {'different relation types': 173, 'location-only': 37, 'same relation types': 17}. Fixed-pair test (both profile nulls leave the pair unlinked in ≤ 5% of graphs): 4 of 227; BH q ≤ 0.10: 0.

### Most unexpected boundaries (smallest worst-case profile p; ties by context similarity), top 15

- **different relation types**, context 0.032, comparable pairs 7 with median 2 links (70% linked); relation p_absent=0.1782 (null mean links 1.82); strict p_absent=0.0495 (null mean links 2.39); profile p_absent=0.0198 (null mean links 3.65); profile2 p_absent=0.0099 (null mean links 3.99); q=1.00
  - A (7): cleanliness (= sanitation, hygiene, being_sanitary), smell_nice (= smell_good, wonderful_smell, smelling_good, smelling_nice), removing_stains (= remove_spots), impressing_others (= impressing_people, impress_other_people), getting_rid_of_dirt (= washing_away_dirt), making_clothes_look_nicer, making_clothes_smell_better — frame UsedFor< clean_clothes (= cleaning_clothes, clothes_cleaned, cleaning_clothing, getting_clothes_clean); UsedFor< washing_clothes (= clean_laundry, making_clothes_clean)
  - B (5): good_health (= healthy_living), better_health (= improved_health, being_more_healthy), shortness_of_breath (= loss_of_breath, breathlessness, running_out_of_breath, getting_short_of_breath), cramps (= cramp, cramping, getting_cramp, crampy, get_cramp), increased_heart_rate (= increase_heart_rate, increased_heartrate, heart_rate_increases) — frame Causes< running (= sprinting); Causes< getting_exercise (= getting_physical_activity, getting_excercise, get_exercise); Causes< doing_exercises (= working_out); Causes< going_for_run (= going_for_jog, go_for_run); Causes< jogging …
  - shared surroundings: get_fit, getting_in_shape, cleaning, have_shower, health, play_sports, getting_clean, effort, get_sweaty, tiredness
  - A→surroundings [['UsedFor<', 19], ['Causes<', 7], ['UsedFor>', 4], ['Causes>', 3], ['HasPrerequisite>', 3]]; B→surroundings [['Causes>', 15], ['UsedFor>', 14], ['Causes<', 9], ['HasSubevent<', 9], ['HasPrerequisite>', 7]]; links between comparable linked pairs are mostly [['UsedFor<', 0.327], ['Causes<', 0.273], ['UsedFor>', 0.145], ['Causes>', 0.073]]
- **location-only**, context 0.022, comparable pairs 10 with median 2 links (91% linked); relation p_absent=0.3861 (null mean links 1.21); strict p_absent=0.0594 (null mean links 2.57); profile p_absent=0.0099 (null mean links 6.07); profile2 p_absent=0.0198 (null mean links 3.63); q=1.00
  - A (9): it's_natural_habitat, indiana, farm_yard (= farm_area, farmer's_field, farmyard), farmland (= farm_field, farm_land), idaho, new_hampshire, new_jersey, ohio, oregon — frame AtLocation< apple_tree; AtLocation< heifer
  - B (4): encyclopedia (= encyclopedias), cartoon, detroit_zoo, jungle (= jungles) — frame AtLocation< jellyfish (= jelly); AtLocation< marmot
  - shared surroundings: united_states, beaver, cow, snake, monkey, field, country, weasel, gazelle, kitten
  - A→surroundings [['AtLocation<', 35], ['AtLocation>', 15], ['PartOf>', 6], ['IsA>', 4], ['PartOf<', 2]]; B→surroundings [['AtLocation<', 23], ['AtLocation>', 15], ['NotDesires<', 1]]; links between comparable linked pairs are mostly [['AtLocation<', 0.562], ['AtLocation>', 0.406], ['UsedFor>', 0.031]]
- **location-only**, context 0.022, comparable pairs 33 with median 5 links (97% linked); relation p_absent=0.2574 (null mean links 1.54); strict p_absent=0.0396 (null mean links 2.54); profile p_absent=0.0198 (null mean links 3.4); profile2 p_absent=0.0198 (null mean links 2.25); q=1.00
  - A (7): landscape (= landscaping, landscapes), nature (= natural_habitat, natural_habitats), california, arboretum, botanical_garden, flower_garden (= field_of_flowers, flower_bed), garden_store (= garden_shop, garden_center, garden_nursery) — frame AtLocation< ficus; AtLocation< rosebush
  - B (5): maine, cartoon, pet_shop (= pet_store, petshop, petstore), spain, cave — frame AtLocation< crab (= crabs); AtLocation< weasel
  - shared surroundings: outside, anemone, trees, garden, forest, lizard, lemur, snake, bee, front_yard
  - A→surroundings [['AtLocation<', 25], ['AtLocation>', 23], ['IsA>', 9], ['RelatedTo>', 7], ['RelatedTo<', 7]]; B→surroundings [['AtLocation<', 32], ['AtLocation>', 22], ['IsA>', 11], ['PartOf>', 1], ['RelatedTo>', 1]]; links between comparable linked pairs are mostly [['AtLocation<', 0.431], ['AtLocation>', 0.412], ['RelatedTo>', 0.028], ['HasA<', 0.019]]
- **location-only**, context 0.022, comparable pairs 26 with median 3 links (96% linked); relation p_absent=0.3366 (null mean links 1.13); strict p_absent=0.2079 (null mean links 1.66); profile p_absent=0.0198 (null mean links 3.16); profile2 p_absent=0.0297 (null mean links 2.65); q=1.00
  - A (7): wild (= wilderness), india (= indian_subcontinent), pet_shop (= pet_store, petshop, petstore), hole (= cavity), south_carolina, dark_place (= shady_spot), cat's_mouth — frame AtLocation< mouse (= mice); AtLocation< lizard (= lizards)
  - B (4): meadow, biology_book, cartoon, flower_garden (= field_of_flowers, flower_bed) — frame AtLocation< anemone; AtLocation< bee (= bees)
  - shared surroundings: country, lemur, forest, garden, water, outside, animals, cat, michigan, nature
  - A→surroundings [['AtLocation<', 34], ['AtLocation>', 31], ['IsA>', 5], ['RelatedTo>', 3], ['IsA<', 2]]; B→surroundings [['AtLocation>', 31], ['AtLocation<', 21], ['IsA>', 5], ['RelatedTo>', 2], ['RelatedTo<', 2]]; links between comparable linked pairs are mostly [['AtLocation>', 0.48], ['AtLocation<', 0.38], ['IsA>', 0.04], ['RelatedTo<', 0.03]]
- **different relation types**, context 0.038, comparable pairs 4 with median 8 links (67% linked); relation p_absent=0.2079 (null mean links 1.61); strict p_absent=0.099 (null mean links 2.0); profile p_absent=0.0396 (null mean links 3.08); profile2 p_absent=0.0594 (null mean links 2.68); q=1.00
  - A (7): becoming_tired (= feeling_tired, becomming_tired), sore_feet (= feet_hurt, getting_sore_feet), shortness_of_breath (= loss_of_breath, breathlessness, running_out_of_breath, getting_short_of_breath), cramps (= cramp, cramping, getting_cramp, crampy, get_cramp), increased_heart_rate (= increase_heart_rate, increased_heartrate, heart_rate_increases), leg_cramps, getting_out_of_breath (= get_winded) — frame Causes< running (= sprinting); Causes< going_for_run (= going_for_jog, go_for_run)
  - B (4): increase_knowledge (= better_knowledge, increased_understanding, increased_knowledge, enhanced_knowledge), insight (= insights), become_smarter (= increase_intelligence, becoming_smarter), improved_performance (= improve_performance) — frame Causes< learning_new (= learn_new, know_new_things, gaining_new_knowledge); HasSubevent< learning (= learn, learned)
  - shared surroundings: fun, visit_art_gallery, reading_book, seeing_exhibits, study, effort, going_to_school, visiting_museum, thinking, play
  - A→surroundings [['Causes<', 8], ['HasSubevent<', 6], ['UsedFor>', 5], ['Causes>', 2], ['CausesDesire>', 1]]; B→surroundings [['Causes<', 14], ['HasSubevent<', 9], ['HasPrerequisite>', 7], ['HasSubevent>', 3], ['UsedFor<', 3]]; links between comparable linked pairs are mostly [['UsedFor<', 0.391], ['Causes<', 0.281], ['HasSubevent>', 0.109], ['Causes>', 0.062]]
- **different relation types**, context 0.042, comparable pairs 3 with median 10 links (60% linked); relation p_absent=0.3366 (null mean links 1.22); strict p_absent=0.1188 (null mean links 1.74); profile p_absent=0.0792 (null mean links 2.6); profile2 p_absent=0.0297 (null mean links 3.07); q=1.00
  - A (6): fitness (= being_fit), good_health (= healthy_living), better_health (= improved_health, being_more_healthy), being_healthy (= being_healthier, getting_healthier), shortness_of_breath (= loss_of_breath, breathlessness, running_out_of_breath, getting_short_of_breath), improving_health (= becoming_more_healthy, improvement_in_health) — frame Causes< getting_exercise (= getting_physical_activity, getting_excercise, get_exercise); Causes< doing_exercises (= working_out); Causes< jogging; UsedFor< getting_exercise (= getting_physical_activity, getting_excercise, get_exercise)
  - B (7): cleanliness (= sanitation, hygiene, being_sanitary), smell_nice (= smell_good, wonderful_smell, smelling_good, smelling_nice), removing_stains (= remove_spots), impressing_others (= impressing_people, impress_other_people), getting_rid_of_dirt (= washing_away_dirt), making_clothes_look_nicer, making_clothes_smell_better — frame UsedFor< clean_clothes (= cleaning_clothes, clothes_cleaned, cleaning_clothing, getting_clothes_clean); UsedFor< washing_clothes (= clean_laundry, making_clothes_clean)
  - shared surroundings: get_fit, getting_in_shape, becoming_more_clean, cleaning, play_sports, health, getting_clean, grooming, cleaning_house, look_better
  - A→surroundings [['UsedFor<', 14], ['Causes>', 12], ['UsedFor>', 9], ['Causes<', 9], ['HasPrerequisite>', 6]]; B→surroundings [['UsedFor<', 21], ['Causes<', 10], ['UsedFor>', 4], ['Causes>', 3], ['HasPrerequisite>', 3]]; links between comparable linked pairs are mostly [['UsedFor<', 0.264], ['Causes<', 0.208], ['UsedFor>', 0.189], ['HasSubevent<', 0.113]]
- **location-only**, context 0.019, comparable pairs 120 with median 5 links (96% linked); relation p_absent=0.198 (null mean links 1.79); strict p_absent=0.0198 (null mean links 3.09); profile p_absent=0.0099 (null mean links 2.64); profile2 p_absent=0.0891 (null mean links 1.93); q=1.00
  - A (8): indiana, great_outdoors (= enjoy_outdoors), idaho, pennsylvania (= pennslyvania), rural_area (= rural_areas), story_book (= storybook), california, tennessee — frame AtLocation< cow (= cattle, cows); AtLocation< fox
  - B (4): maine, pet_shop (= pet_store, petshop, petstore), basket, chinese_restaurant — frame AtLocation< crab (= crabs); AtLocation< small_dog
  - shared surroundings: united_states, administrative_region, state, apple_tree, animals, outside, ficus, weasel, bald_eagle, beaver
  - A→surroundings [['AtLocation<', 29], ['AtLocation>', 19], ['IsA>', 14], ['PartOf>', 5], ['RelatedTo<', 4]]; B→surroundings [['AtLocation<', 26], ['AtLocation>', 24], ['IsA>', 6], ['MannerOf>', 2], ['PartOf>', 1]]; links between comparable linked pairs are mostly [['AtLocation<', 0.355], ['AtLocation>', 0.293], ['RelatedTo>', 0.098], ['RelatedTo<', 0.086]]
- **location-only**, context 0.019, comparable pairs 11 with median 3 links (85% linked); relation p_absent=0.703 (null mean links 0.34); strict p_absent=0.1485 (null mean links 2.12); profile p_absent=0.099 (null mean links 2.15); profile2 p_absent=0.0198 (null mean links 3.35); q=1.00
  - A (17): agent_provocateur, pub (= pubs), aon (= aol), den (= lair), capita, french_connection, harrods, lonsdale, mi5, piccadilly_circus … — frame AtLocation> london; AtLocation> england (= united_kingdom, great_britain)
  - B (4): exploratorium, ign, macromedia, uber — frame AtLocation> san_francisco; AtLocation> california
  - shared surroundings: company, city, fox, subsidiary, corner_grocery, museum, beach, freeway, cow, bridge
  - A→surroundings [['IsA>', 11], ['AtLocation<', 5], ['AtLocation>', 3], ['RelatedTo<', 2], ['HasA>', 1]]; B→surroundings [['IsA>', 5], ['AtLocation<', 5], ['HasA>', 1], ['InstanceOf>', 1]]; links between comparable linked pairs are mostly [['AtLocation<', 0.543], ['AtLocation>', 0.326], ['HasA>', 0.022], ['IsA<', 0.022]]
- **location-only**, context 0.024, comparable pairs 14 with median 2 links (74% linked); relation p_absent=0.6238 (null mean links 0.46); strict p_absent=0.4257 (null mean links 0.87); profile p_absent=0.1089 (null mean links 2.01); profile2 p_absent=0.0891 (null mean links 1.33); q=1.00
  - A (5): catalog, gardening_catalog (= garden_catalog), flower_garden (= field_of_flowers, flower_bed), garden_store (= garden_shop, garden_center, garden_nursery), flower_shops (= flower_shop) — frame AtLocation< anemone; AtLocation< rosebush
  - B (5): great_outdoors (= enjoy_outdoors), ohio, iowa, northern_california, rural_area (= rural_areas) — frame AtLocation< cow (= cattle, cows); AtLocation< bald_eagle (= bald_eagles)
  - shared surroundings: book, trees, outside, apple_tree, canada, field, ficus, garden, nature, picture
  - A→surroundings [['AtLocation>', 19], ['AtLocation<', 8], ['IsA>', 2], ['RelatedTo>', 1], ['RelatedTo<', 1]]; B→surroundings [['AtLocation>', 16], ['AtLocation<', 10], ['RelatedTo>', 2], ['RelatedTo<', 2]]; links between comparable linked pairs are mostly [['AtLocation<', 0.492], ['AtLocation>', 0.295], ['UsedFor<', 0.066], ['IsA>', 0.033]]
- **different relation types**, context 0.038, comparable pairs 7 with median 2 links (64% linked); relation p_absent=0.2079 (null mean links 1.29); strict p_absent=0.2673 (null mean links 1.25); profile p_absent=0.1188 (null mean links 2.05); profile2 p_absent=0.099 (null mean links 1.74); q=1.00
  - A (5): settle_down (= try_to_calm_down), get_weapon (= have_weapon), change_mind (= change_opinion, changing_mind), lack_of_conscience, lack_of_empathy — frame HasPrerequisite< kill (= killing, murder); HasPrerequisite< hurting_else (= hurt_else)
  - B (4): increase_knowledge (= better_knowledge, increased_understanding, increased_knowledge, enhanced_knowledge), insight (= insights), become_smarter (= increase_intelligence, becoming_smarter), improved_performance (= improve_performance) — frame Causes< learning_new (= learn_new, know_new_things, gaining_new_knowledge); HasSubevent< learning (= learn, learned)
  - shared surroundings: reading_book, study_for_subject, study, person, pain, thinking, fun, using_television, watch_tv, transfer_knowledge
  - A→surroundings [['Causes>', 4], ['HasPrerequisite<', 3], ['HasSubevent>', 2], ['RelatedTo>', 2], ['Causes<', 2]]; B→surroundings [['Causes<', 8], ['HasSubevent<', 6], ['HasPrerequisite>', 5], ['HasSubevent>', 3], ['MotivatedByGoal>', 3]]; links between comparable linked pairs are mostly [['HasSubevent>', 0.255], ['Causes<', 0.106], ['HasSubevent<', 0.106], ['UsedFor<', 0.106]]
- **different relation types**, context 0.033, comparable pairs 7 with median 2 links (70% linked); relation p_absent=0.1881 (null mean links 1.71); strict p_absent=0.1188 (null mean links 2.06); profile p_absent=0.0495 (null mean links 2.82); profile2 p_absent=0.1188 (null mean links 1.42); q=1.00
  - A (7): cleanliness (= sanitation, hygiene, being_sanitary), smell_nice (= smell_good, wonderful_smell, smelling_good, smelling_nice), removing_stains (= remove_spots), impressing_others (= impressing_people, impress_other_people), getting_rid_of_dirt (= washing_away_dirt), making_clothes_look_nicer, making_clothes_smell_better — frame UsedFor< clean_clothes (= cleaning_clothes, clothes_cleaned, cleaning_clothing, getting_clothes_clean); UsedFor< washing_clothes (= clean_laundry, making_clothes_clean)
  - B (5): becoming_tired (= feeling_tired, becomming_tired), become_tired (= make_tired), getting_tired_legs (= tired_legs, legs_get_tired, legs_tired), sore_feet (= feet_hurt, getting_sore_feet), sore_legs — frame Causes< dance (= dancing); Causes< hiking (= hikers); Causes< standing_in_line (= take_place_in_line, standing_in_queue, standing_on_line); Causes< going_for_run (= going_for_jog, go_for_run); Causes< going_for_walk (= take_walk_outside) …
  - shared surroundings: person, getting_in_shape, health, running_in_marathon, get_sweaty, tiredness, have_shower, dressing_nice, have_fun, testing_strength
  - A→surroundings [['UsedFor<', 6], ['HasSubevent>', 3], ['Causes>', 2], ['HasPrerequisite>', 2], ['UsedFor>', 2]]; B→surroundings [['UsedFor>', 8], ['Causes>', 5], ['HasSubevent>', 5], ['Causes<', 5], ['HasSubevent<', 3]]; links between comparable linked pairs are mostly [['UsedFor<', 0.327], ['Causes<', 0.273], ['UsedFor>', 0.145], ['Causes>', 0.073]]
- **location-only**, context 0.022, comparable pairs 14 with median 2 links (74% linked); relation p_absent=0.3267 (null mean links 1.0); strict p_absent=0.1287 (null mean links 2.06); profile p_absent=0.0198 (null mean links 4.4); profile2 p_absent=0.1287 (null mean links 1.59); q=1.00
  - A (7): meadow, indiana, great_outdoors (= enjoy_outdoors), idaho, new_hampshire, pennsylvania (= pennslyvania), wooded_area (= found_in_woods) — frame AtLocation< apple_tree; AtLocation< fox
  - B (4): encyclopedia (= encyclopedias), detroit_zoo, strangest_places (= weirdest_places), baltimore_aquarium — frame AtLocation< jellyfish (= jelly); AtLocation< sloth
  - shared surroundings: snake, united_states, cow, country, animals, lizard, marmoset, marmot, gazelle, mammoth
  - A→surroundings [['AtLocation<', 23], ['AtLocation>', 13], ['PartOf>', 4], ['IsA>', 2], ['RelatedTo<', 2]]; B→surroundings [['AtLocation>', 17], ['AtLocation<', 14], ['IsA>', 1]]; links between comparable linked pairs are mostly [['AtLocation<', 0.492], ['AtLocation>', 0.295], ['UsedFor<', 0.066], ['IsA>', 0.033]]
- **location-only**, context 0.019, comparable pairs 11 with median 3 links (85% linked); relation p_absent=0.6238 (null mean links 0.46); strict p_absent=0.198 (null mean links 1.75); profile p_absent=0.1287 (null mean links 1.93); profile2 p_absent=0.0495 (null mean links 3.35); q=1.00
  - A (15): 60_minutes (= about_half_hour), boiling_points, brownstone, conglomerate, dakota, deli_store (= deli_restaurant), ellis_island, guardian_angels, italian_restaurant, kosher_deli (= kosher_delicatessen) … — frame AtLocation> new_york; AtLocation> new_york_city (= manhattan)
  - B (5): buckingham_palace, palace_of_westminster, st_james's_palace, trafalgar_square, westminster_abbey — frame AtLocation> city_of_westminster; AtLocation> england (= united_kingdom, great_britain); AtLocation> greater_london
  - shared surroundings: historic_place, queen, lancaster, administrative_region, mayor, fox, yorkshire, row_house, education, metropolitan_city
  - A→surroundings [['IsA>', 3], ['RelatedTo>', 3], ['PartOf<', 3], ['AtLocation<', 2], ['RelatedTo<', 2]]; B→surroundings [['IsA>', 5], ['RelatedTo>', 3], ['AtLocation<', 3], ['RelatedTo<', 3], ['HasA>', 2]]; links between comparable linked pairs are mostly [['AtLocation<', 0.543], ['AtLocation>', 0.326], ['HasA>', 0.022], ['IsA<', 0.022]]
- **different relation types**, context 0.042, comparable pairs 23 with median 2 links (77% linked); relation p_absent=0.4455 (null mean links 0.85); strict p_absent=0.2772 (null mean links 1.17); profile p_absent=0.1188 (null mean links 1.89); profile2 p_absent=0.1386 (null mean links 1.71); q=1.00
  - A (4): take_music_lessons (= learning_music, learn_music), learn_to_read_music, take_lessons, use_fingers (= move_hands, move_fingers) — frame HasPrerequisite< play_guitar (= playing_guitar, strumming_guitar); HasPrerequisite< play_piano (= playing_piano); HasPrerequisite< playing_violin (= play_violin); HasPrerequisite< playing_harp (= play_harp)
  - B (4): get_sweaty (= getting_sweaty, working_up_sweat), increased_heart_rate (= increase_heart_rate, increased_heartrate, heart_rate_increases), breathe_hard (= breathing_hard, breathe_heavily, breathe_harder, breath_heavily), getting_physically_fit (= feeling_fit) — frame Causes< going_for_run (= going_for_jog, go_for_run); HasSubevent< do_exercises (= excercise, work_out, excersize, exercise_muscles)
  - shared surroundings: fun, play, pleasure, exercises, enjoyment, dance, listen_to_music, dance_samba, have_fun
  - A→surroundings [['UsedFor>', 8], ['HasSubevent>', 3], ['IsA>', 3], ['HasPrerequisite<', 2], ['HasFirstSubevent>', 1]]; B→surroundings [['UsedFor>', 4], ['HasSubevent>', 3], ['UsedFor<', 3], ['HasSubevent<', 2], ['Causes>', 1]]; links between comparable linked pairs are mostly [['HasSubevent>', 0.215], ['HasPrerequisite<', 0.168], ['Causes>', 0.121], ['HasSubevent<', 0.121]]
- **same relation types**, context 0.028, comparable pairs 10 with median 2 links (71% linked); relation p_absent=0.0891 (null mean links 2.25); strict p_absent=0.0792 (null mean links 2.83); profile p_absent=0.1386 (null mean links 2.32); profile2 p_absent=0.0495 (null mean links 2.35); q=1.00
  - A (5): becoming_tired (= feeling_tired, becomming_tired), become_tired (= make_tired), getting_tired_legs (= tired_legs, legs_get_tired, legs_tired), sore_feet (= feet_hurt, getting_sore_feet), sore_legs — frame Causes< dance (= dancing); Causes< hiking (= hikers); Causes< standing_in_line (= take_place_in_line, standing_in_queue, standing_on_line); Causes< going_for_run (= going_for_jog, go_for_run); Causes< going_for_walk (= take_walk_outside) …
  - B (6): throw_ball (= throw_balls, throwing_ball), win_game (= win_match), getting_hurt (= getting_wounded, being_injured, being_hurt), score_goal (= score_goals), get_hurt (= getting_injured, get_injured), knee_injuries (= knee_injury) — frame Causes< playing_football (= play_football); HasSubevent< play_sports (= play_sport, playing_sports, playing_sport); HasSubevent< playing_football (= play_football)
  - shared surroundings: sweat, fun, exercise, having_fun, fatigue, running, foot, get_tired, person, getting_exercise
  - A→surroundings [['Causes>', 45], ['UsedFor>', 44], ['HasSubevent>', 24], ['HasPrerequisite>', 18], ['RelatedTo>', 15]]; B→surroundings [['UsedFor>', 30], ['HasSubevent>', 28], ['Causes>', 21], ['HasPrerequisite>', 15], ['MotivatedByGoal>', 11]]; links between comparable linked pairs are mostly [['HasSubevent>', 0.214], ['HasSubevent<', 0.167], ['Causes<', 0.119], ['Causes>', 0.095]]

