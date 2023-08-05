from .score import score, score_count
from .card import Deck
from random import choice

def discards(players):
    crib = []
    for player in players:
        discards = player.ask_for_discards()
        for c in discards:
            crib.append(c)
    return crib

def count(players, turn, debug=False, gui=True):
    '''
    The counting game. Two loops.

    Inner loop is us counting to 31,
    outer loop runs until we run out of cards
    '''

    game_over = False # this is for if we win during counting
    while True:
        # True, we are playing the counting game.
        # At the beginning of this loop, it is true
        # that we are playing the counting game, since
        # the `main` loop just sent us here.
        # Since this

        plays = []
        while True:
            # we are couting to 31
            current_player = players[turn^1]
            if gui and debug:
                print('Current player:', current_player)

            count = sum(plays)

            # state of current player
            if count == 31:
                # the previous player has made the count 31
                # we can't play on this, just break
                break

            current_cards = [n for n in current_player.hand if not n.ontable]
            if len(current_cards) == 0:
                # no cards
                if gui and debug:
                    print('Current player has no cards')
                turn = turn^1
                break

            pools = [count+c>31 for c in [n for n in current_player.hand if not n.ontable]]
            if all(pools):
                # no legal play
                if gui:
                    print('Current player has no legal move: "Go!"')
                turn = turn^1
                break

            # actually do the turn
            done = None
            while not done:
                card = current_player.ask_for_input(plays)
                if count + card < 32:
                    card.ontable = True
                    done = True

            plays.append(card)
            s = score_count(plays)
            current_player.peg(s)
            if current_player.score > 120:
                game_over = True
            turn = turn^1

            if gui:
                print("Player {} played {} (count: {}, points: {})".format(current_player, card, count+card, s))

            if debug and gui:
                print("Score for the play is", s, "to", current_player)


        # do we still have cards?
        # if so, we want to keep going
        if all([len([n for n in player.hand if not n.ontable]) < 1 for player in players]):
            # no players have cards
            break

        # otherwise, continue to another game of counting to 31

    # this is the level of the original while True

def game(players, debug=False, gui=True):

    turn = choice((0, 1))
    if gui:
        print('Welcome to cribbage')
        for i, player in enumerate(players):
            if i == turn:
                print('Player {}: {} (dealer)'.format(i+1, player))
            else:
                print('Player {}: {}'.format(i+1, player))

    hands = 0
    while all([p.score<121 for p in players]):
        hands +=1
        if gui:
            print('>>> Begin hand', hands)
            #print('Dealer is player', turn, '("{}")'.format( players[turn]))

        # create a fresh deck object
        deck = Deck()

        for player in players:
            player.hand = list(deck.draw(6)) # since it returns generator

        # ask players for thier discards
        crib = discards(players)
        if gui and debug:
            print("Crib:", crib)

        # calculate scores (but do not assign yet)
        turn_card = next(deck.draw(1))
        if gui:
            print('>>> The turn card is', turn_card)

        # run the counting sub-game
        # players get scored in-game
        count(players, turn, debug=debug, gui=gui)
        #if gui:
        #    print("Scores after counting", [p.score for p in players])

        # "turn" card and final scoring
        # add nibs and nobs!

        print('>>> End of hand {}'.format(hands))
        for i, player in enumerate(players):
            my_score = score(player.hand + [turn_card])
            player.peg(my_score)
            print('{}: {} {} {} {} + {} ({})'.format(player, *player.sorted_hand, turn_card, my_score))
            if i == turn: # it's my crib
                crib_score = score(crib + [turn_card])
                player.peg(crib_score)
                print('Crib ({}): {} {} {} {} + {} ({})'.format(player, *crib, turn_card, crib_score))

        turn =  turn^1
        if gui:
            print('>>> The scores are {} {} and {} {}'.format(players[0], players[0].score, players[1], players[1].score))

    # end of game (one player has > 121 points)
    return_val = [player.score for player in players]
    for player in players:
        player.clean()
    return return_val
