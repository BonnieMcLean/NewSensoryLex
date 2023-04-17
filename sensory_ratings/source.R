library(tidyverse)

# when we make this public, then get the ratings through the public url
# osf link is 9szfe
# https://osf.io/9szfe

source <- read_csv("ratings_mcleanetal.csv")

source%>%
  filter(identifier=="gojagoja2_JUMBLED UP"|identifier=="kachikachi_HARD")%>%
  # come back to this and make it actually the raw ratings? or is it not 
  # problematic to combine means from multiple databases if we want to
  # add to this later? Maybe it is better to do  the summarising of the
  # data in these files rather than in the pipeline actually
  select(identifier,domain,mean_rating)%>%unique()%>%
  pivot_wider(names_from = domain, values_from = mean_rating)%>%
  rowwise()%>%
  mutate(interoception = sum(`bodily feeling`,emotion)/2)%>%
  ## get the domains in the order you want them on graphs
  relocate(shape, .before = "texture")%>%
  relocate(light, .before = "pain")%>%
  relocate(interoception, .before = "pain")%>%
  relocate(smell, .before = "taste")%>%
  select(-appearance, -`bodily feeling`, -colour, -emotion, -pattern) %>%
  pivot_longer(!identifier,names_to = "domain", values_to = "mean_rating")%>%
  mutate(lexemeID=1,source="McLean et al. 2023")%>%
  select(lexemeID,identifier,domain,mean_rating,source)%>%
  unique()->processed

write_tsv(processed,"sensory_ratings.tsv")
