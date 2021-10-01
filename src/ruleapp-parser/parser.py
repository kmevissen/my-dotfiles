import xml.etree.ElementTree as ET
from pprint import pprint

FILENAME = 'data.xml'
# FILENAME = 'BudgetairMY_PricingRules.ruleapp'

tree = ET.parse(FILENAME)
root = tree.getroot()

pprint(root.tag)

pprint(root.attrib)

# for child in root:
#     pprint(child.tag)

# a = root.findall(".")
# b = root.findall("./BudgetairMY_PricingRules")
# c = root.findall("./Entities")
# d = root.findall(".//Entities")


# Top-level elements
a = root.findall(".")

# All 'neighbor' grand-children of 'country' children of the top-level
# elements
b = root.findall("./country/neighbor")

# Nodes with name='Singapore' that have a 'year' child
c = root.findall(".//year/..[@name='Singapore']")

# 'year' nodes that are children of nodes with name='Singapore'
d = root.findall(".//*[@name='Singapore']/year")

# All 'neighbor' nodes that are the second child of their parent
e = root.findall(".//neighbor[2]")

f = root.findall("./country")

print("la")