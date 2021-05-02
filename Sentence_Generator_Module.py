# Uses Noam Chomsky Syntactic Structures
# NP + VP
# (T + N) + (V + P)

# print(T, N)
def assemble(*args):
    return " ".join(args)


def NP(T, N):
    return assemble(T, N)


def VP(Verb, NP):
    return assemble(Verb, NP)


def sentence(NP, VP, Adverb1):
    return assemble(NP, VP, Adverb1)

# now i must make several different lists related to the different moods


def loop(X):
    T = ['the', 'their', 'our', 'his', 'her']
    N = ['man', 'ball', 'monkey', 'caroussel',
         'computer', 'edge', 'heart', 'guitar', 'fire']
    Verb = ['hit', 'polished', 'healed', 'tore', 'treated', 'coded', 'ran']

    #angry, joy, sorrow, surprised
    angry_adverb = ['furiously', 'bitterly', 'terribly',
                    'violently', 'intensely', 'savagely']
    joy_adverb = ['joyfully', 'happily',
                  'cheerfully', 'merrily', 'ecstatically', 'gleefully', 'contentedly']
    sorrow_adverb = ['sadly', 'sorrowfully',
                     'dejectedly', 'gloomily', 'joylessly']

    surprised_adverb = ['suddenly', 'shockingly', 'surprisingly']

    import random as ran

    for i in range(X):
        N1, N2 = ran.choice(N), ran.choice(N)
        T1, T2 = ran.choice(T), ran.choice(T)
        Adverb1 = ran.choice(joy_adverb)
        # need to make conditional statements
        # if mood is happy, angry, sorrowful, adverb will be different
        Verb1 = ran.choice(Verb)

        NP1 = NP(T1, N1)
        NP2 = NP(T2, N2)
        VP1 = VP(Verb1, NP2)
        print(sentence(NP1, Adverb1, VP1))


loop(1)  # generates 1 sentence
