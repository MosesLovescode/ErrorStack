from subprocess import Popen, PIPE
import requests
import webbrowser



def parse_output(output):
	args = output.split()
	proc = Popen(args,stdout=PIPE,stderr=PIPE)
	out, err = proc.communicate()
	return out, err

def find_solutions(error):
	rep = requests.get("https://api.stackexchange.com/" + "/2.2/search?order=desc&tagged=python&sort=activity&intitle={}&site=stackoverflow".format(error))
	return rep.json()

def get_address(json_dict):
	url_list = []
	count = 0
	for i in json_dict["items"]:
		if i["is_answered"]:
			url_list.append(i["link"])
			count += 1
		if count == 3 or count == len(i):
			break

		for i in url_list:
			webbrowser.open(i)
  
def stack(path):
	out ,err = parse_output(path)
	error = err.decode("utf-8").strip().split("\r\n")[-1]
	print(error)

	if error:
		filtered_error = error.split(":")
		json1 = find_solutions(filtered_error[0])
		json2 = find_solutions(filtered_error[1])
		json = find_solutions(error)

		get_address(json1)
		get_address(json2)
		get_address(json)
	else:
		print("no error")