## Thompson, Akita and Do 2020 ####

thompson2020 <- read_csv("https://osf.io/2praq/download")

thompson2020%>%
  select(word,rating,informantID=subjCode)%>%
  mutate(ipa=str_replace_all(word,"sh","ʃ"))%>%
  mutate(ipa=str_replace_all(ipa,"ch","tʃ"))%>%
  mutate(source="Thompson et al. 2020")->processed
  
lexemes <- read_tsv("../lexemes.tsv")%>%
  select(paradigmID,lexemeID,ipa)

recovered <- inner_join(lexemes,processed,by="ipa")

write_csv(recovered,"iconicity_ratings.csv")
