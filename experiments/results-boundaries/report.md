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

### Unlinked context-similar group pairs least expected under both profile nulls (top 12)

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

Boundaries by frame kind: {'location-only': 48, 'different relation types': 120, 'same relation types': 15}. Fixed-pair test (both profile nulls leave the pair unlinked in ≤ 5% of graphs): 1 of 183; BH q ≤ 0.10: 0.

### Most unexpected boundaries (smallest worst-case profile p; ties by context similarity), top 12

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

