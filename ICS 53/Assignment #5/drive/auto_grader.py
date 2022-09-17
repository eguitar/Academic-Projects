import os
import sys
import time
import hashlib
from multiprocessing import Process
from subprocess import Popen, PIPE


def check_hash(file_name):
	os.chdir("..")
	local_path = "Client Domain/Local Directory/"
	remote_path = "Server Domain/Remote Directory/"

	try:
		file_1 = local_path + file_name
		md5_1 = hashlib.md5()
		file_1_hash = open(file_1, 'rb')
		file_1_bytes = file_1_hash.read()
		md5_1.update(file_1_bytes)

		file_2 = remote_path + file_name
		md5_2 = hashlib.md5()
		file_2_hash = open(file_2, 'rb')
		file_2_bytes = file_2_hash.read()
		md5_2.update(file_2_bytes)

		if md5_1.hexdigest() == md5_2.hexdigest():
			print("hash match for", file_name)
		else:
			print("error: hash did not match")
			print("hash of", file_1, "=", md5_1.hexdigest())
			print("hash of", file_2, "=", md5_2.hexdigest())
	except FileNotFoundError:
		print("error: file", file_name, "could not be found.")

	os.chdir("Client Domain")


def get_solutions1():
	expected_output_user_1 = []
	expected_output_user_1.append("Welcome to ICS53 Online Cloud Storage.")
	expected_output_user_1.append("> download hello.txt")
	expected_output_user_1.append("File [hello.txt] could not be found in remote directory.")
	expected_output_user_1.append("> upload helo.txt")
	expected_output_user_1.append("File [helo.txt] could not be found in local directory.")
	expected_output_user_1.append("> upload hello.txt")
	expected_output_user_1.append("11 bytes uploaded successfully.")
	expected_output_user_1.append("hash hello.txt")  # Special command for the autograder.
	expected_output_user_1.append("> append hello.txt")
	expected_output_user_1.append("Appending> more hello world")
	expected_output_user_1.append("Appending> pause 2")
	expected_output_user_1.append("Appending> close")
	expected_output_user_1.append("> quit")

	return expected_output_user_1


def get_solutions2():

	expected_output_user_2 = []
	expected_output_user_2.append("Welcome to ICS53 Online Cloud Storage.")
	expected_output_user_2.append("> download hello.txt")
	expected_output_user_2.append("File [hello.txt] is currently locked by another user.")
	expected_output_user_2.append("> syncheck hello.txt")
	expected_output_user_2.append("Sync Check Report:")
	expected_output_user_2.append("- Local Directory:")
	expected_output_user_2.append("-- File Size: 11 bytes.")
	expected_output_user_2.append("- Remote Directory:")
	expected_output_user_2.append("-- File Size: 28 bytes.")
	expected_output_user_2.append("-- Sync Status: unsynced.")
	expected_output_user_2.append("-- Lock Status: locked.")
	expected_output_user_2.append("> pause 2")
	expected_output_user_2.append("> download hello.txt")
	expected_output_user_2.append("28 bytes downloaded successfully.")
	expected_output_user_2.append("hash hello.txt")  # Special command for the autograder.
	expected_output_user_2.append("> close")
	expected_output_user_2.append("Command [close] is not recognized.")
	expected_output_user_2.append("> quit")

	return expected_output_user_2


def run_process(run_command, command_file):
	if command_file == "user1_commands.txt":
		expected_output = get_solutions1()

	if command_file == "user2_commands.txt":
		expected_output = get_solutions2()

	if command_file == "server":
		os.chdir("Server Domain")
		process = Popen(run_command, stdout=PIPE, shell=True)
		# os.system(run_command)
		return

	os.chdir("Client Domain")
	process = Popen(run_command, stdout=PIPE, shell=True)
	print("start executing commands from", command_file)
	for i in range(0, len(expected_output)):
		if expected_output[i][:4] == "hash":  # Note that download/upload then append will not actually be tested in the same test case.
			file_name = expected_output[i][5:]
			check_hash(file_name)
			continue

		line = process.stdout.readline().rstrip().decode('utf')
		if not line:
			break
		# print(line)
		if line == expected_output[i]:
			print("line", i, "from", command_file, ": match")
		else:
			print("mismatch")
			print("line", i, ":", line)
			print("expected_output", i, ":", expected_output[i])

	
if __name__ == "__main__":

	# This python script will be used to grade assignment 5 but with a different scenario than the one used here.
	# The assignment submission assumes the assignment to be zipped in "Assignment 5.zip" folder.
	# If you don't want to zip your assignment everytime you want to test this auto_grader, comment the below line.
	# os.system("unzip Assignment\ 5.zip")

	# These two file are assumed to be outside the "Assignment 5" folder and it will be created and used by the graders,
	# so please make sure not to submit them with your assignment after you finish testing.
	user_1 = "user1_commands.txt"
	user_2 = "user2_commands.txt"
	os.system("cp " + user_1 + " Assignment\ 5/Client\ Domain")
	os.system("cp " + user_2 + " Assignment\ 5/Client\ Domain")

	os.chdir("Assignment 5")

	os.system("python3 auto_compile.py")

	# The IP address assumed in this test case is "127.0.0.1". Feel free to change it.
	sever_run_commnad = "./server 127.0.0.1"
	server_process = Process(target=run_process, args=(sever_run_commnad, "server", ))
	server_process.start()

	client1_run_commnad = "./client " + user_1 + " 127.0.0.1"
	client1_process = Process(target=run_process, args=(client1_run_commnad, user_1, ))
	client1_process.start()

	#--------------------------------------------#
	# If you want to test a two-users scenario (multithreading), uncomment the below lines.
	# --------------------------------------------#
	time.sleep(1)  # The second client starts after 1 second in this test case (like in Assignment 5).
	client2_run_commnad = "./client " + user_2 + " 127.0.0.1"
	client2_process = Process(target=run_process, args=(client2_run_commnad, user_2, ))
	client2_process.start()


