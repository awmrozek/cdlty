from collections import *
import sys
import argparse

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("-all_arguments", action="store_true")
	parser.add_argument("-argument1", action="store_true")
	parser.add_argument("-argument2", action="store_true")

	args = parser.parse_args()
	if not args.all_arguments:
		print("all_arguments not specified, reading argument1 and argument2")
		if args.argument1 and args.argument2:
			argument1 = args.argument1
			argument2 = args.argument2
		else:
			print("Invalid arguments specified. Program cannot continue!")
	else:
		print(f"User specified all_arguments option {args.all_arguments}")


