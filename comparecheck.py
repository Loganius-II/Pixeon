#MLP means Machine Learning Pictures
#PIXEON: Picture Exploration & Neural Training Module
#Author: Logan McDermott
#Date: 5/3/2024

#PICTURES
PICTURE1 = './Pictures/Input/logan7.jpg'
PICTURE2 = './Pictures/Input/gpa.png'
PIXEON_PIGEON = 'PIXEON.png'
#MLPS
MLP = './Pictures/MLP/logan.png'
from time import sleep
FLEXIBILITY = 0.006
'''
#FILES raw text
with open(PICTURE1, 'rb') as f:
    content = f.read()
with open(MLP, 'rb') as f:
    MLP_content = f.read()


if content == MLP_content:
    print("The pictures are the same")
else:
    print("The pictures are different")
'''

class Picture:
  def __init__(self, filepath: str, MLP: str):
    self.filepath = filepath
    self.MLP = MLP
    
  def accuratize(self):
    score = 0
    with open(self.filepath, 'rb') as f1, open(self.MLP, 'rb') as f2:
      content1 = f1.read()
      content2 = f2.read()
      min_len = min(len(content1), len(content2))
      for i in range(min_len):
        if content1[i] == content2[i]:
          score += 1
      accuracy = score / min_len if min_len > 0 else 0
      return score, accuracy

  '''
  def accuratize(self, comparison_picture_path: str):
    accuracy = 0
    score = 0
    with open(self.filepath, 'rb') as f:
      content = str(f.read()).split('\\')
      
      plen = len(content)
    with open(self.MLP, 'rb') as f:
      MLP_content = str(f.read()).split('\\')
      MLPlen = len(MLP_content)
    for character in content:
      for char in MLP_content:
        if character == char:
          if character in MLP_content:
            score += 1
    accuracy = score/plen
    return score, accuracy
  '''
  def catagorize(self):
    #Use MLP to catagorize picture
    #e.g. if picture is a x mark, return "x mark"
    pass
print('Class processed')
if __name__ == '__main__':
  picture1 = Picture(PICTURE1, MLP)
  print('Pic 1 processing', end="", flush=True)
  for _ in range(3):
    sleep(0.1)
    print('.', end='', flush=True)
  sleep(1)
  print('\rPic 1 processed     ')
  picture2 = Picture(PICTURE2, MLP)
  print('Pic 2 processing',end='', flush=True)
  for _ in range(3):
    sleep(0.1)
    print('.', end='', flush=True)
  sleep(1)
  print('\rPic 2 processed     ')
  print('pic 1 accuratizing', end='', flush=True)
  for _ in range(3):
    sleep(0.1)
    print('.', end='', flush=True)
  
  _, acc = picture1.accuratize()
  print('\rpic 1 accuratized     ')
  _, acc2 = picture2.accuratize()
  print('pic 2 accuratized    ')
  #print((acc, acc2))
  more_accurate = 1 if acc > acc2 else 2
  ischeck = 1 if acc > FLEXIBILITY else 2 if acc2 > FLEXIBILITY else 'None' 
  if ischeck == 'None':
    print("None of the pictures are logan")
  else:
    print(f'Picture {ischeck} is logan ')
    #print(picture1.accuratize(MLP))
    