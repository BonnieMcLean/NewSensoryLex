library(tidyverse)

source <- read_csv("https://raw.githubusercontent.com/BonnieMcLean/IconicityMeasuresJaponic/main/GuessingRatingScores.csv")

source%>%
  filter(grepl("PRICKLING",identifier))%>%
  rowwise()%>%
  mutate(lexeme=str_split(identifier,"_")[[1]][1])%>%
  filter(method=="guesses")%>%
  mutate(conceptID=1)%>%
  select(lexeme,score,conceptID)->processed

write_csv(processed,"guesses.csv")
