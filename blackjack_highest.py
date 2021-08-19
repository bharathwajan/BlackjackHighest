points={'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'ten':10,'jack':10,'queen':10,'king':10,'ace':11}
priority={'jack':13,'queen':12,'king':11}
priority_reverse={13:'jack',12:'queen',11:'king'}
#reverse_points={1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten',11:'king',12:'queen',13:'jack'}
def BlackjackHighest(strArr):
    dup=strArr #taking a duplicate for later usage
    numeric=[]
    for i in strArr:
        value=points[i]
        numeric.append(value)
    numeric_with_priority=[]
    for i in strArr:
        if i in priority:
            numeric_with_priority.append(priority[i])
        else:
            numeric_with_priority.append(points[i])
    #print('with priority',numeric_with_priority)    
    #print('without priority',numeric)
    if points['ace'] in numeric: # checking for ace card in parameter
        if sum(numeric)>21: #if sum is greater than 21
            index_of_ace=numeric.index(points['ace'])
            numeric[index_of_ace]=1 #changing the value of ace to 1
            sum_up=sum(numeric) 
            highest_card=max(numeric)
            if sum_up > 21:
                first_value='above'
            elif sum_up <21:
                first_value='below'
            elif sum_up ==21:
                first_value="blackjack"
            later_index=numeric.index(highest_card)
            second_value=dup[later_index]
            return first_value+' '+second_value
        else:#if sum is equals or less than 21 #no need change ace value # check first and highest
            highest_card=max(numeric)
            sum_up=sum(numeric)
            if sum_up > 21:
                first_value='above'
            elif sum_up <21:
                first_value='below'
            elif sum_up ==21:
                first_value="blackjack"
            later_index=numeric.index(highest_card)
            second_value=dup[later_index]
            return first_value+' '+second_value
    else: # if no ace card
        highest_card=max(numeric_with_priority)
        sum_up=sum(numeric)
        if sum_up > 21:
            first_value='above'
        elif sum_up <21:
            first_value='below'
        elif sum_up ==21:
            first_value="blackjack"
        #print(highest_card)
        later_index=numeric_with_priority.index(highest_card)
        second_value=numeric_with_priority[later_index]
        #print(second_value)
        return  first_value+' '+priority_reverse[second_value]

 
print(BlackjackHighest(["ace","queen"] )) #excepected above king
