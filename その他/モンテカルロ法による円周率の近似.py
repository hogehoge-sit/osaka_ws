
# coding: utf-8

# # $$モンテカルロ法の実装$$<br>
# 乱数を用いて円周率πの近似値を出してみる<br>
# 正方形に内接する円の中にある乱数によって生成した点と正方形内の点の比から、円周率πを求める。<br>

# # 式は以下の通りになる。
# $$πR^2:4R^2 = n:m$$
# $$π = 4+n/m$$
# $$但しn,mは正方形内に内接する円と正方形内に含まれる点の個数とする。$$
# $$今回は1/4の円で考えてみた（負の数の乱数が出せなかったため）$$

# In[2]:


#coding: utf-8
import numpy as np

#get_ipython().run_line_magic('matplotlib', 'inline')


# In[6]:


def randomplot(n):
    x_list = np.array(np.random.random(n))
    y_list = np.array(np.random.random(n))
    r_list = (x_list**2 + y_list**2) ** 0.5
    cir_point = 0
    for i in range(n):
        if r_list[i] <= 1:
            cir_point += 1
    square_point = n
    pi = 4*cir_point / square_point
    print("円内の点の数: ", cir_point)
    print("円外の点の数: ", square_point)
    print("近似した円周率(点が{}個の時): ".format(n), pi)
    
if __name__ == "__main__":
    n = int(input("プロットする点の数: "))
    randomplot(n)


# $$結論$$
# $$10^8くらいのオーダーだと1分ほどかかる。まず間違いなくfor文で回してるからだと思う。$$
