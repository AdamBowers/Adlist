from time import sleep


url = str(input("enter url: ").strip())

with open('Adlist', 'r+', encoding='utf-8') as fp:

    for i in fp:

        if i.strip() == url:
            print("url exsists in file!")

            input('press enter to exit...')
            quit()
        else:
           pass
    
    fp.write(f"\n{url.lower()}")
    print ("url added!")
    input("press enter to exit...")