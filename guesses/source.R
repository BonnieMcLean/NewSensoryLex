library(tidyverse)
library(httr)

# when we make this public, then get the guesses through the public url


source <- read_csv("guessing_results.csv")

source%>%
  filter(identifier=="gojagoja2_JUMBLED UP",method=="audio")%>%
  mutate(paradigmID=1,lexemeID=1,source="Thompson et al. 2023 audio condition")%>%
  select(paradigmID,lexemeID,identifier,guess=participant_grade,informantID=ProlificID,source)%>%
  unique()->processed

write_csv(processed,"guesses.csv")
