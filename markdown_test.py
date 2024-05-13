import markdown

md_text = """
###The Tale of Max and the Whispers of the Wild###

##Chapter 1: The Unexpected Journey##

As I stepped out into the crisp morning air, I couldn't help but feel a sense of unease. My trusty companion, Max, a rugged golden retriever with a heart of gold, stood by my side, his big brown eyes fixed on me with an unspoken understanding. We had been through thick and thin together, and I knew he sensed something was amiss.
"""

html = markdown.markdown(md_text)
print(html)