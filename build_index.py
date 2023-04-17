import csv
import os
import codecs

## Read in the information on the language

with open("language.tsv") as infile:
    reader=csv.DictReader(infile,delimiter="\t")
    for row in reader:
        glottocode=row["glottocode"]
        language_name=row["language_name"]
        native_name=row["native_name"]
        orthography=row["orthography"]
infile.close()

### Make the index page from the template
f=open("index_template_eng.html","r")
template=f.readlines()
f.close()

lines=[]
for l in template:
    line=l
    if 'LANGUAGE_NAME' in l:
        line=line.replace('LANGUAGE_NAME',language_name)
    if 'NATIVE_NAME' in l:
        line=line.replace('NATIVE_NAME',native_name)
    if 'GLOTTOCODE' in l:
        line=line.replace('GLOTTOCODE',glottocode)
    lines.append(line)

filename=glottocode+'_index.html'
out_f=open(filename,'w')
out_f.writelines(lines)
out_f.close()

