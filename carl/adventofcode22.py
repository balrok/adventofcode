#hp, dmg, def, mana
player = (50, 0, 0, 500)
boss = (71, 10, 0, 0)

# cost, effect_boss, effect_player, effect_turns, tmp_effect on player
NO_EFFECT = (0,0,0,0)
spells = (
    (53,  (-4,0,0,0),   NO_EFFECT, 0, True ),
    (73,  (-2,0,0,0),   (2,0,0,0), 0, True ),
    (113,  NO_EFFECT,   (0,0,7,0), 6, True ),
    (173, (-3,0,0,0),   NO_EFFECT, 6, False),
    (229,  NO_EFFECT, (0,0,0,101), 5, False)
)


def apply_spell(s, player, boss):
    boss = [x+y for x,y in zip(boss,s[1])]
    player = [x+y for x,y in zip(player,s[2])]
    return player, boss

def remove_spell(s, player, boss):
    boss = [x-y for x,y in zip(boss,s[1])]
    player = [x-y for x,y in zip(player,s[2])]
    return player, boss

def apply_timer(timer, player, boss):
    for tid in range(len(timer)):
        t = timer[tid]
        if t > 0 and spells[tid][4] == False:
            player, boss = apply_spell(spells[tid], player, boss)
            timer[tid] -= 1
        if t > 0 and spells[tid][4] == True:
            if t == spells[tid][3]:
                player, boss = apply_spell(spells[tid], player, boss)
                if player[2]>7:
                    player[2] = 7
            timer[tid] -= 1
            # remove tmp effect
            if timer[tid] == 0:
                player, boss = remove_spell(spells[tid], player, boss)

    return timer, player, boss


def fight(base_player, base_boss, base_timer, turn=1, used_mana=0, fewest_mana = 13560):
    if used_mana > fewest_mana:
        return False, fewest_mana
    player0 = base_player[:]
    boss0 = base_boss[:]
    timer0 = base_timer[:]
    timer0, player0, boss0 = apply_timer(timer0, player0, boss0)
    if boss0[0] <= 0:
        return True, used_mana
    won = False
    for sid in range(len(spells)):
        #print turn, sid
        s = spells[sid]
        player = player0[:]
        boss = boss0[:]
        timer = timer0[:]
        # can not cast a spell which is already in effect
        if s[3] > 0 and timer[sid] > 0:
            #print "timer"
            continue
        # spell too expensive
        if s[0] > player[3]:
            #print "mana", player
            break
        # only those with instant effect now
        #print turn, "cast", s[0]
        player[3] -= s[0]
        if s[3] == 0:
            player, boss = apply_spell(s, player, boss)
        if s[3] > 0:
            timer[sid] = s[3]
        if boss[0] <= 0:
            return True, used_mana+s[0]

        timer, player, boss = apply_timer(timer, player, boss)
        player[0] -= boss[1]-player[2]
        #print turn, player, boss, timer
        if player[0] <= 0:
            #print "player dead"
            return False, fewest_mana
        #print turn, player, boss
        result, mana = fight(player, boss, timer, turn+1, used_mana+s[0], fewest_mana)
        if result:
            if mana < fewest_mana:
                print turn, mana, player, boss, s[0], timer
            fewest_mana = min(mana, fewest_mana)
            won = True
    return won, fewest_mana



    


# 1161 too low
timer = len(spells) * [0]
print fight(list(player[:]), list(boss[:]), timer)

# this is a test
#player = (10, 0, 0, 250)
#boss = (13, 8, 0, 0)
#fight(player[:], boss[:], spells)
