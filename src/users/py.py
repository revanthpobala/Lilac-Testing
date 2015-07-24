import time
import hashlib

class generator:
    
    def generate(self,total_users):
        users = []
        for i in range(0,total_users):
            ra = time.time()
            users1= hashlib.sha224(str(ra+i)).hexdigest()
            users.append(users1)
        if len(users) == total_users:
            file_open = open('users.txt','w')
            for item in users:
                item = (item[1:12] + " \n")
                file_open.write(item)
            file_open.close()
        print "Done"
upload = generator()
upload.generate(10)