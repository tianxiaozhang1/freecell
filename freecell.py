import pygame, sys, random, math

class Card():
    def __init__(self, rank, suit, stack, pos, clicked, moving):
        draw_card(rank, suit, stack, pos, clicked, moving)

def new_game():
    #Setup new game

    deck = []
    cascades = [[], [], [], [], [], [], [], []]
    backup_cascades = [[], [], [], [], [], [], [], []]
    
    #Assign new deck and assign to the eight cascades
    for i1 in range(52):
        deck.append(i1)

    for i4 in range(4):
        for i5 in range(7):
            new_card = random.choice(deck)
            deck.remove(new_card)
            rank = new_card%13+1
            suit_num = new_card//13
            cascades[i4].append([rank, suit_num+1])
            backup_cascades[i4].append([rank, suit_num+1])

    for i6 in range(4, 8):
        for i7 in range(6):
            new_card = random.choice(deck)
            deck.remove(new_card)
            rank = new_card%13+1
            suit_num = new_card//13
            cascades[i6].append([rank, suit_num+1])
            backup_cascades[i6].append([rank, suit_num+1])

    #Display all 52 cards
    for c1 in cascades:
        for d1 in c1:
            cas_num = cascades.index(c1) + 9
            cas_pos = c1.index(d1)
            Card(d1[0], d1[1], cas_num, cas_pos, clicked = False, moving = False)

    display_graphics_part()
    return cascades, backup_cascades

def draw_suit(suit, left, top, clicked, embroider = False):
    
    # 1: Diamonds      5: Upside down diamonds
    # 2: Clubs         6: Upside down clubs
    # 3: Hearts        7: Upside down hearts
    # 4: Spades        8: Upside down spades

    if clicked == True:
        if suit%2 == 1:
            S_COLOUR = TEAL
        if suit%2 == 0:
            S_COLOUR = WHITE
        if embroider == True:
            S_COLOUR = BLACK
    else:
        if suit%2 == 1:
            S_COLOUR = RED
        if suit%2 == 0:
            S_COLOUR = BLACK
        if embroider == True:
            S_COLOUR = WHITE

    # Diamonds
    if suit == 1 or suit == 5:
        pygame.draw.rect(screen, S_COLOUR, pygame.Rect(left+15, top+5, 3, 23)) 
        pygame.draw.rect(screen, S_COLOUR, pygame.Rect(left+13, top+7, 7, 19)) 
        pygame.draw.rect(screen, S_COLOUR, pygame.Rect(left+11, top+9, 11, 15)) 
        pygame.draw.rect(screen, S_COLOUR, pygame.Rect(left+9, top+11, 15, 11)) 
        pygame.draw.rect(screen, S_COLOUR, pygame.Rect(left+7, top+13, 19, 7)) 
        pygame.draw.rect(screen, S_COLOUR, pygame.Rect(left+5, top+15, 23, 3)) 
    
    #Clubs
    elif suit == 2:
        pygame.draw.rect(screen, S_COLOUR, pygame.Rect(left+12, top+5, 9, 7)) 
        pygame.draw.rect(screen, S_COLOUR, pygame.Rect(left+5, top+12, 7, 9)) 
        pygame.draw.rect(screen, S_COLOUR, pygame.Rect(left+21, top+12, 7, 9)) 
        pygame.draw.rect(screen, S_COLOUR, pygame.Rect(left+15, top+12, 3, 11)) 
        pygame.draw.rect(screen, S_COLOUR, pygame.Rect(left+12, top+15, 11, 3)) 
        pygame.draw.rect(screen, S_COLOUR, pygame.Rect(left+13, top+22, 7, 3)) 
        pygame.draw.rect(screen, S_COLOUR, pygame.Rect(left+5, top+25, 23, 3)) 
    elif suit == 6:
        pygame.draw.rect(screen, S_COLOUR, pygame.Rect(left+5, top+5, 23, 3)) 
        pygame.draw.rect(screen, S_COLOUR, pygame.Rect(left+13, top+8, 7, 3)) 
        pygame.draw.rect(screen, S_COLOUR, pygame.Rect(left+15, top+11, 3, 10)) 
        pygame.draw.rect(screen, S_COLOUR, pygame.Rect(left+12, top+15, 9, 3)) 
        pygame.draw.rect(screen, S_COLOUR, pygame.Rect(left+5, top+12, 7, 9)) 
        pygame.draw.rect(screen, S_COLOUR, pygame.Rect(left+21, top+12, 7, 9)) 
        pygame.draw.rect(screen, S_COLOUR, pygame.Rect(left+12, top+21, 9, 7))
    
    #Hearts
    elif suit == 3:
        pygame.draw.rect(screen, S_COLOUR, pygame.Rect(left+5, top+7, 10, 11)) 
        pygame.draw.rect(screen, S_COLOUR, pygame.Rect(left+15, top+9, 3, 19)) 
        pygame.draw.rect(screen, S_COLOUR, pygame.Rect(left+18, top+7, 10, 11)) 
        pygame.draw.rect(screen, S_COLOUR, pygame.Rect(left+7, top+5, 6, 15)) 
        pygame.draw.rect(screen, S_COLOUR, pygame.Rect(left+20, top+5, 6, 15)) 
        pygame.draw.rect(screen, S_COLOUR, pygame.Rect(left+13, top+18, 7, 2)) 
        pygame.draw.rect(screen, S_COLOUR, pygame.Rect(left+9, top+20, 15, 2)) 
        pygame.draw.rect(screen, S_COLOUR, pygame.Rect(left+11, top+22, 11, 2)) 
        pygame.draw.rect(screen, S_COLOUR, pygame.Rect(left+13, top+24, 7, 2)) 
    
    #Spades
    elif suit == 7:
        pygame.draw.rect(screen, S_COLOUR, pygame.Rect(left+15, top+5, 3, 19)) 
        pygame.draw.rect(screen, S_COLOUR, pygame.Rect(left+13, top+7, 7, 17)) 
        pygame.draw.rect(screen, S_COLOUR, pygame.Rect(left+11, top+9, 11, 15)) 
        pygame.draw.rect(screen, S_COLOUR, pygame.Rect(left+9, top+11, 15, 13)) 
        pygame.draw.rect(screen, S_COLOUR, pygame.Rect(left+7, top+13, 19, 11)) 
        pygame.draw.rect(screen, S_COLOUR, pygame.Rect(left+5, top+15, 10, 11)) 
        pygame.draw.rect(screen, S_COLOUR, pygame.Rect(left+18, top+15, 10, 11)) 
        pygame.draw.rect(screen, S_COLOUR, pygame.Rect(left+7, top+26, 6, 2)) 
        pygame.draw.rect(screen, S_COLOUR, pygame.Rect(left+20, top+26, 6, 2)) 
    elif suit == 4:
        pygame.draw.rect(screen, S_COLOUR, pygame.Rect(left+15, top+5, 3, 23)) 
        pygame.draw.rect(screen, S_COLOUR, pygame.Rect(left+13, top+7, 7, 14)) 
        pygame.draw.rect(screen, S_COLOUR, pygame.Rect(left+11, top+9, 11, 12)) 
        pygame.draw.rect(screen, S_COLOUR, pygame.Rect(left+9, top+11, 15, 10)) 
        pygame.draw.rect(screen, S_COLOUR, pygame.Rect(left+7, top+13, 19, 8)) 
        pygame.draw.rect(screen, S_COLOUR, pygame.Rect(left+5, top+15, 8, 8)) 
        pygame.draw.rect(screen, S_COLOUR, pygame.Rect(left+20, top+15, 8, 8)) 
        pygame.draw.rect(screen, S_COLOUR, pygame.Rect(left+5, top+25, 23, 3)) 
    elif suit == 8:
        pygame.draw.rect(screen, S_COLOUR, pygame.Rect(left+5, top+5, 23, 3)) 
        pygame.draw.rect(screen, S_COLOUR, pygame.Rect(left+15, top+8, 3, 20)) 
        pygame.draw.rect(screen, S_COLOUR, pygame.Rect(left+5, top+10, 8, 8)) 
        pygame.draw.rect(screen, S_COLOUR, pygame.Rect(left+20, top+10, 8, 8)) 
        pygame.draw.rect(screen, S_COLOUR, pygame.Rect(left+7, top+12, 19, 8)) 
        pygame.draw.rect(screen, S_COLOUR, pygame.Rect(left+9, top+20, 15, 2)) 
        pygame.draw.rect(screen, S_COLOUR, pygame.Rect(left+11, top+22, 11, 2))
        pygame.draw.rect(screen, S_COLOUR, pygame.Rect(left+13, top+24, 7, 2))
        pygame.draw.rect(screen, S_COLOUR, pygame.Rect(left+15, top+26, 3, 2))

def draw_card(rank, suit, stack, pos, clicked, moving = False):

    #When cards are meant to be in motion, coordinates are directly used;
    #When the staionary ones in the 16 various slots, slot numbers are used instead for simplicity

    #Clicked sequence, draggable
    if clicked == True:
        BORDERCOLOUR = LIGHTGREY
        CARDCOLOUR = BLACK

        if suit%2 == 0:
            C_COLOUR = WHITE
        else:
            C_COLOUR = TEAL
        left = stack
        top = pos

    else:
        BORDERCOLOUR = GREY
        CARDCOLOUR = WHITE

        if suit%2 == 0:
            C_COLOUR = BLACK
        else:
            C_COLOUR = RED
        if stack <= 4:
            left = 50 + 221 * (stack - 1)
            top = 30+75
        elif stack <= 8:
            left = 1114 + 221 * (stack - 5)
            top = 30+75
        else:
            left = 140 + 221 * (stack - 9)
            top = 47 * pos + 330+75
    
    #foundation_values = []
    #for x6 in foundations:
    #    foundation_values.append(x6[0])
    #foundation_num = min(foundation_values)+1

    if moving == True:
        left = stack
        top = pos

    pygame.draw.rect(screen, BORDERCOLOUR, pygame.Rect(left, top, 201, 280))
    pygame.draw.rect(screen, CARDCOLOUR, pygame.Rect(left+4, top+4, 193, 272))

    #For each number, the first half is the top left number,
    #and the latter is the bottom right upside down number

    if rank == 1:
        pygame.draw.rect(screen, C_COLOUR, pygame.Rect(left+3+10, top+4+7, 23, 29))
        pygame.draw.rect(screen, CARDCOLOUR, pygame.Rect(left+3+10, top+4+7, 6, 6))
        pygame.draw.rect(screen, CARDCOLOUR, pygame.Rect(left+3+10+17, top+4+7, 6, 6))
        pygame.draw.rect(screen, CARDCOLOUR, pygame.Rect(left+3+16, top+4+13, 11, 5))
        pygame.draw.rect(screen, CARDCOLOUR, pygame.Rect(left+3+16, top+4+24, 11, 12))

        pygame.draw.rect(screen, C_COLOUR, pygame.Rect(left+155+10, top+233+7, 23, 29))
        pygame.draw.rect(screen, CARDCOLOUR, pygame.Rect(left+155+10, top+233+7+23, 6, 6))
        pygame.draw.rect(screen, CARDCOLOUR, pygame.Rect(left+155+10+17, top+233+7+23, 6, 6))
        pygame.draw.rect(screen, CARDCOLOUR, pygame.Rect(left+155+16, top+240, 11, 12))
        pygame.draw.rect(screen, CARDCOLOUR, pygame.Rect(left+155+16, top+258, 11, 5))
        draw_suit(suit, left+32+52, top+67+56, clicked, False)

    if rank == 2:
        pygame.draw.rect(screen, C_COLOUR, pygame.Rect(left+3+10, top+4+7, 23, 29))
        pygame.draw.rect(screen, CARDCOLOUR, pygame.Rect(left+3+10, top+4+13, 17, 5))
        pygame.draw.rect(screen, CARDCOLOUR, pygame.Rect(left+3+16, top+4+24, 17, 6))

        pygame.draw.rect(screen, C_COLOUR, pygame.Rect(left+155+10, top+233+7, 23, 29))
        pygame.draw.rect(screen, CARDCOLOUR, pygame.Rect(left+155+10, top+233+13, 17, 6))
        pygame.draw.rect(screen, CARDCOLOUR, pygame.Rect(left+155+16, top+233+25, 17, 5))

        draw_suit(suit, left+32+52, top+67+56-76, clicked, False)
        draw_suit(suit+4, left+32+52, top+67+56+78, clicked, False)

    if rank == 3:
        pygame.draw.rect(screen, C_COLOUR, pygame.Rect(left+3+10, top+4+7, 23, 29))
        pygame.draw.rect(screen, CARDCOLOUR, pygame.Rect(left+3+10, top+4+13, 17, 5))
        pygame.draw.rect(screen, CARDCOLOUR, pygame.Rect(left+3+10, top+4+18, 6, 6))
        pygame.draw.rect(screen, CARDCOLOUR, pygame.Rect(left+3+10, top+4+24, 17, 6))

        pygame.draw.rect(screen, C_COLOUR, pygame.Rect(left+155+10, top+233+7, 23, 29))
        pygame.draw.rect(screen, CARDCOLOUR, pygame.Rect(left+155+16, top+233+13, 17, 6))
        pygame.draw.rect(screen, CARDCOLOUR, pygame.Rect(left+155+27, top+233+19, 6, 6))
        pygame.draw.rect(screen, CARDCOLOUR, pygame.Rect(left+155+16, top+233+25, 17, 5))

        draw_suit(suit, left+32+52, top+67+56-76, clicked, False)
        draw_suit(suit, left+32+52, top+67+56, clicked, False)
        draw_suit(suit+4, left+32+53, top+67+56+78, clicked, False)
        
    if rank == 4:
        pygame.draw.rect(screen, C_COLOUR, pygame.Rect(left+3+27, top+4+7, 6, 29))
        pygame.draw.rect(screen, C_COLOUR, pygame.Rect(left+3+10, top+4+18, 23, 6))
        pygame.draw.rect(screen, C_COLOUR, pygame.Rect(left+3+14, top+4+7, 6, 11))

        pygame.draw.rect(screen, C_COLOUR, pygame.Rect(left+155+10, top+233+7, 6, 29))
        pygame.draw.rect(screen, C_COLOUR, pygame.Rect(left+155+16, top+233+19, 17, 6))
        pygame.draw.rect(screen, C_COLOUR, pygame.Rect(left+155+23, top+233+25, 6, 11))

        draw_suit(suit, left+32+53-28, top+67+56-76, clicked, False)
        draw_suit(suit, left+32+53+26, top+67+56-76, clicked, False)
        draw_suit(suit+4, left+32+53-28, top+67+56+78, clicked, False)
        draw_suit(suit+4, left+32+53+26, top+67+56+78, clicked, False)

    if rank == 5:
        pygame.draw.rect(screen, C_COLOUR, pygame.Rect(left+3+10, top+4+7, 23, 29))
        pygame.draw.rect(screen, CARDCOLOUR, pygame.Rect(left+3+16, top+4+13, 17, 5))
        pygame.draw.rect(screen, CARDCOLOUR, pygame.Rect(left+3+10, top+4+24, 17, 6))

        pygame.draw.rect(screen, C_COLOUR, pygame.Rect(left+155+10, top+233+7, 23, 29))
        pygame.draw.rect(screen, CARDCOLOUR, pygame.Rect(left+155+16, top+233+13, 17, 6))
        pygame.draw.rect(screen, CARDCOLOUR, pygame.Rect(left+155+10, top+233+25, 17, 5))

        draw_suit(suit, left+32+53-28, top+67+56-76, clicked, False)
        draw_suit(suit, left+32+53+26, top+67+56-76, clicked, False)
        draw_suit(suit, left+32+52, top+67+56, clicked, False)
        draw_suit(suit+4, left+32+53-28, top+67+56+78, clicked, False)
        draw_suit(suit+4, left+32+53+26, top+67+56+78, clicked, False)
        
    if rank == 6:
        pygame.draw.rect(screen, C_COLOUR, pygame.Rect(left+3+10, top+4+7, 23, 29))
        pygame.draw.rect(screen, CARDCOLOUR, pygame.Rect(left+3+16, top+4+13, 17, 5))
        pygame.draw.rect(screen, CARDCOLOUR, pygame.Rect(left+3+16, top+4+24, 11, 6))

        pygame.draw.rect(screen, C_COLOUR, pygame.Rect(left+155+10, top+233+7, 23, 29))
        pygame.draw.rect(screen, CARDCOLOUR, pygame.Rect(left+155+10, top+233+25, 17, 5))
        pygame.draw.rect(screen, CARDCOLOUR, pygame.Rect(left+155+16, top+233+13, 11, 6))

        draw_suit(suit, left+32+53-28, top+67+56-76, clicked, False)
        draw_suit(suit, left+32+53+26, top+67+56-76, clicked, False)
        draw_suit(suit, left+32+53-28, top+67+56, clicked, False)
        draw_suit(suit, left+32+53+26, top+67+56, clicked, False)
        draw_suit(suit+4, left+32+53-28, top+67+56+78, clicked, False)
        draw_suit(suit+4, left+32+53+26, top+67+56+78, clicked, False)

    if rank == 7:
        pygame.draw.rect(screen, C_COLOUR, pygame.Rect(left+3+10, top+4+7, 23, 29))
        pygame.draw.rect(screen, CARDCOLOUR, pygame.Rect(left+3+10, top+4+13, 17, 23))

        pygame.draw.rect(screen, C_COLOUR, pygame.Rect(left+155+10, top+233+7, 23, 29))
        pygame.draw.rect(screen, CARDCOLOUR, pygame.Rect(left+155+16, top+233+7, 17, 23))

        draw_suit(suit, left+32+53-28, top+67+56-76, clicked, False)
        draw_suit(suit, left+32+53+26, top+67+56-76, clicked, False)
        draw_suit(suit, left+32+52, top+67+56+1-39, clicked, False)
        draw_suit(suit, left+32+53-28, top+67+56, clicked, False)
        draw_suit(suit, left+32+53+26, top+67+56, clicked, False)
        draw_suit(suit+4, left+32+53-28, top+67+56+78, clicked, False)
        draw_suit(suit+4, left+32+53+26, top+67+56+78, clicked, False)

    if rank == 8:
        pygame.draw.rect(screen, C_COLOUR, pygame.Rect(left+3+10, top+4+7, 23, 29))
        pygame.draw.rect(screen, CARDCOLOUR, pygame.Rect(left+3+16, top+4+13, 11, 5))
        pygame.draw.rect(screen, CARDCOLOUR, pygame.Rect(left+3+16, top+4+24, 11, 6))

        pygame.draw.rect(screen, C_COLOUR, pygame.Rect(left+155+10, top+233+7, 23, 29))
        pygame.draw.rect(screen, CARDCOLOUR, pygame.Rect(left+155+16, top+233+25, 11, 5))
        pygame.draw.rect(screen, CARDCOLOUR, pygame.Rect(left+155+16, top+233+13, 11, 6))

        draw_suit(suit, left+32+53-28, top+67+56-76, clicked, False)
        draw_suit(suit, left+32+53+26, top+67+56-76, clicked, False)
        draw_suit(suit, left+32+52, top+67+56+1-39, clicked, False)
        draw_suit(suit, left+32+53-28, top+67+56, clicked, False)
        draw_suit(suit, left+32+53+26, top+67+56, clicked, False)
        draw_suit(suit+4, left+32+52, top+67+56+56-17, clicked, False)
        draw_suit(suit+4, left+32+53-28, top+67+56+78, clicked, False)
        draw_suit(suit+4, left+32+53+26, top+67+56+78, clicked, False)

    if rank == 9:
        pygame.draw.rect(screen, C_COLOUR, pygame.Rect(left+3+10, top+4+7, 23, 29))
        pygame.draw.rect(screen, CARDCOLOUR, pygame.Rect(left+3+16, top+4+13, 11, 5))
        pygame.draw.rect(screen, CARDCOLOUR, pygame.Rect(left+3+10, top+4+24, 17, 6))

        pygame.draw.rect(screen, C_COLOUR, pygame.Rect(left+155+10, top+233+7, 23, 29))
        pygame.draw.rect(screen, CARDCOLOUR, pygame.Rect(left+155+16, top+233+13, 17, 6))
        pygame.draw.rect(screen, CARDCOLOUR, pygame.Rect(left+155+16, top+233+25, 11, 5))

        draw_suit(suit, left+32+53-28, top+67+56-76, clicked, False)
        draw_suit(suit, left+32+53+26, top+67+56-76, clicked, False)
        draw_suit(suit, left+32+53-28, top+67+56-18, clicked, False)
        draw_suit(suit, left+32+53+26, top+67+56-18, clicked, False)
        
        draw_suit(suit, left+32+52, top+67+56, clicked, False)

        draw_suit(suit, left+32+53-28, top+67+56+20, clicked, False)
        draw_suit(suit, left+32+53+26, top+67+56+20, clicked, False)
        draw_suit(suit+4, left+32+53-28, top+67+56+78, clicked, False)
        draw_suit(suit+4, left+32+53+26, top+67+56+78, clicked, False)

    if rank == 10:
        pygame.draw.rect(screen, C_COLOUR, pygame.Rect(left+3+7, top+4+7, 6, 29))
        pygame.draw.rect(screen, C_COLOUR, pygame.Rect(left+3+16, top+4+7, 20, 29))
        pygame.draw.rect(screen, CARDCOLOUR, pygame.Rect(left+3+22, top+4+13, 8, 17))

        pygame.draw.rect(screen, C_COLOUR, pygame.Rect(left+155+7, top+233+7, 20, 29))
        pygame.draw.rect(screen, C_COLOUR, pygame.Rect(left+155+30, top+233+7, 6, 29))
        pygame.draw.rect(screen, CARDCOLOUR, pygame.Rect(left+155+13, top+233+13, 8, 17))

        draw_suit(suit, left+32+53-28, top+67+56-76, clicked, False)
        draw_suit(suit, left+32+53+26, top+67+56-76, clicked, False)
        draw_suit(suit, left+32+53-28, top+67+56-18, clicked, False)
        draw_suit(suit, left+32+53+26, top+67+56-18, clicked, False)
        draw_suit(suit, left+32+52, top+67+56+1-48, clicked, False)
        draw_suit(suit+4, left+32+52, top+67+56+56-7, clicked, False)
        draw_suit(suit+4, left+32+53-28, top+67+56+20, clicked, False)
        draw_suit(suit+4, left+32+53+26, top+67+56+20, clicked, False)
        draw_suit(suit+4, left+32+53-28, top+67+56+78, clicked, False)
        draw_suit(suit+4, left+32+53+26, top+67+56+78, clicked, False)

    if rank == 11:
        pygame.draw.rect(screen, C_COLOUR, pygame.Rect(left+3+10, top+4+7, 23, 6))
        pygame.draw.rect(screen, C_COLOUR, pygame.Rect(left+3+22, top+4+13, 6, 23))
        pygame.draw.rect(screen, C_COLOUR, pygame.Rect(left+3+10, top+4+26, 6, 10))
        pygame.draw.rect(screen, C_COLOUR, pygame.Rect(left+3+16, top+4+30, 6, 6))

        pygame.draw.rect(screen, C_COLOUR, pygame.Rect(left+155+15, top+233+7, 6, 23))
        pygame.draw.rect(screen, C_COLOUR, pygame.Rect(left+155+21, top+233+7, 6, 6))
        pygame.draw.rect(screen, C_COLOUR, pygame.Rect(left+155+27, top+233+7, 6, 10))
        pygame.draw.rect(screen, C_COLOUR, pygame.Rect(left+155+10, top+233+30, 23, 6))

        pygame.draw.rect(screen, C_COLOUR, pygame.Rect(left+3+59, top+4+97, 77, 78))
        pygame.draw.rect(screen, CARDCOLOUR, pygame.Rect(left+3+75, top+4+97, 15, 8))
        pygame.draw.rect(screen, CARDCOLOUR, pygame.Rect(left+3+105, top+4+97, 15, 8))
        pygame.draw.rect(screen, CARDCOLOUR, pygame.Rect(left+3+59, top+4+113, 8, 46))
        pygame.draw.rect(screen, CARDCOLOUR, pygame.Rect(left+3+128, top+4+113, 8, 46))
        pygame.draw.rect(screen, CARDCOLOUR, pygame.Rect(left+3+67, top+4+121, 8, 30))
        pygame.draw.rect(screen, CARDCOLOUR, pygame.Rect(left+3+120, top+4+121, 8, 30))
        draw_suit(suit, left+59+25, top+97+27, clicked, embroider = True)

    if rank == 12:
        pygame.draw.rect(screen, C_COLOUR, pygame.Rect(left+3+10, top+4+7, 23, 29))
        pygame.draw.rect(screen, CARDCOLOUR, pygame.Rect(left+3+16, top+4+13, 11, 17))
        pygame.draw.rect(screen, C_COLOUR, pygame.Rect(left+3+23, top+4+36, 6, 4))

        pygame.draw.rect(screen, C_COLOUR, pygame.Rect(left+155+10, top+233+7, 23, 29))
        pygame.draw.rect(screen, CARDCOLOUR, pygame.Rect(left+155+16, top+233+13, 11, 17))
        pygame.draw.rect(screen, C_COLOUR, pygame.Rect(left+155+14, top+233+3, 6, 4))

        pygame.draw.rect(screen, C_COLOUR, pygame.Rect(left+3+59, top+4+97, 77, 78))
        pygame.draw.rect(screen, CARDCOLOUR, pygame.Rect(left+3+67, top+4+97, 27, 8))
        pygame.draw.rect(screen, CARDCOLOUR, pygame.Rect(left+3+101, top+4+97, 27, 8))
        pygame.draw.rect(screen, CARDCOLOUR, pygame.Rect(left+3+75, top+4+103, 12, 10))
        pygame.draw.rect(screen, CARDCOLOUR, pygame.Rect(left+3+108, top+4+103, 12, 10))
        pygame.draw.rect(screen, CARDCOLOUR, pygame.Rect(left+3+59, top+4+167, 16, 8))
        pygame.draw.rect(screen, CARDCOLOUR, pygame.Rect(left+3+120, top+4+167, 16, 8))
        draw_suit(suit, left+59+25, top+97+27, clicked, embroider = True)

    if rank == 13:
        pygame.draw.rect(screen, C_COLOUR, pygame.Rect(left+3+10, top+4+7, 6, 29))
        pygame.draw.rect(screen, C_COLOUR, pygame.Rect(left+3+16, top+4+18, 5, 6))
        pygame.draw.rect(screen, C_COLOUR, pygame.Rect(left+3+21, top+4+13, 6, 5))
        pygame.draw.rect(screen, C_COLOUR, pygame.Rect(left+3+21, top+4+24, 6, 6))
        pygame.draw.rect(screen, C_COLOUR, pygame.Rect(left+3+27, top+4+7, 6, 6))
        pygame.draw.rect(screen, C_COLOUR, pygame.Rect(left+3+27, top+4+30, 6, 6))

        pygame.draw.rect(screen, C_COLOUR, pygame.Rect(left+155+27, top+233+7, 6, 29))
        pygame.draw.rect(screen, C_COLOUR, pygame.Rect(left+155+9+1, top+233+7, 6, 6))
        pygame.draw.rect(screen, C_COLOUR, pygame.Rect(left+155+15+1, top+233+13, 6, 6))
        pygame.draw.rect(screen, C_COLOUR, pygame.Rect(left+155+21+1, top+233+19, 5, 6))
        pygame.draw.rect(screen, C_COLOUR, pygame.Rect(left+155+15+1, top+233+25, 6, 5))
        pygame.draw.rect(screen, C_COLOUR, pygame.Rect(left+155+9+1, top+233+30, 6, 6))

        pygame.draw.rect(screen, C_COLOUR, pygame.Rect(left+3+59, top+4+97, 77, 78))
        pygame.draw.rect(screen, CARDCOLOUR, pygame.Rect(left+3+59, top+4+159, 8, 16))
        pygame.draw.rect(screen, CARDCOLOUR, pygame.Rect(left+3+128, top+4+159, 8, 16))
        pygame.draw.rect(screen, CARDCOLOUR, pygame.Rect(left+3+59, top+4+97, 77, 14))
        pygame.draw.rect(screen, CARDCOLOUR, pygame.Rect(left+3+83, top+4+111, 3, 8))
        pygame.draw.rect(screen, CARDCOLOUR, pygame.Rect(left+3+109, top+4+111, 3, 8))
        pygame.draw.rect(screen, C_COLOUR, pygame.Rect(left+3+85, top+4+100, 25, 8))
        pygame.draw.rect(screen, C_COLOUR, pygame.Rect(left+3+93, top+4+97, 9, 16))
        draw_suit(suit, left+59+25, top+97+27, clicked, embroider = True)
    
    if suit == 1:
        draw_suit(1, left+8, top+43, clicked)
        draw_suit(1, left+160, top+204, clicked)

    if suit == 2:
        draw_suit(2, left+8, top+43, clicked)
        draw_suit(6, left+160, top+204, clicked)

    if suit == 3:
        draw_suit(3, left+8, top+43, clicked)
        draw_suit(7, left+160, top+204, clicked)

    if suit == 4:
        draw_suit(4, left+8, top+43, clicked)
        draw_suit(8, left+160, top+204, clicked)

def recognize_part(cascade_num, y_pos):

    #Decide whether it's a draggable sequence with the mouse coordinates at the time of click

    top_card = y_pos//47
    if top_card > len(cascades[cascade_num]) - 1:
        top_card = len(cascades[cascade_num]) - 1
    sequence = cascades[cascade_num][top_card:]
    
    draggable = True

    if len(sequence) > 1:
        colour_sequence = []

        #Set up colour sequence
        for j in sequence:
            if j[1] == 4 or j[1] == 2:
                colour_sequence.append(1)
            if j[1] == 3 or j[1] == 1:
                colour_sequence.append(2)
        
        for i in range(len(sequence)-1):
            #Make sure colours alternate
            if sequence[i][0] - sequence[i+1][0] != 1:
                draggable = False
            #Make sure the suit in downward continuous
            if colour_sequence[i] == colour_sequence[i+1]:
                draggable = False

    if draggable == True:
        return sequence
    else:
        return []

def display_graphics_part():

    #Background
    pygame.draw.rect(screen, BACKGROUND_2, pygame.Rect(0, 0, 2028, 1320))
    pygame.draw.rect(screen, BACKGROUND, pygame.Rect(10, 10+85, 2008, 1300-85))
    pygame.draw.rect(screen, BACKGROUND, pygame.Rect(10, 0, 2008, 95))

    #Foundations and Free Cells
    for i1 in range(4):
        pygame.draw.rect(screen, BACKGROUND_L, pygame.Rect(50+221*i1, 30+75, 201, 280))
        pygame.draw.rect(screen, BACKGROUND, pygame.Rect(50+20+221*i1, 30+20+75, 161, 240))
        pygame.draw.rect(screen, BACKGROUND_L2, pygame.Rect(1114+221*i1, 30+75, 201, 280))
        pygame.draw.rect(screen, BACKGROUND, pygame.Rect(1114+20+221*i1, 30+75+20, 161, 240))

    #Eight cascades
    for i2 in range(8):
        if len(cascades[i2]) == 0:
            pygame.draw.rect(screen, BACKGROUND_2, pygame.Rect(140+221*i2, 330+75, 201, 280))
            pygame.draw.rect(screen, BACKGROUND, pygame.Rect(140+20+221*i2, 330+20+75, 161, 240))

    #Logo
    pygame.draw.rect(screen, GREY, pygame.Rect(50, 0, 201, 85))
    pygame.draw.rect(screen, WHITE, pygame.Rect(50+4, 0, 193, 81))
    #F
    pygame.draw.rect(screen, RED, pygame.Rect(50+13, 10, 24, 29))
    pygame.draw.rect(screen, WHITE, pygame.Rect(50+13+6, 10+6, 18, 5))
    pygame.draw.rect(screen, WHITE, pygame.Rect(50+13+6, 10+17, 18, 12))
    pygame.draw.rect(screen, WHITE, pygame.Rect(50+13+18, 10+11, 6, 6))
    #R
    pygame.draw.rect(screen, RED, pygame.Rect(50+30+13, 10, 24, 29))
    pygame.draw.rect(screen, WHITE, pygame.Rect(50+30+13+6, 10+6, 12, 5))
    pygame.draw.rect(screen, WHITE, pygame.Rect(50+30+13+6, 10+17, 12, 12))
    pygame.draw.rect(screen, WHITE, pygame.Rect(50+30+13+18, 10+11, 6, 6))
    pygame.draw.rect(screen, WHITE, pygame.Rect(50+30+13+18, 10, 6, 6))
    #E
    pygame.draw.rect(screen, RED, pygame.Rect(50+60+13, 10, 24, 29))
    pygame.draw.rect(screen, WHITE, pygame.Rect(50+60+13+6, 10+6, 18, 5))
    pygame.draw.rect(screen, WHITE, pygame.Rect(50+60+13+6, 10+17, 18, 6))
    pygame.draw.rect(screen, WHITE, pygame.Rect(50+60+13+18, 10+11, 6, 6))
    #E
    pygame.draw.rect(screen, RED, pygame.Rect(50+90+13, 10, 24, 29))
    pygame.draw.rect(screen, WHITE, pygame.Rect(50+90+13+6, 10+6, 18, 5))
    pygame.draw.rect(screen, WHITE, pygame.Rect(50+90+13+6, 10+17, 18, 6))
    pygame.draw.rect(screen, WHITE, pygame.Rect(50+90+13+18, 10+11, 6, 6))
    #C
    pygame.draw.rect(screen, RED, pygame.Rect(50+13, 45, 24, 29))
    pygame.draw.rect(screen, WHITE, pygame.Rect(50+13+6, 45+6, 18, 17))
    #E
    pygame.draw.rect(screen, RED, pygame.Rect(50+30+13, 45, 24, 29))
    pygame.draw.rect(screen, WHITE, pygame.Rect(50+30+13+6, 45+6, 18, 5))
    pygame.draw.rect(screen, WHITE, pygame.Rect(50+30+13+6, 45+17, 18, 6))
    pygame.draw.rect(screen, WHITE, pygame.Rect(50+30+13+18, 45+11, 6, 6))
    #L
    pygame.draw.rect(screen, RED, pygame.Rect(50+60+13, 45, 24, 29))
    pygame.draw.rect(screen, WHITE, pygame.Rect(50+60+13+6, 45, 18, 23))
    #L
    pygame.draw.rect(screen, RED, pygame.Rect(50+90+13, 45, 24, 29))
    pygame.draw.rect(screen, WHITE, pygame.Rect(50+90+13+6, 45, 18, 23))

    #Autostack    
    if autostack == True:
        D_COLOUR = BACKGROUND
    else:
        D_COLOUR = LIGHTGREY

    pygame.draw.rect(screen, GREY, pygame.Rect(1114, 0, 201, 85))
    pygame.draw.rect(screen, WHITE, pygame.Rect(1114+4, 0, 193, 81))
    #A
    pygame.draw.rect(screen, D_COLOUR, pygame.Rect(1114+13, 10, 24, 29))
    pygame.draw.rect(screen, WHITE, pygame.Rect(1114+13, 10, 6, 6))#
    pygame.draw.rect(screen, WHITE, pygame.Rect(1114+13+18, 10, 6, 6))#
    pygame.draw.rect(screen, WHITE, pygame.Rect(1114+13+6, 10+6, 12, 5))
    pygame.draw.rect(screen, WHITE, pygame.Rect(1114+13+6, 10+17, 12, 12))
    #U
    pygame.draw.rect(screen, D_COLOUR, pygame.Rect(1114+30+13, 10, 24, 29))
    pygame.draw.rect(screen, WHITE, pygame.Rect(1114+30+13+6, 10, 12, 23))
    #T
    pygame.draw.rect(screen, D_COLOUR, pygame.Rect(1114+60+13, 10, 24, 6))
    pygame.draw.rect(screen, D_COLOUR, pygame.Rect(1114+60+13+9, 10+6, 6, 23))
    #O
    pygame.draw.rect(screen, D_COLOUR, pygame.Rect(1114+90+13, 10, 24, 29))
    pygame.draw.rect(screen, WHITE, pygame.Rect(1114+90+13+6, 10+6, 12, 17))
    
    #S
    pygame.draw.rect(screen, D_COLOUR, pygame.Rect(1114+13+6, 45, 18, 6))
    pygame.draw.rect(screen, D_COLOUR, pygame.Rect(1114+13, 45+6, 6, 5))
    pygame.draw.rect(screen, D_COLOUR, pygame.Rect(1114+13+6, 45+11, 12, 6))
    pygame.draw.rect(screen, D_COLOUR, pygame.Rect(1114+13+18, 45+17, 6, 6))
    pygame.draw.rect(screen, D_COLOUR, pygame.Rect(1114+13, 45+23, 18, 6))
    #T
    pygame.draw.rect(screen, D_COLOUR, pygame.Rect(1114+30+13, 45, 24, 6))
    pygame.draw.rect(screen, D_COLOUR, pygame.Rect(1114+30+13+9, 51, 6, 23))
    #A
    pygame.draw.rect(screen, D_COLOUR, pygame.Rect(1114+60+13, 45, 24, 29))
    pygame.draw.rect(screen, WHITE, pygame.Rect(1114+60+13, 45, 6, 6))
    pygame.draw.rect(screen, WHITE, pygame.Rect(1114+60+13+18, 45, 6, 6))
    pygame.draw.rect(screen, WHITE, pygame.Rect(1114+60+13+6, 45+6, 12, 5))
    pygame.draw.rect(screen, WHITE, pygame.Rect(1114+60+13+6, 45+17, 12, 12))
    #C
    pygame.draw.rect(screen, D_COLOUR, pygame.Rect(1114+90+13, 45, 24, 29))
    pygame.draw.rect(screen, WHITE, pygame.Rect(1114+90+13+6, 45+6, 18, 17))
    #K
    pygame.draw.rect(screen, D_COLOUR, pygame.Rect(1114+120+3+10, 45-7+7, 6, 29))
    pygame.draw.rect(screen, D_COLOUR, pygame.Rect(1114+120+3+16, 45-7+18, 6, 6))
    pygame.draw.rect(screen, D_COLOUR, pygame.Rect(1114+120+3+22, 45-7+13, 6, 5))
    pygame.draw.rect(screen, D_COLOUR, pygame.Rect(1114+120+3+22, 45-7+24, 6, 6))
    pygame.draw.rect(screen, D_COLOUR, pygame.Rect(1114+120+3+28, 45-7+7, 6, 6))
    pygame.draw.rect(screen, D_COLOUR, pygame.Rect(1114+120+3+28, 45-7+30, 6, 6))

    #Undo Button
    if len(game_log) > 0:
        F_COLOUR = YELLOW
    else:
        F_COLOUR = LIGHTGREY
    pygame.draw.rect(screen, GREY, pygame.Rect(1114+221, 0, 201, 85))
    pygame.draw.rect(screen, WHITE, pygame.Rect(1114+221+4, 0, 193, 81))
    #U
    pygame.draw.rect(screen, F_COLOUR, pygame.Rect(1114+221+13, 10, 24, 29))
    pygame.draw.rect(screen, WHITE, pygame.Rect(1114+221+13+6, 10, 12, 23))
    #N
    pygame.draw.rect(screen, F_COLOUR, pygame.Rect(1114+221+30+13, 10, 24, 29))
    pygame.draw.rect(screen, WHITE, pygame.Rect(1114+221+30+13+6, 10+6, 12, 23))
    #D
    pygame.draw.rect(screen, F_COLOUR, pygame.Rect(1114+221+60+13, 10, 24, 29))
    pygame.draw.rect(screen, WHITE, pygame.Rect(1114+221+60+13+6, 10+6, 12, 17))
    pygame.draw.rect(screen, WHITE, pygame.Rect(1114+221+60+13+18, 10, 6, 6))
    pygame.draw.rect(screen, WHITE, pygame.Rect(1114+221+60+13+18, 10+23, 6, 6))
    #O
    pygame.draw.rect(screen, F_COLOUR, pygame.Rect(1114+221+90+13, 10, 24, 29))
    pygame.draw.rect(screen, WHITE, pygame.Rect(1114+221+90+13+6, 10+6, 12, 17))
    #L
    pygame.draw.rect(screen, F_COLOUR, pygame.Rect(1114+221+13, 45, 24, 29))
    pygame.draw.rect(screen, WHITE, pygame.Rect(1114+221+13+6, 45, 18, 23))
    #A
    pygame.draw.rect(screen, F_COLOUR, pygame.Rect(1114+221+30+13, 45, 24, 29))
    pygame.draw.rect(screen, WHITE, pygame.Rect(1114+221+30+13, 45, 6, 6))
    pygame.draw.rect(screen, WHITE, pygame.Rect(1114+221+30+13+18, 45, 6, 6))
    pygame.draw.rect(screen, WHITE, pygame.Rect(1114+221+30+13+6, 45+6, 12, 5))
    pygame.draw.rect(screen, WHITE, pygame.Rect(1114+221+30+13+6, 45+17, 12, 12))
    #S
    pygame.draw.rect(screen, F_COLOUR, pygame.Rect(1114+221+13+60+6, 45, 18, 6))
    pygame.draw.rect(screen, F_COLOUR, pygame.Rect(1114+221+13+60, 45+6, 6, 5))
    pygame.draw.rect(screen, F_COLOUR, pygame.Rect(1114+221+13+60+6, 45+11, 12, 6))
    pygame.draw.rect(screen, F_COLOUR, pygame.Rect(1114+221+13+60+18, 45+17, 6, 6))
    pygame.draw.rect(screen, F_COLOUR, pygame.Rect(1114+221+13+60, 45+23, 18, 6))
    #T
    pygame.draw.rect(screen, F_COLOUR, pygame.Rect(1114+221+90+13, 45, 24, 6))
    pygame.draw.rect(screen, F_COLOUR, pygame.Rect(1114+221+90+13+9, 45+6, 6, 23))

    #Restart Button
    pygame.draw.rect(screen, GREY, pygame.Rect(1114+221*2, 0, 201, 85))
    pygame.draw.rect(screen, WHITE, pygame.Rect(1114+221*2+4, 0, 193, 81))
    #R
    pygame.draw.rect(screen, BLUE, pygame.Rect(1114+221*2+13, 10, 24, 29))
    pygame.draw.rect(screen, WHITE, pygame.Rect(1114+221*2+13+6, 10+6, 12, 5))
    pygame.draw.rect(screen, WHITE, pygame.Rect(1114+221*2+13+6, 10+17, 12, 12))
    pygame.draw.rect(screen, WHITE, pygame.Rect(1114+221*2+13+18, 10+11, 6, 6))
    pygame.draw.rect(screen, WHITE, pygame.Rect(1114+221*2+13+18, 10, 6, 6))
    #E
    pygame.draw.rect(screen, BLUE, pygame.Rect(1114+221*2+30+13, 10, 24, 29))
    pygame.draw.rect(screen, WHITE, pygame.Rect(1114+221*2+30+13+6, 10+6, 18, 5))
    pygame.draw.rect(screen, WHITE, pygame.Rect(1114+221*2+30+13+6, 10+17, 18, 6))
    pygame.draw.rect(screen, WHITE, pygame.Rect(1114+221*2+30+13+18, 10+11, 6, 6))
    #S
    pygame.draw.rect(screen, BLUE, pygame.Rect(1114+221*2+13+6, 45, 18, 6))
    pygame.draw.rect(screen, BLUE, pygame.Rect(1114+221*2+13, 45+6, 6, 5))
    pygame.draw.rect(screen, BLUE, pygame.Rect(1114+221*2+13+6, 45+11, 12, 6))
    pygame.draw.rect(screen, BLUE, pygame.Rect(1114+221*2+13+18, 45+17, 6, 6))
    pygame.draw.rect(screen, BLUE, pygame.Rect(1114+221*2+13, 45+23, 18, 6))
    #T
    pygame.draw.rect(screen, BLUE, pygame.Rect(1114+221*2+30+13, 45, 24, 6))
    pygame.draw.rect(screen, BLUE, pygame.Rect(1114+221*2+30+13+9, 51, 6, 23))
    #A
    pygame.draw.rect(screen, BLUE, pygame.Rect(1114+221*2+60+13, 45, 24, 29))
    pygame.draw.rect(screen, WHITE, pygame.Rect(1114+221*2+60+13, 45, 6, 6))#
    pygame.draw.rect(screen, WHITE, pygame.Rect(1114+221*2+60+13+18, 45, 6, 6))#
    pygame.draw.rect(screen, WHITE, pygame.Rect(1114+221*2+60+13+6, 45+6, 12, 5))
    pygame.draw.rect(screen, WHITE, pygame.Rect(1114+221*2+60+13+6, 45+17, 12, 12))
    #R
    pygame.draw.rect(screen, BLUE, pygame.Rect(1114+221*2+90+13, 45, 24, 29))
    pygame.draw.rect(screen, WHITE, pygame.Rect(1114+221*2+90+13+6, 45+6, 12, 5))
    pygame.draw.rect(screen, WHITE, pygame.Rect(1114+221*2+90+13+6, 45+17, 12, 12))
    pygame.draw.rect(screen, WHITE, pygame.Rect(1114+221*2+90+13+18, 45+11, 6, 6))
    pygame.draw.rect(screen, WHITE, pygame.Rect(1114+221*2+90+13+18, 45, 6, 6))
    #T
    pygame.draw.rect(screen, BLUE, pygame.Rect(1114+221*2+120+13, 45, 24, 6))
    pygame.draw.rect(screen, BLUE, pygame.Rect(1114+221*2+120+13+9, 51, 6, 23))

    #New Game Button
    pygame.draw.rect(screen, GREY, pygame.Rect(1114+221*3, 0, 201, 85))
    pygame.draw.rect(screen, WHITE, pygame.Rect(1114+221*3+4, 0, 193, 81))
    #N
    pygame.draw.rect(screen, RED, pygame.Rect(1114+221*3+13, 10, 24, 29))
    pygame.draw.rect(screen, WHITE, pygame.Rect(1114+221*3+13+6, 16, 12, 23))
    #E
    pygame.draw.rect(screen, RED, pygame.Rect(1114+221*3+30+13, 10, 24, 29))
    pygame.draw.rect(screen, WHITE, pygame.Rect(1114+221*3+30+13+6, 10+6, 18, 5))
    pygame.draw.rect(screen, WHITE, pygame.Rect(1114+221*3+30+13+6, 10+17, 18, 6))
    pygame.draw.rect(screen, WHITE, pygame.Rect(1114+221*3+30+13+18, 10+11, 6, 6))
    #W
    pygame.draw.rect(screen, RED, pygame.Rect(1114+221*3+60+13, 10, 24, 29))
    pygame.draw.rect(screen, WHITE, pygame.Rect(1114+221*3+60+13+6, 10, 3, 23))
    pygame.draw.rect(screen, WHITE, pygame.Rect(1114+221*3+60+13+15, 10, 3, 23))
    pygame.draw.rect(screen, WHITE, pygame.Rect(1114+221*3+60+13, 10+23, 6, 6))
    pygame.draw.rect(screen, WHITE, pygame.Rect(1114+221*3+60+13+18, 10+23, 6, 6))
    #G
    pygame.draw.rect(screen, RED, pygame.Rect(1114+221*3+13, 45, 24, 29))
    pygame.draw.rect(screen, WHITE, pygame.Rect(1114+221*3+13+6, 45+6, 12, 17))
    pygame.draw.rect(screen, WHITE, pygame.Rect(1114+221*3+13+18, 45+6, 6, 5))
    pygame.draw.rect(screen, RED, pygame.Rect(1114+221*3+13+12, 45+11, 6, 6))
    #A
    pygame.draw.rect(screen, RED, pygame.Rect(1114+221*3+30+13, 45, 24, 29))
    pygame.draw.rect(screen, WHITE, pygame.Rect(1114+221*3+30+13, 45, 6, 6))
    pygame.draw.rect(screen, WHITE, pygame.Rect(1114+221*3+30+13+18, 45, 6, 6))
    pygame.draw.rect(screen, WHITE, pygame.Rect(1114+221*3+30+13+6, 45+6, 12, 5))
    pygame.draw.rect(screen, WHITE, pygame.Rect(1114+221*3+30+13+6, 45+17, 12, 12))
    #M
    pygame.draw.rect(screen, RED, pygame.Rect(1114+221*3+60+13, 45, 24, 29))
    pygame.draw.rect(screen, WHITE, pygame.Rect(1114+221*3+60+13+6, 45+6, 3, 23))
    pygame.draw.rect(screen, WHITE, pygame.Rect(1114+221*3+60+13+15, 45+6, 3, 23))
    #E
    pygame.draw.rect(screen, RED, pygame.Rect(1114+221*3+90+13, 45, 24, 29))
    pygame.draw.rect(screen, WHITE, pygame.Rect(1114+221*3+90+13+6, 45+6, 18, 5))
    pygame.draw.rect(screen, WHITE, pygame.Rect(1114+221*3+90+13+6, 45+17, 18, 6))
    pygame.draw.rect(screen, WHITE, pygame.Rect(1114+221*3+90+13+18, 45+11, 6, 6))

def display_base_and_cascades():
    
    #This section displays everything, namely the cards on top of the (mostly) stationary background

    display_graphics_part()

    for f1 in freecells:
        if f1 != []:
            cell_num = freecells.index(f1)+1
            Card(f1[0], f1[1], cell_num, 0, clicked = False, moving = False)

    for f2 in foundations:
        if f2[0] > 0:
            cell_num = foundations.index(f2)#+1
            Card(f2[0], f2[1], cell_num+5, 0, clicked = False, moving = False)

    for c1 in cascades:
        for d1 in c1:
            cas_num = cascades.index(c1) + 9
            cas_pos = c1.index(d1)
            Card(d1[0], d1[1], cas_num, cas_pos, clicked = False, moving = False)

def autostack_hover():

    if 1114 <= pygame.mouse.get_pos()[0] <= 1114+201 and pygame.mouse.get_pos()[1] <= 85:
        D_COLOUR = YELLOW
    else:
        if autostack == True:
            D_COLOUR = BACKGROUND
        else:
            D_COLOUR = LIGHTGREY

    pygame.draw.rect(screen, GREY, pygame.Rect(1114, 0, 201, 85))
    pygame.draw.rect(screen, WHITE, pygame.Rect(1114+4, 0, 193, 81))
    #A
    pygame.draw.rect(screen, D_COLOUR, pygame.Rect(1114+13, 10, 24, 29))
    pygame.draw.rect(screen, WHITE, pygame.Rect(1114+13, 10, 6, 6))#
    pygame.draw.rect(screen, WHITE, pygame.Rect(1114+13+18, 10, 6, 6))#
    pygame.draw.rect(screen, WHITE, pygame.Rect(1114+13+6, 10+6, 12, 5))
    pygame.draw.rect(screen, WHITE, pygame.Rect(1114+13+6, 10+17, 12, 12))
    #U
    pygame.draw.rect(screen, D_COLOUR, pygame.Rect(1114+30+13, 10, 24, 29))
    pygame.draw.rect(screen, WHITE, pygame.Rect(1114+30+13+6, 10, 12, 23))
    #T
    pygame.draw.rect(screen, D_COLOUR, pygame.Rect(1114+60+13, 10, 24, 6))
    pygame.draw.rect(screen, D_COLOUR, pygame.Rect(1114+60+13+9, 10+6, 6, 23))
    #O
    pygame.draw.rect(screen, D_COLOUR, pygame.Rect(1114+90+13, 10, 24, 29))
    pygame.draw.rect(screen, WHITE, pygame.Rect(1114+90+13+6, 10+6, 12, 17))
    
    #S
    pygame.draw.rect(screen, D_COLOUR, pygame.Rect(1114+13+6, 45, 18, 6))
    pygame.draw.rect(screen, D_COLOUR, pygame.Rect(1114+13, 45+6, 6, 5))
    pygame.draw.rect(screen, D_COLOUR, pygame.Rect(1114+13+6, 45+11, 12, 6))
    pygame.draw.rect(screen, D_COLOUR, pygame.Rect(1114+13+18, 45+17, 6, 6))
    pygame.draw.rect(screen, D_COLOUR, pygame.Rect(1114+13, 45+23, 18, 6))
    #T
    pygame.draw.rect(screen, D_COLOUR, pygame.Rect(1114+30+13, 45, 24, 6))
    pygame.draw.rect(screen, D_COLOUR, pygame.Rect(1114+30+13+9, 51, 6, 23))
    #A
    pygame.draw.rect(screen, D_COLOUR, pygame.Rect(1114+60+13, 45, 24, 29))
    pygame.draw.rect(screen, WHITE, pygame.Rect(1114+60+13, 45, 6, 6))
    pygame.draw.rect(screen, WHITE, pygame.Rect(1114+60+13+18, 45, 6, 6))
    pygame.draw.rect(screen, WHITE, pygame.Rect(1114+60+13+6, 45+6, 12, 5))
    pygame.draw.rect(screen, WHITE, pygame.Rect(1114+60+13+6, 45+17, 12, 12))
    #C
    pygame.draw.rect(screen, D_COLOUR, pygame.Rect(1114+90+13, 45, 24, 29))
    pygame.draw.rect(screen, WHITE, pygame.Rect(1114+90+13+6, 45+6, 18, 17))
    #K
    pygame.draw.rect(screen, D_COLOUR, pygame.Rect(1114+120+3+10, 45-7+7, 6, 29))
    pygame.draw.rect(screen, D_COLOUR, pygame.Rect(1114+120+3+16, 45-7+18, 6, 6))
    pygame.draw.rect(screen, D_COLOUR, pygame.Rect(1114+120+3+22, 45-7+13, 6, 5))
    pygame.draw.rect(screen, D_COLOUR, pygame.Rect(1114+120+3+22, 45-7+24, 6, 6))
    pygame.draw.rect(screen, D_COLOUR, pygame.Rect(1114+120+3+28, 45-7+7, 6, 6))
    pygame.draw.rect(screen, D_COLOUR, pygame.Rect(1114+120+3+28, 45-7+30, 6, 6))

def undo_hover():
    if len(game_log) > 0:
        if 1114+221 <= pygame.mouse.get_pos()[0] <= 1114+221+201 and pygame.mouse.get_pos()[1] <= 85:
            B_COLOUR = BLUE
        else:
            B_COLOUR = YELLOW
    else:
        B_COLOUR = LIGHTGREY

    pygame.draw.rect(screen, GREY, pygame.Rect(1114+221, 0, 201, 85))
    pygame.draw.rect(screen, WHITE, pygame.Rect(1114+221+4, 0, 193, 81))
    #U
    pygame.draw.rect(screen, B_COLOUR, pygame.Rect(1114+221+13, 10, 24, 29))
    pygame.draw.rect(screen, WHITE, pygame.Rect(1114+221+13+6, 10, 12, 23))
    #N
    pygame.draw.rect(screen, B_COLOUR, pygame.Rect(1114+221+30+13, 10, 24, 29))
    pygame.draw.rect(screen, WHITE, pygame.Rect(1114+221+30+13+6, 10+6, 12, 23))
    #D
    pygame.draw.rect(screen, B_COLOUR, pygame.Rect(1114+221+60+13, 10, 24, 29))
    pygame.draw.rect(screen, WHITE, pygame.Rect(1114+221+60+13+6, 10+6, 12, 17))
    pygame.draw.rect(screen, WHITE, pygame.Rect(1114+221+60+13+18, 10, 6, 6))
    pygame.draw.rect(screen, WHITE, pygame.Rect(1114+221+60+13+18, 10+23, 6, 6))
    #O
    pygame.draw.rect(screen, B_COLOUR, pygame.Rect(1114+221+90+13, 10, 24, 29))
    pygame.draw.rect(screen, WHITE, pygame.Rect(1114+221+90+13+6, 10+6, 12, 17))
    #L
    pygame.draw.rect(screen, B_COLOUR, pygame.Rect(1114+221+13, 45, 24, 29))
    pygame.draw.rect(screen, WHITE, pygame.Rect(1114+221+13+6, 45, 18, 23))
    #A
    pygame.draw.rect(screen, B_COLOUR, pygame.Rect(1114+221+30+13, 45, 24, 29))
    pygame.draw.rect(screen, WHITE, pygame.Rect(1114+221+30+13, 45, 6, 6))
    pygame.draw.rect(screen, WHITE, pygame.Rect(1114+221+30+13+18, 45, 6, 6))
    pygame.draw.rect(screen, WHITE, pygame.Rect(1114+221+30+13+6, 45+6, 12, 5))
    pygame.draw.rect(screen, WHITE, pygame.Rect(1114+221+30+13+6, 45+17, 12, 12))
    #S
    pygame.draw.rect(screen, B_COLOUR, pygame.Rect(1114+221+13+60+6, 45, 18, 6))
    pygame.draw.rect(screen, B_COLOUR, pygame.Rect(1114+221+13+60, 45+6, 6, 5))
    pygame.draw.rect(screen, B_COLOUR, pygame.Rect(1114+221+13+60+6, 45+11, 12, 6))
    pygame.draw.rect(screen, B_COLOUR, pygame.Rect(1114+221+13+60+18, 45+17, 6, 6))
    pygame.draw.rect(screen, B_COLOUR, pygame.Rect(1114+221+13+60, 45+23, 18, 6))
    #T
    pygame.draw.rect(screen, B_COLOUR, pygame.Rect(1114+221+90+13, 45, 24, 6))
    pygame.draw.rect(screen, B_COLOUR, pygame.Rect(1114+221+90+13+9, 45+6, 6, 23))

def restart_hover():
    if 1114+221*2 <= pygame.mouse.get_pos()[0] <= 1114+221*2+201 and pygame.mouse.get_pos()[1] <= 85:
        B_COLOUR = RED
    else:
        B_COLOUR = BLUE

    pygame.draw.rect(screen, GREY, pygame.Rect(1114+221*2, 0, 201, 85))
    pygame.draw.rect(screen, WHITE, pygame.Rect(1114+221*2+4, 0, 193, 81))
    #R
    pygame.draw.rect(screen, B_COLOUR, pygame.Rect(1114+221*2+13, 10, 24, 29))
    pygame.draw.rect(screen, WHITE, pygame.Rect(1114+221*2+13+6, 10+6, 12, 5))
    pygame.draw.rect(screen, WHITE, pygame.Rect(1114+221*2+13+6, 10+17, 12, 12))
    pygame.draw.rect(screen, WHITE, pygame.Rect(1114+221*2+13+18, 10+11, 6, 6))
    pygame.draw.rect(screen, WHITE, pygame.Rect(1114+221*2+13+18, 10, 6, 6))
    #E
    pygame.draw.rect(screen, B_COLOUR, pygame.Rect(1114+221*2+30+13, 10, 24, 29))
    pygame.draw.rect(screen, WHITE, pygame.Rect(1114+221*2+30+13+6, 10+6, 18, 5))
    pygame.draw.rect(screen, WHITE, pygame.Rect(1114+221*2+30+13+6, 10+17, 18, 6))
    pygame.draw.rect(screen, WHITE, pygame.Rect(1114+221*2+30+13+18, 10+11, 6, 6))
    #S
    pygame.draw.rect(screen, B_COLOUR, pygame.Rect(1114+221*2+13+6, 45, 18, 6))
    pygame.draw.rect(screen, B_COLOUR, pygame.Rect(1114+221*2+13, 45+6, 6, 5))
    pygame.draw.rect(screen, B_COLOUR, pygame.Rect(1114+221*2+13+6, 45+11, 12, 6))
    pygame.draw.rect(screen, B_COLOUR, pygame.Rect(1114+221*2+13+18, 45+17, 6, 6))
    pygame.draw.rect(screen, B_COLOUR, pygame.Rect(1114+221*2+13, 45+23, 18, 6))
    #T
    pygame.draw.rect(screen, B_COLOUR, pygame.Rect(1114+221*2+30+13, 45, 24, 6))
    pygame.draw.rect(screen, B_COLOUR, pygame.Rect(1114+221*2+30+13+9, 51, 6, 23))
    #A
    pygame.draw.rect(screen, B_COLOUR, pygame.Rect(1114+221*2+60+13, 45, 24, 29))
    pygame.draw.rect(screen, WHITE, pygame.Rect(1114+221*2+60+13, 45, 6, 6))#
    pygame.draw.rect(screen, WHITE, pygame.Rect(1114+221*2+60+13+18, 45, 6, 6))#
    pygame.draw.rect(screen, WHITE, pygame.Rect(1114+221*2+60+13+6, 45+6, 12, 5))
    pygame.draw.rect(screen, WHITE, pygame.Rect(1114+221*2+60+13+6, 45+17, 12, 12))
    #R
    pygame.draw.rect(screen, B_COLOUR, pygame.Rect(1114+221*2+90+13, 45, 24, 29))
    pygame.draw.rect(screen, WHITE, pygame.Rect(1114+221*2+90+13+6, 45+6, 12, 5))
    pygame.draw.rect(screen, WHITE, pygame.Rect(1114+221*2+90+13+6, 45+17, 12, 12))
    pygame.draw.rect(screen, WHITE, pygame.Rect(1114+221*2+90+13+18, 45+11, 6, 6))
    pygame.draw.rect(screen, WHITE, pygame.Rect(1114+221*2+90+13+18, 45, 6, 6))
    #T
    pygame.draw.rect(screen, B_COLOUR, pygame.Rect(1114+221*2+120+13, 45, 24, 6))
    pygame.draw.rect(screen, B_COLOUR, pygame.Rect(1114+221*2+120+13+9, 51, 6, 23))

def newgame_hover():
    if 1114+221*3 <= pygame.mouse.get_pos()[0] <= 1114+221*3+201 and pygame.mouse.get_pos()[1] <= 85:
        B_COLOUR = TEAL
        C_COLOUR = BLACK
        pygame.draw.rect(screen, LIGHTGREY, pygame.Rect(1114+221*3, 0, 201, 85))
        pygame.draw.rect(screen, BLACK, pygame.Rect(1114+221*3+4, 0, 193, 81))
    else:
        B_COLOUR = RED
        C_COLOUR = WHITE
        pygame.draw.rect(screen, GREY, pygame.Rect(1114+221*3, 0, 201, 85))
        pygame.draw.rect(screen, WHITE, pygame.Rect(1114+221*3+4, 0, 193, 81))

    #N
    pygame.draw.rect(screen, B_COLOUR, pygame.Rect(1114+221*3+13, 10, 24, 29))
    pygame.draw.rect(screen, C_COLOUR, pygame.Rect(1114+221*3+13+6, 16, 12, 23))
    #E
    pygame.draw.rect(screen, B_COLOUR, pygame.Rect(1114+221*3+30+13, 10, 24, 29))
    pygame.draw.rect(screen, C_COLOUR, pygame.Rect(1114+221*3+30+13+6, 10+6, 18, 5))
    pygame.draw.rect(screen, C_COLOUR, pygame.Rect(1114+221*3+30+13+6, 10+17, 18, 6))
    pygame.draw.rect(screen, C_COLOUR, pygame.Rect(1114+221*3+30+13+18, 10+11, 6, 6))
    #W
    pygame.draw.rect(screen, B_COLOUR, pygame.Rect(1114+221*3+60+13, 10, 24, 29))
    pygame.draw.rect(screen, C_COLOUR, pygame.Rect(1114+221*3+60+13+6, 10, 3, 23))
    pygame.draw.rect(screen, C_COLOUR, pygame.Rect(1114+221*3+60+13+15, 10, 3, 23))
    pygame.draw.rect(screen, C_COLOUR, pygame.Rect(1114+221*3+60+13, 10+23, 6, 6))
    pygame.draw.rect(screen, C_COLOUR, pygame.Rect(1114+221*3+60+13+18, 10+23, 6, 6))
    #G
    pygame.draw.rect(screen, B_COLOUR, pygame.Rect(1114+221*3+13, 45, 24, 29))
    pygame.draw.rect(screen, C_COLOUR, pygame.Rect(1114+221*3+13+6, 45+6, 12, 17))
    pygame.draw.rect(screen, C_COLOUR, pygame.Rect(1114+221*3+13+18, 45+6, 6, 5))
    pygame.draw.rect(screen, B_COLOUR, pygame.Rect(1114+221*3+13+12, 45+11, 6, 6))
    #A
    pygame.draw.rect(screen, B_COLOUR, pygame.Rect(1114+221*3+30+13, 45, 24, 29))
    pygame.draw.rect(screen, C_COLOUR, pygame.Rect(1114+221*3+30+13, 45, 6, 6))
    pygame.draw.rect(screen, C_COLOUR, pygame.Rect(1114+221*3+30+13+18, 45, 6, 6))
    pygame.draw.rect(screen, C_COLOUR, pygame.Rect(1114+221*3+30+13+6, 45+6, 12, 5))
    pygame.draw.rect(screen, C_COLOUR, pygame.Rect(1114+221*3+30+13+6, 45+17, 12, 12))
    #M
    pygame.draw.rect(screen, B_COLOUR, pygame.Rect(1114+221*3+60+13, 45, 24, 29))
    pygame.draw.rect(screen, C_COLOUR, pygame.Rect(1114+221*3+60+13+6, 45+6, 3, 23))
    pygame.draw.rect(screen, C_COLOUR, pygame.Rect(1114+221*3+60+13+15, 45+6, 3, 23))
    #E
    pygame.draw.rect(screen, B_COLOUR, pygame.Rect(1114+221*3+90+13, 45, 24, 29))
    pygame.draw.rect(screen, C_COLOUR, pygame.Rect(1114+221*3+90+13+6, 45+6, 18, 5))
    pygame.draw.rect(screen, C_COLOUR, pygame.Rect(1114+221*3+90+13+6, 45+17, 18, 6))
    pygame.draw.rect(screen, C_COLOUR, pygame.Rect(1114+221*3+90+13+18, 45+11, 6, 6))

def drag_cards():

    #Have sequence of cards to follow the mouse while left button down

    display_base_and_cascades()

    for c2 in sequence:
        x_pos = pygame.mouse.get_pos()[0] - x_left_diff
        y_pos = pygame.mouse.get_pos()[1] - y_top_diff + 47 * sequence.index(c2)
        Card(c2[0], c2[1], x_pos, y_pos, clicked = True, moving = False)
    pygame.display.update()

def destination_decision(sequence, ori_cell, c_pos, m_pos, x_left_diff, y_top_diff, x_right_diff, y_btm_diff, double_click = False):
    
    #Once sequence of cards are dragged, they must go somewhere -- either where they were or a new location

    #Use five points - the mouse's coordinates at the instant of the mouse's left button up
    #as well as all four corners of the top card in the sequence, favouring the corner that points to the direction of motion

    target_list = []
    target_list.append(m_pos)

    top_left = [m_pos[0]-x_left_diff, m_pos[1]-y_top_diff]
    top_right = [m_pos[0]+x_right_diff, m_pos[1]-y_top_diff]
    btm_left = [m_pos[0]-x_left_diff, m_pos[1]+y_btm_diff]
    btm_right = [m_pos[0]+x_right_diff, m_pos[1]+y_btm_diff]

    if m_pos[1] < c_pos[1]:                                                                           #moved_up
        if m_pos[0] < c_pos[0]:                                                                       #moved_left
            target_list.append(top_left)
            target_list.append(top_right)
            target_list.append(btm_left)
            target_list.append(btm_right)
        else:                                                                                         #moved_right
            target_list.append(top_right)
            target_list.append(top_left)
            target_list.append(btm_right)
            target_list.append(btm_left)
    else:                                                                                             #moved_down
        if m_pos[0] < c_pos[0]:                                                                       #moved_left
            target_list.append(btm_left)
            target_list.append(btm_right)
            target_list.append(top_left)
            target_list.append(top_right)
        else:                                                                                         #moved_right                                                                 
            target_list.append(btm_right)
            target_list.append(btm_left)
            target_list.append(top_right)
            target_list.append(top_left)
    
    #-1 means back to where it was, >= 0 will be the new location
    target_cell = -1

    #Decide where the sequence can go
    for t1 in target_list:
        if len(sequence) == 1 and 30+75 <= t1[1] <= 385:
            #Foundations
            if 1114 <= t1[0] <= 1978:
                if foundations[sequence[0][1]-1][0] == sequence[0][0] - 1:
                    target_cell = sequence[0][1]-1 + 4
                    break
                    
            #Free Cells
            if 50 <= t1[0] <= 914:
                if (t1[0]-50)%221 <= 201:
                    cell_num = (t1[0]-50)//221
                    if len(freecells[cell_num]) == 0:
                        target_cell = cell_num
                        break
        
        #Cascades
        elif 140 <= t1[0] <= 1888 and 330+75 <= t1[1] <= 1320:
            if (t1[0]-140)%221 <= 201:
                target_cascade_num = (t1[0]-140)//221

                if target_cascade_num+8 != ori_cell:
                    
                    #Decide the max length of a moveable sequence given the space available 
                    empty_cells = len(list(enumerate(j1 for j1, x1 in enumerate(freecells) if x1 == [])))
                    empty_cascades = len(list(enumerate(j2 for j2, x2 in enumerate(cascades) if x2 == [])))
                    moveable = (empty_cells + 1) * (empty_cascades + 1)

                    if len(sequence) <= moveable:
                        #Empty cascade
                        if len(cascades[target_cascade_num]) == 0:
                            target_cell = target_cascade_num + 8
                            break
                        
                        #Suit and rank are both suitable for a move
                        else:
                            if cascades[target_cascade_num][-1][0] - sequence[0][0] == 1 and cascades[target_cascade_num][-1][1]%2 != sequence[0][1]%2:
                                target_cell = target_cascade_num + 8
                                break
    
    #Double click detected
    if double_click == True and target_cell < 0:
        first_empty = -1

        #Foundations are the first option
        for x7 in range(4):
            if (foundations[x7][0] == sequence[0][0] - 1) and foundations[x7][1] == sequence[0][1]:
                target_cell = sequence[0][1]-1 + 4
                break

        #If can't be stacked to foundation, then will consider the free cells
        if target_cell < 0:
            for x8 in range(4):
                if freecells[x8] == []:
                    first_empty = x8
                    break
        
        #Will send card to the first available space in the free cells (if any)
        if first_empty >= 0:
            target_cell = first_empty

    #Unable to find any destination - sequence moving back
    if target_cell < 0:
        target_cell = ori_cell

    #Log the move (if one) for the undo log
    if target_cell != ori_cell:
        game_log.append([])
        game_log[-1].append(sequence)
        game_log[-1].append(ori_cell)
        game_log[-1].append(target_cell)

    move_cards(sequence, m_pos, target_cell, x_left_diff, y_top_diff)
    sequence = []
    
    #Auto-complete is optional
    #(Written as AUTO STACK in game since the buttons only fit up to six letters at a time)

    if autostack == True:
        possible = True
        
        #Figure out which number to auto complete
        while possible == True:
            foundation_values = []
            for x5 in foundations:
                foundation_values.append(x5[0])
            fly_num = min(foundation_values)+1

            cascades_something = [0, 0, 0, 0, 0, 0, 0, 0]
            freecells_something = [0, 0, 0, 0]

            #From the cascades
            for ac1 in cascades:
                if len(ac1) > 0:
                    if ac1[-1][0] == fly_num:
                        auto_target_cell = ac1[-1][1]-1 + 4
                        auto_sequence = [ac1[-1]]
                        m_pos = []
                        m_pos.append(140+221*cascades.index(ac1))
                        m_pos.append(330+75+47*(len(ac1)-1))
                        cascades_something[cascades.index(ac1)] = 1
                        ac1.remove(ac1[-1])
                        
                        #Log the move
                        game_log.append([])
                        game_log[-1].append(auto_sequence)
                        game_log[-1].append(cascades.index(ac1)+8)
                        game_log[-1].append(auto_target_cell)

                        move_cards(auto_sequence, m_pos, auto_target_cell, 0, 0)

                        auto_sequence = []
            
            #From the free cells
            for ac2 in freecells:
                if len(ac2) > 0:
                    if ac2[0] == fly_num:
                        auto_target_cell = ac2[1]-1 + 4
                        auto_sequence = [ac2]
                        m_pos = []
                        m_pos.append(50+221*freecells.index(ac2))
                        m_pos.append(30+75)
                        temp_num = freecells.index(ac2)
                        freecells_something[freecells.index(ac2)] = 1
                        
                        #Log the move
                        game_log.append([])
                        game_log[-1].append(auto_sequence)
                        game_log[-1].append(freecells.index(ac2))
                        game_log[-1].append(auto_target_cell)

                        freecells.remove(ac2)
                        freecells.insert(temp_num, [])

                        move_cards(auto_sequence, m_pos, auto_target_cell, 0, 0)

                        auto_sequence = []
            
            #No possibility detected - quit loop
            if sum(cascades_something) == 0 and sum(freecells_something) == 0:
                possible = False
            
def move_cards(sequence, m_pos, target_cell, x_left_diff, y_top_diff):

    #Function to animate the moving process

    display_base_and_cascades()

    start_x_pos = m_pos[0] - x_left_diff
    start_y_pos_base = m_pos[1] - y_top_diff

    #Given the slot number, decide where the sequence is going

    #Free cells
    if 0 <= target_cell <= 3:
        des_x_pos = 50 + 221 * target_cell
        des_y_pos_base = 30+75

    #Foundations
    if 4 <= target_cell <= 7:
        des_x_pos = 1114 + 221 * (target_cell-4)
        des_y_pos_base = 30+75
    
    #Cascades
    if target_cell >= 8:
        des_x_pos = 140 + 221 * (target_cell-8)
        des_y_pos_base = 330+75 + len(cascades[target_cell-8]) * 47
    
    #Distance of motion in both x and y axis

    x_distance = start_x_pos - des_x_pos
    y_distance = start_y_pos_base - des_y_pos_base
    
    x_distance =  start_x_pos - des_x_pos
    y_distance =  start_y_pos_base - des_y_pos_base

    #This swing section animates a small amount of difference in trajetory for a sequence of more than one card
    x_swing_factor = 0
    y_swing_factor = 0

    if start_x_pos > des_x_pos: #Coming from right
        x_swing_factor = 1
    elif start_x_pos < des_x_pos: #Coming from left
        x_swing_factor = -1

    if start_y_pos_base > des_y_pos_base: #Coming from below
        y_swing_factor = 1
    elif start_y_pos_base < des_y_pos_base: #Coming from above
        y_swing_factor = -1

    if start_x_pos - des_x_pos != 0:
        x_swing_amount = math.log2(abs(start_x_pos - des_x_pos))
    else:
        x_swing_amount = 0
    if start_y_pos_base - des_y_pos_base != 0:
        y_swing_amount = math.log(abs(start_y_pos_base - des_y_pos_base))
    else:
        y_swing_amount = 0

    time_1 = 0
    time_t = 11
    
    moving = True

    while time_1 < time_t:
        clock.tick(58)

        display_base_and_cascades()
        for c3 in sequence:
            
            x_pos = start_x_pos - x_distance * (speed_chart)[time_1] + sequence.index(c3) * x_swing_factor * x_swing_amount
            y_pos = start_y_pos_base - y_distance * (speed_chart)[time_1] + 47 * sequence.index(c3) + y_swing_factor * y_swing_amount 
            
            Card(c3[0], c3[1], x_pos, y_pos, clicked = False, moving = True)
        pygame.display.update()

        time_1 += 1
        
    #Add the sequence to the new slot
    if 0 <= target_cell <= 3:
        freecells[target_cell] = []
        freecells[target_cell].append(sequence[0][0])
        freecells[target_cell].append(sequence[0][1])
    if 4 <= target_cell <= 7:
        foundations[target_cell-4][0] += 1
    if target_cell >= 8:
        for c4 in sequence:
            cascades[target_cell-8].append(c4)

    sequence = []

    #When all 4 Ks are up, game won
    foundation_values = []
    for x6 in foundations:
        foundation_values.append(x6[0])
    foundation_num = min(foundation_values)+1
    if foundation_num == 14:
        celebration()
    
    #Update the graphics is game is still on
    if foundation_num < 14:
        display_base_and_cascades()
        pygame.display.update()

def undo_last():

    #Reverse the previous move, up to the beginning

    #If anything has moved
    if len(game_log) > 0:
        action_item = game_log.pop()
        cur_pos = []
        if 0 <= action_item[2] <= 3:
            cur_pos.append(50 + 221 * action_item[2])
            cur_pos.append(30+75)
            freecells[action_item[2]] = []
        elif 4 <= action_item[2] <= 7:
            cur_pos.append(1114 + 221 * (action_item[2]-4))
            cur_pos.append(30+75)
            foundations[action_item[2]-4][0] -= 1
        else:
            cur_pos.append(140 + 221 * (action_item[2]-8))
            cur_pos.append(330+75 + len(cascades[action_item[2]-8]) * 47)
            for un1 in action_item[0]:
                cascades[action_item[2]-8].remove(un1)

            backup_action_item = []
            for un1a in action_item[0]:
                backup_action_item.append(un1a)
            backup_action_item.reverse()

        move_cards(action_item[0], cur_pos, action_item[1], 0, 0)

def celebration():

    #A little nostalgia

    x_rand_chart = []
    while len(x_rand_chart) < 4:
        x_rand_chart.append(random.randint(92, 108))
    
    for i1 in range(4):
        Card(13, i1+1, 1114 + 221*i1, 30+75, clicked = False, moving = True)

    for i1 in range(4):
        x_pos2 = 1114
        y_pos2 = 30+75
        time1 = 0
        dir1 = 1
        y_spd_chart = [0, 0, 0, 0, 1, 1, 2, 3, 4, 5, 6, 7, 9, 11, 12, 14, 16, 19, 21, 23, 26, 29, 31, 34, 38, 41, 44, 48, 51, 55, 59, 63, 67, 71, 76, 81, 86, 92, 98, 104, 111, 118]
        temp_y_spd_chart = []
        for sp1 in range(len(y_spd_chart)):
            temp_y_spd_chart.append(y_spd_chart[sp1])
        
        while x_pos2 > -201 - 221*i1:
            clock.tick(22)
            
            y_pos2 += temp_y_spd_chart[time1] * dir1
            x_pos2 -= int(32 * (x_rand_chart[i1]/100))

            if y_pos2 > 1040:
                y_pos2 = 1040
                temp_y_spd_chart = temp_y_spd_chart[:len(temp_y_spd_chart)-6]
                temp_y_spd_chart.reverse()
                time1 = 0
                dir1 *= -1
                
            time1 += 1

            Card(13, i1+1, 221*i1 + x_pos2, y_pos2, clicked = False, moving = True)
            pygame.display.update()
    
pygame.init()
screen = pygame.display.set_mode((2028, 1320))
clock = pygame.time.Clock()
pygame.display.set_caption('FREECELL')

#Colours
BACKGROUND = (36, 76, 26)
BACKGROUND_2 = (68, 108, 56)

BACKGROUND_L = (78, 112, 70)
BACKGROUND_L2 = (102, 146, 92)

WHITE = (236, 236, 232)
GREY = (138, 138, 128)
DARKGREY = (88, 88, 78)
LIGHTGREY = (188, 188, 178)
RED = (200, 22, 28)
BLACK = (26, 36, 46)
TEAL = (88, 146, 140)

YELLOW = (198, 122, 22)
BLUE = (46, 88, 168)

deck = []
freecells = [[], [], [], []]
foundations = [[0, 1], [0, 2], [0, 3], [0, 4]]
cascades = [[], [], [], [], [], [], [], []]
game_log = []
recent_click = []

clicked = False
moving = False
autostack = True

speed_chart = [0, 0.19, 0.36, 0.51, 0.64, 0.75, 0.84, 0.91, 0.96, 0.99, 1]

two_copies = new_game()
cascades = two_copies[0]
backup_cascades = two_copies[1]

undo_duo = 0

display_base_and_cascades()

while True:

    #Dragging cards
    if clicked == True:
        drag_cards()
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        #Mouse left button released
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if len(sequence) > 0:
                clicked = False
                double_click = False

                #If two consecutive clicks occur at the same place, it's considered a double click
                if len(sequence) == 1:
                    if len(recent_click) == 0:
                        recent_click.append(sequence[0])
                        recent_click.append(pygame.mouse.get_pos())
                    elif len(recent_click) == 2:
                        new_pos = pygame.mouse.get_pos()
                        if recent_click[0] == sequence[0] and recent_click[1] == new_pos:
                            double_click = True
                            recent_click = []
                        else:
                            recent_click = []

                destination_decision(sequence, ori_cell, clicking_pos, pygame.mouse.get_pos(), x_left_diff, y_top_diff, x_right_diff, y_btm_diff, double_click)

        #Mouse left button pressed
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            sequence = []
            
            #The four top right buttons
            if pygame.mouse.get_pos()[1] <= 85:

                #Autostack
                if 1114 <= pygame.mouse.get_pos()[0] <= 1114+201:
                    if autostack == True:
                        autostack = False
                    else:
                        autostack = True

                #Undo
                if 1114+221 <= pygame.mouse.get_pos()[0] <= 1114+221+201:
                    undo_last()
                    
                #Restart
                #Nearly identical to start new game, but not generating a new arrangement
                if 1114+221*2 <= pygame.mouse.get_pos()[0] <= 1114+221*2+201: 
                    autostack = True
                    game_log = []
                    sequence = [] 
                    freecells = [[], [], [], []]
                    foundations = [[0, 1], [0, 2], [0, 3], [0, 4]]
                    cascades = [[], [], [], [], [], [], [], []]
                    for bu2 in range(8):
                        for itj in range(len(backup_cascades[bu2])):
                            cascades[bu2].append(backup_cascades[bu2][itj])
                    display_base_and_cascades()

                #New game
                if 1114+221*3 <= pygame.mouse.get_pos()[0] <= 1114+221*3+201: 
                    autostack = True                
                    game_log = []
                    sequence = [] 
                    freecells = [[], [], [], []]
                    foundations = [[0, 1], [0, 2], [0, 3], [0, 4]]              
                    two_copies = new_game()
                    cascades = two_copies[0]
                    backup_cascades = two_copies[1]
                    display_base_and_cascades()
            
            #Free cells area
            if 50 <= pygame.mouse.get_pos()[0] <= 914 and 30+75 <= pygame.mouse.get_pos()[1] <= 385:                
                if (pygame.mouse.get_pos()[0]-50)%221 <= 201:                                                                     #If not clicking intervals between cards
                    cell_num = (pygame.mouse.get_pos()[0]-50)//221
                    if len(freecells[cell_num]) > 0:
                        sequence = [freecells[cell_num]]
                        freecells[cell_num] = []
                        clicked = True
                        ori_cell = cell_num
                        clicking_pos = pygame.mouse.get_pos()
                        x_left_diff = pygame.mouse.get_pos()[0] - (50 + 221 * cell_num)
                        y_top_diff = pygame.mouse.get_pos()[1] - (30 + 75)
                        x_right_diff = abs(x_left_diff-201)
                        y_btm_diff = abs(y_top_diff-280)

            #If clicking somewhere on one of the cards
            if 140 <= pygame.mouse.get_pos()[0] <= 1888 and 330+75 <= pygame.mouse.get_pos()[1] <= 1320:                
                if (pygame.mouse.get_pos()[0]-140)%221 <= 201:                                                                    #If not clicking intervals between cards      
                    cascade_num = (pygame.mouse.get_pos()[0]-140)//220                                                            #Determine which cascade clicked
                    cascade_len = 0                                                                                               #Determine length of that cascade
                    if len(cascades[cascade_num]) > 0:
                        cascade_len = (len(cascades[cascade_num]) - 1) * 47 + 280
                    if pygame.mouse.get_pos()[1]-(330+75) < cascade_len:                                                          #If clicking somewhere on one of the cards
                        sequence = recognize_part(cascade_num, pygame.mouse.get_pos()[1]-(330+75))
                        if len(sequence) > 0:
                            clicked = True
                            ori_cell = cascade_num + 8
                            clicking_pos = pygame.mouse.get_pos()
                            for i in sequence:
                                cascades[cascade_num].remove(i)
                                x_left_diff = pygame.mouse.get_pos()[0] - (140 + 221 * cascade_num)
                                y_top_diff = pygame.mouse.get_pos()[1] - ((len(cascades[cascade_num])) * 47 + 330+75)
                                x_right_diff = abs(x_left_diff-201)
                                y_btm_diff = abs(y_top_diff-280)

        #Ctrl + Z part - also can undo (identical to pressing the undo button)
        if event.type == pygame.KEYUP:
            if undo_duo > 0:
                undo_duo = 0

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LCTRL:
                undo_duo += 1
            if event.key == pygame.K_z:
                undo_duo += 1

            if undo_duo == 2:
                if len(game_log) > 0:
                    undo_last()

            if event.key == pygame.K_SPACE:
                pass

    if clicked == False and moving == False:
        undo_hover()
        restart_hover()
        newgame_hover()
        autostack_hover()
 
    pygame.display.update()

    clock.tick(30)
