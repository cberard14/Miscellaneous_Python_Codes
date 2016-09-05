import copy
import time
import sys
from random import randint

##### demonstration of merge sort algorithm
def merge(list1,list2):
	merged_list=[]
	index1=0
	index2=0
	all_merged=False
	while (all_merged==False):
		if ((index1<len(list1)) and (index2<len(list2))):
			if (list1[index1]>=list2[index2]):
				merged_list.append(list2[index2])
				index2+=1
			else:
				merged_list.append(list1[index1])
				index1+=1
		else: 
			if (index1 != len(list1)):
				while (index1  < len(list1)):
					merged_list.append(list1[index1])
					index1+=1
			elif (index2 != len(list2)):
				while (index2 < len(list2)):
					merged_list.append(list2[index2])
					index2+=1		
			all_merged=True
	return merged_list

def merge_step(unsorted_list):
	merged_list=[]
	if (len(unsorted_list)%2==0):
		for list_number in range(0,len(unsorted_list),2):
			merged_list.append(merge(unsorted_list[list_number],unsorted_list[list_number+1]))
	else:
		for list_number in range(0,len(unsorted_list)-1,2):
			merged_list.append(merge(unsorted_list[list_number],unsorted_list[list_number+1]))
		merged_list.append(unsorted_list[len(unsorted_list)-1])
	return merged_list

def split_list(unsplit_list):
	split=[]
	unsplit_copy=copy.copy(unsplit_list)
	for i in range(len(unsplit_copy)):
		split.append([unsplit_copy[i]])
	return split

def merge_sort(unsorted_list):
	original_length=len(unsorted_list)
	split_unsorted=split_list(unsorted_list)
	unsorted=True
	sorted_list=split_unsorted
	while (unsorted==True):
		if (original_length==len(sorted_list[0])):
			unsorted=False
		else:
			sorted_list = merge_step(sorted_list)
	return sorted_list[0]

def brute_force_sort(unsorted_list):
	for i in range(len(unsorted_list)):
		for j in range(len(unsorted_list)):
			if (unsorted_list[i]<=unsorted_list[j]):
				temp=unsorted_list[i]
				unsorted_list[i]=unsorted_list[j]
				unsorted_list[j]=temp
	return unsorted_list

if (__name__=="__main__"):
	to_be_sorted=[]
	N=5000
	for i in range(N):
		to_be_sorted.append(randint(0,100))

	merge_start=time.time()
	merge_sorted=merge_sort(to_be_sorted)
	merge_end=time.time()

	brute_start=time.time()
	brute_force_sorted=brute_force_sort(to_be_sorted)
	brute_end=time.time()

	print "list is N=",str(N)," elements long"
	print "Merge sort done in ",merge_end-merge_start,"s"
	print "Brute force sort done in ",brute_end-brute_start,"s"



