from os import replace
from PreStage.ROI.make_roi import selectROI
path = 'E:/Segmentation'
selROI = selectROI(direc = path, replaceImg = False, scale = 0.25) 
#replace img with ROI if relapceImg = True else create folder RoiImage and save image with ROI
selROI.createROI() #create new ROI img
selROI.applyROI() 