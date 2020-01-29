import numpy as np
import pandas as pd


def readData():
	dataSet = pd.read_csv("data_latih_opsi_1.txt",delimiter =',')
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
		"ya" : c1/80,
		"tidak" : c2/80
	}

	return layak

def condition_probability(data,data_tes):

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

	for index_tes, row_tes in data_tes.iterrows():		
		for index, row in data.iterrows():
			if row["suhu"] == row_tes["suhu"] and row["terbang"] == "ya":
				layak_suhu["ya"] += 1/80
			if row["suhu"] == row_tes["suhu"] and row["terbang"] == "tidak":
				layak_suhu["tidak"] += 1/80

			if row["kondisi"] == row_tes["kondisi"] and row["terbang"] == "ya":
				layak_kondisi["ya"] += 1/80
			if row["kondisi"] == row_tes["kondisi"] and row["terbang"] == "tidak":
				layak_kondisi["tidak"] += 1/80

			if row["cuaca"] == row_tes["cuaca"] and row["terbang"] == "ya":
				layak_cuaca["ya"] += 1/80
			if row["cuaca"] == row_tes["cuaca"] and row["terbang"] == "tidak":
				layak_cuaca["tidak"] += 1/80

			if row["kelembapan"] == row_tes["kelembapan"] and row["terbang"] == "ya":
				layak_kelembapan["ya"] += 1/80
			if row["kelembapan"] == row_tes["kelembapan"] and row["terbang"] == "tidak":
				layak_kelembapan["tidak"] += 1/80

	print(layak_suhu)
	print(layak_kondisi)
	print(layak_cuaca)
	print(layak_kelembapan)

	return layak_suhu,layak_kelembapan,layak_cuaca,layak_kondisi

if __name__ == '__main__' :
	#layak = prior_probability(readData())
	data_tes = readData_tes()
	cond_prob = condition_probability(readData(),data_tes)
	ya = cond_prob[0]["ya"]*cond_prob[1]["ya"]*cond_prob[2]["ya"]*cond_prob[3]["ya"]
	tidak = cond_prob[0]["tidak"]*cond_prob[1]["tidak"]*cond_prob[2]["tidak"]*cond_prob[3]["tidak"]
	print(ya,tidak)	


