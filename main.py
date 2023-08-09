import json
from datetime import datetime

PARTICIPANTS = {}
def load_participants():
    global PARTICIPANTS
    with open("competitors2.json", encoding="utf-8") as file:       
        PARTICIPANTS = json.load(file)

def get_run_results():
    results_list = []
    with open("results_RUN.txt", "r", encoding="utf-8-sig") as results_file:
        line_start = results_file.readline()
        line_finish = results_file.readline()
        
        while line_start != '':
            
            participant = line_start.split(" ")[0]

            start_time_str = line_start.split(" ")[2][:-2]
            start_time = datetime.strptime(start_time_str,"%H:%M:%S,%f")

            finish_time_str = line_finish.split(" ")[2][:-2]
            finish_time = datetime.strptime(finish_time_str,"%H:%M:%S,%f")
            
            results_list.append((participant, finish_time-start_time))

            line_start = results_file.readline()
            line_finish = results_file.readline()
        
    results_list = sorted(results_list, key=lambda x: x[1])
    return results_list

def print_results(runs):
    global PARTICIPANTS
    place = 0
    print("Занятое место | Нагрудный номер | Имя | Фамилия | Результат")
    for run in runs:
        place += 1
        number = run[0]
        # В задаче не указано насколько точным должно быть выведено время пробега,
        # судя по данным оно всегда меньше часа, поэтому часы можно просто обрезать.
        # Так же поступил и с сотыми и меньшими секундами.
        print(str(place) + " | " + number + " | " + PARTICIPANTS[number]['Name'] + " | " + PARTICIPANTS[number]['Surname'] + " | " + str(run[1])[2:-4])
        

def main():
    # save competitors in local dictionary
    load_participants()
    
    # Handle main data (start, finish times)
    results = get_run_results()
    
    print_results(results)

if __name__=="__main__":
    main()