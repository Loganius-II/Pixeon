#MLP means Machine Learning Pictures
#PIXEON: Picture Exploration & Neural Training Module
#Author: Logan McDermott
#Date: 5/3/2024
from Pictures.MLP.MLPPATH import MLPS
#PICTURES
PICTURE1 = './Pictures/Input/landscape.png'
PICTURE2 = ''
#MLPS
MLP = MLPS

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
  def __init__(self, filepath: str, MLP: list):
    self.filepath = filepath
    self.MLP = MLP
  def accuratize(self):
    accuracy = 0
    score = 0
    directory_list = []
    MLP_content = []
    MLP_charCount = 0
    with open(self.filepath, 'rb') as f:
      content = str(f.read()).split('\\')
      
      plen = len(content)
    for picture in self.MLP:
      directory_list.append(f'./Pictures/MLP/{picture}')
    for picture in directory_list:
      try:
        with open(picture, 'rb') as f:
          MLP_content.append(str(f.read()).split('\\'))

      except Exception:
        pass
    score_list = []
    MLP_content_unnested = [ x for x in MLP_content if isinstance(x, list) is not True] + \
    [ e for each in MLP_content for e in each if isinstance(each, list) is True]
    length = len(''.join(MLP_content_unnested))
    for picture in MLP_content:
      for character in picture:
        if character in content:
          score += 1
      score_list.append(score)
      score = 0
    score_avg = sum(score_list)/len(score_list)
    accuracy = score_avg/ length
    return score_avg, accuracy
  def catagorize(self):
    #Use MLP to catagorize picture
    #e.g. if picture is a x mark, return "x mark"
    pass
if __name__ == '__main__':
  picture1 = Picture(PICTURE1, MLP)
  with open('results.txt', 'a') as f:
    results = picture1.accuratize()
    f.write(f'src: {PICTURE1}, {str(results)}')
  print(results)
 