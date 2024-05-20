import xml.etree.ElementTree as ET
import xml.sax
from xml.sax.handler import ContentHandler
import datetime
import matplotlib.pyplot as plt

xml_file_path = 'c:\\Users\\彭成远\\Desktop\\IBI\\IBI1_2023-24\\Practical_14\\go_obo.xml'

def parse_with_dom(xml_file_path):
    start_time = datetime.datetime.now()
    tree = ET.parse(xml_file_path)
    root = tree.getroot()
    
    ontology_count = {'molecular_function': 0, 'biological_process': 0, 'cellular_component': 0}
    
    for term in root.findall('term'):
        namespace = term.find('namespace').text
        if namespace in ontology_count:
            ontology_count[namespace] += 1
    
    end_time = datetime.datetime.now()
    return ontology_count, (end_time - start_time).total_seconds()

class SaxHandler(ContentHandler):
    def __init__(self):
        self.ontology_count = {'molecular_function': 0, 'biological_process': 0, 'cellular_component': 0}
        self.current_namespace = ''
    
    def startElement(self, name, attrs):
        if name == 'namespace':
            self.current_namespace = attrs.getValue('type')
    
    def endElement(self, name):
        if name == 'namespace' and self.current_namespace in self.ontology_count:
            self.ontology_count[self.current_namespace] += 1

def parse_with_sax(xml_file_path):
    start_time = datetime.datetime.now()
    handler = SaxHandler()
    parser = xml.sax.make_parser()
    parser.setContentHandler(handler)
    parser.parse(xml_file_path)
    end_time = datetime.datetime.now()
    return handler.ontology_count, (end_time - start_time).total_seconds()

def plot_ontology_counts(counts):
    plt.bar(['Molecular Function', 'Biological Process', 'Cellular Component'], counts)
    plt.xlabel('Ontology')
    plt.ylabel('Number of GO Terms')
    plt.title('Gene Ontology Term Counts by Ontology')
    plt.show()

if __name__ == "__main__":
    dom_counts, dom_time = parse_with_dom(xml_file_path)
    sax_counts, sax_time = parse_with_sax(xml_file_path)
    
    print(f"DOM API Time: {dom_time} seconds")
    print(f"SAX API Time: {sax_time} seconds")
    print(f"Fastest API: {('DOM' if dom_time < sax_time else 'SAX')} API")
    
    plot_ontology_counts(dom_counts) 


    for ontology in ['molecular_function', 'biological_process', 'cellular_component']:
        print(f"{ontology.title()}: DOM Count = {dom_counts[ontology]}, SAX Count = {sax_counts[ontology]}")