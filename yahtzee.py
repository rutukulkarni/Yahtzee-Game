import sys

dices = []

def predict_next_dice_roll(roll_count, score):
    probabilities = []
    if len(roll_count.keys()) == 1:
        print 'Bingo!!'
        score += 25
        return

    if len(roll_count.keys()) > 1:
        probabilities.append(float(dice_1)/6)
        probabilities.append(float(dice_2)/6)
        probabilities.append(float(dice_3)/6)
        for i in range(3):
            if probabilities[i] < 0.5:
                print 'Re-roll dice ',i+1
        return
        print 'Do not roll'
        return

def get_roll_count(score):
    roll_count ={}
    if dice_1 not in roll_count:    roll_count[dice_1] = 1
    else:   roll_count[dice_1]+=1
    if dice_2 not in roll_count:    roll_count[dice_2] = 1
    else:   roll_count[dice_2]+=1
    if dice_3 not in roll_count:    roll_count[dice_3] = 1
    else:   roll_count[dice_3]+=1

    predict_next_dice_roll(roll_count, score)


if __name__== '__main__':
    "command line arguments"
    print 'in'
    dice_1 = sys.argv[1]
    print dice_1
    dice_2 = sys.argv[2]
    dice_3  = sys.argv[3]

    dices.append(dice_1)
    dices.append(dice_2)
    dices.append(dice_3)
    print dices
    score = 0
    get_roll_count(score)