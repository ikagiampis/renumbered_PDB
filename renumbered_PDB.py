#!/usr/bin/python
#For bugs e-mail ikagiampis@gmail.com
import re
import glob
import os

filesArray = glob.glob("*.pdb")

directory = 'Modified_PDB'
if not os.path.exists(directory):
    os.makedirs(directory)

for file in filesArray:

    newFileName = 'modified_' + str(file)
    filePath = str(directory) + '/' + str(newFileName)
    outFile = open(filePath, 'w')
    array_elements = 0
    print("\n"+"Cylon found the file: " + file)
    shiftNumberDict = {}
    
    for line in open(file):
        
        numberChain = re.match(r'COMPND.+CHAIN:(.+)\;', line, flags=0)
        
        if numberChain:
            chains = numberChain.group(1)
            
            pattern = re.compile(r'\s+')
            chains = re.sub(pattern, '', chains)
            
            chainArray = chains.split(",", 20)
            print ("Cylon found the following protein chains into the PDB file:")
            print (chainArray)
            array_elements = len(chainArray)
            
            i = 0
            while i in range(0, array_elements):
                chain = chainArray[i]
                print ("Cylon wants to know the numbering shift (for example .. -2, -1, 0, 1, 2 .. ) for the chain: " + chain)
                number = input("Insert number:")
                
                try:
                    number = int(number)   
                    shiftNumberDict[chain] = number
                    i = i + 1
                    
                except ValueError:
                    print("Not an integer. Try again")
                    i = 0
        
        ##ATOM             
        numberChain1 = re.match(r'(^A\w+.+?\d+\s+?\w+\s*?\w*\s+?)(\w+)(\s+?)(\d+)(\s+?)(.+)', line, flags=0)
        
        if numberChain1:
            
            #print(line, end = '')
            startLine = numberChain1.group(1)
            chainName = numberChain1.group(2)
            gapLine1 = numberChain1.group(3)
            aaNumber = numberChain1.group(4)
            gapLine2 = numberChain1.group(5)
            restLine = numberChain1.group(6)
            
            numberLength = len(str(aaNumber)) 
            
            number = shiftNumberDict[chainName]
            
            new_aaNumber = int(aaNumber) + int(number)
            
            new_numberLength = len(str(new_aaNumber))

            gap1Length = len(gapLine1)
            
            if numberLength == new_numberLength:  
                newLine = str(startLine)+str(chainName)+str(gapLine1)+str(new_aaNumber)+str(gapLine2)+str(restLine)+"\n"
                outFile.write(newLine)
            elif number > 0:
                newLength = gap1Length - 1        
                ngapLine1 = ''.ljust(newLength) #remove one empty space
                newLine = str(startLine)+str(chainName)+str(ngapLine1)+str(new_aaNumber)+str(gapLine2)+str(restLine)+"\n"
                outFile.write(newLine)
            elif number < 0:
                newLength = gap1Length + 1
                ngapLine1 = ''.ljust(newLength) #remove one empty space
                newLine = str(startLine)+str(chainName)+str(ngapLine1)+str(new_aaNumber)+str(gapLine2)+str(restLine)+"\n"
                outFile.write(newLine)
   
        numberChain2 = re.match(r'(TER.+?\d+\s+?\w+\s*?)(\w+)(\s+?)(\d+)', line, flags=0)
        
        if numberChain2:
            
            startLine = numberChain2.group(1)
            chainName = numberChain2.group(2)
            gapLine = numberChain2.group(3)
            aaNumber = numberChain2.group(4)
            
            number = shiftNumberDict[chainName]
            new_aaNumber = int(aaNumber) + int(number)
            
            newLine = str(startLine)+str(chainName)+str(gapLine)+str(new_aaNumber)+"\n"
            outFile.write(newLine)
            
        numberChain3 = re.match(r'^HEADER|^TITLE|^COMPND|^MASTER|^END|^CONECT|^HETATM', line, flags=0)
        if numberChain3:
            outFile.write(line)
            
                        
outFile.close()

print("\n Cylon finished!") 
    
