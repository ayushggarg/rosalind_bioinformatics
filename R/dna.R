seq <- read_lines("rosalind_dna.txt")
split_seq = strsplit(seq, "")[[1]]
count_A <- 0
count_C <- 0
count_G <- 0
count_T <- 0

for (nuc in split_seq){
  if (nuc == 'A'){
    count_A <- count_A + 1
  }
  else if (nuc == 'C'){
    count_C <- count_C + 1
  }
  else if (nuc == 'G'){
    count_G <- count_G + 1
  }
  else
    count_T <- count_T + 1
}

sprintf ("%d %d %d %d", count_A, count_C, count_G, count_T)
