if __name__ == "__main__":
    
    # dict_obj = {"P1":[0,2],
    #         "P2":[1,2],
    #         "P3":[5,3],
    #         "P4":[6,4],
    # }   
    dict_obj = {"P1":[1,3],
            "P2":[2,4],
            "P3":[1,2],
            "P4":[4,4],
    }   
    
    sorted_process = sorted(dict_obj.items(), key = lambda kv: kv[1])
    
    print(sorted_process)
    
    ct = 0
    wt=0
    swt=0
    stat=0
    print('PID|',"AT|","BT|","CT|","TAT|","WT")
    for index, process in enumerate(sorted_process):
        if index == 0 and process[1][0] != 0:
            ct = ct+process[1][0]

        diff = process[1][0] - ct
        if diff > 0 :
            ct += diff

        ct = ct + process[1][1]
        tat = ct - process[1][0]
        stat=tat+stat
        wt = tat-process[1][1]
        swt = wt+swt
        print(process[0],'|', process[1][0],'|',process[1][1],'|',ct,"|",tat,"|",wt)
       
print("Average TAT = ",stat/ len(dict_obj))
print("Average Waiting time = ", swt/ len(dict_obj))