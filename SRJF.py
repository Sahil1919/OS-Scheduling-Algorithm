

def execute_all_process():  

    remaining_sorted_process = sorted(dict(waiting_process).items(), key = lambda kv:kv[1][1])

    for process in remaining_sorted_process:

        prev_time = completed_process[-1][1][1]

        temp_process = [process[0],[process[1][0],process[1][1]+prev_time]]

        comp_time.append(temp_process)
        completed_process.append(temp_process)
    
def process_to_run(process:set,diff:int): 

    temp_diff = diff
          
    process_run_com = process[1][1] - diff

    # process_run_com = process_run_com if process_run_com >= 0 else diff-process[1][1] 

    if process_run_com > 0 :
        temp_process = [process[0],[process[1][0],process_run_com]]
        waiting_process.append(temp_process)

        update_sorted_process = list(process)

        if comp_time:
            
            update_sorted_process[1][1] =  comp_time[-1][1][1] + temp_diff

        else : update_sorted_process[1][1] =  process[1][1] - process_run_com
        
        return update_sorted_process
    
    else:
        diff = diff if process[1][1] >= diff else process[1][1]
        temp_process = [process[0],[process[1][0],completed_process[-1][1][1]+diff]]
        process_to_pop = [index for (index, item) in enumerate(waiting_process) if item[0] == process[0]]
        waiting_process.pop(process_to_pop[0])
        comp_time.append(temp_process)

        diff = temp_diff-diff
        
        return {'temp_process':temp_process,"remaining_time":diff}

if __name__ == "__main__":
    
    dict_obj = {"P1":[3,5],
            "P2":[1,3],
            "P3":[3,4],
            "P4":[5,1],
            # "P5":[5,1],
    }
    
    sorted_process = sorted(dict_obj.items(), key = lambda kv:kv[1])

    bt = [bt[1][1] for bt in sorted_process]

    print(sorted_process,"\n")

    waiting_process = []
    completed_process = []
    comp_time = []

    ct = 0
    for index, process in enumerate(sorted_process):           
        try:  
            if index == 0 and process[1][0] > 0:
                ct += process[1][0]

            diff = sorted_process[index+1][1][0] - sorted_process[index][1][0]


            if diff==0 or diff > 1:
                if diff==0:
                    diff = sorted_process[index+2][1][0] - sorted_process[index+1][1][0]
                    waiting_process.append(sorted_process[index+1])
                waiting_process.append(list(process))
                short_process = sorted(dict(waiting_process).items(), key= lambda kv:kv[1][1])
                temp_process = process_to_run(short_process[0],diff)

                try:
                    while temp_process['remaining_time'] > 0:
                        completed_process.append(temp_process['temp_process'])
                        short_process = sorted(dict(waiting_process).items(), key= lambda kv:kv[1][1])
                        temp_process = process_to_run(short_process[0], temp_process['remaining_time'])
                except Exception as e:
                    process_to_pop = [index for (index, item) in enumerate(waiting_process) if item[0] == temp_process[0]]
                    waiting_process.pop(process_to_pop[0])
                    temp_process[1][1] += ct
                    completed_process.append(temp_process)
                # finally:
                #     if (temp_process) == dict(): temp_process =  temp_process['temp_process']

                # completed_process.append(temp_process)


            else:
                process_to_run(sorted_process[index],diff)

                ct = ct+diff            

                temp_process = [process[0],[process[1][0],ct]] 
            
                completed_process.append(temp_process)

        except IndexError:
            
            temp_process = [sorted_process[index][0],[process[1][0],process[1][1]]]

            waiting_process.append(temp_process)
    
    execute_all_process()

    print("Gantt Chart for step by step process - ")
    for comp_process in completed_process:
        
        print(comp_process)

    print()
    print("Final Gantt Chart -- ")
    for process in comp_time:
        print(process) 

    tat = [ct[1][1]-ct[1][0] for ct in comp_time]

    wt  = [tat_time-wt for tat_time,wt in zip(tat,bt)]

    print()
    print("Average TAT - ", sum(tat)/len(dict_obj))
    print("Average WT - ", sum(wt)/len(dict_obj))


            