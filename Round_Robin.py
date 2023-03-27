

def process_to_run(process: set):

    executed_process = process[1][1]-time_quantum

    temp_process = [process[0],[process[1][0],executed_process]]

    if executed_process >= 1:
        process_to_pop = [index for (index, item) in enumerate(waiting_process) if item[0] == process[0]]
        waiting_process.pop(process_to_pop[0])
        waiting_process.append(temp_process)
       
        if not completed_process:
            executed_process = process[1][1] - executed_process
        else:
            executed_process = completed_process[-1][1][1] + (
                process[1][1] - executed_process)

        temp_process = [process[0], [process[1][0], executed_process]]
        completed_process.append(temp_process)
        
        return temp_process
    
    else:      
        if completed_process:
            update_time = completed_process[-1][1][1] +process[1][1]
        else:
            update_time = process[1][1] + time_quantum if process[1][1] >= 2 else process[1][1]
            
        temp_process = [process[0],[process[1][0],update_time]]
        process_to_pop = [index for (index, item) in enumerate(waiting_process) if item[0] == process[0]]
        waiting_process.pop(process_to_pop[0])
        comp_time.append(temp_process)
        completed_process.append(temp_process)

        return temp_process


if __name__ == '__main__':

    dict_obj = {"P1": [0, 10],
                "P2": [1, 4],
                "P3": [2, 5],
                "P4": [3, 3],
                # "P5": [5, 6],
                }
    # dict_obj = {"P1": [3, 2],
    #             "P2": [1, 3],
    #             "P3": [0, 1],
    #             "P4": [6, 4],
    #             "P5": [5, 6],
    #             }

    time_quantum = 2

    sorted_process = sorted(dict_obj.items(), key=lambda kv: kv[1])

    bt = [bt[1][1] for bt in sorted_process]

    print(sorted_process, "\n")

    waiting_process = []
    completed_process = []
    comp_time = []

    ct = 0
    next_index = 0
    for index, process in enumerate(sorted_process):

        try:
            if index == 0 or index == len(sorted_process)-2 : 
                ct+=process[1][0]
                diff = sorted_process[index+1][1][0] - sorted_process[index][1][0] 
                
            else: diff =   process[1][1] - completed_process[-1][1][1]

            if index == len(sorted_process) - 1: 
                diff = sorted_process[index+2][1][0] - sorted_process[index+1][1][0]
                

            if diff == 0 or diff > 1:
                
                if diff == 0:
                    waiting_process.append(sorted_process[index])
                    continue

                while completed_process[-1][1][1] >= sorted_process[next_index+1][1][0]:
                    waiting_process.append(list(sorted_process[index+1]))

                short_process = sorted(dict(waiting_process).items(), key=lambda kv: kv[1][1])
                temp_process = process_to_run(short_process[0])
            
                if temp_process[1][1] - sorted_process[index][1][1] > 0 and index != len(sorted_process) - 2:

                    short_process = sorted(dict(waiting_process).items(), key=lambda kv: kv[1][1])
                    temp_process = process_to_run(short_process[0])   
               

            else:
                if not waiting_process and index==0: waiting_process.append(process)
                short_process = sorted(dict(waiting_process).items(), key=lambda kv: kv[1][1])
                process_to_run(short_process[0])
                while completed_process[-1][1][1] >= sorted_process[next_index+1][1][0]:
                    waiting_process.append(list(sorted_process[next_index+1]))
                    next_index += 1

        except IndexError as e:
           
            while waiting_process:
                    
                short_process = sorted(dict(waiting_process).items(), key=lambda kv: kv[1][1])
                temp_process = process_to_run(short_process[0])
            
                if waiting_process:
                    if temp_process[1][1] - waiting_process[-1][1][1] > 0:

                        short_process = sorted(dict(waiting_process).items(), key=lambda kv: kv[1][1])
                        temp_process = process_to_run(short_process[0])   

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
                

