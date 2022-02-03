#!/opt/homebrew/bin/python3

import random, sys

# Interesting Symbols
ESH = 'ʃ'
EZH = 'ʒ'
ETH = 'ð'
GLOTTAL = 'ʔ'
ENG = 'ŋ'
THETA = 'Θ'

# Example Words
EXAMPLES = {
  "p" : "pie",
  "b" : "buy",
  "m" : "my",
  "f" : "five",
  "v" : "view",
  THETA : "thigh",
  ETH : "thus",
  "t" : "tie",
  "d" : "die",
  "n" : "night",
  "s" : "sip",
  "z" : "zip",
  "l" : "light",
  "r" : "rock",
  ESH : "miSSion",
  EZH : "meaSure",
  't' + ESH : "CHeap",
  'd' + EZH : "juDGE",
  "j" : "you",
  "k" : "baCK",
  "g" : "baG",
  ENG : "baNG",
  "h" : "High",
  GLOTTAL : "UH-oh",
  "w" : "Witch",
}

MANNER_OF_ARTICULATION = {
  "oral" : [ 'p', 'b', 't', 'd', 'k', 'g', GLOTTAL ],
  "nasal" : [ 'm', 'n', ENG ],
  "fricative" : [ 'f', 'v', THETA, ETH, 's', 'z', ESH, EZH, 'h' ],
  "affricate" : [ 't' + ESH, 'd' + EZH ],

  # 4 more that wasn't specified
  "." : [ 'j', 'w', 'l', 'r' ]
}

# Place of Articulation
BILABIALS = [ 'p', 'b', 'm' ]
LABIODENTALS  = [ 'f', 'v' ]
INTERDENTALS = [ THETA, ETH ]
ALVEOLARS = [ 't', 'd', 'n', 's', 'z', 'l', 'r' ]
PALATALS = [ ESH, EZH, 't' + ESH, 'd' + EZH, 'j' ]
VELARS = [ 'k', 'g', 'ŋ' ]
GLOTTALS = [ 'h', GLOTTAL ]
LABIOVELARS = [ 'w' ]

# Create Dictionary of Terms
CONSONANTS = BILABIALS + \
             LABIODENTALS + \
             INTERDENTALS + \
             ALVEOLARS + \
             PALATALS + \
             VELARS + \
             GLOTTALS + \
             LABIOVELARS

PLACE_OF_ARTICULATION = {
  "bilabials" : BILABIALS,
  "labiodentals" : LABIODENTALS,
  "interdentals" : INTERDENTALS,
  "alveolars" : ALVEOLARS,
  "palatals" : PALATALS,
  "velars" : VELARS,
  "glottals" : GLOTTALS,
  "labiovelars" : LABIOVELARS
}


def testPlaceOfArticulation( conCov, manner=False ):
  dictionaryToLookAt = MANNER_OF_ARTICULATION if manner else \
    PLACE_OF_ARTICULATION

  choices = list( dictionaryToLookAt.keys() )

  while 1:
    randIndex = random.randrange( 0, len( choices ), 1 ) 

    correctPlaceOfArticulation = choices[ randIndex ]

    givenCosonant = None

    givenConsonant = random.choice( 
        dictionaryToLookAt[ correctPlaceOfArticulation ] )

    if not givenConsonant in conCov:
      break

  print( givenConsonant ) 

  returnVal = None

  while 1:
    inputStr = input()

    if inputStr == correctPlaceOfArticulation:
      print( "CORRECT!" )
      returnVal = inputStr
      conCov.add( givenConsonant )
      break
    elif inputStr == "example":
      print( "EXAMPLE - " + EXAMPLES[ givenConsonant ] )
    elif inputStr == "status":
      print( "STATUS - " + str( len( conCov ) ) + \
             "/" + str( len( CONSONANTS ) ) )
    else:
      print( "WRONG - " + correctPlaceOfArticulation )
      break

  return returnVal

def printHelper():
  print()
  print( "help: ./cons.py [ manner | place ]" )
  print()
  print( "ex. ./cons.py manner ... will help you practice manner of articulation" )
  print()
  print( "When practicing, you can view the options to type. You can type 'status'" )
  print( "if you want to view how many consanants you learned" )
  print( "Note that once all consonants have been learned the program will stop" )
  print()

if __name__ == "__main__":

  # Simple argparse
  if len( sys.argv ) != 2:
    printHelper()
    exit( 1 )

  dictToUse = None
  if sys.argv[ 1 ] == "manner":
    dictToUse = MANNER_OF_ARTICULATION
  elif sys.argv[ 1 ] == "place":
    dictToUse = PLACE_OF_ARTICULATION
  else:
    printHelper()
    exit( 1 )

  try:
    consonantsCovered = set()
    choices = list( dictToUse.keys() )
    while 1:
      print( "CHOOSE " + str( choices ) )
      testPlaceOfArticulation( consonantsCovered, sys.argv[ 1 ] == "manner" )

      if len( consonantsCovered ) == len( CONSONANTS ):
        print( "\nAll Consonants Covered!\n" )
        break
        
      print( "===" )

  except KeyboardInterrupt as e :
    print( "\n\nBYE!\n" )
