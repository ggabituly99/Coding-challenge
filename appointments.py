import json
import pandas as pd
import os


def main():
	createAppointment()
	# optimize()



def createAppointment():
	with open('data-set/CustomerData.json', 'r') as f:
		raw = f.read()
		customer_data  = json.loads(raw)


	with open('data-set/TellerData.json', 'r') as f:
		raw = f.read()
		teller_data  = json.loads(raw)

	teller_df = pd.DataFrame(teller_data['Teller'])
	customer_df = pd.DataFrame(customer_data['Customer'])
	appointment_path = 'appointments.json'

	if os.path.exists(appointment_path):
		os.remove(appointment_path)


	# Create type-teller dataset:

	type_teller  = {}

	for i, row in teller_df.iterrows():
		t = row['SpecialtyType']
		multiplier = float(row['Multiplier'])

		teller_id = row['ID']
		if t in type_teller.keys():
			type_teller[t][teller_id]= {'appointments':[], 'multiplier':multiplier,'total-time' : 0}
		else:
			type_teller[t] = {teller_id:{'appointments':[], 'multiplier':multiplier, 'total-time': 0}}



	t_index = 0


	for i, row in customer_df.iterrows():

		t = row['type']
		customer_id = row['Id']
		duration = row['duration']
		if t =='4':
			t = '0'
		customer_id = row['Id']

		try:
			current_teller = list(type_teller[t].keys())[t_index]
			type_teller[t][current_teller]['appointments'].append({'id':customer_id, 'duration':duration})
			type_teller[t][current_teller]['total-time'] += float(duration) * type_teller[t][current_teller]['multiplier']
			# print(current_teller)
			t_index+=1


		except Exception as e: 
			t_index = 0

			current_teller = list(type_teller[t].keys())[t_index]
			type_teller[t][current_teller]['appointments'].append({'id':customer_id, 'duration':duration})
			type_teller[t][current_teller]['total-time'] += float(duration) * type_teller[t][current_teller]['multiplier']
	  
			t_index+=1

	teller_appointments = {}

	for t, infos in type_teller.items():                  
		for k, v in infos.items():
			v['type'] = t
			teller_appointments[k] = v
	schedule = {}
	sorted_appointments =  sorted(teller_appointments.items(), key=lambda k_v: k_v[1]['total-time'])
	for x in sorted_appointments:
		schedule[x[0]] = x[1]
	

	while float(sorted_appointments[-1][1]["total-time"]) - float(sorted_appointments[0][1]["total-time"]) > 30:
	    for i, teller in enumerate(sorted_appointments):
	        if float(sorted_appointments[-i-1][1]["total-time"]) - float(sorted_appointments[i][1]["total-time"]) < 10:
	            break
	        min_teller = sorted_appointments[i]
	        max_teller = sorted_appointments[-i-1]
	        min_teller[1]['appointments'] = min_teller[1]['appointments']+max_teller[1]['appointments'][-1:]
	        min_teller[1]['total-time'] = sum([int(x['duration'])*float(min_teller[1]['multiplier']) for x in min_teller[1]['appointments']])
	        max_teller[1]['appointments'] = max_teller[1]['appointments'][0:-1]
	        max_teller[1]['total-time'] = sum([int(x['duration'])*float(max_teller[1]['multiplier']) for x in max_teller[1]['appointments']])
	    sorted_appointments =  sorted(schedule.items(), key=lambda k_v: k_v[1]['total-time']) 

	final_schedule = {}


	max_time = sorted_appointments[-1][1]['total-time']
	print(f"The teller {sorted_appointments[-1][0]} has the maximum time of {max_time}")

	print(f"The sum of all the appointments time in {sum([float(x[1]['total-time']) for x in sorted_appointments])}")




	for x in sorted_appointments:
	    final_schedule[x[0]] = x[1]
	optimized_path = 'appoitment_final.json'


	if os.path.exists(optimized_path):
	    os.remove(optimized_path)
	with open(optimized_path, 'w') as f:
		json.dump(final_schedule, f)


if __name__ == '__main__':
	main()