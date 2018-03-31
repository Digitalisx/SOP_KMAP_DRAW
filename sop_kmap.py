import os
import sys

class draw_map():
	
	def __init__(self):

		# User Interface
		print("\n")
		print("==========================================================\n")
		print("              Sum of Product -> Karnaugh Map              \n")
		print("   Ajou University - Computer Architecture Assignment 01  \n")
		print("         201720678 Cyber Security - Donghyun Kim          \n")
		print("==========================================================\n")
  		
		# Variable Input Area
		self.var = input("Input Variable : ")
		self.var_list = self.var.split(",")
		self.var_len = len(self.var_list)
		
		# Essential Minterm Input Area
		self.minterm = input("Input Minterm Number : ")
		self.minterm_list = self.minterm.split(",")

		# Convert List String to Int
		self.minterm_list = list(map(int, self.minterm_list))
		self.minterm_len = len(self.minterm_list)

		if(self.var_len == 1):

			print("\n[+] Converting Data..")
			print("\n[!] Drawing Square..")
			print("[!] Exporting Table to HTML File..")

			html = open("result.html", "w")

			self.standard_area = "<title>Result</title><style>table {width: 50%;}table th, td {text-align: center; border: 1px solid #bcbcbc;}</style><table><tr>"
		
			self.colum_head = "<tr><th colspan=\"2\">f</th><th>-</th></tr>"
			self.colum_span = "<tr><td rowspan=\"2\">"

			self.colum_name = self.var_list[0]
			self.colum_name = self.colum_head + self.colum_span + self.colum_name
			
			if(self.minterm_list[0] == 1):
				self.row_span = "</td><td>0</td><td>0</td></tr><tr><td>1</td><td>1</td></table>"
			elif(self.minterm_list[0] == 0):
				self.row_span = "</td><td>0</td><td>1</td></tr><tr><td>1</td><td>0</td></table>"
			
			# Write Data
			html.write(self.standard_area)
			html.write(self.colum_name)
			html.write(self.row_span)
			html.close()

			sys.exit(1)
	

		elif(self.var_len == 2):

			self.colum_name = self.var_list[1]
			self.row_name = self.var_list[0]
			self.row_k = ["0", "1"]
			self.colum_k = ["0", "1"]

		elif(self.var_len == 3):
			
			self.colum_name = self.var_list[1] + self.var_list[2]
			self.row_name = self.var_list[0]
			self.row_k = ["00", "01", "11", "10"]
			self.colum_k = ["0", "1"]
		
		elif(self.var_len == 4):

			self.colum_name = self.var_list[2] + self.var_list[3]
			self.row_name = self.var_list[0] + self.var_list[1]
			self.row_k = ["00", "01", "11", "10"]
			self.colum_k = ["00", "01", "11", "10"]

		else:
			print("Not Supported Variable Type")
			return 0

	def bin_int_cov(self, i, j):

		print("[+] Converting Data..")

		# Convert String to Binary
		self.min_val = "0b" + str(self.colum_k[i] + str(self.row_k[j]))
		self.min_val = int(self.min_val, 2)
		
		return self.min_val

	def draw_square(self):

		print("\n[!] Drawing Square..")

		self.map_element = []
		self.map_min_element = []
		# Columns Count
		for self.colum_status in range(0,len(self.colum_k)):
			# Rows Count
			for self.row_status in range(0,len(self.row_k)):

				self.element = self.bin_int_cov(self.colum_status, self.row_status)
				
				if(self.element in self.minterm_list):
					self.map_min_element.append(1)

				else:
					self.map_min_element.append(0)

				# Cutting Two-Variable Map

				if(self.var_len == 2 ):
					
					if((len(self.map_min_element) == 2)):
						self.map_element.append(self.map_min_element)
						self.map_min_element = []

				# Cutting Another Map
				else:		
					if((len(self.map_min_element) % 4) == 0):
						self.map_element.append(self.map_min_element)
						self.map_min_element = []

		# Export HTML Area

		print("\n[!] Exporting Table to HTML File..")

		html = open("result.html", "w")

		self.standard_area = "<title>Result</title><style>table {width: 50%;}table th, td {text-align: center; border: 1px solid #bcbcbc;}</style><table><tr><th colspan=\"2\" rowspan=\"2\">f</th>"
	
		self.colum_span = "<th colspan=\"" + str(len(self.map_element[0])) + "\">"
		self.colum_name = self.colum_span + self.colum_name + "</th></tr><tr>"
		
		self.row_span = "<tr><td rowspan=\"" + str(len(self.map_element) + 2) + "\"><strong>"
		self.row_name = self.row_span + self.row_name + "</strong></td></tr>"	

		# Write Data

		html.write(self.standard_area)
		html.write(self.colum_name)

		for z in self.row_k:

			self.xis = "<td>" + z + "</td>"
			html.write(self.xis)

		html.write(self.row_name)

		index = 0

		for k in self.map_element:

			html.write("<tr>")

			self.yis = "<td>" + self.colum_k[index] + "</td>"

			html.write(self.yis)
			
			index += 1

			for j in k:

				self.colum_value = "<td>" + str(j) + "</td>"
				html.write(self.colum_value)
				
			html.write("</tr>")

		html.write("</table>")
		html.close()

		print("[!] Success! Please open result.html\n")

ajou = draw_map()
ajou.draw_square()
os.system("Pause")