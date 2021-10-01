import xml.etree.ElementTree as ET
from StringIO import StringIO
from pprint import pprint

FILENAME = 'BudgetairMY_PricingRules.ruleapp'

namespaces = {'inrule': 'http://www.inrule.com/XmlSchema/Schema',
              'w3': 'http://www.w3.org/2001/XMLSchema-instance',
              'ms': 'urn:schemas-microsoft-com:xml-diffgram-v1'}


class XmlListConfig(list):
    def __init__(self, aList):
        for element in aList:
            if len(element) > 0:
                # treat like dict
                if len(element) == 1 or element[0].tag != element[1].tag:
                    self.append(XmlDictConfig(element))
                # treat like list
                elif element[0].tag == element[1].tag:
                    self.append(XmlListConfig(element))
            elif element.text:
                text = element.text.strip()
                if text:
                    self.append(text)


class XmlDictConfig(dict):
    '''
    Example usage:

    >>> tree = ElementTree.parse('your_file.xml')
    >>> root = tree.getroot()
    >>> xmldict = XmlDictConfig(root)

    Or, if you want to use an XML string:

    >>> root = ElementTree.XML(xml_string)
    >>> xmldict = XmlDictConfig(root)

    And then use xmldict for what it is... a dict.
    '''
    def __init__(self, parent_element):
        if parent_element.items():
            self.update(dict(parent_element.items()))
        for element in parent_element:
            if len(element) > 0:
                # treat like dict - we assume that if the first two tags
                # in a series are different, then they are all different.
                if len(element) == 1 or element[0].tag != element[1].tag:
                    aDict = XmlDictConfig(element)
                # treat like list - we assume that if the first two tags
                # in a series are the same, then the rest are the same.
                else:
                    # here, we put the list in dictionary; the key is the
                    # tag name the list elements all share in common, and
                    # the value is the list itself
                    aDict = {element[0].tag: XmlListConfig(element)}
                # if the tag has attributes, add those to the dict
                if element.items():
                    aDict.update(dict(element.items()))
                self.update({element.tag: aDict})
            # this assumes that if you've got an attribute in a tag,
            # you won't be having any text. This may or may not be a
            # good idea -- time will tell. It works for the way we are
            # currently doing XML configuration files...
            elif element.items():
                self.update({element.tag: dict(element.items())})
            # finally, if there are no child tags and no attributes, extract
            # the text
            else:
                self.update({element.tag: element.text})


with open(FILENAME, 'r') as f:
    XML = f.read()

# instead of ET.fromstring(xml)
it = ET.iterparse(StringIO(XML))
for _, el in it:
    if '}' in el.tag:
        el.tag = el.tag.split('}', 1)[1]  # strip all namespaces
root = it.root

tree = ET.parse(FILENAME)
# root = tree.getroot()

pprint(root.attrib)

a = root.findall(".")

# b = root.findall(".//{http://www.inrule.com/XmlSchema/Schema}DataElementDef")
# c = root.findall(".//inrule:DataElementDef", namespaces)
# g = root.findall(".//inrule:InlineDataSet", namespaces)
all_data_elements = root.findall(".//inrule:DataElementDef/.[@w3:type='TableDef']", namespaces)

for bla in all_data_elements:
    # ds = bla.findall(".//ms:diffgram/NewDataSet", namespaces)
    ds = bla.find(".//inrule:InlineDataSet/ms:diffgram", namespaces)
    xmldict = XmlDictConfig(ds)

    # Table Attributes
    data = bla.attrib
    data.pop('{http://www.w3.org/2001/XMLSchema-instance}type')

    print(data)


print("The End...")
