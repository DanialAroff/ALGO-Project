from News import News


n = News("https://www.thejakartapost.com/news/2019/05/27/jokowi-eyes-young-people-in-next-cabinet.html")
bandar = News("https://www.dhakatribune.com/bangladesh/dhaka/2019/05/25/dncc-mayor-footpaths-must-be-kept-clear"
              "-to-reduce-tailbacks")
print(bandar.get_text())
