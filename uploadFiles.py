import os
import dropbox

class TransferData(object):
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        for root, files in os.walk(file_from):
            for name in files:
                path = os.path.join(root, name)
                print(path)

                relative_path = os.path.relpath(path, file_from)
                dropbox_path = os.path.join(file_to, relative_path)

                with open(path, "rb") as f:
                    dbx.files_upload(f.read(), dropbox_path, mode=dropbox.files.WriteMode.overwrite)

def main():
    access_token = "8hXbQGIDB5IAAAAAAAAAAd-JW98XFJO8eb7LCYd-UfTtNrO76lkzAHI9HYrFof2x"
    transfer_data = TransferData(access_token)

    file_from = input("Enter the path of file to be taken :- ")
    file_to = input("Enter the path where the file is to be dropped :- ")

    transfer_data.upload_file(file_from, file_to)

    print("Your file has been uploaded successfully")
    
main()