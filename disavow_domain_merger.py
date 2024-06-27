import sys
from datetime import datetime 

if __name__ == "__main__":
  if len(sys.argv) !=3:
    print("Insufficient arguments")
  else:
    file_1 = sys.argv[1]
    file_2 = sys.argv[2]
    new_domains=[]
    for file in sys.argv[1:]:
      with open(file) as fd:
        print(f"File : {file}")
        data = fd.readlines()
        domains = [entry for entry in data if entry.startswith("domain:")]
        print(f"Data={len(data)} -> Domains={len(domains)}")
        new_domains.extend(domains)
    print(f"Combined domains: {len(new_domains)}")
    unique_domains = list(set(new_domains))
    print(f"Unique domains: {len(unique_domains)}")
    print(f"Newly added domains: {len(new_domains)- len(unique_domains)}")

    current_dt = datetime.now()
    formatted_dt = current_dt.strftime("%Y%m%d%H%M%S")

    with open(f"disavow_{formatted_dt}.txt", "w") as fd:

      for dmn in unique_domains:
        fd.write(dmn)


