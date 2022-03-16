import os
class FiLe:
    txt_exist = []
    txt_new_create= []
    pdf_exist = []
    pdf_new_create = []
    def sort(self):
        while True:
            try:
                self.n = int(input("enter a number of files:"))
                for i in range(self.n):
                    self.fname = input("enter a file name")
                    assert self.fname.endswith('txt') | self.fname.endswith('pdf'),(f" invalid extension {self.fname}")
                    #txt files
                    if self.fname.endswith('txt'):
                        if os.path.isfile(self.fname):
                            print("this file is exist",self.fname)
                            d = input("do you want to delete file Y|N").lower()
                            if 'y' == d:
                                os.unlink(self.fname)
                            else:
                                continue
                        else:
                            FiLe.txt_new_create.append(self.fname)
                            with open(self.fname,'w') as fp:
                                fp.write('new file created')
                     #pdf files
                    elif self.fname.endswith('pdf'):
                        if os.path.isfile(self.fname):
                            print("this file exist:", self.fname)
                            d = input("do you want to delete file Y|N").lower()
                            if 'y' == d:
                                os.unlink(self.fname)
                            else:
                                continue
                        else:
                            FiLe.pdf_new_create.append(self.fname)
                            with open(self.fname,'w') as fp:
                                fp.write("new file created")
                else:
                    p = input("do you want to continue[y|n]:").lower()
                    if 'n' == p:
                        break
            except AssertionError as v:
                print(v)
                p = input("do you want to continue[y|n]:").lower()
                if 'n' == p:
                    print("Existing txt files:", FiLe.txt_exist)
                    print("newly created txt files:", self.txt_new_create)
                    print("exixting pdf files:", FiLe.pdf_exist)
                    print("newly created pdf files:", self.pdf_new_create)
                    break
            except ValueError as msg:
                print(msg)
            except Exception as msg:
                print(msg)
            finally:
                print("File sorting Completed")

f = FiLe()
f.sort()