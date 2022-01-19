#!/usr/bin/env python3
import random

men_list = ["Abe", "Bob", "Col", "Dan", "Ed", "Fred", "Gav", "Hal", "Ian", "Jon"]
women_list = ["Abi", "Bea", "Cath", "Dee", "Eve", "Fay", "Gay", "Hope", "Ivy", "Jan"]

def shuffle(array):
    a=len(array)
    b=a-1
    for d in range(b,0,-1):
      e=random.randint(0,d)
      if e == d:
            continue
      array[d],array[e]=array[e],array[d]
    return array

def generate_preference_ranking(list_1, list_2):
    preference_dict = {}
    for person in list_1:
        preference_dict[person] = shuffle(list_2)
    return preference_dict

preferred_women_rankings = generate_preference_ranking(women_list, men_list)
preferred_men_rankings = generate_preference_ranking(men_list, women_list)



#Tentatively engaged people
tentative_engagements = []

#men who still need to get paired
free_men = []

def init_free_men():
    for man in preferred_men_rankings:
        free_men.append(man)

def stable_matching():
    while(len(free_men)>0):
        for man in free_men:
            start_matching(man)

def start_matching(man):
    for woman in preferred_men_rankings[man]:

        taken_match = [couple for couple in tentative_engagements if woman in couple]

        if (len(taken_match) == 0):
            tentative_engagements.append([man,woman])
            free_men.remove(man)
            print('%s proposes to  %s'%(man, woman))
            print('%s is engaged to %s'%(man, woman))
            break
        elif (len(taken_match)> 0):
            print('%s is taken already'%(woman))

            current_man = preferred_women_rankings[woman].index(taken_match[0][0])
            potential_man = preferred_women_rankings[woman].index(man)

            if (current_man < potential_man):
                print('Woman is satisfied with %s'%(taken_match[0][0]))
            else:
                print('%s dumps %s'%(woman, taken_match[0][0]))

                #The new guy is engaged
                free_men.remove(man)

                #The old guy is now single
                free_men.append(taken_match[0][0])

                taken_match[0][0] = man
                break

def main():
    init_free_men()
    stable_matching()

    for i in preferred_men_rankings.items():
        print(i)
   

    print('Pairings:')
    for i in tentative_engagements:
        men = i[0]
        women = i[1]

        print("\t"+men + " - " + women)

main()
        
        
    
