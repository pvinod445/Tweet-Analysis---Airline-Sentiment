
oldKey = None
pcount = 0
ncount = 0
neutralcount = 0
f = open("moutput.txt","r")  
o = open("r1output.txt", "w")
for line in f:
       
	data = line.strip().split(",")
	
	
	if len(data) != 2:
		continue
	thisKey, feedback = data
	
	#print "{0},{1}".format(thiskey ,feedback)
	if oldKey and oldKey != thisKey:
                
                #print "{0},{1}".format(thiskey ,feedback)
		print "{0}\t{1}\t{2}\t{3}".format(oldKey, ncount, neutralcount, pcount)	
                o.write("{0}\t{1}\t{2}\t{3}\n".format(oldKey, ncount, neutralcount, pcount))        
                pcount = 0
                ncount = 0
                neutralcount = 0
        oldKey = thisKey
       
        
        if thisKey == "Virgin America":
                
                if feedback == "positive":
                       
                        pcount +=1
                        
                elif feedback == "neutral":
                        
                        neutralcount += 1
                else:
                        ncount+=1
                        
        elif thisKey == "United":
                if feedback == "positive":
                       
                        pcount +=1
                elif feedback == "neutral":
                       
                        neutralcount += 1
                else:
                        ncount+=1
        elif thisKey == "Southwest":
                if feedback == "positive":
                       
                        pcount +=1
                elif feedback == "neutral":
                       
                        neutralcount += 1
                else:
                        ncount+=1
        elif thisKey == "Delta":
                if feedback == "positive":
                       
                        pcount +=1
                elif feedback == "neutral":
                       
                        neutralcount += 1
                else:
                        ncount+=1
        elif thisKey == "US Airways":
                if feedback == "positive":
                       
                        pcount +=1
                elif feedback == "neutral":
                       
                        neutralcount += 1
                else:
                        ncount+=1
        elif thisKey == "American":
                if feedback == "positive":
                       
                        pcount +=1
                elif feedback == "neutral":
                       
                        neutralcount += 1
                else:
                        ncount+=1                        
                       
                        
                    
		
if oldKey == thisKey:
        print oldKey, "\t", ncount, "\t", neutralcount, "\t", pcount
        o.write("{0}\t{1}\t{2}\t{3}\n".format(oldKey, ncount, neutralcount, pcount))
  
