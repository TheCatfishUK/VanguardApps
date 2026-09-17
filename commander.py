import random, math

C = ["Same culture as recruiter", "Same culture as recruiter", "Same culture as recruiter", "Same culture as a Unit", "Same culture as a Unit", "Random culture"]
background_title = ["Academy Cadet", "Foreign-trained", "Village Leader", "Bandit", "Ideologue", "Academic", "Bureaucrat", "Enlisted", "Aide-de-camp", "Schoolteacher"]

trait_list = [
    "Beloved: Your army gains +1 resting morale. If you receive troops at maximum morale, they will gain 1 morale.",
    "Brutal: Strongholds you besiege lower their threshold by an extra -1/week.",
    "Commando. You can designate one infantry unit in your army as guerrillas.",
    "Crusader. Your army gains a +1 bonus in battles against factions of a different ideology.",
    "Defensive Engineer. When you defend a stronghold or fortification in an assault, add +2 to the garrison’s defensive bonus.",
    "Frontliner. You count as 20 years younger for the purposes of surviving perilous situations.",
    "Guardian. Your army suffers 5% fewer casualties in battle. -1-in-6 chance to be captured in battle.",
    "Honorable. Your army always stops pillaging when you give the order to halt. -1-in-6 chance to spark a revolt when foraging, torching, or raising additional armies.",
    "Ironsides. When you defend a stronghold or fortification in a siege, add +5 to its threshold.",
    "Logistician. Your army can carry 20% more total supplies and fuel. Your army stretches half as long on the road.",
    "Outrider. With a guerrilla unit, your scouting range expands to 24 miles, and you may forage up to three additional hexes that are within 2 hexes of your army.",
    "Poet. Your morale rolls count as 2 higher for the purposes of determining failed morale consequences.",
    "Raider. 20% extra loot is able to be removed from captured strongholds per day. Your units have +1 chance of success on Raid rolls and add +1 to the amount of loot, fuel, supplies, or equipment stolen.",
    "Ranger. Bad weather does not reduce your scouting ranges.",
    "Fastidious. Your army never loses equipment in battles. Equipment losses from a rout are halved.",
    "Foreign Training. You get a bonus to interacting with one of the off-map superpowers (picked when you receive this trait.)",
    "Spartan. Your army has only half as many noncombatants attached. When you acquire new noncombatants, you pick up only half as many.",
    "Stubborn. Your army does not lose morale on defeat in battle. This does not apply to the 1 morale lost from attacking.",
    "Vanquisher. You deal an extra 5% casualties to the enemy in battle. +1-in-6 chance to capture enemy commanders in battle.",
    "Veteran. Your army never routs upon defeat in battle.",
    "Scavenger. You forage 10% extra supplies. If you salvage a battlefield, on a 3-up the equipment is repairable, and on a 5-up the equipment is instantly usable.",
    "Sailor. Boats under your command are not slowed by rough water and bad weather.",
    "Flight Controller. Aircraft under your command prep for missions faster. You can organize extra air missions each day, either 3 Near missions or 2 Far missions. Your aircraft can run 5 missions per week, or 7 counting as a Forced March.",
    "Treadhead. Armored units under your command always count as fighting in open terrain.",
    "Mathematician. Artillery units under your command have +1-in-6 chance to hit their targets, and add +1 to all out-of-battle damage rolls.",
    "Multicultural. You count as another being one additional culture (chosen when you receive the trait). This trait can be received multiple times.",
    "Theorist. You are a respected and widely-known advocate for your ideology. You get a bonus to interact with factions, groups, or NPCs of your ideology and sub-ideology.",
    "Fortifier. Fortifications you construct cost half as much loot and supplies (rounded up.)",
    "Interceptor. Combat Aircraft units you command get +1 to Air Battle rolls, and +1 to damage rolls against intercepted aircraft.",
    "Merchant. The stronghold you are garrisoned in produces twice as much loot and supplies each week, additive to other multipliers. In a port, you can purchase items and import goods at half price (rounded up.)",
    "Industrialist. Factory runs you order produce twice as much supplies, fuel, or equipment. You can speed Factory construction and expansion time with the expenditure of extra manpower or fuel as if it were a Fortification. The cost in Loot and Supplies is unaltered.",
    "Occupier. You can designate one 200-person or larger infantry unit as a police unit. This unit increases the difficulty of any enemy operations in its hex or any of the surrounding hexes, and gives -1-in-6 revolt chance when foraging. The police unit gains +1 chance of success on Patrol rolls, and adds +1 to Investigation and Arrest rolls.",
    "Medic. The chance of disease spreading to your army is halved, and you get a bonus on attempts to mitigate the effects of disease.",
    "Pioneer. The time needed to construct and repair roads and railroads is halved additively.",
    "Switchman. You can transport double the amount of fuel, supplies, loot and equipment per railroad level, and your army counts as being half its length (rounded up) when traveling by rail. If you command an armored train, it grants +1 to your battle roll. GMs will provide information on the construction and use of armored trains to commanders with Switchman.",
    "Decisive. In any battle you initiate (on defense or offense), you may choose to increase or decrease the duration by 1 day, to a maximum of 6 and a minimum of 1.",
    "Trainer (X). You may act as a trainer for a specific unit type. The type of unit will be influenced by other traits, or determined randomly otherwise.",
]

background_ages = [
    [23, 2, 6],
    [22, 3, 6],
    [20, 3, 20],
    [20, 1, 20],
    [16, 3, 6],
    [22, 2, 20],
    [25, 2, 20],
    [22, 3, 6],
    [20, 3, 6],
    [20, 1, 20],
]

culture = random.randint(0,5)
ideology = random.randint(0,9)
background = random.randint(0,9)

def age_calc(a):
    age = 0
    for i in range(a[1]):
        age += random.randint(0,a[2]-1)
    return age + a[0]
    
def gen_trait():
    gen = random.randint(0, len(trait_list))
    print("•", trait_list[gen])
    trait_list.pop(gen)


if ideology == 0:
    I = "Sub ideology"
else:
    I = "Same as faction"

print(C[culture])
print(I)

print(background_title[background])

age = age_calc(background_ages[background])
print(age, "Years old")

traits = math.floor((age-10) /10)
print("\n Traits:")

for i in range(traits):
    gen_trait()

print("\n",random.choice(["Male", "Female", "Non-binary"]))
