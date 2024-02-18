###############
# Bad Stories #
#   by voxj.  #
###############

import random as r
r.c = r.choice
def genbs():
    things = ["cat", "dog", "banana", "chair", "wizard", "killer"] # you're free to change those!
    actions = ["ate", "kicked", "destroyed", "stole", "hid", "killed"] # you're free to change those!
    whattheyare = ["angry", "gloomy", "clumsy", "greedy", "lazy", "deathly"] # you're free to change those!
    howtheydid = ["quickly", "carelessly", "loudly", "rudely", "awkwardly", "badly"] # you're free to change those!
    story = ""
    for _ in range(5):
        things2 = r.c(things)
        actions2 = r.c(actions)
        whattheyare2 = r.c(whattheyare)
        howtheydid2 = r.c(howtheydid)
        things3 = r.c(things)
        actions3 = r.c(actions)
        whattheyare3 = r.c(whattheyare)
        howtheydid3 = r.c(howtheydid)
        variations = [
            f"The {things2} {actions2} {whattheyare2} {howtheydid2}.",
            f"The {whattheyare2} {things2} {actions2} {howtheydid2}.",
            f"The {howtheydid2} {things2} {actions2} the {whattheyare3} {things3}.",
            f"The {whattheyare2} {things2} {actions2} {howtheydid2} and the {whattheyare3} {things3} {actions3} {howtheydid3}."
        ] # you're free to make new variations, but keep in mind you'll need more things, actions and etc!
        sentence = r.c(variations)
        story += sentence + " "
    return story
bs = genbs()
print(bs)

###############
# made w/ lov #
#   by voxj.  #
###############
