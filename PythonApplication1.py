import MasterClass
import urllib.request
import json
import xml.etree.ElementTree as ET
import pymssql

class TestClass1(MasterClass.MasterClass):

    def __init__(self):
        return

    def setUp():
        print ("This method should run before each test case")
        return

    def tearDown():
        print ("This method should run after each test case")
        return

    def fun1():
        print ("This is fun1")
        url = "http://www.thomas-bayer.com/sqlrest/CUSTOMER/"
        request = urllib.request.Request(url)
        response = urllib.request.urlopen(request).read()
        strrep = str(response)
        strrep = strrep.replace("b","").replace("\\n","").replace("'","")
        #print (strrep)
        tree = ET.fromstring(strrep)
        print (len(tree.getchildren()))
        print (tree[1].text)
        #root = tree.getroot() 
        #print (root[0][1].text)
        #jsondata = json.loads(response)
        #print (jsondata)
        #print (json.loads(str(response)))
        return

    def run():
        TestClass1.setUp()
        TestClass1.fun1()
        TestClass1.tearDown()

if __name__ == "__main__":
    TestClass1.run()