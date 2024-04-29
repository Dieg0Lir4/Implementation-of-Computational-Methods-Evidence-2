import nltk
from nltk import CFG
nltk.download('punkt')

# Define a context-free grammar
grammar = CFG.fromstring("""
    S -> G
    G -> P GPrime
    GPrime -> M GPrime | '.'
    M -> 'captures' P 'in' B | 'moves' 'to' B | 'checkmates' C 'king' 'in' B
    P -> C F
    C -> 'black' | 'white'
    F -> 'king' | 'queen' | 'bishop' | 'knight' | 'rook' | 'pawn'
    B -> L N
    L -> 'a' | 'b' | 'c' | 'd' | 'e' | 'f' | 'g' | 'h'
    N -> '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8'
""")

# Create a parser with the defined grammar
parser = nltk.ChartParser(grammar)

# Flag to track if any parse is successful
parsed = False

def parse_sentence(sentence):

  
    global parsed
    # Tokenize the sentence
    tokens = nltk.word_tokenize(sentence)

    # Parse the sentence
    for tree in parser.parse(tokens):
        tree.pretty_print()
        parsed = True

    # Print message based on whether any parse was successful
    if parsed:
        print("VALID sentence for this grammar")
    else:
        print("INVALID sentence for this grammar")

    parsed = False

# Define test sentences
test_sentences = {
    "VALID": [
        "black pawn moves to c 5 .",
        "white king captures black bishop in b 5 .",
        "black queen captures white knight in a 2 ."
    ],
    "INVALID": [
        "black pawn moves to c c .",
        "white king captures bishop in 3 b .",
        "queen captures white knight in 2 a ."
    ]
}

# Function to run tests
def run_tests():
    for sentence_type, sentences in test_sentences.items():
        print(sentence_type + " sentences:")
        for sentence in sentences:
            print("INPUT:", sentence)
            parse_sentence(sentence)
            print()

# Main loop
while True:
    # Input sentence to be parsed
    sentence = input("Please enter a sentence: ")

    if sentence.lower() == "run all tests":
        run_tests()
    else:
        parse_sentence(sentence)

    # Ask if the user wants to continue
    choice = input("Do you want to enter another sentence? (yes/no): ")
    if choice.lower() != 'yes':
        break