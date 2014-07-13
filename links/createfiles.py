from bs4 import BeautifulSoup
import urllib

def main(Word):
    file = open("%s.txt" % Word,'wb')
    file.write("https://play.google.com/store/apps/category/%s/collection/topselling_paid\n" % Word)
    file.write("https://play.google.com/store/apps/category/%s/collection/topselling_free\n" % Word)




if __name__ == '__main__':

    file = open("W.txt","r")
    lines = file.readlines()
    for i in lines:
      thisline = i.split(" ")
      for a in thisline:
          main(a)