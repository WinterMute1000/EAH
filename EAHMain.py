import argparse
import time
from EmployeeNameGetter import EmployeeNameGetter
from IDGeneratorByName import IDGeneratorByName

parser = argparse.ArgumentParser()

# The part that organizes the Arguments.(Add more Arguments later)
parser.add_argument('--company', '-c', required=True, help="Input company name that generate candidate id")

args = parser.parse_args()
company_name = args.company
employee_name_getter = EmployeeNameGetter()
employee_name_list = employee_name_getter.get_employee_name(company_name)

employee_id_gen = IDGeneratorByName(employee_name_list)
employee_id_list = employee_id_gen.generate_id_list()

now_time = time.strftime('%Y-%m-%d', time.localtime(time.time()))

with open(company_name + '_candidate_id_list' + now_time + '.txt', 'w') as result_file:
    for employee_id in employee_id_list:
        result_file.write(employee_id)
