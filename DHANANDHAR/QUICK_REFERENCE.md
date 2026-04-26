# 📖 DHANANDHAR Series — Quick Reference Guide

## 📂 Folder Structure

```
DHANANDHAR/
├── ROADMAP.md                 ← Start here! Master index of all seasons
├── generate_episodes.py       ← Script to generate episode templates
│
├── seasons/
│   ├── season_01_the_fire/
│   │   ├── README.md          ← Season overview & episode list
│   │   └── episodes/
│   │       ├── ep_01_1_crore_not_rich/
│   │       │   ├── README.md           ← Episode metadata & links
│   │       │   ├── idea.md             ← Core concept
│   │       │   ├── script.md           ← Full dialogue breakdown
│   │       │   └── video/              ← Raw video files
│   │       ├── ep_02_salary_not_wealth/
│   │       └── ... (10 episodes per season)
│   │
│   ├── season_02_safety_net/
│   ├── season_03_earn_high/
│   ├── season_04_spend_less/
│   ├── season_05_invest_rest/
│   ├── season_06_wealth_engine/
│   ├── season_07_mistakes_traps/
│   ├── season_08_money_mindset/
│   ├── season_09_freedom_mode/
│   └── season_10_endgame/
│
└── raw_data/
    └── logos/
        └── canva_ai
```

---

## 🎯 How to Use Each File

### ROADMAP.md
Master index with all seasons and their statuses. Update here for overall project tracking.

### Season README (e.g., `season_01_the_fire/README.md`)
- Season overview
- Goal and theme
- Episode list with links
- Season-wide resources

### Episode README (e.g., `ep_01_1_crore_not_rich/README.md`)
- Episode metadata
- Links to all platform versions
- Status tracking (Draft → Ready → Published)
- Post-publish metrics

### idea.md
- Hook/angle that grabs attention
- Core concept explanation
- Key points to cover
- Visual concepts needed
- CTA (Call-to-action)
- Research/references

### script.md
- Timed breakdown (Hook → Body → Punchline)
- Full dialogue
- On-screen text/visuals
- Production notes

### video/ folder
Place raw video files, clips, and media assets here.

---

## ✅ Workflow for Creating an Episode

1. **Open Episode Folder**
   - Navigate to: `seasons/season_XX/episodes/ep_YY_title/`

2. **Fill in idea.md**
   - Define your hook
   - Outline key points
   - Plan visuals

3. **Write script.md**
   - Full dialogue
   - Timing markers
   - Visual cues

4. **Add video assets**
   - Place raw clips in `video/` folder

5. **Update episode README.md**
   - Change status to "In Progress"
   - Add platform links once published
   - Track metrics

6. **Update season README.md**
   - Mark episode status in the table

7. **Update master ROADMAP.md**
   - Update season/episode status if needed

---

## 📊 Status Tracking

Update statuses across files as you progress:

```
Draft → In Progress → Ready → Published
```

### Quick Status Check
1. Open `ROADMAP.md` to see season statuses
2. Open `seasons/season_XX/README.md` to see episode statuses
3. Open individual episode `README.md` for details

---

## 🔗 Adding Links to Each Episode

### Platform Links (Add to episode README.md)

Once your episode is published, add:

```markdown
- **YouTube:** https://youtube.com/watch?v=XXXXX
- **Instagram Reels:** https://instagram.com/reel/XXXXX
- **YouTube Shorts:** https://youtube.com/shorts/XXXXX
```

### Cross-linking Between Files

Link from season README to episodes:
```markdown
| 01 | [₹1 Crore is NOT rich anymore](episodes/ep_01_1_crore_not_rich/README.md) | - | - |
```

Link from master ROADMAP to seasons:
```markdown
| 1 | [The Fire 🔥](seasons/season_01_the_fire/README.md) | ... | - |
```

---

## 💾 Saving & Organizing Raw Assets

### Inside each episode folder:

```
ep_01_1_crore_not_rich/
├── README.md
├── idea.md
├── script.md
└── video/
    ├── raw_clip_1.mp4
    ├── raw_clip_2.mov
    ├── intro_sequence.mp4
    └── b_roll_footage/
```

---

## 🚀 Quick Actions

### Check Overall Progress
```bash
# Count total episodes created
find seasons -name "README.md" | wc -l

# See file structure
tree seasons -L 3
```

### Find All Episodes of a Season
- Navigate to: `seasons/season_XX/README.md`
- See episode list with status

### Update All Episode Statuses
1. Edit `seasons/season_XX/README.md`
2. Update the "Status" column in the episode table
3. Save

---

## 📝 Template Fields Reference

**In idea.md:**
- Angle/Hook
- Core Concept
- Key Points (min. 4)
- Visual Concepts
- Call-to-Action
- References

**In script.md:**
- Timing info
- Hook section (0:00 - 0:05)
- Body section (0:05 - 0:25)
- Punchline section (0:25 - 0:30)
- On-screen visuals
- Production notes

---

## 🎬 Next Steps

1. ✅ Folder structure complete
2. ⬜ Fill in `idea.md` for Episode 1
3. ⬜ Write `script.md` for Episode 1
4. ⬜ Add video assets
5. ⬜ Publish and track metrics
6. ⬜ Repeat for remaining episodes

---

## 📞 Pro Tips

- **Batch similar work**: Fill all `idea.md` files for a season first
- **Use templates**: All files have pre-formatted templates
- **Track status**: Keep README tables updated for easy overview
- **Version control**: Commit regularly to git if using version control
- **Backup videos**: Store high-quality originals separately if needed

---

**Happy creating! 🚀**
