import os
import thread
def rename_file(old_name,new_name):
    try:
        os.rename(old_name,new_name)
        print(f"成功")
    except OSError as e:
        print(f"失败,{str(e)}")
def main():
  a = ["test.txt"]
  b = ["test2.txt"]
threads = []
for old_name,new_name in zip("a","b"):
    thread=threading.Thread(target=rename_file,args=(old_name,new_name))
    thread.start()
    threads.append(thread)
for thread in threads:
    thread.join()
print("completed")

if __name__ == "__main__":
    main()