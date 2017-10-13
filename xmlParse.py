import requests 
import xml.etree.ElementTree as ET 

rssURL = "http://synd.cricbuzz.com/j2me/1.0/livematches.xml"

def xmlRss(url):
	resp = requests.get(url)
	xmlFile = "cricbuzz.xml"
	with open(xmlFile,"wb") as f:
		f.write(resp.content)
	return xmlFile

def xmlParse(file):
	tree = ET.parse(file)
	root = tree.getroot()
	matches = []
	for match in tree.findall('./match'):
		mch = {};
		mch['name'] = match.attrib['srs']
		mch['vs'] = match.attrib['mchDesc']
		mch['type'] = match.attrib['type']
		for child in match:
			if child.tag == 'state':
				mch['status'] = child.attrib['status']
			if child.tag == 'Tme':
				mch['stime'] = child.attrib['stTme']
				mch['date'] = child.attrib['Dt']
		
		matches.append(mch)
	return matches

def Matches():
	fileName = xmlRss(rssURL)
	mchs = xmlParse(fileName)
	return mchs