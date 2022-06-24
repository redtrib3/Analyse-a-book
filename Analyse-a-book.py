# Objectives
# > convert Pdf to txt
# > read all lines, strip white spaces
# > remove a,an, question words etc..
# > make a dict with word as key and freq as value
# > simplify and clean

import PyPDF2


user = input("Path to file (with .pdf) >>")

def listfilter(thelist):

	# filtering out anything extra 
	extras = ['',"\n","a","an","the","thus","what","where","when","who","which",'for','from','and','or','of','to',
	'on','in','at','that', 'you','your','the', 'he', 'is', 'i', 'it', 'they', 'be', 'with', 'but', 'was', 'are', 'this', 'have',
	 'if', 'can', 'a', 'about', 'as']	
	#extra_upper = [ 'A', 'AN', 'THE', 'THUS', 'WHAT', 'WHERE', 'WHEN', 'WHO', 'WHICH']
	#filterList = []
	
	for j in thelist:
		if j in extras:
			index_j = thelist.index(j)
			del thelist[index_j]

		try:

			for addons in ['.','\n','.','?',',',')','(']:
				if addons in j:
					ind = thelist.index(j)
					thelist[ind] = j.replace(addons,'')
		except ValueError:
			 continue
	print("[+] Filtering process - 100%.")


	freq = {}
	for value in thelist:
		if value in freq:
			freq[value] += 1
		else:
			freq[value] = 1

	new_freq = {}
	for counters in freq:
		if freq[counters] > 9:
			new_freq[counters] = freq[counters]
	
	# sort end result by keys ascending
	new_freq_sorted = sorted(new_freq, key=new_freq.get, reverse=True) 
	
	print("[+] Sorting Data...\n")
	c = 0
	for r in new_freq_sorted:
		if len(r) > 4:
			print(r,f"---> {new_freq[r]}")
			c += 1
			if c>=10:
				break


def pdf2txt(pdfbook):
	# Create a object
	pdfObject = open(pdfbook,'rb')
	# read all the text from the object pdf	
	pdfreader = PyPDF2.PdfFileReader(pdfObject)
	# Find the total no. of pages in book
	pages = pdfreader.numPages
	print("[+] Initialization Complete. ")

	
	# the array to store each word
	array_st = list()

	# loop through each page
	for i in range(1,pages):

		# get the single page(i) and extract the text
		pageObj = pdfreader.getPage(i)
		text = pageObj.extractText()
		
		# split by space into a list/array
		text = text.split(" ")
		# append the list to form a large list of all words in range
		array_st = array_st + text

		array_lw = []
		for uppers in array_st:
			array_lw.append(uppers.lower())

	print("[+] Extracting pages...")
	print("[+] Ready to Filter data")
	print(f"[~] {pages} Pages Found")
	listfilter(array_lw)




pdf2txt(user)



