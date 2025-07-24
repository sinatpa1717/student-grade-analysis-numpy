import numpy as np

x = np.array([18, 12, 15, 10, 20, 17, 8, 14, 19, 11, 16, 7, 13, 9, 20])


print("بیشترین نمره : " , x.max())
print("کمترین نمره : " , x.min())


a = np.sort(x)
print("مرتب شده : " , a)


gam = np.sum(x)
print("gham kole nomarat : " , gam)


mean = np.mean(x)
print("میانگین نمرات کل کلاس : " , mean)


shart = np.where(x >= 18 , "عالی",
        np.where(x >= 15 , "خوب",
        np.where(x >= 10,"قابل قبول ",
        np.where(x <10 , "نیاز به تلاش","مردود"))))

print(shart)


tedad_20 = np.sum(x == 20)
print("تعداد دانش‌آموزانی که نمره کامل گرفتن: ", tedad_20)


tedad_20 = np.sum(x < 10)
print("مردودی ها : ", tedad_20)
