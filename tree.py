import os

def tree(dir):
  result = [os.path.basename(dir)]
  for d in os.listdir(dir):
    abs_path = dir + "/" + d
    if d[0] == ".":
      pass
    elif os.path.isdir(abs_path):
      result += [tree(abs_path)]
    else:
      result +=[[d]]
  return result


