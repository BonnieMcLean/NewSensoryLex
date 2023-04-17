import csv
import sys
import os
import plotly.express as px
import pandas as pd
import math
from sympy import Polygon,pi 

## Read in the language

with open("01-language.tsv",encoding="UTF-8") as infile:
    reader=csv.DictReader(infile,delimiter="\t")
    for row in reader:
        glottocode=row["glottocode"]
        language_name=row["language_name"]
        language_ortho=row["orthography"]

## Read in the lexemes

lexemes={}

with open("02-lexemes.tsv",encoding="UTF-8") as infile:
    reader=csv.DictReader(infile,delimiter="\t")
    for row in reader:
        lexemeID=row["lexemeID"]
        lexeme=row["lexeme"]
        orthography=row["orthography"]
        lexemes[lexemeID]=[lexeme,orthography]
infile.close()

## Read in pronunciations

with open("03-pronunciations.tsv",encoding="UTF-8") as infile:
    reader=csv.DictReader(infile,delimiter="\t")
    for row in reader:
        lexemeID=row["lexemeID"]
        ipa=row["ipa"]
        orthography=row["orthography"]
        lexemes[lexemeID].append((ipa,orthography))
infile.close()

## Read in usages

done=[]
with open("04-usages.tsv",encoding="UTF-8") as infile:
    reader=csv.DictReader(infile,delimiter="\t")
    for row in reader:
        lexemeID=row["lexemeID"]
        usageID=row["usageID"]
        gloss=row["gloss"]
        pos=row["pos"]
        gloss_ortho=row["gloss-ortho"]
        definition=row["definition"]
        definition_eng=row["definition-eng"]
        date=row["date"]
        source=row["source"]
        source_date=row["source-date"]

        if lexemeID not in done:
            done.append(lexemeID)
            lexemes[lexemeID].append([])
        lexemes[lexemeID][3].append((usageID,gloss,pos,gloss_ortho,definition,definition_eng,date,source,source_date))
            
infile.close()

# Read in sensory ratings
sensory_ratings=[]
try:
    with open("sensory_ratings/sensory_ratings.tsv", "r") as infile:
        reader=csv.DictReader(infile,delimiter="\t")
        for row in reader:
            try:
                lexemeID=row["lexemeID"]
                domain=row["domain"]
                mean_rating=row["mean_rating"]
                source=row["source"]
            except KeyError:
                print("Sensory_ratings.tsv is either missing required columns or the columns are labelled incorrectly. Correct it by checking the ReadMe on Github.")
            if lexemeID not in sensory_ratings:
                sensory_ratings.append(lexemeID)
                lexemes[lexemeID].append([])
            lexemes[lexemeID][4].append((domain,mean_rating))
                        
except FileNotFoundError:
    pass

### Calculate cartesian coordinates for vertices of polygons representing each ideophone
### (the same polygons in the polar charts)

first_coord=True
for lexemeID in sensory_ratings:
    # make an empty list to store coordinates
    lexemes[lexemeID].append([])

    # get domains and ratings
    data=lexemes[lexemeID][4]

    n_domains=len(data)
    pie_angles=360/n_domains

    for item in data:
        ## transform ratings
        domain=item[0]
        rating=float(item[1])
        rating=round(rating,2)

        if first_coord:
            n_pies=math.floor(90/pie_angles)
            theta_1=90-n_pies*pie_angles
            first_coord=False
            theta=theta_1
            previous_theta=theta
        else:
            theta=previous_theta+pie_angles
            previous_theta=theta

        x=round(rating*math.cos(math.radians(theta)),2)
        y=round(rating*math.sin(math.radians(theta)),2)
        lexemes[lexemeID][5].append((x,y))


## Make a polygon for each ideophone

for lexemeID in sensory_ratings:
    print(lexemeID)
    vertices=lexemes[lexemeID][5]
    v1,v2,v3,v4,v5,v6,v7,v8,v9=vertices
    polygon=Polygon(v1,v2,v3,v4,v5,v6,v7,v8,v9)
    lexemes[lexemeID].append(polygon)

print(lexemes)
sys.exit()


    
##    ## start from shape
##    order_vertices=vertices[n_pies:]+vertices[:n_pies]
##    print(order_vertices)
##    polygon=Polygon(order_vertices)
##    domains=[]
##    x_cords=[]
##    y_cords=[]
##    for v in vertices:
##        x_cords.append(v[0])
##        y_cords.append(v[1])
##        domains.append(v[2])
##    fig=px.scatter(x=x_cords,y=y_cords,text=domains)
##    fig.write_image("sensory_ratings/images/"+lexemeID+"_scatter.svg")
##

    
  #  print(vertices)
  #  polygon=Polygon(vertices)
   # print(lexemeID)
   # print(polygon.area)

        
# Read in guessing accuracies


# Read in iconicity ratings



# make the folder for the lexicon
directory="lexicon/english"
if not os.path.isdir(directory):
    os.mkdir(directory)



##
##### Make the basic pages
##f=open("templates/lexemes.html","r")
##template=f.readlines()
##f.close()
####	
##    # make the basic page for each lexeme, using the template
##    all_lexs=lexemes[paradigm]
##    for lex in all_lexs:
##        lines=[]
##        for l in template:
##            if "LEXEME" in l:
##                new_line=l.replace('LEXEME',lex[1])
##                lines.append(new_line)
##            elif "IPA" in l:
##                new_line=l.replace('IPA',lex[2])
##                lines.append(new_line)
##            elif "GLOSS" in l:
##                new_line=l.replace('GLOSS',lex[3])
##                lines.append(new_line)
##            elif "DEFINITION" in l:
##                new_line=l.replace("DEFINITION",lex[4].capitalize()+'.')
##                lines.append(new_line)
##            elif "MAJOR_SENSES" in l:
##                for sense in lex[5]:
##                    new_line=l.replace("MAJOR_SENSES",sense)
##                    lines.append(new_line)
##            else:
##                lines.append(l)
##
##        filename='lexicon/'+paradigm+'/'+paradigm+lex[0]+'.html'
##        out_f=open(filename,"w")
##        out_f.writelines(lines)
##        out_f.close()


        
# Make the graphs based on sensory ratings

# make the folder to store the graphs
directory="sensory_ratings/images"
if not os.path.isdir(directory):
    os.mkdir(directory)
    
#print(lexemes)
for lexemeID in sensory_ratings:
    data=lexemes[lexemeID][4]
    labels=[]
    ratings=[]
    for item in data:
        ## transform ratings
        rating=float(item[1])
        rating=round(rating,2)
        labels.append(item[0])
        ratings.append(rating)
    df=pd.DataFrame(dict(r=ratings,l=labels))
    fig=px.line_polar(df,r="r",theta="l",range_r=[0,6],line_close=True)
    fig.update_traces(fill='toself',fillcolor="rgb(100, 149, 237)")
    fig.update_layout(annotations = [dict(
        x=0.75,
        y=-1,    
        text='(McLean et al. 2023)')])
    fig.update_annotations(font_size=30)

    # styling
    fig.update_polars(radialaxis_showticklabels=False)
    fig.update_polars(bgcolor="rgb(232,232,232)")
    fig.update_polars(angularaxis_tickfont_size=40)

    # write image to file
    fig.write_image("sensory_ratings/images/"+lexemeID+".svg")
    
