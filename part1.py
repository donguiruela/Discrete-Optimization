    sample = items
    value_arr = []
    taken_arr = []

    def get_value (arr) :
        return arr.value

    while(True) :        
        value = 0
        weight = 0
        taken = [0]*len(items)    

        # iterate each item        

        for item in sample :
            if weight + item.weight <= capacity :
                taken[item.index] = 1
                value += item.value
                weight += item.weight
                        
        value_arr.append(value)
        taken_arr.append(taken)

        # resize the array by ignoring every first element of previous array        
        
        sample = sample[1::]
        sample.sort(key = get_value, reverse = True)    
        
        ref = 0
        max = 0        
        
        # determine the index of the max value to match its corresponding taken value

        for i in range(0, len(value_arr)) :
            if value_arr[i] > ref :
                max = i
                ref = value_arr[i]            
               
        # output                

        if len(sample) == 0 :            
            output_data = str(value_arr[max]) + ' ' + str(1) + '\n'
            output_data += ' '.join(map(str, taken_arr[max]))
            return output_data
