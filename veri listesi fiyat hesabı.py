fiyatlar=[283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300,218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237,197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216,270, 271, 272, 273, 274, 275, 276, 277, 278, 279,281, 282, 283, 284, 285, 286, 287, 288, 289,290,197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207,230, 231, 232, 233, 234, 235, 236, 237,197, 198, 199]
print(len(fiyatlar))
for i in range(len(fiyatlar)-1):
  for j in range(len(fiyatlar)-i-1):
    if fiyatlar[j]>fiyatlar[j+1]:
      fiyatlar[j],fiyatlar[j+1]=fiyatlar[j+1],fiyatlar[j]
fiyatlar[0]=(fiyatlar[0]-fiyatlar[0]*0.08)
fiyatlar[99]=(fiyatlar[99]+fiyatlar[99]*0.06)
print(fiyatlar)
