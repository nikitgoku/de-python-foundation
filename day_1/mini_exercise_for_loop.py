from loguru import logger

'''
Mini Exercise: For Loops
---------------------------------
Write a Python function that takes a paragraph of text as input and counts the number of times the
'''

def find_thes_in_paragraph(paragraph):
    """
    This functions takes a pargraph as input and return the count of the word 'the' in it.
    """
    words = paragraph.split(" ")    # Split the entire paragraph into words
    count = 0   # initialise counter variable
    for word in words:
        if word.lower() == 'the':   # Check if the word is 'the' (case insensitive)
            count += 1  # Increment the counter
    return count

paragraph = """Ralph Kimball founded the Kimball Group. Since the mid-1980s, he has been the 
data warehouse and business intelligence industry’s thought leader on the dimen
sional approach. He has educated tens of thousands of IT professionals. The Toolkit 
books written by Ralph and his colleagues have been the industry’s best sellers 
since 1996. Prior to working at Metaphor and founding Red Brick Systems, Ralph 
coinvented the Star workstation, the fi rst commercial product with windows, icons, 
and a mouse, at Xerox’s Palo Alto Research Center (PARC). Ralph has a PhD in 
electrical engineering from Stanford University"""

logger.info(f"Count of 'the' from paragraph: {find_thes_in_paragraph(paragraph)}")