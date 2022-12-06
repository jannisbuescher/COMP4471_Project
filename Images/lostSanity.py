import os
import shutil
import random

big_folder = "JPEGImage"
small_folder = "JPEGImage\JPEGImage"

def createDataset(negativedirectory, positivedirectory, enddirectory, ratio):
    n_positives = 0
    for filename in os.listdir(positivedirectory):
        if filename[0]=='P':
            src = os.path.join(positivedirectory, filename)
            dst = os.path.join(enddirectory, filename)
            shutil.copyfile(src, dst)
            n_positives += 1
    print(f"{n_positives} Positives transfered")
    print("August det skal nok gaa")

    for e,_ in enumerate(range(ratio*n_positives)):
        filename = random.choice(os.listdir(negativedirectory)[0:120000])
        src = os.path.join(negativedirectory, filename)
        dst = os.path.join(enddirectory, filename)
        shutil.copyfile(src, dst)
        if e%1000==0:
            print(f"{e} negatives transferred")
            print("smil :)")

createDataset(r"JPEGImage",r"val", r"test10", 10)

# for filename in os.listdir(small_folder):
#     f = os.path.join(small_folder, filename)
#     # checking if it is a file
#     if os.path.isfile(f):
#         os.replace(f, os.path.join(big_folder, filename))
#         #os.replace("path/to/current/file.foo", "path/to/new/destination/for/file.foo")
# n = 0
# p = 0
# for file in os.listdir(big_folder):
#     if file[0]=="P":
#         p+=1
#     elif file[0]=="N":
#         n+=1
# not_found = 0
# labels = [a[:-4] for a in os.listdir("positive-Annotation")]
# pics = [a[:-4] for a in os.listdir("JPEGImage")]
# print("I made the lists")
# n_labels = len(labels)
# for e,file in enumerate(labels):
#     if file not in pics:
#         print(file, "  not found in JPEGImage")
#         file_doomed = file+".xml"
#         os.remove(os.path.join("positive-Annotation",file_doomed))
#         not_found += 1
#     if e%1000==0:
#         print(f"{e} pics done")

# print("Negative pictures: ",n)
# print("Positive pictures: ",p)
# print("Not found: ",not_found)