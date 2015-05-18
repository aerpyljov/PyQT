import xml.etree.ElementTree as ET
p = r'D:\PW_DATA\WinFolders\desktop\example1.xml'
tree = ET.parse(p)
root = tree.getroot()
elem = root.find('element')
elem.tag
elem.attrib
elem.text

root = ET.Element('root2')
elem = ET.SubElement(root, 'elem2')
elem.set('count', str(123))
elem.text = 'SOME TEXT'

tree = ET.ElementTree(root)
p2 = r'D:\PW_DATA\WinFolders\desktop\example2.xml'
tree.write(p2)

from xml.dom import minidom
xml = minidom.parseString( ET.tostring(tree.getroot()) ).toprettyxml()
f = open(p2, 'w')
f.write(xml)
f.close()

p3 = r'D:\PW_DATA\WinFolders\desktop\example3.xml'
tree = ET.parse(p3)
root = tree.getroot()
for elem in root:
    print elem
for elem in root.getiterator():
    print elem.tag