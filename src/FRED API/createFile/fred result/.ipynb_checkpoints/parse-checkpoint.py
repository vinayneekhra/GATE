from bs4 import BeautifulSoup

# for all sentence indices
# go through all the output files
# take out another file as output where first line is the sentence 
# followed by the RDF-Graph node values

for i in range(15):
    for j in range(2):
        prefix = str(i) + "_" + str(j)
        read_file = prefix + "_output.html"
        soup = BeautifulSoup(open(read_file), features="lxml")

        links = soup.find_all('table')
        
        result = open(prefix + "_nodes.txt", 'w')

        for link in links:
            tds = link.find_all('td')
            result.write(tds[1].contents[0] + "\n")
        result.close()
    
