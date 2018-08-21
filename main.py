#! /usr/bin/python3 
# -*- coding: utf-8 -*-
import csv
import json
import sys
import os
import subprocess

def main():
	exit_commands = ['exit', 'exit()', '\\q']

	if len(sys.argv) < 3:
		print("Json file filename and filename to write csv data are required.")
		input_file = str(input("\nEnter valid json file name or print exit to exit: "))
		if input_file in exit_commands:
			sys.exit()
		output_file = str(input("\nEnter file name to export csv or print exit to exit: "))
		if output_file in exit_commands:
			sys.exit()
	else:
		input_file = sys.argv[1]
		output_file = sys.argv[2]
	
	checkfile(input_file, output_file)


def checkfile(input_file, output_file):
	if not os.path.lexists(input_file):
		main()	
	json_to_csv(input_file, output_file)


def json_to_csv(file_input, file_output):	
	# opens a json file
	with open(file_input) as input_file:
		
		# loads a csv file
		with open(file_output, "w") as output_file:
			
			# loads json content
			data = json.load(input_file) 
			# close the input file
			input_file.close()

			# creates a csv.writer
			output = csv.writer(output_file)
			# header line
			output.writerow(data[0].keys())

			for line in data:
			    # values line
			    output.writerow(line.values())
			command = (["ls"] if not sys.platform.startswith("win") else
			["cmd.exe", "/C", "dir"])
			subprocess.call(command)

if __name__ == '__main__':
	main()