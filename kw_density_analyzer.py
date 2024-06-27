from collections import Counter
import re

content = """Your content here"""
tokens = re.findall(r'\b\w+\b', content.lower())
counter = Counter(tokens)

# Get the most common keywords
print(counter.most_common(10))
