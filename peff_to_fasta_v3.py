# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 10:45:01 2018

@author: heeyoun
"""

pefffile = open("nextprot_all.peff")
pefffile_line = pefffile.readlines()
result_file=open("nextprot_all.fasta",'w')
for line in pefffile_line :
    #print line
    if line[0]=="#" :
        pass
    else :
        if line[0] == ">":
            gname = ''
            pe = ''
            pname = ''
            
            lines = line[:-1].split(' \\')
            #print lines
            for line_ in lines:
                if "GName=" in line_:
                    gname_ = line_.split('=')
                    gname = gname_[1]
                elif "PE=" in line_:
                    pe=line_
                elif "PName=" in line_:
                    pname_ = line_.split('=')
                    pname = pname_[1]
            
            name_=lines[0].split(":")
            name='nxp|' + name_[1]


            #pname=lines[2].split('=')
            print ('>'+name+'|'+gname+' |'+pe+' |'+pname, file = result_file)
        else:
        
            print (line[:-1], file = result_file)
result_file.close()