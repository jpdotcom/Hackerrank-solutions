def unique_scores(scores):
    scores_copy=[-1]
    for i in range(len(scores)):
        if scores[i]!=scores_copy[len(scores_copy)-1]:
            scores_copy.append(scores[i])
    scores_copy.remove(-1)
    return scores_copy


def climbingLeaderboard(scores, alice):
    place=[]
    scores=unique_scores(scores)
    print(scores)
    for games in alice:
        i=0
        j=len(scores)-1
        k=int((i+j)/2)
        while abs(i-j)>1:
            if scores[k]>games:
                i=k
                k=int((i+j)/2)
            elif scores[k]<games:
                j=k
                k=int((i+j)/2)
            else:
                break
        if scores[k]==games:
            place.append(k+1)
        elif scores[i]>games and games>scores[j]:
            place.append(i+2)
        #next three booleans are edge cases (best score/lowest score/or equal to the lowest score)
        elif scores[i]<games:
            place.append(1)
        elif scores[j]>games:
            place.append(len(scores)+1)
        elif scores[j]==games:
            place.append(j+1)


scores=[100,90,90,80,75,60]
alice=[50,65,77,90,102,104,108]

print(climbingLeaderboard(scores,alice))