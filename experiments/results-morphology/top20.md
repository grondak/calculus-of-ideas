# Structural anomalies in ConceptNet (original weights + WikiText halves)

Visible ideas 52,863; core 25,383; candidate pairs 873,856; gap pairs 287,486 (lexical variants 6,304 and alias-explained 240,573 removed); null-significant gap pairs 112,150; fragmented neighbourhoods 1,323; groups 46 (36 unnamed).

Global similarity structure (3,000 sampled core ideas): real {"J>=0.1": 10651, "J>=0.1_unlinked": 9799, "J>=0.2": 2229, "J>=0.2_unlinked": 2087, "J>=0.3": 422, "J>=0.3_unlinked": 374}
- global null mean: J>=0.1 79.5, J>=0.1_unlinked 46.2, J>=0.2 0.3, J>=0.2_unlinked 0.3, J>=0.3 0.0, J>=0.3_unlinked 0.0
- relation null mean: J>=0.1 41.6, J>=0.1_unlinked 25.8, J>=0.2 0.3, J>=0.2_unlinked 0.3, J>=0.3 0.1, J>=0.3_unlinked 0.1
- reciprocal null mean: J>=0.1 30.4, J>=0.1_unlinked 30.4, J>=0.2 0.7, J>=0.2_unlinked 0.7, J>=0.3 0.1, J>=0.3_unlinked 0.1

## 1. missing_link: new_york — county_seat
degrees [358, 971], common neighbours 177, Jaccard 0.154, typed Jaccard 0.144, containment [0.494, 0.182]; P(linked | comparable) {'original': 0.964, 'wiki_half0': 0.968, 'wiki_half1': 0.968}; gap score 4.807
nulls: global p=0.0476 z=6.4; relation p=0.0476 z=4.9; reciprocal p=0.0476 z=24.6
WikiText: wiki_half0 1 obs / 0.78 exp; wiki_half1 0 obs / 1.11 exp → mixed
shared relation profile: <RelatedTo 177, RelatedTo> 177, <PartOf 18, IsA> 1, <AtLocation 1
shared neighbours (relation from a | from b): mcdonough (<RelatedTo,RelatedTo> | <RelatedTo,RelatedTo>); binghamton (<PartOf,RelatedTo> | <RelatedTo,RelatedTo>); schenectady (<PartOf,RelatedTo> | <RelatedTo,RelatedTo>); herkimer (<RelatedTo,RelatedTo> | <RelatedTo,RelatedTo>); malone (<RelatedTo,RelatedTo> | <RelatedTo,RelatedTo>); rensselaer (<RelatedTo,RelatedTo> | <RelatedTo,RelatedTo>); lewiston (<PartOf | <RelatedTo,RelatedTo>); niagara_county (<RelatedTo,RelatedTo> | <RelatedTo,RelatedTo>); laurens (<RelatedTo,RelatedTo> | <RelatedTo,RelatedTo>); chautauqua_county (<RelatedTo,RelatedTo> | <RelatedTo,RelatedTo>); seneca (<RelatedTo,RelatedTo> | <RelatedTo,RelatedTo>); new_city (<RelatedTo,RelatedTo> | <RelatedTo,RelatedTo>)
only new_york: state (<RelatedTo,IsA>); united_states (PartOf>); place (IsA>); ohio (<RelatedTo,RelatedTo>); united_states_of_america (<RelatedTo,RelatedTo>); lake (<AtLocation); root (<RelatedTo,RelatedTo>); ontario (<RelatedTo,RelatedTo>)
only county_seat: indiana (<RelatedTo,RelatedTo>); california (<RelatedTo,RelatedTo>); government (<RelatedTo,RelatedTo>); london (<RelatedTo,RelatedTo>); virginia (<RelatedTo,RelatedTo>); english (<RelatedTo,RelatedTo>); post (<RelatedTo,RelatedTo>); center (<RelatedTo,RelatedTo>)

## 2. missing_link: diminutive — given_name
degrees [169, 458], common neighbours 134, Jaccard 0.272, typed Jaccard 0.343, containment [0.793, 0.293]; P(linked | comparable) {'original': 0.955, 'wiki_half0': 0.958, 'wiki_half1': 0.958}; gap score 4.478
nulls: global p=0.0476 z=29.2; relation p=0.0476 z=34.4; reciprocal p=0.0476 z=43.9
WikiText: wiki_half0 0 obs / 0.0 exp; wiki_half1 1 obs / 0.0 exp → mixed
shared relation profile: <RelatedTo 134, RelatedTo> 134, <IsA 2
shared neighbours (relation from a | from b): roxy (<RelatedTo,RelatedTo> | <RelatedTo,RelatedTo>); lizzie (<RelatedTo,RelatedTo> | <RelatedTo,RelatedTo>); gabe (<RelatedTo,RelatedTo> | <RelatedTo,RelatedTo>); artie (<RelatedTo,RelatedTo> | <RelatedTo,RelatedTo>); reggie (<RelatedTo,RelatedTo> | <RelatedTo,RelatedTo>); gracie (<RelatedTo,RelatedTo> | <RelatedTo,RelatedTo>); trudy (<RelatedTo,RelatedTo> | <RelatedTo,RelatedTo>); suzy (<RelatedTo,RelatedTo> | <RelatedTo,RelatedTo>); jen (<RelatedTo,RelatedTo> | <RelatedTo,RelatedTo>); jeri (<RelatedTo,RelatedTo> | <RelatedTo,RelatedTo>); lenny (<RelatedTo,RelatedTo> | <RelatedTo,RelatedTo>); vinnie (<RelatedTo,RelatedTo> | <RelatedTo,RelatedTo>)
only diminutive: word (IsA>); small (<RelatedTo,RelatedTo>); cat (<RelatedTo,RelatedTo>); law (<RelatedTo,RelatedTo>); fan (<RelatedTo,RelatedTo>); positive (<RelatedTo,RelatedTo>); ash (<RelatedTo,RelatedTo>); diminish (<RelatedTo,RelatedTo>)
only given_name: name (IsA>); child (<RelatedTo,RelatedTo>); virginia (<IsA); beat (<IsA); surname (<SimilarTo,SimilarTo>); list (IsA>); young (<RelatedTo,RelatedTo>); jin (<RelatedTo,RelatedTo>)

## 3. missing_link: chemical_element — atomic_number
degrees [45, 84], common neighbours 36, Jaccard 0.387, typed Jaccard 0.066, containment [0.8, 0.429]; P(linked | comparable) {'original': 0.766, 'wiki_half0': 0.789, 'wiki_half1': 0.776}; gap score 2.096
nulls: global p=0.0476 z=32.8; relation p=0.0476 z=40.5; reciprocal p=0.0476 z=71.2
WikiText: wiki_half0 2 obs / 0.0 exp; wiki_half1 2 obs / 0.0 exp → mixed
shared relation profile: <RelatedTo 36, RelatedTo> 36, <IsA 30, <PartOf 1
shared neighbours (relation from a | from b): cadmium (<IsA | <RelatedTo,RelatedTo>); ununennium (<RelatedTo,RelatedTo> | <RelatedTo,RelatedTo>); lawrencium (<IsA | <RelatedTo,RelatedTo>); selenium (<IsA,RelatedTo> | <RelatedTo,RelatedTo>); zirconium (<IsA | <RelatedTo,RelatedTo>); ytterbium (<IsA,RelatedTo> | <RelatedTo,RelatedTo>); yttrium (<IsA | <RelatedTo,RelatedTo>); argon (<IsA | <RelatedTo,RelatedTo>); ruthenium (<IsA | <RelatedTo,RelatedTo>); beryllium (<IsA,RelatedTo> | <RelatedTo,RelatedTo>); xenon (<IsA | <RelatedTo,RelatedTo>); germanium (<IsA | <RelatedTo,RelatedTo>)
only chemical_element: element (<Synonym,Synonym>); substance (IsA>); chemical (<RelatedTo,RelatedTo>); reaction (<RelatedTo,RelatedTo>); decompose (<RelatedTo,RelatedTo>); noble_gas (<IsA); plutonium (<IsA); iupac (<RelatedTo,RelatedTo>)
only atomic_number: number (IsA>); iron (<RelatedTo,RelatedTo>); silver (<RelatedTo,RelatedTo>); isotope (<RelatedTo,RelatedTo>); aluminum (<RelatedTo,RelatedTo>); periodic_table (<RelatedTo,RelatedTo>); nickel (<RelatedTo,RelatedTo>); aluminium (<RelatedTo,RelatedTo>)

## 4. missing_link: coach — player
degrees [79, 166], common neighbours 34, Jaccard 0.161, typed Jaccard 0.156, containment [0.43, 0.205]; P(linked | comparable) {'original': 0.733, 'wiki_half0': 0.759, 'wiki_half1': 0.765}; gap score 1.905
nulls: global p=0.0476 z=6.1; relation p=0.0476 z=11.1; reciprocal p=0.0476 z=19.8
WikiText: wiki_half0 76 obs / 27.34 exp; wiki_half1 95 obs / 30.37 exp → attested
shared relation profile: <RelatedTo 33, RelatedTo> 33, <PartOf 1, PartOf> 1, AtLocation> 1, IsA> 1
shared neighbours (relation from a | from b): glover (<RelatedTo,RelatedTo> | <RelatedTo,RelatedTo>); black_cat (<RelatedTo,RelatedTo> | <RelatedTo,RelatedTo>); bantam (<RelatedTo,RelatedTo> | <RelatedTo,RelatedTo>); hornet (<RelatedTo,RelatedTo> | <RelatedTo,RelatedTo>); sky_blue (<RelatedTo,RelatedTo> | <RelatedTo,RelatedTo>); trotter (<RelatedTo,RelatedTo> | <RelatedTo,RelatedTo>); seagull (<RelatedTo,RelatedTo> | <RelatedTo,RelatedTo>); magpie (<RelatedTo,RelatedTo> | <RelatedTo,RelatedTo>); potter (<RelatedTo,RelatedTo> | <RelatedTo,RelatedTo>); gunner (<RelatedTo,RelatedTo> | <RelatedTo,RelatedTo>); robin (<RelatedTo,RelatedTo> | <RelatedTo,RelatedTo>); claret (<RelatedTo,RelatedTo> | <RelatedTo,RelatedTo>)
only coach: car (<RelatedTo,RelatedTo>); business (<RelatedTo,RelatedTo>); worker (IsA>); vehicle (IsA>); drive (MannerOf>); train (<Synonym,Synonym>); tool (<RelatedTo,RelatedTo>); leader (<RelatedTo,RelatedTo>)
only player: band (<RelatedTo,RelatedTo>); game (<RelatedTo,RelatedTo>); home (<RelatedTo,RelatedTo>); break (<RelatedTo,RelatedTo>); war (<RelatedTo,RelatedTo>); record (<RelatedTo,RelatedTo>); call (<RelatedTo,RelatedTo>); hole (<RelatedTo,RelatedTo>)

## 5. missing_link: shelf — table
degrees [89, 208], common neighbours 28, Jaccard 0.104, typed Jaccard 0.069, containment [0.315, 0.135]; P(linked | comparable) {'original': 0.725, 'wiki_half0': 0.705, 'wiki_half1': 0.7}; gap score 1.737
nulls: global p=0.0476 z=9.0; relation p=0.0476 z=5.6; reciprocal p=0.0476 z=7.7
WikiText: wiki_half0 1 obs / 0.17 exp; wiki_half1 0 obs / 0.19 exp → mixed
shared relation profile: <AtLocation 19, RelatedTo> 7, AtLocation> 6, <RelatedTo 6, UsedFor> 1, <IsA 1
shared neighbours (relation from a | from b): plates (<AtLocation | <AtLocation); vase (<AtLocation | <AtLocation); keys (<AtLocation | <AtLocation); dishes (<AtLocation | <AtLocation); dictionary (<AtLocation | <AtLocation); gum (<AtLocation | <AtLocation); rigid (<RelatedTo,RelatedTo> | HasProperty>); lamp (<AtLocation | <AtLocation); candle (<AtLocation | <AtLocation); cupboard (AtLocation> | <RelatedTo,RelatedTo>); bedroom (AtLocation> | AtLocation>); books (<AtLocation,UsedFor> | <AtLocation)
only shelf: support (<RelatedTo,IsA>); structure (<RelatedTo,RelatedTo>); box (<RelatedTo,RelatedTo>); store (<RelatedTo,RelatedTo>); product (<AtLocation); wall (<RelatedTo,AtLocation>); cabinet (<RelatedTo,PartOf>); flower (<AtLocation)
only table: place (<RelatedTo,RelatedTo>); building (AtLocation>); point (<RelatedTo,RelatedTo>); cut (<RelatedTo,RelatedTo>); game (<AtLocation); space (<AtLocation); bar (<RelatedTo,RelatedTo>); surface (<RelatedTo,RelatedTo>)

## 6. missing_link: silk — cotton
degrees [98, 108], common neighbours 21, Jaccard 0.114, typed Jaccard 0.091, containment [0.214, 0.194]; P(linked | comparable) {'original': 0.652, 'wiki_half0': 0.647, 'wiki_half1': 0.633}; gap score 1.447
nulls: global p=0.0476 z=3.2; relation p=0.0476 z=3.3; reciprocal p=0.0476 z=7.1
WikiText: wiki_half0 21 obs / 0.48 exp; wiki_half1 20 obs / 0.34 exp → attested
shared relation profile: <RelatedTo 20, RelatedTo> 19, IsA> 2, HasProperty> 1, ReceivesAction> 1, AtLocation> 1
shared neighbours (relation from a | from b): georgette (<RelatedTo,RelatedTo> | <RelatedTo,RelatedTo>); dyed (ReceivesAction> | ReceivesAction>); coburg (<RelatedTo,RelatedTo> | <RelatedTo,RelatedTo>); sari (<RelatedTo,RelatedTo> | <RelatedTo,RelatedTo>); shirts (UsedFor> | <RelatedTo,RelatedTo>); valencia (<RelatedTo,RelatedTo> | <RelatedTo,RelatedTo>); batting (<RelatedTo,RelatedTo> | <RelatedTo,RelatedTo>); underwear (<RelatedTo,RelatedTo> | <MadeOf,RelatedTo>); fiber (<RelatedTo,RelatedTo> | <RelatedTo,RelatedTo>); shirt (AtLocation> | <RelatedTo,RelatedTo>); organic (HasProperty> | <RelatedTo,RelatedTo>); ferret (<RelatedTo,RelatedTo> | <RelatedTo,RelatedTo>)
only silk: water (<RelatedTo,RelatedTo>); book (IsA>); make (<RelatedTo,RelatedTo>); condition (<RelatedTo,RelatedTo>); single (<RelatedTo,RelatedTo>); china (<RelatedTo,AtLocation>); product (<RelatedTo,RelatedTo>); love (<RelatedTo,RelatedTo>)
only cotton: plant (<RelatedTo,IsA>); light (<RelatedTo,RelatedTo>); field (<RelatedTo,AtLocation>); ball (<RelatedTo,RelatedTo>); georgia (<RelatedTo,AtLocation>); fly (<RelatedTo,RelatedTo>); north_carolina (AtLocation>); white (<RelatedTo,RelatedTo>)

## 7. missing_link: zoo — mammal
degrees [67, 150], common neighbours 15, Jaccard 0.074, typed Jaccard 0.0, containment [0.224, 0.1]; P(linked | comparable) {'original': 0.597, 'wiki_half0': 0.603, 'wiki_half1': 0.607}; gap score 1.311
nulls: global p=0.0476 z=2.5; relation p=0.0476 z=4.5; reciprocal p=0.0476 z=5.6
WikiText: wiki_half0 0 obs / 0.1 exp; wiki_half1 0 obs / 0.06 exp → under
shared relation profile: <AtLocation 15, <IsA 12, RelatedTo> 7, <RelatedTo 2, IsA> 1, <HasProperty 1
shared neighbours (relation from a | from b): polar_bear (<AtLocation | <IsA); rhinoceros (<AtLocation | <IsA); chimpanzee (<AtLocation | <IsA); giraffe (<AtLocation | <IsA); zebra (<AtLocation | <IsA); elephant (<AtLocation | <IsA,RelatedTo>); gazelle (<AtLocation | <IsA); tiger (<AtLocation | <IsA,RelatedTo>); lion (<AtLocation | <IsA); weasel (<AtLocation | <IsA,RelatedTo>); beaver (<AtLocation | <IsA); cat (<AtLocation | <HasProperty,RelatedTo>)
only zoo: person (<AtLocation); people (<AtLocation); place (<RelatedTo,RelatedTo>); food (<AtLocation); tree (<AtLocation); home (<RelatedTo,RelatedTo>); train (<AtLocation); live (<RelatedTo,RelatedTo>)
only mammal: play (CapableOf>); bird (<RelatedTo,RelatedTo>); class (<RelatedTo,RelatedTo>); dog (<IsA,RelatedTo>); eye (<AtLocation); bear (<IsA,RelatedTo>); hair (<PartOf,RelatedTo>); bone (<RelatedTo,RelatedTo>)

## 8. missing_link: play_music — orchestra
degrees [27, 69], common neighbours 12, Jaccard 0.143, typed Jaccard 0.0, containment [0.444, 0.174]; P(linked | comparable) {'original': 0.597, 'wiki_half0': 0.606, 'wiki_half1': 0.572}; gap score 1.224
nulls: global p=0.0476 z=23.7; relation p=0.0476 z=23.4; reciprocal p=0.0476 z=15.6
WikiText: wiki_half0 0 obs / 0.03 exp; wiki_half1 0 obs / 0.03 exp → under
shared relation profile: <UsedFor 11, <AtLocation 10, RelatedTo> 3, <RelatedTo 2, <CapableOf 1
shared neighbours (relation from a | from b): bassoon (<UsedFor | <AtLocation); piccolo (<UsedFor | <AtLocation); tuba (<UsedFor | <AtLocation); trombone (<UsedFor | <AtLocation); clarinet (<UsedFor | <AtLocation); woodwind (<UsedFor | <RelatedTo,RelatedTo>); cornet (<UsedFor | <AtLocation); violin (<UsedFor | <AtLocation); triangle (<UsedFor | <AtLocation); viola (<UsedFor | <AtLocation); trumpet (<UsedFor | <AtLocation,RelatedTo>); band (<CapableOf | <RelatedTo,RelatedTo>)
only play_music: dance (<HasPrerequisite); organ (<UsedFor); radio (<CapableOf); entertaining (<HasSubevent); comb (<UsedFor); entertain (<HasPrerequisite); keyboard (<UsedFor); bugle (<UsedFor)
only orchestra: music (<RelatedTo,RelatedTo>); play (<RelatedTo,RelatedTo>); group (<RelatedTo,RelatedTo>); space (<RelatedTo,RelatedTo>); area (<RelatedTo,RelatedTo>); instrument (<AtLocation,RelatedTo>); stage (<RelatedTo,RelatedTo>); musical (<RelatedTo,RelatedTo>)

## 9. nested: s.a — company
degrees [12, 464], common neighbours 12, Jaccard 0.026, typed Jaccard 0.0, containment [1.0, 0.026]; P(linked | comparable) {'original': 0.299, 'wiki_half0': 0.32, 'wiki_half1': 0.316}; gap score 0.513; nested score 0.974
nulls: global p=0.0476 z=15.5; relation p=0.0476 z=23.8; reciprocal p=0.0476 z=24.0
WikiText: wiki_half0 2 obs / 2.97 exp; wiki_half1 2 obs / 2.4 exp → under
shared relation profile: <InstanceOf 12, <IsA 12
shared neighbours (relation from a | from b): wenger (<InstanceOf | <IsA); citroën (<InstanceOf | <IsA); chanel (<InstanceOf | <IsA); cora (<InstanceOf | <IsA); zara (<InstanceOf | <IsA); renault (<InstanceOf | <IsA); nos (<InstanceOf | <IsA); pirelli (<InstanceOf | <IsA); ferrari (<InstanceOf | <IsA); dia (<InstanceOf | <IsA); vale (<InstanceOf | <IsA); seat (<InstanceOf | <IsA)
only s.a: 
only company: person (<Desires); city (AtLocation>); people (<RelatedTo,RelatedTo>); country (AtLocation>); body (<RelatedTo,RelatedTo>); place (<RelatedTo,RelatedTo>); building (<RelatedTo,RelatedTo>); work (<RelatedTo,RelatedTo>)

## 10. nested: blisters — exercise
degrees [10, 166], common neighbours 7, Jaccard 0.041, typed Jaccard 0.007, containment [0.7, 0.042]; P(linked | comparable) {'original': 0.265, 'wiki_half0': 0.288, 'wiki_half1': 0.28}; gap score 0.445; nested score 0.685
nulls: global p=0.0476 z=11.3; relation p=0.0476 z=11.0; reciprocal p=0.0476 z=7.1
WikiText: wiki_half0 0 obs / 0.02 exp; wiki_half1 0 obs / 0.03 exp → under
shared relation profile: <Causes 6, RelatedTo> 3, <UsedFor 3, <RelatedTo 2, <IsA 2
shared neighbours (relation from a | from b): hiking (<Causes | <UsedFor); jogging (<Causes | <IsA,RelatedTo>); climbing (<Causes | <UsedFor); dancing (<Causes | <UsedFor); walking (<Causes | <IsA); working (<Causes | <RelatedTo,RelatedTo>); burn (<RelatedTo,RelatedTo> | <RelatedTo,RelatedTo>)
only blisters: person (<NotDesires); shoes (<Causes); blister (<RelatedTo)
only exercise: action (<Synonym,IsA>); body (<RelatedTo,RelatedTo>); work (<Synonym,Synonym>); move (Entails>); run (<RelatedTo,HasPrerequisite>); event (IsA>); set (<IsA,RelatedTo>); activity (<RelatedTo,RelatedTo>)

## 11. nested: minor_key — root
degrees [8, 134], common neighbours 7, Jaccard 0.052, typed Jaccard 0.054, containment [0.875, 0.052]; P(linked | comparable) {'original': 0.2, 'wiki_half0': 0.207, 'wiki_half1': 0.208}; gap score 0.321; nested score 0.706
nulls: global p=0.0476 z=3.6; relation p=0.0476 z=4.6; reciprocal p=0.0476 z=8.7
WikiText: wiki_half0 0 obs / 0.02 exp; wiki_half1 0 obs / 0.02 exp → under
shared relation profile: <RelatedTo 7, RelatedTo> 7
shared neighbours (relation from a | from b): f_minor (<RelatedTo,RelatedTo> | <RelatedTo,RelatedTo>); d_minor (<RelatedTo,RelatedTo> | <RelatedTo,RelatedTo>); b_minor (<RelatedTo,RelatedTo> | <RelatedTo,RelatedTo>); c_minor (<RelatedTo,RelatedTo> | <RelatedTo,RelatedTo>); g_minor (<RelatedTo,RelatedTo> | <RelatedTo,RelatedTo>); e_minor (<RelatedTo,RelatedTo> | <RelatedTo,RelatedTo>); minor (<RelatedTo,RelatedTo> | <RelatedTo,RelatedTo>)
only minor_key: key (<RelatedTo,IsA>)
only root: water (<RelatedTo,RelatedTo>); plant (<RelatedTo,MannerOf>); new_york (<RelatedTo,RelatedTo>); software (IsA>); part (<RelatedTo,RelatedTo>); tree (<RelatedTo,AtLocation>); number (<RelatedTo,IsA>); power (<RelatedTo,RelatedTo>)

## 12. nested: classical_greek — letter
degrees [13, 192], common neighbours 10, Jaccard 0.051, typed Jaccard 0.006, containment [0.769, 0.052]; P(linked | comparable) {'original': 0.254, 'wiki_half0': 0.311, 'wiki_half1': 0.303}; gap score 0.423; nested score 0.632
nulls: global p=0.0476 z=9.8; relation p=0.0476 z=10.7; reciprocal p=0.0476 z=17.4
WikiText: wiki_half0 0 obs / 0.08 exp; wiki_half1 0 obs / 0.16 exp → under
shared relation profile: <RelatedTo 10, <IsA 10, RelatedTo> 10
shared neighbours (relation from a | from b): omicron (<RelatedTo,RelatedTo> | <IsA); upsilon (<RelatedTo,RelatedTo> | <IsA); psi (<RelatedTo,RelatedTo> | <IsA); rho (<RelatedTo,RelatedTo> | <IsA); sigma (<RelatedTo,RelatedTo> | <IsA); pi (<RelatedTo,RelatedTo> | <IsA); omega (<RelatedTo,RelatedTo> | <IsA,RelatedTo>); tau (<RelatedTo,RelatedTo> | <IsA); xi (<RelatedTo,RelatedTo> | <IsA); chi (<RelatedTo,RelatedTo> | <IsA,RelatedTo>)
only classical_greek: ancient_greek (<RelatedTo,RelatedTo>); ionic (<Synonym,Synonym>); modern_greek (<RelatedTo,RelatedTo>)
only letter: line (<PartOf,RelatedTo>); point (<RelatedTo,RelatedTo>); part (<RelatedTo,RelatedTo>); number (<Antonym,Antonym>); unit (<RelatedTo,RelatedTo>); office (<RelatedTo,RelatedTo>); capital (<RelatedTo,RelatedTo>); paper (<RelatedTo,MadeOf>)

## 13. nested: austro_hungarian — europe
degrees [9, 169], common neighbours 8, Jaccard 0.047, typed Jaccard 0.02, containment [0.889, 0.047]; P(linked | comparable) {'original': 0.205, 'wiki_half0': 0.275, 'wiki_half1': 0.253}; gap score 0.33; nested score 0.711
nulls: global p=0.0476 z=15.2; relation p=0.0476 z=15.0; reciprocal p=0.0476 z=15.3
WikiText: wiki_half0 0 obs / 3.37 exp; wiki_half1 1 obs / 3.01 exp → under
shared relation profile: <RelatedTo 8, RelatedTo> 8, <PartOf 5, <IsA 1
shared neighbours (relation from a | from b): austria_hungary (<RelatedTo,RelatedTo> | <PartOf); slovakia (<RelatedTo,RelatedTo> | <PartOf); slovenia (<RelatedTo,RelatedTo> | <RelatedTo,RelatedTo>); hungary (<RelatedTo,RelatedTo> | <PartOf,RelatedTo>); central_europe (<RelatedTo,RelatedTo> | <IsA,RelatedTo>); czech_republic (<RelatedTo,RelatedTo> | <PartOf); austria (<RelatedTo,RelatedTo> | <PartOf); croatia (<RelatedTo,RelatedTo> | <RelatedTo,RelatedTo>)
only austro_hungarian: u_boat (<RelatedTo,RelatedTo>)
only europe: england (<PartOf); country (<AtLocation); capital (<AtLocation); earth (PartOf>); france (<PartOf); germany (<PartOf); magazine (IsA>); university (<RelatedTo,RelatedTo>)

## 14. hole around nebraska
degree 168, neighbourhood component sizes [64, 4, 2, 2, 2, 1], fragmentation 0.617, score 51.52 by weights {'original': 51.77, 'wiki_half0': 53.85, 'wiki_half1': 53.97}; cross pairs 100, null-significant 87
WikiText cross-cluster co-occurrence: wiki_half0 52 obs / 53.9 exp; wiki_half1 49 obs / 53.0 exp → under
cluster X: state (IsA>); united_states (PartOf>); south_dakota (<RelatedTo,RelatedTo>); union (<RelatedTo,RelatedTo>); washington_county (<RelatedTo,RelatedTo>); grant (<RelatedTo,RelatedTo>); franklin_county (<RelatedTo,RelatedTo>); jefferson_county (<RelatedTo,RelatedTo>); aurora (<RelatedTo,RelatedTo>); oxford (<RelatedTo,RelatedTo>); franklin (<RelatedTo,RelatedTo>); smithfield (<RelatedTo,RelatedTo>)
cluster Y: wayne_county (<RelatedTo,RelatedTo>); ashland (<RelatedTo,RelatedTo>); walworth (<RelatedTo,RelatedTo>); wayne (<RelatedTo,RelatedTo>)
ideas outside the neighbourhood touching both: hagerstown, corydon, fairfield, huron, greenville, coldwater, milton, detroit, richmond, monticello, williamsburg, clark_county
strongest missing cross pairs (common nbrs, J, excess surprisal): franklin–ashland (21, 0.375, 1.582); bridgeport–ashland (20, 0.417, 1.58); jefferson_county–ashland (19, 0.275, 1.473); washington_county–ashland (18, 0.214, 1.378); united_states–ashland (25, 0.054, 1.343); jefferson_county–wayne_county (17, 0.23, 1.318)

## 15. hole around coffee
degree 56, neighbourhood component sizes [36, 5, 1, 1, 1, 1], fragmentation 0.333, score 28.32 by weights {'original': 29.11, 'wiki_half0': 30.05, 'wiki_half1': 30.46}; cross pairs 125, null-significant 0
WikiText cross-cluster co-occurrence: wiki_half0 709 obs / 1997.9 exp; wiki_half1 709 obs / 1971.4 exp → under
cluster X: person (<Desires); water (<AtLocation); plant (<RelatedTo,RelatedTo>); tree (IsA>); ground (<RelatedTo,RelatedTo>); liquid (IsA>); walk (<RelatedTo,RelatedTo>); drink (<RelatedTo,RelatedTo>); container (AtLocation>); meeting (AtLocation>); hot (HasProperty>); sugar (<AtLocation,RelatedTo>)
cluster Y: work (AtLocation>); office (AtLocation>); break (<RelatedTo,RelatedTo>); morning (<RelatedTo,RelatedTo>); begin_work (<HasFirstSubevent)
ideas outside the neighbourhood touching both: more_money, school_building, day_off, spelt, placebo, employees, works, paperwork, commuter, minutes, postmaster, backstory
strongest missing cross pairs (common nbrs, J, excess surprisal): person–work (63, 0.026, 2.525); person–office (43, 0.019, 1.975); person–break (21, 0.009, 1.132); walk–work (14, 0.025, 0.895); meeting–office (12, 0.032, 0.769); water–break (13, 0.018, 0.763)

## 16. hole around web
degree 50, neighbourhood component sizes [22, 7, 1, 1, 1, 1], fragmentation 0.542, score 25.33 by weights {'original': 26.29, 'wiki_half0': 27.13, 'wiki_half1': 27.84}; cross pairs 154, null-significant 0
WikiText cross-cluster co-occurrence: wiki_half0 416 obs / 1047.0 exp; wiki_half1 388 obs / 1010.9 exp → under
cluster X: home (<RelatedTo,RelatedTo>); fabric (IsA>); shaft (<RelatedTo,RelatedTo>); silk (<RelatedTo,RelatedTo>); network (<Synonym,Synonym>); tissue (<RelatedTo,RelatedTo>); net (<Synonym,Synonym>); internet (<RelatedTo,RelatedTo>); feather (<RelatedTo,RelatedTo>); carriage (<RelatedTo,RelatedTo>); site (<RelatedTo,RelatedTo>); trap (IsA>)
cluster Y: band (<RelatedTo,RelatedTo>); head (<RelatedTo,RelatedTo>); set (<RelatedTo,RelatedTo>); object (IsA>); foot (<RelatedTo,RelatedTo>); chain (<RelatedTo,RelatedTo>); hood (<RelatedTo,RelatedTo>)
ideas outside the neighbourhood touching both: pillows, broadband, baiting, sari, ligament, alarm_clock, headliner, hydration, kangaroo, harpoon, isthmus, elastic
strongest missing cross pairs (common nbrs, J, excess surprisal): home–set (16, 0.031, 0.907); shaft–head (16, 0.041, 0.901); home–object (15, 0.031, 0.88); home–band (11, 0.018, 0.654); home–head (11, 0.02, 0.646); shaft–foot (11, 0.044, 0.641)

## 17. hole around transformation
degree 66, neighbourhood component sizes [32, 7, 2, 1, 1, 1], fragmentation 0.492, score 24.81 by weights {'original': 25.83, 'wiki_half0': 26.99, 'wiki_half1': 26.83}; cross pairs 175, null-significant 0
WikiText cross-cluster co-occurrence: wiki_half0 1242 obs / 1674.2 exp; wiki_half1 1216 obs / 1645.0 exp → under
cluster X: change (<RelatedTo,IsA>); value (<RelatedTo,RelatedTo>); function (<RelatedTo,RelatedTo>); appearance (<RelatedTo,RelatedTo>); expression (<RelatedTo,RelatedTo>); transfer (<RelatedTo,RelatedTo>); convert (<RelatedTo,RelatedTo>); translation (<Synonym,Synonym>); better (<RelatedTo,RelatedTo>); reaction (<RelatedTo,RelatedTo>); reduction (<RelatedTo,RelatedTo>); shift (<Synonym,Synonym>)
cluster Y: position (<RelatedTo,RelatedTo>); space (<RelatedTo,RelatedTo>); character (<RelatedTo,RelatedTo>); rule (<RelatedTo,RelatedTo>); direction (<RelatedTo,RelatedTo>); sentence (<RelatedTo,RelatedTo>); coordinate (<RelatedTo,RelatedTo>)
ideas outside the neighbourhood touching both: coordinates, positional, lex, self_improvement, persona, alternate_universe, classicism, saying, slider, veer, versatile, back_out
strongest missing cross pairs (common nbrs, J, excess surprisal): change–position (18, 0.025, 1.057); change–space (17, 0.025, 0.984); function–position (12, 0.024, 0.807); change–direction (15, 0.026, 0.765); value–position (12, 0.023, 0.625); change–character (11, 0.018, 0.589)

## 18. unnamed group (9 ideas)
gap density 0.778, internal link density 0.0, score 17.13, named by none
members: swimming, surfing, playing, skating, going_to_play, playing_cards, skiing, dancing, singing
frame (neighbour, members touching it, relations): having_fun 9 [UsedFor>×5, Causes>×4, <HasSubevent×1]; fun 9 [UsedFor>×7, Causes>×2, <RelatedTo×1]; pleasure 8 [UsedFor>×7, HasSubevent>×1]; enjoyment 8 [UsedFor>×5, Causes>×3]; entertainment 7 [UsedFor>×6, Causes>×1]; activity 7 [IsA>×4, <RelatedTo×2, RelatedTo>×2]; exercise 6 [UsedFor>×6]

## 19. unnamed group (4 ideas)
gap density 0.833, internal link density 0.0, score 3.48, named by none
members: writing, classroom, desktop, backpack
frame (neighbour, members touching it, relations): pen 4 [<AtLocation×3, <UsedFor×1, HasPrerequisite>×1]; pencils 4 [<AtLocation×3, <RelatedTo×1, RelatedTo>×1]; computer 4 [<AtLocation×3, <UsedFor×1, IsA>×1]; books 4 [<AtLocation×3, <RelatedTo×1, RelatedTo>×1]; pencil 4 [<AtLocation×3, <RelatedTo×1, RelatedTo>×1]; notebook 4 [<AtLocation×3, <UsedFor×1]; school 3 [<AtLocation×2, <RelatedTo×1, RelatedTo>×1]; paper 3 [<AtLocation×2, <RelatedTo×1, HasPrerequisite>×1]; book 3 [<AtLocation×2, <RelatedTo×1, RelatedTo>×1]; desk 3 [<RelatedTo×3, RelatedTo>×3]

## 20. unnamed group (4 ideas)
gap density 0.833, internal link density 0.0, score 3.15, named by none
members: chair, apartment, basement, dresser
frame (neighbour, members touching it, relations): human 3 [<AtLocation×3]; home 3 [AtLocation>×2, <RelatedTo×1, RelatedTo>×1]; bed 3 [<AtLocation×2, <Antonym×1, Antonym>×1]; cat 3 [<AtLocation×3]; table 3 [<Antonym×1, Antonym>×1, <AtLocation×1]; building 3 [AtLocation>×2, <RelatedTo×1, IsA>×1]; bedroom 3 [AtLocation>×2, <AtLocation×1, RelatedTo>×1]; room 3 [<RelatedTo×2, AtLocation>×1, <AtLocation×1]; house 3 [<DistinctFrom×1, DistinctFrom>×1, <HasA×1]; kitchen 3 [<RelatedTo×2, AtLocation>×1, <AtLocation×1]
