globmin = 10000
boss_damage = 10
boss_initial_hp = 71
my_initial_hp = 50
my_initial_mana = 500
def turn(mode, level, spent_mana, l, my_turn, my_mana,  my_hp, boss_hp, shield_effect, poison_effect, recharge_effect):
	global globmin
	if spent_mana > globmin:
		pass #return ["too much mana used"], 10000
	if level > 26:
		return ["level too high"], 10000
	if my_turn:
		if mode:
			my_hp -= 1
			if my_hp <= 0:
				return ["lost"],10000
		# effects (shield does not apply)
		if poison_effect > 0:
			boss_hp -= 3
			if boss_hp <= 0:
				globmin = spent_mana
				return l,spent_mana
		if recharge_effect > 0:
			my_mana += 101
		# turn
		minman = 10000
		ml = []
		# magic missile
		if my_mana >= 53:
			sm = spent_mana + 53
			mana = my_mana - 53
			bhp = boss_hp - 4
			if bhp <= 0:
				if globmin > sm:
					globmin = sm
				return l,sm
			nl = l[:]
			nl.append("Missile")
			rl,nsm = turn(mode, level+1,sm, nl, not my_turn, mana, my_hp, bhp, shield_effect-1, poison_effect-1, recharge_effect-1)
			if nsm < minman:
				minman = nsm
				ml = rl
		# drain
		if my_mana >= 73:
			sm = spent_mana + 73
			mana = my_mana - 73
			bhp = boss_hp - 2
			hp = my_hp + 2
			if bhp <= 0:
				if globmin > sm:
					globmin = sm
				return l,sm
			nl = l[:]
			nl.append("Drain")
			rl,nsm = turn(mode, level+1,sm, nl, not my_turn, mana, hp, bhp, shield_effect-1, poison_effect-1, recharge_effect-1)
			if nsm < minman:
				minman = nsm
				ml = rl
		# shield
		if my_mana >= 113 and shield_effect < 2:
			sm = spent_mana + 113
			mana = my_mana - 113
			nl = l[:]
			nl.append("Shield")
			rl,nsm = turn(mode, level+1,sm, nl, not my_turn, mana, my_hp, boss_hp, 6, poison_effect-1, recharge_effect-1)
			if nsm < minman:
				minman = nsm
				ml = rl
		# poison
		if my_mana >= 173 and poison_effect < 2:
			sm = spent_mana + 173
			mana = my_mana - 173
			nl = l[:]
			nl.append("Poison")
			rl,nsm = turn(mode, level+1,sm, nl, not my_turn, mana, my_hp, boss_hp, shield_effect-1, 6, recharge_effect-1)
			if nsm < minman:
				minman = nsm
				ml = rl
		# recharge
		if my_mana >= 229 and recharge_effect < 2:
			sm = spent_mana + 229
			mana = my_mana - 229
			nl = l[:]
			nl.append("Recharge")
			rl,nsm = turn(mode, level+1,sm, nl, not my_turn, mana, my_hp, boss_hp, shield_effect-1, poison_effect-1, 5)
			if nsm < minman:
				minman = nsm
				ml = rl
		return ml, minman
	else:
		# effects
		if shield_effect > 0:
			armor = 7
		else:
			armor = 0
		if poison_effect > 0:
			boss_hp -= 3
			if boss_hp <= 0:
				if globmin > spent_mana:
					globmin = spent_mana
				return l,spent_mana
		if recharge_effect > 0:
			my_mana += 101
		my_hp -= boss_damage - armor
		if my_hp <= 0:
			return ["lost"],10000
		result = turn(mode, level+1,spent_mana, l, not my_turn, my_mana, my_hp, boss_hp, shield_effect-1, poison_effect-1, recharge_effect-1)
		return result

print turn(False, 0,0,[], True, my_initial_mana, my_initial_hp, boss_initial_hp, 0, 0, 0)
print turn(True, 0,0,[], True, my_initial_mana, my_initial_hp, boss_initial_hp, 0, 0, 0)
