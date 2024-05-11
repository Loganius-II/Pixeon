from pixeon import Picture

picture1 = 'your/file/path.png'
picture2 =  'other file path/png'
comparison_pic = 'file/to/mlp.jpg'
comparison_pic2 = 'other/mlp.png'
comparison_bulk = ['list/of/files.png','other/picture.png']
if __name__ == '__main__':
  #initialize picture and MLP (what ever you want to compare all of your pictures with)
  pic = Picture(picture1, comparison_pic)
  #get the (amount of times things matched, accuracy)
  print(pic.accuratize())
  #change the filepath
  pic.config(filepath=picture2)
  print(pic.accuratize())
  #you can change the comparison pic too
  pic.config(MLP=comparison_pic2)
  #Now for comparing one picture to entire directories or just multiple pictures 
  pic.config(MLP=comparison_bulk)
  #notice that i am using the catagorize function
  #NOTE: the accuracy on bulks may be higher if you are comparing
  #an image that is already in the list (You probably could've guessed that anyway)
  pic.catagorize()