#Defining winner
def determine_winner(player1, player2):
    player1_posb = calculate_posb(player1)
    player2_posb = calculate_posb(player2)

    if player1_posb>player2_posb:
        return "Ashok"
    elif player1_posb<player2_posb:
        return "Anand"
    else:
        return "Draw"

#Calculating possibilities
def calculate_posb(tree_row):
    posb_count = 0
    row_length = len(tree_row)

    for i in range(row_length - 2):
        for j in range(i + 1, row_length - 1):
            for k in range(j + 1, row_length):
                if tree_row[i] != tree_row[j] and tree_row[j] != tree_row[k]:
                    posb_count += 1
    print(posb_count)
    return posb_count

#Input
Ashok = input().strip()
Anand = input().strip()

#Output
winner_result = determine_winner(Ashok, Anand)
print(winner_result)
