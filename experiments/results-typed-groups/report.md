# Typed-relation groups (Wiktionary-only links removed)

Variant: 689,944 of 4,341,307 links; datasets {'/d/wiktionary': 27365, '/d/verbosity': 45512, '/d/conceptnet': 220555, '/d/dbpedia': 45038, '/d/wordnet': 296711, '/d/opencyc': 86828}. Typed features 19,369 columns / 178,516 incidences.
Groups mined 1,511; significant under all nulls (global, relation, reciprocal, strict) 1,096; robust (all nulls + recovered in ≥60% of 80% edge subsamples + still present with Wiktionary restored) 434.
Robust tiers: {'partly_named': 70, 'crosscutting': 185, 'uncategorised': 146, 'named': 33}. Subsample re-mining group counts: [771, 730, 800, 780, 764].
Selection control (re-mining null graphs): {"real": {"groups": 1511, "size_ge_6": 571, "size_ge_10": 155}, "global": {"groups": [99, 114, 111, 141], "size_ge_6": [43, 57, 61, 74], "size_ge_10": [1, 6, 6, 9]}, "relation": {"groups": [739, 730, 752, 790], "size_ge_6": [174, 159, 206, 207], "size_ge_10": [16, 14, 16, 16]}, "reciprocal": {"groups": [706, 718, 704, 785], "size_ge_6": [203, 189, 174, 195], "size_ge_10": [9, 9, 11, 10]}, "strict": {"groups": [361, 337, 402, 368], "size_ge_6": [60, 59, 63, 64], "size_ge_10": [3, 3, 7, 2]}}

## Shapes (clusters of relation profiles)

| shape | relation profile (share of member–frame incidences) | groups | robust | robust tiers |
|---|---|---|---|---|
| 30 | AtLocation> 0.99 | 510 | 196 | {'crosscutting': 135, 'partly_named': 44, 'named': 10, 'uncategorised': 7} |
| 26 | UsedFor> 0.75, AtLocation> 0.24 | 196 | 54 | {'uncategorised': 8, 'named': 17, 'crosscutting': 15, 'partly_named': 14} |
| 2 | HasPrerequisite< 0.98 | 158 | 46 | {'uncategorised': 46} |
| 18 | AtLocation< 0.94, AtLocation> 0.05 | 156 | 35 | {'crosscutting': 24, 'uncategorised': 3, 'partly_named': 5, 'named': 3} |
| 32 | UsedFor< 0.98 | 94 | 17 | {'crosscutting': 2, 'uncategorised': 15} |
| 4 | Causes> 0.75, UsedFor> 0.23 | 71 | 14 | {'uncategorised': 13, 'crosscutting': 1} |
| 31 | CapableOf< 0.96 | 25 | 11 | {'uncategorised': 10, 'crosscutting': 1} |
| 36 | Causes< 0.94, HasSubevent< 0.05 | 53 | 11 | {'uncategorised': 8, 'crosscutting': 2, 'partly_named': 1} |
| 7 | HasPrerequisite> 0.51, Causes> 0.49 | 29 | 8 | {'uncategorised': 8} |
| 10 | HasPrerequisite> 0.87, HasLastSubevent> 0.06 | 38 | 6 | {'uncategorised': 6} |
| 16 | HasA< 0.96 | 14 | 5 | {'uncategorised': 3, 'crosscutting': 2} |
| 14 | MotivatedByGoal> 0.68, CausesDesire< 0.32 | 15 | 4 | {'uncategorised': 4} |
| 27 | HasProperty> 0.49, AtLocation> 0.48 | 9 | 3 | {'partly_named': 1, 'crosscutting': 2} |
| 29 | AtLocation> 0.49, ReceivesAction> 0.48 | 11 | 3 | {'partly_named': 3} |
| 6 | CausesDesire< 0.88, HasLastSubevent> 0.12 | 4 | 2 | {'uncategorised': 2} |

## Easy to name: an existing category covers ≥50% of members

### group 18 — 14 members, shape 30, tier named
members: bass_drum, brass, brass_family, cornet, crash_cymbal, drum, flute, percussion_instrument, saxophone, snare_drum, string_bass, trombone, trumpet, tuba
frame: AtLocation> marching_band; AtLocation> orchestra
density 1.0; support 14 (with Wiktionary 14); nulls global p=0.0099 z=28.0 (null mean 0.0), relation p=0.0099 z=27.8 (null mean 0.09), reciprocal p=0.0099 z=27.8 (null mean 0.11), strict p=0.0099 z=27.6 (null mean 0.22); BH q 0.0136; subsample recovery 0.6
category: best direct musical_instrument (0.64), best within 2 IsA-steps musical_instrument (0.86), members with any category 1.0
member categories: bass_drum→drum,instrument,musical_instrument,percussion_instrument; brass→conductor,album,memorial,wind_instrument; brass_family→class; cornet→brass,brass_instrument,musical_instrument; crash_cymbal→drum_set; drum→can,play,sound,container; flute→crimp,instrument,wind_instrument,woodwind; percussion_instrument→instrument,musical_instrument,music_instrument,acoustic_instrument; saxophone→instrument,musical_instrument,tool,woodwind; snare_drum→drum,musical_instrument,percussion_instrument,percussion
internal links among members 10 (configuration expectation 0.09); relative weight of member–frame links {'original': 1.058, 'wiki_half0': 1.026, 'wiki_half1': 1.071}
WikiText (obs/exp): wiki_half0 member–frame 43/2.9, member–member 108/1.6; wiki_half1 member–frame 24/2.9, member–member 70/1.6

### group 9 — 18 members, shape 26, tier named
members: acoustic_guitar, bagpipes, bass_fiddle, clavichord, cornet, french_horn, harmonica, keyboard, mandolin, symphony_hall, organ, string_bass, stringed_instrument, trombone, trumpet, viola, violin, woodwind
frame: UsedFor> play_music; UsedFor> playing_music
density 1.0; support 18 (with Wiktionary 18); nulls global p=0.0099 z=36.0 (null mean 0.0), relation p=0.0099 z=32.4 (null mean 0.38), reciprocal p=0.0099 z=26.8 (null mean 0.46), strict p=0.0099 z=17.1 (null mean 1.05); BH q 0.0136; subsample recovery 1.0
category: best direct musical_instrument (0.72), best within 2 IsA-steps musical_instrument (0.94), members with any category 1.0
member categories: acoustic_guitar→guitar,acoustic_instrument,larger_than_violin; bagpipes→best,musical_instrument,musical_instruments,from_scotland; bass_fiddle→bass,instrument,stringed_instrument,bowed_stringed_instrument; clavichord→keyboard_instrument,musical_instrument,stringed_instrument,archaic_musical_instrument; cornet→brass,brass_instrument,musical_instrument; french_horn→brass,brass_instrument,instrument,musical_instrument; harmonica→instrument,musical_instrument,reed,wind_instrument; keyboard→terminal,piano,computer,organ; mandolin→instrument,musical_instrument,stringed_instrument,chordophone; symphony_hall→where_orchestras_play
internal links among members 9 (configuration expectation 0.19); relative weight of member–frame links {'original': 1.251, 'wiki_half0': 1.266, 'wiki_half1': 1.265}
WikiText (obs/exp): wiki_half0 member–frame 0/0.1, member–member 176/2.8; wiki_half1 member–frame 1/0.1, member–member 113/2.9

### group 171 — 9 members, shape 26, tier named
members: accordion, guitar, instrument_triangle, oboe, percussion_instrument, tuba, wind_instrument, woodwind, playing_harp
frame: UsedFor> make_music; UsedFor> making_music; UsedFor> playing_in_orchestra; UsedFor> playing_in_band
density 0.833; support 9 (with Wiktionary 9); nulls global p=0.0099 z=18.0 (null mean 0.0), relation p=0.0099 z=18.0 (null mean 0.01), reciprocal p=0.0099 z=17.9 (null mean 0.03), strict p=0.0099 z=18.0 (null mean 0.01); BH q 0.0136; subsample recovery 0.6
category: best direct musical_instrument (0.78), best within 2 IsA-steps musical_instrument (0.89), members with any category 0.89
member categories: accordion→instrument,keyboard_instrument,musical_instrument,man_made_object; guitar→instrument,stringed_instrument,lute,chordophone; instrument_triangle→musical_instrument; oboe→instrument,musical_instrument,wind_instrument,woodwind; percussion_instrument→instrument,musical_instrument,music_instrument,acoustic_instrument; tuba→brass_instrument,musical_instrument,large_musical_instrument,instrument_in_band; wind_instrument→musical_instrument,acoustic_instrument,single_user_device,member_of_orchestra; woodwind→instrument,musical_instrument,wind_instrument,musical_instriment; playing_harp→–
internal links among members 3 (configuration expectation 0.06); relative weight of member–frame links {'original': 1.126, 'wiki_half0': 1.139, 'wiki_half1': 1.139}
WikiText (obs/exp): wiki_half0 member–frame 1/0.3, member–member 9/0.9; wiki_half1 member–frame 1/0.2, member–member 13/1.0

### group 142 — 7 members, shape 30, tier named
members: bernstein, bromberg, ipf, jako, porsche, steinberg, totenkopf
frame: AtLocation> germany; AtLocation> baden_württemberg
density 1.0; support 7 (with Wiktionary 7); nulls global p=0.0099 z=14.0 (null mean 0.0), relation p=0.0099 z=13.8 (null mean 0.12), reciprocal p=0.0099 z=13.9 (null mean 0.07), strict p=0.0099 z=13.6 (null mean 0.22); BH q 0.0136; subsample recovery 0.8
category: best direct mountain (0.71), best within 2 IsA-steps landscape (0.71), members with any category 1.0
member categories: bernstein→mountain; bromberg→mountain; ipf→mountain; jako→company; porsche→company,sports_car,german_car,luxury_automobile; steinberg→mountain,company,limited_liability_company; totenkopf→mountain
internal links among members 0 (configuration expectation 0.0); relative weight of member–frame links {'original': 0.542, 'wiki_half0': 0.564, 'wiki_half1': 0.564}
WikiText (obs/exp): wiki_half0 member–frame 1/1.4, member–member 0/0.0; wiki_half1 member–frame 0/1.6, member–member 1/0.0

### group 83 — 7 members, shape 22, tier named
members: december, august, january, july, march, may, october
frame: HasA> 31_days; HasA> thirty_one_days
density 1.0; support 7 (with Wiktionary 7); nulls global p=0.0099 z=14.0 (null mean 0.0), relation p=0.0099 z=13.5 (null mean 0.24), reciprocal p=0.0099 z=13.7 (null mean 0.17), strict p=0.0099 z=13.7 (null mean 0.13); BH q 0.0136; subsample recovery 1.0
category: best direct gregorian_calendar (1.0), best within 2 IsA-steps gregorian_calendar (1.0), members with any category 1.0
member categories: december→gregorian_calendar,month,gregorian_month,gregorian_calendar_month; august→gregorian_calendar,month,gregorian_month,gregorian_calendar_month; january→gregorian_calendar,q1,month,gregorian_month; july→gregorian_calendar,month,gregorian_month,gregorian_calendar_month; march→walk,gregorian_calendar,progress,book; may→gregorian_calendar,month,musical_artist,gregorian_month; october→gregorian_calendar,month,gregorian_month,gregorian_calendar_month
internal links among members 1 (configuration expectation 0.01); relative weight of member–frame links {'original': 0.949, 'wiki_half0': 0.972, 'wiki_half1': 0.972}
WikiText (obs/exp): wiki_half0 member–frame 3/2.2, member–member 6301/5993.6; wiki_half1 member–frame 0/1.0, member–member 6743/6157.0

### group 313 — 7 members, shape 20, tier named
members: apple, banana, bread, chocolate, corn, fruit, pickle
frame: ReceivesAction> eaten; UsedFor> eating
density 1.0; support 7 (with Wiktionary 7); nulls global p=0.0099 z=14.0 (null mean 0.0), relation p=0.0099 z=13.7 (null mean 0.17), reciprocal p=0.0099 z=13.7 (null mean 0.17), strict p=0.0099 z=11.3 (null mean 0.35); BH q 0.0136; subsample recovery 0.6
category: best direct food (0.57), best within 2 IsA-steps food_item (0.86), members with any category 1.0
member categories: apple→plant,tree,fruit,fruit_tree; banana→food,hand,dessert,fruit; bread→cover,commonly,sandwich,cereal; chocolate→food,candy,dessert,brown; corn→vegetable,disease,food,feed; fruit→bear,rarely,solid_object,living_thing; pickle→vegetable,food,preserve,cucumber
internal links among members 3 (configuration expectation 0.26); relative weight of member–frame links {'original': 1.038, 'wiki_half0': 0.938, 'wiki_half1': 0.875}
WikiText (obs/exp): wiki_half0 member–frame 60/3.8, member–member 30/4.4; wiki_half1 member–frame 37/3.9, member–member 29/4.9


## Hard to name: partial category (33–50%, or ≥50% only at 2 IsA-steps), or members mostly uncategorised

### group 3 — 36 members, shape 30, tier partly_named
members: accordion, acoustic_guitar, balalaika, banjo, bass_baritone, bass_clarinet, bass_drum, bass_fiddle, bassoon, clarinet, cornet, double_bass, drum, fiddle, flute, gong, guitar, harpsichord, instrument, instrument_triangle, keyboard_instrument, mandolin, music_stand, musical_instrument …
frame: AtLocation> band; AtLocation> orchestra; UsedFor> making_music
density 0.824; support 36 (with Wiktionary 36); nulls global p=0.0099 z=72.0 (null mean 0.01), relation p=0.0099 z=48.9 (null mean 0.58), reciprocal p=0.0099 z=43.1 (null mean 0.79), strict p=0.0099 z=26.3 (null mean 2.21); BH q 0.0136; subsample recovery 0.6
category: best direct stringed_instrument (0.17), best within 2 IsA-steps device (0.72), members with any category 0.97
member categories: accordion→instrument,keyboard_instrument,musical_instrument,man_made_object; acoustic_guitar→guitar,acoustic_instrument,larger_than_violin; balalaika→stringed_instrument,chordophone,stringed_music_instrument; banjo→musical_instrument,stringed_instrument,string_instrument,acoustic_instrument; bass_baritone→–; bass_clarinet→clarinet,reed_instrument; bass_drum→drum,instrument,musical_instrument,percussion_instrument; bass_fiddle→bass,instrument,stringed_instrument,bowed_stringed_instrument; bassoon→musical_instrument,wind_instrument,woodwind,woodwind_instrument; clarinet→instrument,musical_instrument,woodwind_instrument,horn_musical_instrument
internal links among members 53 (configuration expectation 0.84); relative weight of member–frame links {'original': 1.185, 'wiki_half0': 1.131, 'wiki_half1': 1.12}
WikiText (obs/exp): wiki_half0 member–frame 499/123.7, member–member 599/22.1; wiki_half1 member–frame 350/114.8, member–member 611/20.4

### group 0 — 53 members, shape 24, tier partly_named
members: rich, bill, chase, john, milan, andrew, bob, charles, chris, harry, henry, jeff, jim, joe, larry, mary, mike, robert, terry, tim, jill, gene, bobby, brent …
frame: Desires> sex; HasA> kids; HasProperty> nuts
density 0.943; support 53 (with Wiktionary 53); nulls global p=0.0099 z=106.0 (null mean 0.0), relation p=0.0099 z=82.1 (null mean 0.54), reciprocal p=0.0099 z=75.5 (null mean 0.43), strict p=0.0099 z=10.8 (null mean 24.47); BH q 0.0136; subsample recovery 1.0
category: best direct washing_car (0.45), best within 2 IsA-steps washing_car (0.45), members with any category 0.83
member categories: rich→name_for_male,not_at_work; bill→list,paper_money,money,statement; chase→cut,bank,frame,washing_car; john→person,student,college_student,crying; milan→lombardy,in_italy; andrew→person,goof,in_fourth_grade; bob→dog,person,dress,move; charles→person,massachusetts,standing_up; chris→violinist,welder,programmer,given_name; harry→destroy,washing_car,given_name,moving_quickly
internal links among members 0 (configuration expectation 0.26); relative weight of member–frame links {'original': 0.917, 'wiki_half0': 0.918, 'wiki_half1': 0.93}
WikiText (obs/exp): wiki_half0 member–frame 132/216.4, member–member 6635/3781.8; wiki_half1 member–frame 108/227.3, member–member 6328/3796.2

### group 11 — 23 members, shape 30, tier partly_named
members: apple, pie, cheese, turkey, bad_smell, butter, carrots, carton_of_milk, fresh_vegetables, frozen_foods, fruit, ham, juice, ketchup, pickles, left_overs, leftovers, lemon, milk, mold, mustard, orange_juice, vegetables
frame: AtLocation> fridge; AtLocation> refrigerator
density 1.0; support 23 (with Wiktionary 23); nulls global p=0.0099 z=46.0 (null mean 0.0), relation p=0.0099 z=16.0 (null mean 1.68), reciprocal p=0.0099 z=18.3 (null mean 1.45), strict p=0.0099 z=26.5 (null mean 0.83); BH q 0.0136; subsample recovery 1.0
category: best direct food (0.35), best within 2 IsA-steps food (0.52), members with any category 0.78
member categories: apple→plant,tree,fruit,fruit_tree; pie→pastry,semisolid,tangible_thing,inanimate_object; cheese→discontinue,food,software,magazine; turkey→country,food,flop,middle_east; bad_smell→–; butter→cover,food,fat,solid_object; carrots→food,rinsed_in_sinks; carton_of_milk→–; fresh_vegetables→–; frozen_foods→–
internal links among members 10 (configuration expectation 0.53); relative weight of member–frame links {'original': 1.137, 'wiki_half0': 1.184, 'wiki_half1': 1.184}
WikiText (obs/exp): wiki_half0 member–frame 3/0.4, member–member 178/14.1; wiki_half1 member–frame 1/0.3, member–member 136/14.0

### group 27 — 14 members, shape 30, tier partly_named
members: blood_pressure_machine, waiting_room, examination_table, needle, exam_table, hypodermic_needle, medical_records, reflex_hammer, scale, stethoscope, syringe, thermometer, tongue_depressor, x_ray_machine
frame: AtLocation> doctor; AtLocation> doctor's_office
density 1.0; support 14 (with Wiktionary 14); nulls global p=0.0099 z=28.0 (null mean 0.0), relation p=0.0099 z=27.6 (null mean 0.2), reciprocal p=0.0099 z=23.7 (null mean 0.31), strict p=0.0099 z=27.6 (null mean 0.18); BH q 0.0136; subsample recovery 0.8
category: best direct medical_device (0.29), best within 2 IsA-steps device (0.5), members with any category 0.71
member categories: blood_pressure_machine→–; waiting_room→room,place_where_patient_sits; examination_table→–; needle→pointer,shaft,harass,implement; exam_table→desk,table_where_person_examed; hypodermic_needle→needle,medical_device,hypodermic_syringe; medical_records→–; reflex_hammer→–; scale→remove,bit,take,climb; stethoscope→tool,device,consumer_durable,non_powered_device
internal links among members 1 (configuration expectation 0.05); relative weight of member–frame links {'original': 1.157, 'wiki_half0': 1.177, 'wiki_half1': 1.205}
WikiText (obs/exp): wiki_half0 member–frame 5/5.0, member–member 3/0.5; wiki_half1 member–frame 3/4.9, member–member 1/0.5

### group 20 — 19 members, shape 30, tier partly_named
members: blotter, lamp, calculator, calendar, telephone, checkbook, computer_monitor, notebook, highlighter_pen, keyboard, phone, monitor, mousepad, notepad, paper_clips, paper_punch, paperclips, paperweight, stapler
frame: AtLocation> desk; AtLocation> desktop
density 1.0; support 19 (with Wiktionary 19); nulls global p=0.0099 z=38.0 (null mean 0.0), relation p=0.0099 z=14.8 (null mean 1.56), reciprocal p=0.0099 z=15.0 (null mean 1.55), strict p=0.0099 z=17.6 (null mean 0.95); BH q 0.0136; subsample recovery 0.6
category: best direct machine (0.16), best within 2 IsA-steps device (0.53), members with any category 0.84
member categories: blotter→written_record; lamp→electrical_device,furniture,source_of_illumination; calculator→expert,machine,electronic_device,noun; calendar→table,software,list,schedule; telephone→electronic_equipment,telecommunication,communication_device,telephone_system; checkbook→record,non_agentive_artifact,single_purpose_device,single_user_device; computer_monitor→monitor; notebook→generally,artifact,book,computer; highlighter_pen→–; keyboard→terminal,piano,computer,organ
internal links among members 2 (configuration expectation 0.19); relative weight of member–frame links {'original': 1.194, 'wiki_half0': 1.208, 'wiki_half1': 1.229}
WikiText (obs/exp): wiki_half0 member–frame 11/0.9, member–member 9/3.2; wiki_half1 member–frame 11/0.8, member–member 5/2.9

### group 45 — 11 members, shape 2, tier uncategorised
members: go_to_concert, buy_ticket, open_eyes, go_to_theater, go_to_theatre, buy_tickets, buy_tickets_to_concert, buy_ticket_to_concert, go_to_club, buy_concert_ticket, attend_concert
frame: HasPrerequisite< watch_musician_perform; HasPrerequisite< see_band
density 1.0; support 11 (with Wiktionary 11); nulls global p=0.0099 z=21.9 (null mean 0.05), relation p=0.0099 z=21.9 (null mean 0.04), reciprocal p=0.0099 z=21.8 (null mean 0.08), strict p=0.0099 z=21.9 (null mean 0.06); BH q 0.0136; subsample recovery 1.0
category: best direct 0 (0.0), best within 2 IsA-steps 0 (0.0), members with any category 0.0
member categories: go_to_concert→–; buy_ticket→–; open_eyes→–; go_to_theater→–; go_to_theatre→–; buy_tickets→–; buy_tickets_to_concert→–; buy_ticket_to_concert→–; go_to_club→–; buy_concert_ticket→–
internal links among members 1 (configuration expectation 0.01); relative weight of member–frame links {'original': 1.182, 'wiki_half0': 1.182, 'wiki_half1': 1.182}
WikiText (obs/exp): wiki_half0 member–frame 0/0.0, member–member 0/0.0; wiki_half1 member–frame 0/0.0, member–member 0/0.0

### group 51 — 12 members, shape 30, tier partly_named
members: scientist, petri_dish, beaker, beakers, bunsen_burner, bunsen_burners, chemicals, test_tube, flask, helium, sulfur, test_tubes
frame: AtLocation> chemistry_lab; AtLocation> laboratory
density 1.0; support 12 (with Wiktionary 12); nulls global p=0.0099 z=24.0 (null mean 0.0), relation p=0.0099 z=20.1 (null mean 0.38), reciprocal p=0.0099 z=18.1 (null mean 0.37), strict p=0.0099 z=23.6 (null mean 0.22); BH q 0.0136; subsample recovery 0.8
category: best direct lab_glassware (0.33), best within 2 IsA-steps tangible_thing (0.5), members with any category 0.75
member categories: scientist→human,band,person,magazine; petri_dish→dish,storage_device,lab_glassware; beaker→cup,jar,storage_device,lab_glassware; beakers→–; bunsen_burner→gas_burner,tangible_thing,laboratory_equipment,combusion_heating_element; bunsen_burners→–; chemicals→medicines,materials,all_around_us,plural_for_chemical; test_tube→tube,lab_glassware; flask→bottle,software,container,containerful; helium→gas,element,chemical_element,inert_gas
internal links among members 0 (configuration expectation 0.07); relative weight of member–frame links {'original': 1.273, 'wiki_half0': 1.261, 'wiki_half1': 1.261}
WikiText (obs/exp): wiki_half0 member–frame 16/1.9, member–member 2/0.8; wiki_half1 member–frame 18/2.3, member–member 1/1.1

### group 4 — 27 members, shape 26, tier uncategorised
members: surprising, swimming_pool, playroom, canoe, discothque, playing_hockey, tickling, creating_art, dreaming, fencing, going_on_internet, going_outside_for_evening, going_see_film, going_to_play, going_to_zoo, having_friends_over, laughing_at_joke, playing_guitar, playing_harp, playing_poker, riding_horse, running_after_ball, seeing_band, seeing_people_play_game …
frame: UsedFor> fun; UsedFor> having_fun
density 1.0; support 27 (with Wiktionary 27); nulls global p=0.0099 z=53.9 (null mean 0.04), relation p=0.0099 z=8.3 (null mean 6.43), reciprocal p=0.0099 z=8.6 (null mean 6.51), strict p=0.0099 z=7.9 (null mean 8.39); BH q 0.0136; subsample recovery 1.0
category: best direct intelligent_agent_activity (0.11), best within 2 IsA-steps action (0.15), members with any category 0.37
member categories: surprising→–; swimming_pool→pond,pool,artificial_pond,lido; playroom→where_children_play; canoe→vehicle,boat,ship,user_powered_device; discothque→–; playing_hockey→playing_game,intelligent_agent_activity,playing_of_sports_event; tickling→form_of_torture,touching,pressing,sensory_event; creating_art→–; dreaming→–; fencing→play,fight,intelligent_agent_activity,olympic_sport
internal links among members 0 (configuration expectation 2.05); relative weight of member–frame links {'original': 1.199, 'wiki_half0': 1.213, 'wiki_half1': 1.213}
WikiText (obs/exp): wiki_half0 member–frame 4/1.5, member–member 2/0.5; wiki_half1 member–frame 3/1.5, member–member 0/0.4

### group 32 — 11 members, shape 26, tier partly_named
members: apartment_building, brick_row_house, brownstone, bungalow, condominium, cottage, ranch_house, rented_apartment, row_house, terraced_house, townhouse
frame: UsedFor> living_in; UsedFor> live_in
density 1.0; support 11 (with Wiktionary 11); nulls global p=0.0099 z=22.0 (null mean 0.0), relation p=0.0099 z=21.7 (null mean 0.14), reciprocal p=0.0099 z=21.8 (null mean 0.1), strict p=0.0099 z=19.3 (null mean 0.34); BH q 0.0136; subsample recovery 0.8
category: best direct house (0.45), best within 2 IsA-steps home (0.73), members with any category 0.91
member categories: apartment_building→building,modern_residence; brick_row_house→often_in_clusters_of_five; brownstone→home,real_estate,row_house,sandstone; bungalow→building,house,one_storeyed_house,small_house_or_home; condominium→home,dwelling,housing,where_people_live; cottage→home,house,small_home,small_house; ranch_house→house,where_farmers_live,where_rancher_lives; rented_apartment→–; row_house→house; terraced_house→row_house
internal links among members 5 (configuration expectation 0.03); relative weight of member–frame links {'original': 1.322, 'wiki_half0': 1.337, 'wiki_half1': 1.303}
WikiText (obs/exp): wiki_half0 member–frame 6/1.5, member–member 1/0.1; wiki_half1 member–frame 10/1.7, member–member 2/0.1

### group 203 — 10 members, shape 2, tier uncategorised
members: careful, strike_match, light_match, go_outdoors, get_matches, gather_kindling, rub_two_sticks_together, use_lighter, use_match, use_matches
frame: HasPrerequisite< light_fire; HasPrerequisite< start_fire; HasPrerequisite< start_flame_or_fire
density 0.833; support 10 (with Wiktionary 10); nulls global p=0.0099 z=18.5 (null mean 0.31), relation p=0.0099 z=19.7 (null mean 0.14), reciprocal p=0.0099 z=19.6 (null mean 0.18), strict p=0.0099 z=19.8 (null mean 0.12); BH q 0.0136; subsample recovery 0.8
category: best direct 0 (0.0), best within 2 IsA-steps 0 (0.0), members with any category 0.0
member categories: careful→–; strike_match→–; light_match→–; go_outdoors→–; get_matches→–; gather_kindling→–; rub_two_sticks_together→–; use_lighter→–; use_match→–; use_matches→–
internal links among members 4 (configuration expectation 0.02); relative weight of member–frame links {'original': 1.17, 'wiki_half0': 1.17, 'wiki_half1': 1.171}
WikiText (obs/exp): wiki_half0 member–frame 0/0.0, member–member 0/0.0; wiki_half1 member–frame 0/0.0, member–member 0/0.0

### group 377 — 10 members, shape 2, tier uncategorised
members: on_time, register, get_out_of_bed, enroll, matriculate, sign_up, get_dressed, enroll_at_school, go_to_college, get_on_school_bus
frame: HasPrerequisite< go_to_school; HasPrerequisite< attend_school; HasPrerequisite< attend_class
density 0.8; support 10 (with Wiktionary 10); nulls global p=0.0099 z=16.7 (null mean 0.37), relation p=0.0099 z=19.6 (null mean 0.2), reciprocal p=0.0099 z=18.7 (null mean 0.3), strict p=0.0099 z=18.0 (null mean 0.3); BH q 0.0136; subsample recovery 0.6
category: best direct join (0.1), best within 2 IsA-steps show (0.2), members with any category 0.4
member categories: on_time→–; register→show,play,mail,furnace; get_out_of_bed→–; enroll→register; matriculate→college_student,enroll; sign_up→join; get_dressed→–; enroll_at_school→–; go_to_college→–; get_on_school_bus→–
internal links among members 3 (configuration expectation 0.01); relative weight of member–frame links {'original': 1.122, 'wiki_half0': 1.122, 'wiki_half1': 1.123}
WikiText (obs/exp): wiki_half0 member–frame 0/0.1, member–member 0/0.2; wiki_half1 member–frame 0/0.1, member–member 1/0.2

### group 93 — 9 members, shape 2, tier uncategorised
members: stretch_muscles, put_on_shoes, dress_appropriately, go_to_park, stretch_first, put_on_jogging_clothes, put_on_jogging_suit, wear_good_shoes, wear_jogging_shoes
frame: HasPrerequisite< go_jogging; HasPrerequisite< go_for_jog
density 1.0; support 9 (with Wiktionary 9); nulls global p=0.0099 z=17.8 (null mean 0.12), relation p=0.0099 z=17.7 (null mean 0.14), reciprocal p=0.0099 z=17.9 (null mean 0.07), strict p=0.0099 z=17.7 (null mean 0.15); BH q 0.0136; subsample recovery 0.6
category: best direct 0 (0.0), best within 2 IsA-steps 0 (0.0), members with any category 0.0
member categories: stretch_muscles→–; put_on_shoes→–; dress_appropriately→–; go_to_park→–; stretch_first→–; put_on_jogging_clothes→–; put_on_jogging_suit→–; wear_good_shoes→–; wear_jogging_shoes→–
internal links among members 0 (configuration expectation 0.0); relative weight of member–frame links {'original': 1.083, 'wiki_half0': 1.084, 'wiki_half1': 1.084}
WikiText (obs/exp): wiki_half0 member–frame 0/0.0, member–member 0/0.0; wiki_half1 member–frame 0/0.0, member–member 0/0.0


## Coherent but resisting: members are categorised, but no category within 2 steps covers ≥33%

### group 1 — 50 members, shape 30, tier crosscutting
members: flat, stranger, bank, bookshop, sporting_goods_store, pub, cafe, bookstore, court, movie_theater, parking_lot, avenue, back_garden, dentist, steak_house, barbershop, graveyard, cinema, dental_office, buildings, diner, circular_route, city_hall, condominium …
frame: AtLocation> city; AtLocation> town
density 1.0; support 50 (with Wiktionary 50); nulls global p=0.0099 z=99.8 (null mean 0.11), relation p=0.0099 z=27.3 (null mean 3.04), reciprocal p=0.0099 z=27.0 (null mean 2.99), strict p=0.0099 z=19.3 (null mean 5.67); BH q 0.0136; subsample recovery 1.0
category: best direct restaurant (0.08), best within 2 IsA-steps building (0.24), members with any category 0.82
member categories: flat→box,plain,house,scenery; stranger→person,book,being,intruder; bank→reserve,array,cover,depository; bookshop→shop,fun_place_to_spend_time; sporting_goods_store→retail_store; pub→bar,building,place,another_word_for_bar; cafe→band,restaurant,modern_shelter_construction,restaurant_space; bookstore→shop,retail_store,facility,good_place_to_steal_books; court→building,room,government,residence; movie_theater→business,dark_place,entertainment_organization,commercial_service_establishment
internal links among members 7 (configuration expectation 2.53); relative weight of member–frame links {'original': 1.083, 'wiki_half0': 0.955, 'wiki_half1': 0.98}
WikiText (obs/exp): wiki_half0 member–frame 1425/929.4, member–member 736/430.9; wiki_half1 member–frame 1462/953.8, member–member 893/446.2

### group 2 — 39 members, shape 30, tier crosscutting
members: clutter, feet, printer, trash_can, lamp, cup_of_coffee, calculator, calendar_pad, card_case, telephone, chairs, clip, clock, correction_fluid, desk_tray, notebook, electric_pencil_sharpener, glue_stick, highlighter, highlighter_pen, keyboard, phone, staples, notepad …
frame: AtLocation> desk; AtLocation> office
density 1.0; support 39 (with Wiktionary 39); nulls global p=0.0099 z=78.0 (null mean 0.02), relation p=0.0099 z=15.6 (null mean 4.74), reciprocal p=0.0099 z=19.2 (null mean 4.15), strict p=0.0099 z=17.4 (null mean 4.18); BH q 0.0136; subsample recovery 1.0
category: best direct machine (0.1), best within 2 IsA-steps device (0.26), members with any category 0.77
member categories: clutter→fill,software,noise,mess; feet→–; printer→machine,device,peripheral,skilled_worker; trash_can→garbage_container; lamp→electrical_device,furniture,source_of_illumination; cup_of_coffee→pleasant_way_to_relax; calculator→expert,machine,electronic_device,noun; calendar_pad→–; card_case→container; telephone→electronic_equipment,telecommunication,communication_device,telephone_system
internal links among members 5 (configuration expectation 0.93); relative weight of member–frame links {'original': 1.193, 'wiki_half0': 1.182, 'wiki_half1': 1.202}
WikiText (obs/exp): wiki_half0 member–frame 65/82.2, member–member 30/45.4; wiki_half1 member–frame 46/85.4, member–member 33/47.6

### group 7 — 20 members, shape 30, tier crosscutting
members: black_hole, cold, moon, space_shuttle, asteroid, asteroids, space_station, planet, black_holes, comet, cosmic_dust, cosmic_rays, hydrogen, meteor, stars, planets, quasar, satellites, star, vaccuum
frame: AtLocation> space; AtLocation> outerspace
density 1.0; support 20 (with Wiktionary 20); nulls global p=0.0099 z=40.0 (null mean 0.0), relation p=0.0099 z=28.0 (null mean 0.46), reciprocal p=0.0099 z=30.9 (null mean 0.41), strict p=0.0099 z=39.5 (null mean 0.26); BH q 0.0136; subsample recovery 0.8
category: best direct astronomical_object (0.3), best within 2 IsA-steps astronomical_object (0.35), members with any category 0.9
member categories: black_hole→blackness,region,film,roller_coaster; cold→disease,sickness,adjective,temperature; moon→far_away,expose,single,place; space_shuttle→spacecraft,rocket,rocket_plane,fuel_powered_device; asteroid→celestial_body,astronomical_object,rocky_planetary_body,subplanetary_stellar_orbiter; asteroids→video_game,big_rocks_adrift_in_space,remnant_planet; space_station→satellite,manned_spacecraft; planet→count_noun,large_object,celestial_body,planemo; black_holes→in_space; comet→scrubbing_cleanser,astronomical_object,subplanetary_stellar_orbiter,dirty_iceball
internal links among members 5 (configuration expectation 0.3); relative weight of member–frame links {'original': 1.192, 'wiki_half0': 0.991, 'wiki_half1': 1.054}
WikiText (obs/exp): wiki_half0 member–frame 194/65.1, member–member 1003/132.7; wiki_half1 member–frame 179/65.3, member–member 956/126.3

### group 6 — 23 members, shape 30, tier crosscutting
members: seat, backdrop, balcony, balcony_railing, balcony_seat, seats, candy, catwalk, chairs, ticket_booth, costumes, curtain, curtains, makeup, movie_theater_seat, orchestra_seat, rehearsing_room, rows_of_seats, theater_box, stage_entrance, sticky_floors, theater_ticket, usher
frame: AtLocation> theater; AtLocation> theatre
density 1.0; support 23 (with Wiktionary 23); nulls global p=0.0099 z=46.0 (null mean 0.0), relation p=0.0099 z=27.5 (null mean 0.73), reciprocal p=0.0099 z=21.4 (null mean 0.93), strict p=0.0099 z=27.3 (null mean 0.83); BH q 0.0136; subsample recovery 1.0
category: best direct supply (0.09), best within 2 IsA-steps artifact (0.17), members with any category 0.65
member categories: seat→accommodate,chair,center,support; backdrop→curtain,scenery; balcony→artwork,structure,level_of_construction,fixed_structure_platform; balcony_railing→–; balcony_seat→above_other_seats; seats→baseball_stadium,in_cars; candy→sweet,food,junk_food,snack; catwalk→walk,platform,narrow_walkway; chairs→usually_on_floor,optimized_for_sitting; ticket_booth→where_obtain_ticket
internal links among members 5 (configuration expectation 0.22); relative weight of member–frame links {'original': 1.097, 'wiki_half0': 1.079, 'wiki_half1': 1.062}
WikiText (obs/exp): wiki_half0 member–frame 142/28.9, member–member 67/14.2; wiki_half1 member–frame 116/31.2, member–member 83/17.5

### group 5 — 24 members, shape 30, tier crosscutting
members: dollar, return_ticket, comb, car_keys, cash_coin, coin_purse, change, checkbook_holder, cheque_book_holder, condom, credit_card_wallet, dollar_bill, eyeglasses_case, glasses_case, key, key_case, keys, kleenex, lint, movie_ticket, penny, subway_pass, train_ticket, writing_instrument
frame: AtLocation> purse; AtLocation> pocket
density 1.0; support 24 (with Wiktionary 24); nulls global p=0.0099 z=48.0 (null mean 0.01), relation p=0.0099 z=20.4 (null mean 1.11), reciprocal p=0.0099 z=28.6 (null mean 0.72), strict p=0.0099 z=20.8 (null mean 1.17); BH q 0.0136; subsample recovery 1.0
category: best direct coin (0.12), best within 2 IsA-steps artifact (0.21), members with any category 0.67
member categories: dollar→money,currency,bill,coin; return_ticket→–; comb→groom,straighten,plate,tool; car_keys→–; cash_coin→always_less_dollar; coin_purse→small_bag_in,small_purse; change→action,dress,money,cash; checkbook_holder→–; cheque_book_holder→container; condom→commonly,contraceptive,contraceptive_device,disposable_object
internal links among members 7 (configuration expectation 0.72); relative weight of member–frame links {'original': 1.196, 'wiki_half0': 1.245, 'wiki_half1': 1.213}
WikiText (obs/exp): wiki_half0 member–frame 8/5.9, member–member 61/44.9; wiki_half1 member–frame 11/7.0, member–member 54/39.2

### group 8 — 23 members, shape 18, tier crosscutting
members: fair, texas, america, it's_natural_habitat, indiana, farm_yard, idaho, ohio, stew, barnyard, corral, county_fair, cow_barn, cow_pasture, cow_shed, cowshed, dairy_farm, farmer's_pasture, farmyard, feed_lot, milking_barn, slaughter_house, stall
frame: AtLocation< cow; AtLocation< heifer
density 1.0; support 23 (with Wiktionary 23); nulls global p=0.0099 z=26.0 (null mean 0.85), relation p=0.0099 z=12.4 (null mean 2.68), reciprocal p=0.0099 z=13.4 (null mean 2.86), strict p=0.0099 z=18.9 (null mean 1.33); BH q 0.0136; subsample recovery 0.8
category: best direct united_states (0.17), best within 2 IsA-steps unnatural_thing (0.26), members with any category 0.52
member categories: fair→join,exhibition,gathering; texas→country,southwest,united_states,united_states_of_america; america→country,continent,world,ship; it's_natural_habitat→–; indiana→united_states,state,midwest,administrative_region; farm_yard→–; idaho→united_states,state,administrative_region; ohio→united_states,state,midwest,administrative_region; stew→soup,cook,dish,resent; barnyard→yard
internal links among members 0 (configuration expectation 0.1); relative weight of member–frame links {'original': 1.057, 'wiki_half0': 1.1, 'wiki_half1': 1.1}
WikiText (obs/exp): wiki_half0 member–frame 4/3.3, member–member 152/73.4; wiki_half1 member–frame 2/4.0, member–member 165/74.0


## Earlier groups 18–20, located
