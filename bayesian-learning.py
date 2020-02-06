import numpy as np
import pandas as pd

def readData():
	dataSet = pd.read_csv("data_latih_opsi_1.csv",delimiter =',')
	return dataSet

def readData_tes():
	dataSet = pd.read_csv("data_tes.txt",delimiter =',')
	return dataSet

def prior_probability(data):
	c1,c2 = 0,0
	for i in data["terbang"]:
		if i == "ya":
			c1 += 1
		else:
			c2 += 1

	layak = {
		"ya" : c1,
		"tidak" : c2
	}

	return layak

def condition_probability(data,data_tes):

	layak = prior_probability(data)

	layak_suhu = {
		"ya" : 0,
		"tidak" : 0
	}
	layak_cuaca = {
		"ya" : 0,
		"tidak" : 0
	}
	layak_kelembapan = {
		"ya" : 0,
		"tidak" : 0
	}
	layak_kondisi = {
		"ya" : 0,
		"tidak" : 0
	}
	predict = []


	for index_tes, row_tes in data_tes.iterrows():		
		for index, row in data.iterrows():
			if row["suhu"] == row_tes["suhu"] and row["terbang"] == "ya":
				layak_suhu["ya"] += 1/layak["ya"]
			if row["suhu"] == row_tes["suhu"] and row["terbang"] == "tidak":
				layak_suhu["tidak"] += 1/layak["tidak"]

			if row["kondisi"] == row_tes["kondisi"] and row["terbang"] == "ya":
				layak_kondisi["ya"] += 1/layak["ya"]
			if row["kondisi"] == row_tes["kondisi"] and row["terbang"] == "tidak":
				layak_kondisi["tidak"] += 1/layak["tidak"]

			if row["cuaca"] == row_tes["cuaca"] and row["terbang"] == "ya":
				layak_cuaca["ya"] += 1/layak["ya"]
			if row["cuaca"] == row_tes["cuaca"] and row["terbang"] == "tidak":
				layak_cuaca["tidak"] += 1/layak["tidak"]

			if row["kelembapan"] == row_tes["kelembapan"] and row["terbang"] == "ya":
				layak_kelembapan["ya"] += 1/layak["ya"]
			if row["kelembapan"] == row_tes["kelembapan"] and row["terbang"] == "tidak":
				layak_kelembapan["tidak"] += 1/layak["tidak"]

		ya = layak_suhu["ya"]*layak_kelembapan["ya"]*layak_cuaca["ya"]*layak_kondisi["ya"] 
		tidak = layak_suhu["tidak"]*layak_kelembapan["tidak"]*layak_cuaca["tidak"]*layak_kondisi["tidak"]
		
		if ya > tidak:
			predict.append("ya")
		else:
			predict.append("tidak")

	return predict

if __name__ == '__main__' :
	layak = prior_probability(readData())
	print(layak)
	# data_tes = readData_tes()
	# cond_prob = condition_probability(readData(),data_tes)
	# print(cond_prob)


