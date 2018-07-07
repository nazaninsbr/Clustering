import csv
import kClustering
import fuzzyClustering 


def read_file(path):
	data = []
	count = 0 
	with open(path) as f:
		reader = csv.reader(f)
		data = []
		for r in reader:
			count += 1
			data.append((count, r))
		data.pop(0) # remove header
	
	return data
	



if __name__ == '__main__':
	choice = input('1.K-Clustering 2.Fuzzy C-means Clustering (1/2)')
	car_data = read_file("./files/cars.csv")
	k = (2, 3, 5, 6)
	if choice=='1':
		kClustering.run_k_clustering(car_data, k)
	elif choice=='2':
		fuzzyClustering.run_fuzzy_c_mean_clustering(car_data, k)



