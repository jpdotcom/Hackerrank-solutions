def find_best_team(topic):
    all_comb=[]
    smart_boi=0
    temp=0
    all_good_teams=0
    for i in range(0,len(topic)-1):
        b=int(topic[i])
        for j in range(i,len(topic)):
            if i!=j:
                c=int(topic[j])
                total_topics=str(b+c)
                for k in range(0,len(total_topics)):
                    if total_topics[k]=="1" or total_topics[k]=="2":
                        temp+=1
                all_comb.append(temp)
                smart_boi=max(smart_boi,temp)
                temp=0
    print(all_comb)
    for scores in all_comb:
        if scores==smart_boi:
            all_good_teams+=1
    return (smart_boi,all_good_teams)


topic=['10101', '11100', '11010', '00101']

print(find_best_team(topic))



        

