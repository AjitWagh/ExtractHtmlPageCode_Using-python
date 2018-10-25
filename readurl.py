 # read the data from the URL and print it
import urllib2

def main():
# open a connection to a URL using urllib2
   webUrl = urllib2.urlopen("http://18.217.5.131:3000/#!/app/dashboard")
  
#get the result code and print it
   print "result code: " + str(webUrl.getcode()) 
  
# read the data from the URL and print it
   data = webUrl.read()
   print data
 
if __name__ == "__main__":
  main()