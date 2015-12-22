import functools

items  = {
"Weapons": ((8,4,0),
(10,    5,      0),
(25,    6,      0),
(40,    7,      0),
(74,    8,      0)
),
"Armor":(
(0,    0,      0), # additional because we can buy nothing
( 13,    0,      1),
( 31,    0,      2),
( 53,    0,      3),
( 75,    0,      4),
(102,    0,      5)
),
"Rings":(
# price, dmg, def
(0,    0,      0), # additional because we can buy nothing
(0,    0,      0), # additional because we can buy nothing
( 20,    0,      1),
( 25,    1,      0),
( 40,    0,      2),
( 50,    2,      0),
( 80,    0,      3),
(100,    3,      0)
)}

#hp, dmg, def
enemy=(104, 8, 1)



@functools.lru_cache(maxsize=None)
def fight(damage, defense):
    #print("fight:",damage, defense)
    me_hp = 100
    enemy_hp = enemy[0]
    if damage < enemy[2]:
        return False, enemy_hp
    for _ in range(max(me_hp, enemy_hp)+1):
        enemy_hp -= damage-enemy[2]
        if enemy_hp <= 0:
            return True, me_hp
        me_hp -= enemy[1]-defense
        if me_hp <= 0:
            return False, enemy_hp
        #print(me_hp, enemy_hp)
    return False, 0


def buy_all(base_money):
    for w in items["Weapons"]:
        equip1 = [0, 0]
        money1 = base_money
        if w[0] > money1:
            break
        money1 -= w[0]
        equip1[0] += w[1]
        equip1[1] += w[2]
        for a in items["Armor"]:
            equip2 = equip1[:]
            money2 = money1
            if a[0] > money2:
                break
            money2 -= a[0]
            equip2[0] += a[1]
            equip2[1] += a[2]
            for r1_num in range(len(items["Rings"])):
                equip3 = equip2[:]
                money3 = money2
                r1 = items["Rings"][r1_num]
                if r1[0] > money3:
                    break
                money3 -= r1[0]
                equip3[0] += r1[1]
                equip3[1] += r1[2]
                for r2_num in range(r1_num+1, len(items["Rings"])):
                    equip4 = equip3[:]
                    money4 = money3
                    r2 = items["Rings"][r2_num]
                    if r2[0] > money4:
                        break
                    money4 -= r2[0]
                    equip4[0] += r2[1]
                    equip4[1] += r2[2]
                    yield((equip4, money4, [w[0], a[0], r1[0], r2[0]]))


def task1():
    for money in range(1, 10000):
        print(money)
        for equip,it in buy_all(money):
            me_won, hp = fight(equip[0], equip[1])
            if me_won:
                print(it)
                print(money, equip)
                return
def task2():
    most_spent = 0
    money = 999999
    print(money)
    for equip,mon, it in buy_all(money):
        me_won, hp = fight(equip[0], equip[1])
        spent = money-mon
        if me_won == False and spent > most_spent:
            most_spent = spent
            print("new record: ", most_spent)
#task1()
task2()
#fight(6,4)

#41 too low
# 48 too high

#enemy=(12, 7, 2)
#fight(5,5)
