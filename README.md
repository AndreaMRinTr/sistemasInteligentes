# sistemasInteligentes

Breast cancer prediction

The purpose of this program is to analize different breast tumor characteristics to classify the tumor as bening or malignant. 
the characteristics we are taking as features are.


   1. Clump Thickness               1 - 10
   2. Uniformity of Cell Size       1 - 10
   3. Uniformity of Cell Shape      1 - 10
   4. Marginal Adhesion             1 - 10
   5. Single Epithelial Cell Size   1 - 10
   6. Bare Nuclei                   1 - 10
   7. Bland Chromatin               1 - 10
   8. Normal Nucleoli               1 - 10
   9. Mitoses                       1 - 10
  10. Class:                        (2 for benign, 4 for malignant)



Algorithm: decision trees
This is a classification algotithm. 

Title: Wisconsin Breast Cancer Database (January 8, 1991) This breast cancer databases was obtained from the University of Wisconsin Hospitals, Madison from Dr. William H. Wolberg. 

TO RUN IT 

You can make a copy of the repository using the command git clone then you can move to the folder 
you can run it with the command python tree_cancer.py (it depends on the version)
In the framework you will be asked to introduce 9 different numbers, one for each characteristic to consider in the calculation.
The calculation is going to be the number of the class + --> + if the sample results malignant or benign.
