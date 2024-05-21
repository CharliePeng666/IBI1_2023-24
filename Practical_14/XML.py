import xml.dom.minidom
import datetime
import xml.sax
import matplotlib.pyplot as plt
bio = 0
mole = 0
cell = 0
file_path = r'c:\Users\彭成远\Desktop\IBI\IBI1_2023-24\go_obo.xml'

start_time = datetime.datetime.now()
DOM1 = xml.dom.minidom.parse(file_path)
collection = DOM1.documentElement
TAG = collection.getElementsByTagName("term")
for each_tag in TAG:
    if each_tag.getElementsByTagName("namespace")[0].firstChild.data == "biological_process":
        bio += 1
    if each_tag.getElementsByTagName("namespace")[0].firstChild.data == "molecular_function":
        mole += 1
    if each_tag.getElementsByTagName("namespace")[0].firstChild.data == "cellular_component":
        cell += 1
end_time1 = datetime.datetime.now()
execution_time = end_time1 - start_time
print('DOM methods takes ', execution_time)
plt.bar(['bio','mole','cell'], [bio, mole, cell])
plt.show()
plt.clf()




start_time2 = datetime.datetime.now()
namelist = []
total = {}
class namespaceHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.currentElement = ''
        self.namespace = ''
    
    def startElement(self, tag, attrs):
        self.currentElement = tag
    
    def characters(self, content):
        if self.currentElement == 'namespace':
            self.namespace += content.strip()
    
    def endElement(self, tag):
        if tag == 'namespace':
            if self.namespace:  
                namelist.append(self.namespace)  
                self.namespace = ''  
    
handler = namespaceHandler()
parser = xml.sax.make_parser()
parser.setContentHandler(handler)
parser.parse(file_path)
    
for name in namelist:
    if name not in total:
        total[name] = 1
    else:
        total[name] += 1
    
end_time2 = datetime.datetime.now()
time_taken = end_time2 - start_time2
print('SAX methods takes', time_taken)
plt.bar(['bio','mole','cell'], [total['biological_process'], total['molecular_function'], total['cellular_component']])
plt.show()
plt.clf()