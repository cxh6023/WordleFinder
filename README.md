# WordleFinder

Currently, the WordleFinder works with only one flaw. The WordleFinder is unable to handle solutions that have multiple letters in them.

There are two variables that have to be adjusted with each run to succesfully get the next guess.

The first(line 12). This needs to be the history of attempted words. In which 
  # Capital means the letter isn't in the spot
  # Lowercase means the letter isn't in the word
  # UnderScore means the letter is in the right spot
 
The second(line 18). This needs to be the most recent move. In which
  # Capital letter(we know it's here)
  # Lowercase Letter (we know it's in a different spot)
  # Underscore(_) (we know it's a new letter)
