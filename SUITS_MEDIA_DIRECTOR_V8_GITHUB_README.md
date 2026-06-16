# 🎬 $uits Media Director v8

> **Boundary:** Fictional GTA/FiveM / machinima media analysis.  
> All “predation,” “kill,” “prey,” “tactics,” and “strategy” labels are **editorial media-analysis tags**, not real-world conduct or instruction.

`$uits Media Director v8` is a local-first AI/ML-assisted media director for GTA/FiveM role-play footage. It scans video folders, scans music folders, builds cue sheets, scores gameplay clips against music sections, renders 29-second social edits and full-track cinematic edits, and produces metadata for website galleries, social media packs, training datasets, and human review.

The project treats the song as the spine of the edit:

```text
video evidence
+ audio/music structure
+ beat/drop timing
+ optional server truth logs
+ OCR/HUD clues
+ player/weapon labels
+ human feedback
+ Sun Tzu / Janus / UQEBM / humour lenses
= trainable cinematic intelligence
```

---

## ✨ Core idea

The system does not merely ask:

> “What clip looks cool?”

It asks:

```text
What happened?
Why did it happen?
What behaviour created vulnerability?
Where does the music want the moment?
Does the lyric create drama, irony, sarcasm, wit, or humour?
Should this become a 29s teaser, a full-track edit, a website card, or training data?
```

---

## 🧭 Project map

| Icon | Layer | Purpose |
|---|---|---|
| 🎬 | Media scanner | Finds videos, durations, formats, and candidate assets |
| 🎵 | Music scanner | Finds music tracks, durations, and song profiles |
| 🥁 | Beat/cue engine | Splits music into intro, build, impact, chorus/chain, aftermath, finale |
| 🔥 | Kill auto-tune | Places high-impact kill candidates on drops, choruses, and final hits |
| 🩸 | Wounding auto-tune | Places hits/survivals in build-ups and rising sections |
| 🪽 | Winging auto-tune | Places disruption, broken routes, and formation breaks in tension sections |
| 😂 | Comedy auto-tune | Places panic, poach, absurd motion, and lyric irony on breaks or punchlines |
| 🧠 | Tactical auto-tune | Finds clean angles, low waste motion, and pre-shot setup |
| 🏰 | Strategic auto-tune | Finds team pressure, territory control, aftermath, and scene-state change |
| 🌀 | Odd auto-tune | Finds weird geometry, strange falls, rare outcomes, and odd survivals |
| 🐑 | Prey review | Classifies the behaviour that made a player vulnerable |
| 🦁 | Predator pressure | Classifies the pressure pattern applied to the scene |
| ☯️ | Sun Tzu lens | Timing, terrain, weak points, manoeuvre, foreknowledge |
| 🪞 | Janus lens | Attacker view, defender view, team view, aftermath view |
| 💡 | Humour lens | Irony, sarcasm, wit, lateral punchlines, consequence jokes |
| 🗃️ | Evidence storage | JSON, CSV, HTML reports, future SQLite/Neo4j training data |
| 🌐 | Publishing | Website galleries, player packs, .org pages, social media outputs |

---

## 🧬 Evidence hierarchy

The system should preserve truth levels instead of pretending every detection is equal.

```text
server_confirmed
> client_confirmed
> manual_confirmed
> OCR_confirmed
> video_strong
> video_inferred
> filename_guess
```

Example:

```json
{
  "event_type": "kill_candidate",
  "truth_level": "video_inferred",
  "server_confirmation": null,
  "video_confidence": 0.76,
  "music_alignment": "chorus_drop",
  "human_review": "pending"
}
```

When server logs become available, the same event can be upgraded:

```json
{
  "event_type": "player_killed",
  "truth_level": "server_confirmed",
  "video_confidence": 0.76,
  "server_confidence": 1.0,
  "alignment_error_s": 0.18
}
```

---

## 🐑 Prey classification

Prey classification is not an identity. It is a temporary behaviour state.

The key review question is:

> **What behaviour made this player become prey?**

| Icon | Prey type | Behaviour that led to it |
|---|---|---|
| 🐑 | Exposed prey | stayed visible too long / no cover |
| 🐐 | Isolated prey | split from group / late regroup |
| 🐇 | Panicked prey | erratic route / reactive movement |
| 🩸 | Wounded prey | previously damaged, now finishable |
| 🪽 | Winged prey | aim, path, vehicle, or formation disrupted |
| 🐢 | Shelled prey | defensive but static |
| 🐃 | Counter-threat prey | dangerous but overcommitted |
| 🐓 | Comedic prey | mistake creates clip value |
| 🚗 | Route prey | chased into predictable path |
| 🎯 | Tunnel prey | focused forward, blind to side pressure |
| 🔄 | Reload prey | reload/ammo transition exposed |
| 🧲 | Baited prey | accepted lure or false opportunity |
| 🕳️ | Trap prey | entered bad geometry or dead zone |

Behaviour labels:

```text
overextended
split_from_team
late_regroup
bad_route
no_cover
over_pursuit
reload_exposure
tunnel_vision
panic_turn
vehicle_trap
missed_escape_window
ignored_pressure
accepted_bait
entered_dead_zone
lost_line_of_sight
failed_crossfire
static_under_fire
poor_cover_choice
blind_side_pressure
bad_vehicle_exit
```

Anti-predation review:

```text
How did we become prey?
What signal warned us?
Where was the recovery window?
What team behaviour would have prevented it?
```

---

## 🦁 Predator-pressure taxonomy

These labels describe fictional gameplay pressure patterns for media editing and review.

| Icon | Archetype | Meaning |
|---|---|---|
| 🦁 | Lion front push | frontal dominance / direct pressure |
| 🐆 | Leopard ambush | stealth, flank, sudden pounce |
| 🐍 | Snake trap | bait, delay, deception, angle |
| 🦈 | Shark pursuit | relentless chase pressure |
| 🟣 | Hyena cleanup | pack pressure, poach, cleanup |
| 🐝 | Wasp harassment | repeated sting / disruption |

---

## 🎵 Beat-to-kill auto-tune

The beat-to-kill system aligns visual impact with musical structure.

### 🔥 Kill auto-tune

Selects:

```text
kill_candidate high
shotline strong
body collapse or route stop
server death / killfeed / OCR if available
clear aftermath
strong music beat
```

Best music placement:

```text
chorus
drop
final hit
hard riff accent
last beat before transition
```

### 🩸 Wounding auto-tune

Selects:

```text
hit evidence
target survives
route changes
speed drops
team pressure increases after hit
```

Best placement:

```text
build-up
pre-chorus
rising section
first half of a chain
```

### 🪽 Winging auto-tune

Selects:

```text
no clear kill
formation breaks
aim/path/vehicle movement disrupted
prey loses options
```

Best placement:

```text
bridge
tension section
comic pause
chase segment
```

### 😂 Comedy auto-tune

Selects:

```text
bad timing
panic turn
mistimed confidence
absurd vehicle/body motion
unexpected poach
subtitle potential
lyric irony
```

Best placement:

```text
lyric punchline
beat stop
sudden silence
bridge
Dougie / [o][o] commentary gap
```

---

## 🎤 Lyric-assisted drama, irony, sarcasm, wit, and humour

The system can use lyrics as **short cue metadata**, not as copied lyric text.

Recommended lyric metadata fields:

```json
{
  "lyric_cue_id": "shoot_to_thrill_chorus_001",
  "time_s": 72.4,
  "cue_type": "chorus_hook",
  "mood": "swagger",
  "rhetorical_use": ["drama", "irony", "recognition"],
  "safe_keywords": ["thrill", "fire", "aim", "impact"],
  "clip_targets": ["controlled_burst", "spectacular", "team_play"],
  "avoid": ["literal_threat", "real_world_instruction"]
}
```

Use lyrics to guide:

| Icon | Lyric function | Example media use |
|---|---|---|
| 🎭 | Drama | big reveal, title card, slow approach |
| 😏 | Irony | lyric says confidence while player panics |
| 🧂 | Sarcasm | caption contradicts the visual mistake |
| 🧠 | Wit | clever setup, bait, recovery, Janus double-read |
| 😂 | Humour | absurd motion, bad timing, panic turn, poach |
| 🔥 | Recognition | kill/drop alignment, apex moment |
| 🕯️ | Omen | bell/introduction/slow threat building |
| 🏁 | Payoff | chorus, final hit, aftermath card |

Lyric-assisted scoring:

```text
cue_score =
  video_event_score
+ beat_alignment_score
+ lyric_mood_match
+ irony_bonus
+ humour_bonus
+ tactical_fit
+ strategic_fit
- repetition_penalty
- public_safety_penalty
```

Important: do not store or publish full copyrighted lyrics unless rights are cleared. Store timestamps, short descriptors, mood, keywords, and editorial intent.

---

## 🎸 Song profiles

### 💅 good_4_u

Tone:

```text
fast irony
comedy
panic-turn energy
social clip punch
```

Preferred tags:

```text
funny
panic_event
odd_unusual
comedic_prey
plus_chain
spectacular
```

Best placements:

```text
verse  -> setup and social context
chorus -> comedy / impact payoff
break  -> lyric irony and [o][o] captions
```

### 🎸 Shoot to Thrill

Tone:

```text
swagger
action
controlled burst
team pressure
```

Preferred tags:

```text
spectacular
controlled_burst
plus_chain
team_play
solo_precision
prey_panic_turn
route_prey
```

Best placements:

```text
riffs   -> shotlines / pursuit
chorus  -> kills / chain peaks
breaks  -> comedy / reload exposure
finale  -> recognition card
```

### 🏍️ Bat Out of Hell

Tone:

```text
epic ride
pursuit
escape
long-form cinematic narrative
```

Preferred tags:

```text
route_prey
shark_pursuit
team_play
survival_escape
spectacular
aftermath_control
```

Best placements:

```text
intro  -> ride / territory / title stills
build  -> pursuit and route pressure
impact -> collision, pressure, chase payoff
finale -> long aftermath and doctrine card
```

### 🔔 Hells Bells

Tone:

```text
ominous
strategic
aftermath-heavy
judgement
```

Preferred tags:

```text
ambush
territory
all_out_assault
strategic_pressure
aftermath_control
odd_unusual
```

Best placements:

```text
bell intro -> slow stills / APNGs / omen
build      -> stalking / terrain / route control
chorus     -> decisive impacts
ending     -> aftermath / doctrine card
```

---

## 🧠 Lens stack

### ☯️ Sun Tzu lens

```text
timing
terrain
deception
weak_points
manoeuvre
foreknowledge
```

### 🪞 Janus lens

Every event receives four possible reads:

```text
attacker_view  -> what opportunity was seen?
defender_view  -> what made the target vulnerable?
team_view      -> what coordination helped or failed?
aftermath_view -> what changed after the event?
```

### 🔷 13S lens

```text
strategy
structure
systems
skills
style
staff
shared_values
signals
space
sequence
stress
synergy
selection
```

### ⚖️ UQEBM lens

```text
smoothing
norming
scaling
scoping
marginal_value
```

### 💡 De Bono / humour lens

```text
humour
alternatives
consequences
lateral_punchline
```

### 🐜 ACO / 🐝 BCO lens

```text
selection_route
swarm_pressure
repeated_opportunity_trails
```

---

## 🛠️ Example commands

Run all production edits:

```bash
cd /home/andy/Documents/suitsmafia/py_script/suits_media_director_v8
./run_production_all_render.sh
```

Run one 29-second social cut:

```bash
./run_good4u_suits_29s.sh
```

Run one full-track edit:

```bash
./run_shoot_to_thrill_suits_full.sh
```

Run Disciples full-track Bat Out of Hell:

```bash
./run_bat_out_of_hell_disciples_full.sh
```

Direct Python call:

```bash
python3 suits_media_director_v8.py \
  --song-preset shoot_to_thrill_suits \
  --duration-mode full \
  --analysis-depth patient \
  --render \
  --render-final \
  --render-samples \
  --out /home/andy/Documents/suitsmafia/outputs/suits_media_director_v8/shoot_to_thrill_suits_full
```

---

## 📁 Project paths

```text
/home/andy/Documents/suitsmafia/videos
/home/andy/Documents/suitsmafia/videos/disciples
/home/andy/Documents/suitsmafia/videos/disciples/youtube
/home/andy/Documents/suitsmafia/videos/suits_youtube
/home/andy/Documents/suitsmafia/videos/youtube
/home/andy/Documents/suitsmafia/music_mp4
/home/andy/Documents/suitsmafia/outputs/suits_media_director_v8
```

---

## 📤 Outputs

Each run creates:

```text
media_dictionary.json
video_assets.json
video_assets.csv
music_assets.json
music_assets.csv
edit_plan.json
cue_match_plan.json
cue_match_plan.csv
run_manifest.json
curated_music_cue_report.html
renders/clips/*.mp4
renders/stills/*.png
renders/final/*.mp4
renders/final/*_segments.csv
renders/ffmpeg_final.log
renders/ffmpeg_samples.log
```

---

## 🔁 Human feedback loop

Reviewer buttons should include:

```text
correct prey type
wrong prey type
was not prey
predator also vulnerable
funny yes/no
too graphic for public
good social clip
good doctrine example
good training example
server truth needed
video-only confidence wrong
music placement good/bad
lyric irony good/bad
```

This feedback trains the next pass.

```text
scanner finds
cue sheet ranks
renderer proves
human corrects
AI learns
```

---

## 🧀 Dougie doctrine

> Clips are snacks.  
> A full song is dinner.  
> If the artist brought the whole tune, the machine plates the whole course.

[o][o]:

> “The beat tells ye when to strike the edit.  
> The lyric tells ye whether to be dramatic, sarcastic, witty, or a complete wee menace.”

