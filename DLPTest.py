import os
import sys
 
class DLPTest:
    def test_https(self):
        fp = open("test_https.txt", "a")
        fp.write("this is the first keyword\r\n")
        fp.close()
    def test_http(self):
        fp = open("test_http.txt", "a")
        fp.write("this is the first keyword\r\n")
        fp.close()