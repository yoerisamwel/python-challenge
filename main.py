import os
import csv
import operator

company_budget_csv = os.path.join("PyBank", "budget_data.csv")
election_data_csv = os.path.join("PyPoll", "election_data.csv")

output_file = open("output.txt", "a")

with open(company_budget_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csv_reader)
    profit_loss_list = []
    count = 0
    profit_loss_list_both = []
    for row in csv_reader:
        count += 1
        profit_loss_list_both.append(row)
        profit_loss_list.append(row[1])
    profit_loss_int = [eval(number) for number in profit_loss_list]
    profit_loss_sum = sum(profit_loss_int)
    profit_loss_mean = round((sum(profit_loss_int) / len(profit_loss_int)),0)
    profit_loss_max = max(profit_loss_list_both)
    profit_loss_min = min(profit_loss_list_both)

    print('Financial Analysis', file=output_file)
    print('-------------------------------', file=output_file)
    print('Total Months: ' + str(count), file=output_file)
    print('Total: $' + str(profit_loss_sum), file=output_file)
    print('Average Change: $' + str(profit_loss_mean).strip("[]"), file=output_file)
    print('Greatest Increase in Profits: ' + '(' + str(profit_loss_max).strip("[]") + ')', file=output_file)
    print('Greatest Decrease in Profits: ' + '(' + str(profit_loss_max).strip("[]") + ')', file=output_file)

with open(election_data_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csv_reader)
    appended_list = []
    count2 = 0
    election_results_dict = {}
    for row in csv_reader:
        count2 += 1
        x = row[2]
        if x in election_results_dict:
            y = election_results_dict[x] + 1
            election_results_dict.update({x: y})
        else:
            election_results_dict.update({x: 1})
    #got the code below from stack overflow
    election_winner = max(election_results_dict.items(), key=operator.itemgetter(1))[0]

    print('', file=output_file)
    print('Election Results', file=output_file)
    print('-------------------------------', file=output_file)
    print('Total Votes: ' + str(count2), file=output_file)
    for result in election_results_dict:
        print(result + ': ' + str(round(election_results_dict[result] / count2 * 100,3)) +
               '%' + ' ' + str(election_results_dict[result]), file=output_file)
    print('Winner: ' + election_winner, file=output_file)

output_file.close()






