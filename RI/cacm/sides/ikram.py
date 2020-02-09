def getData():
    data = {}
    file = open("cacm.all",encoding='utf-8')
    content = file.readlines()
    line = 0 

    while line < len(content) :
        line_text = content[line]
        if line_text.startswith('.I'):
            docname = line_text.split()[1]
            print(docname)
        
        
        
        if line_text.startswith('.T') :
            line= line + 1
            data[docname]=content[line].lower()
            print(data[docname])
        
              
    
        if line_text.startswith('.W'):
            text = " "
            line= line+1
            line_content = content[line]
            #print(line_content)
            while  line < len(content)-1 and line_content.startswith('.B')==False :
                text=text+" "+line_content
                line=line+1
                #print("aanaaa "+str(line))

                line_content = content[line].lower()    
            
            data[docname] = data[docname]+text
            print(data[docname])    
        
        line=line+1
    
    return data


print(getData())