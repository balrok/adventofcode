#hp, dmg, def, mana
player = (50, 0, 0, 500)
boss = (71, 8, 0, 0)

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
    for id in range(len(boss)):
        boss[id] += s[1][id]
        player[id] += s[2][id]

def remove_spell(s, player, boss):
    for id in range(len(boss)):
        boss[id] -= s[1][id]
        player[id] -= s[2][id]

def apply_timer(timer, player, boss):
    for tid,t in enumerate(timer):
        if t > 0 and spells[tid][4] == False:
            apply_spell(spells[tid], player, boss)
            timer[tid] -= 1
        # tmp effect spells
        if t > 0 and spells[tid][4] == True:
            if t == spells[tid][3]:
                apply_spell(spells[tid], player, boss)
                if player[2]>7:
                    player[2] = 7
            timer[tid] -= 1
            # remove tmp effect
            if timer[tid] == 0:
                remove_spell(spells[tid], player, boss)


def fight(base_player, base_boss, base_timer, turn=1, used_mana=0, fewest_mana = 99999):
    # atk=10 without this optimization 11.9 seconds - with this 7.4 max turn amount is 19
    # atk=8  without this: over 10m - with this 1m38 max turn amount is 57
    # so just len(spells)*19 different routes I think?
    if used_mana > fewest_mana:
        return False, fewest_mana

    # apply the timer
    apply_timer(base_timer, base_player, base_boss)
    if task2:
        base_player[0] -= 1
        if base_player[0] <= 0:
            return False, used_mana
    if base_boss[0] <= 0:
        return True, used_mana

    # now loop through the spells (sorted by mana-amount to break the loop when not enough)
    won = False
    for sid,s in enumerate(spells):
        player = base_player[:]
        boss = base_boss[:]
        timer = base_timer[:]

        # can not cast a spell which is already in effect
        if s[3] > 0 and timer[sid] > 0:
            continue
        # spell too expensive
        if s[0] > player[3]:
            #print "mana", player
            break

        player[3] -= s[0] # mana
        if s[3] == 0: # this is no timer-spell
            apply_spell(s, player, boss)
        else:
            timer[sid] = s[3]

        # Boss turn
        apply_timer(timer, player, boss)
        if boss[0] <= 0:
            return True, used_mana+s[0]
        player[0] -= boss[1]-player[2]
        #print turn, player, boss, timer
        if player[0] <= 0:
            return False, fewest_mana

        # take this spell and go to the next turn
        result, mana = fight(player[:], boss[:], timer[:], turn+1, used_mana+s[0], fewest_mana)
        if result:
            if mana < fewest_mana:
                # with this I can follow back which spells were cast on the best route
                print turn, mana, player, boss, s[0], timer
            fewest_mana = min(mana, fewest_mana)
            won = True
    return won, fewest_mana



    



task2 = False
timer = len(spells) * [0]
print fight(list(player[:]), list(boss[:]), timer)

print "\n\n"

#task2 = True
#timer = len(spells) * [0]
#print fight(list(player[:]), list(boss[:]), timer)
# this is a test
#player = (10, 0, 0, 250)
#boss = (13, 8, 0, 0)
#fight(player[:], boss[:], spells)
