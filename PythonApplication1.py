import MasterClass

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
        return

    def run():
        TestClass1.setUp()
        TestClass1.fun1()
        TestClass1.tearDown()

if __name__ == "__main__":
    TestClass1.run()