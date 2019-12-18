{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "norm = np.random.normal(5,10,5000)\n",
    "\n",
    "normal_dag = np.random.normal(np.mean(norm),np.std(norm),5000)\n",
    "\n",
    "norm.sort()\n",
    "normal_dag.sort()\n",
    "\n",
    "plt.scatter(normal_dag,norm)\n",
    "plt.plot([np.max(normal_dag),np.min(normal_dag)],[np.max(norm),np.min(norm)],c = 'r')\n",
    "plt.show()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(array([  14.,   63.,  314.,  885., 1498., 1319.,  671.,  203.,   29.,\n",
       "           4.]), array([-32.01511473, -24.29022645, -16.56533817,  -8.84044989,\n",
       "         -1.11556161,   6.60932667,  14.33421495,  22.05910323,\n",
       "         29.78399151,  37.50887979,  45.23376807]), <a list of 10 Patch objects>)"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAX0AAAD4CAYAAAAAczaOAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4xLjEsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy8QZhcZAAAVPUlEQVR4nO3df6zd9X3f8eerptClXcsvQz0Ms7taTSFKFGYRtkxWFFowPwT5I9GwqsZgJmsa2dKmUzBDGlKiTGSZRoqWEKHgFSRkh9JEQYGUeG6iatIgGJo4AUJ8Sxi4eODMhGZDDaN974/v58Lh+vrXveeec3y+z4d0dM75fD/nns+993Nf9/v9nM/3801VIUnqh58bdwMkSaNj6EtSjxj6ktQjhr4k9YihL0k9csK4G3A4p59+eq1atWrczdAUe+yxx35cVctH/b72bS2lw/XriQ79VatWsWvXrnE3Q1Msyf8cx/vat7WUDtevHd6RpB4x9CWpRwx9SeoRQ1+SesTQl6QeMfQlqUcMfUnqEUNfknrE0JekHpnoM3J17FZteeCYX/PsLZcvQUukgy2kf4J9dJjc05ekHjH0JalHDH1J6hFDX5J6xNCXpB4x9CWpRwx9SeqRI4Z+kq1JXkry/YGyzyT5QZLdSb6S5OSBbTcmmUnydJJLBsrXt7KZJFuG/61Iko7kaPb0/whYP6dsB/COqnon8EPgRoAk5wJXA+e113w+ybIky4DPAZcC5wIbWl1J0ggdMfSr6s+BA3PKvlFVr7enDwMr2+OrgO1V9bOq+hEwA1zQbjNV9UxVvQZsb3Wlsdm0aRPAuwaPYmcl+bdJKsnp7XmS3NaOVHcnOX+g7sYke9pt4+i+A+nYDWNMfxPw9fb4LOD5gW17W9mhyg+SZHOSXUl27d+/fwjNk+Z3zTXXAOyZW57kbOC3gecGii8F1rTbZuD2VvdU4GbgPXQ7NzcnOWUp2y0txqJCP8lNwOvAPbNF81Srw5QfXFh1R1Wtraq1y5cvX0zzpMNat24ddP13rluBj/PWPnoVcHd1HgZOTrICuATYUVUHqupluqHPucOh0sRY8IJr7TD2CuCiqpr949gLnD1QbSXwQnt8qHJpYiS5Evirqvpu8pZ9laEcxdIdJXDOOecMsdXS0VvQnn6S9cANwJVV9erApvuBq5OclGQ13aHwt4FHgTVJVic5ke7D3vsX13RpuJK8DbgJ+PfzbZ6nzKNYHXeOZsrmNuB/AL+RZG+S64D/Avx9YEeS7yT5AkBVPQHcCzwJ/ClwfVX9bfvQ9yPAQ8BTwL2trjRJ/hGwGvhukmfpjkgfT/KrHPoo9nBHt9LEOeLwTlVtmKf4zsPU/xTwqXnKHwQePKbWSSNUVd8Dzph93oJ/bVX9OMn9wEeSbKf70PaVqtqX5CHgPwx8eHsxbQqzNIm8iIp6a8OGDQBvp5uRuRe4uaoOtUPzIHAZ3TTkV4FrAarqQJJP0g1hAnyiqg7M/yWk8TP01Vvbtm1j+/btu6tq7Xzbq2rVwOMCrj9Eva3A1iVppDRkrr0jST1i6EtSjxj6ktQjhr4k9YihL0k94uydCbVqywPjboI0MRb69/DsLZcPuSXHP/f0JalHDH1J6hFDX5J6xNCXpB4x9CWpRwx9SeoRQ1+SesTQl6QeMfQlqUcMfUnqEUNfknrE0JekHjH0JalHDH311qZNmwDeleT7s2VJPpPkB0l2J/lKkpMHtt2YZCbJ00kuGShf38pmkmwZ7XchHRtDX711zTXXAOyZU7wDeEdVvRP4IXAjQJJzgauB84D1wOeTLEuyDPgccClwLrCh1ZUmkqGv3lq3bh3A64NlVfWNqpotexhY2R5fBWyvqp9V1Y+AGeCCdpupqmeq6jVge6srTaQjhn6SrUlemnMIfGqSHUn2tPtTWnmS3NYOc3cnOX/gNRtb/T1JNi7NtyMN1Sbg6+3xWcDzA9v2trJDlR8kyeYku5Ls2r9//xI0Vzqyo9nT/yO6w9lBW4CdVbUG2NmeQ3eIu6bdNgO3Q/dPArgZeA/dntHNs/8opEmU5Ca6o4B7ZovmqVaHKT+4sOqOqlpbVWuXL18+nIZKx+iIoV9Vfw4cmFN8FXBXe3wX8IGB8rur8zBwcpIVwCXAjqo6UFUv042bzv1HIk2EdiR6BfA7VTUb4HuBsweqrQReOEy5NJEWOqZ/ZlXtA2j3Z7RyD4F1XEuyHrgBuLKqXh3YdD9wdZKTkqymO5r9NvAosCbJ6iQn0n3Ye/+o2y0drWFfGH0oh8DAHQBr166dt440DBs2bAB4O93HUXvphiBvBE4CdiQBeLiq/mVVPZHkXuBJumGf66vqb+le/BHgIWAZsLWqnhj5NyMdpYWG/otJVlTVvjZ881IrP9wh8PvmlH9rge8tDcW2bdvYvn377qpaO1B856HqV9WngE/NU/4g8OASNFEauoUO79wPzM7A2Qh8daD8w20Wz4XAK2345yHg4iSntA9wL25lkqQROuKefpJtdHvppw8cAt8C3JvkOuA54EOt+oPAZXRzmF8FrgWoqgNJPkk3/gnwiaqa++GwJGmJHTH0q2rDITZdNE/dAq4/xNfZCmw9ptZJkobKM3IlqUcMfUnqEUNfknrE0JekHjH0JalHDH1J6hFDX5J6xNCXpB4x9CWpR4a9yqaOQ6u2PLCg1z17y+VDbomkpeaeviT1iKEvST1i6EtSjxj6ktQjhr4k9Yihr97atGkTwLuSfH+2LMmpSXYk2dPuT2nlSXJbkpkku5OcP/Caja3+niQbD34naXIY+uqta665BmDPnOItwM6qWgPsbM8BLgXWtNtm4Hbo/knQXU3uPcAFwM2z/yikSWToq7fWrVsH8Pqc4quAu9rju4APDJTfXZ2HgZOTrAAuAXZU1YGqehnYAaxf8sZLC2ToS291ZlXtA2j3Z7Tys4DnB+rtbWWHKpcmkqEvHZ3MU1aHKT/4CySbk+xKsmv//v1DbZx0tAx96a1ebMM2tPuXWvle4OyBeiuBFw5TfpCquqOq1lbV2uXLlw+94dLRMPSlt7ofmJ2BsxH46kD5h9ssnguBV9rwz0PAxUlOaR/gXtzKpInkgmvqrQ0bNgC8nW5G5l66WTi3APcmuQ54DvhQq/4gcBkwA7wKXAtQVQeSfBJ4tNX7RFUdGNk3IR2jRYV+kt8H/gXdGOb36P4QVgDbgVOBx4HfrarXkpwE3A38Y+B/A/+8qp5dzPtLi7Ft2za2b9++u6rWztl00dy6VVXA9fN9naraCmxdgiZKQ7fg4Z0kZwH/BlhbVe8AlgFXA58Gbm3znF8GrmsvuQ54uap+Hbi11ZMkjdBix/RPAP5ekhOAtwH7gPcD97Xtc+c5z85/vg+4KMl8Mx8kSUtkwaFfVX8F/Ce6cc99wCvAY8BPqmr2hJfBOctvzGdu218BTpv7dZ3WJklLZzHDO6fQ7b2vBv4B8It0p6rPNTtn+ajmMzutTZKWzmKGd34L+FFV7a+q/wd8GfindKenz35APDhn+Y35zG37rwDOcpCkEVpM6D8HXJjkbW1s/iLgSeCbwAdbnbnznGfnP38Q+LM2I0KSNCKLGdN/hO4D2cfppmv+HHAHcAPwsSQzdGP2d7aX3Amc1so/xpurF0qSRmRR8/Sr6ma6E1oGPUO3xOzcun/Dmye6SJLGwGUYJKlHDH1J6hHX3pF0zFZteWDcTdACuacvST1i6EtSjxj6ktQjjukvMcc+JU0S9/QlqUcMfUnqEUNfknrE0JekHjH0pXkk+f0kTyT5fpJtSX4hyeokjyTZk+RLSU5sdU9qz2fa9lXjbb10aIa+NIfXf9Y0M/Sl+Xn9Z00lQ1+aw+s/a5oZ+tIcXv9Z08zQlw7m9Z81tQx96WBe/1lTy9CX5vD6z5pmLrgmzcPrP2tauacvST1i6EtSjxj6ktQjhr4k9ciiQj/JyUnuS/KDJE8l+SdJTk2yoy1KtaOd6EI6t7VFqXYnOX8434Ik6Wgtdk//D4E/raq3A+8CnqKbrrazLUq1kzenr10KrGm3zcDti3xvSdIxWnDoJ/llYB1trnJVvVZVP+Gti0/NXZTq7uo8THd244oFt1ySdMwWs6f/a8B+4L8m+YskX0zyi8CZVbUPoN2f0eq/sShVM7hg1RtclEqSls5iQv8E4Hzg9qp6N/B/OfyZiC5KJUljtpjQ3wvsbaesQ3fa+vnAi7PDNu3+pYH6Zw+8fnDBKknSCCw49KvqfwHPJ/mNVjS7KNXg4lNzF6X6cJvFcyHwyuwwkCRpNBa79s6/Bu5p1wp9BriW7h/JvUmuo1utcHZNkgeBy4AZ4NVWV5I0QosK/ar6DrB2nk0XzVO3gOsX836SdCxWbXlgQa979pbLh9ySyeEZuZLUI4a+JPWIoS9JPWLoS1KPGPqS1COGviT1iKEvzcNlwzWtDH1pfi4brqlk6EtzuGy4ppmhLx3MZcM1tQx96WAuG66pZehLB3PZcE0tQ1+aw2XDNc0Wu7SyNK1cNlxTydCX5uGy4ZpWDu9IUo8Y+pLUI4a+JPWIoS9JPWLoS1KPGPqS1COGviT1iPP0tWCrtjywoNc9e8vlQ26JpKO16D39JMvaSoRfa89XJ3mkXWjiS+2MRpKc1J7PtO2rFvvekqRjM4zhnY/SXWBi1qeBW9uFJl4Grmvl1wEvV9WvA7e2epKkEVpU6CdZCVwOfLE9D/B+ulUJ4eALTcxegOI+4KJWX5I0Iovd0/8s8HHg79rz04CfVNXr7fngxSTeuNBE2/5Kqy9JGpEFh36SK4CXquqxweJ5qtZRbBv8ul5dSJKWyGL29N8LXJnkWWA73bDOZ+muDzo7K2jwYhJvXGiibf8V4MDcL+rVhSRp6Sw49KvqxqpaWVWrgKuBP6uq3wG+CXywVZt7oYnZC1B8sNU/aE9fkrR0luLkrBuAjyWZoRuzv7OV3wmc1so/xuGvOSpJWgJDOTmrqr4FfKs9fga4YJ46f8ObVxqSJI2ByzBIUo8Y+tIheLa5ppGhLx2aZ5tr6hj60jw821zTytCX5ufZ5ppKhr40h2eba5oZ+tLBPNtcU8vQl+bwbHNNM0NfOnqeba7jnpdLPEoLvTSgjm+eba5p456+JPWIoS9JPWLoS1KPGPqS1COGviT1iKEvST3ilE2p55yO3C/u6UtSjxj6ktQjhr4k9YihL0k9YuhLUo8Y+pLUI4a+JPXIgkM/ydlJvpnkqSRPJPloKz81yY4ke9r9Ka08SW5LMpNkd5Lzh/VNSJKOzmL29F8H/qCqfhO4ELg+ybl0F5DYWVVrgJ28eUGJS4E17bYZuH0R7y1JWoAFh35V7auqx9vjnwJPAWcBVwF3tWp3AR9oj68C7q7Ow3TXG12x4JZLko7ZUMb0k6wC3g08ApxZVfug+8cAnNGqnQU8P/Cyva1s7tfanGRXkl379+8fRvMkSc2iQz/JLwF/AvxeVf314arOU3bQxaOr6o6qWltVa5cvX77Y5kmSBiwq9JP8PF3g31NVX27FL84O27T7l1r5XuDsgZevBF5YzPtLS8FJCppmi5m9E+BO4Kmq+s8Dm+4HNrbHG4GvDpR/uP2BXAi8MjsMJE0YJyloai1maeX3Ar8LfC/Jd1rZvwNuAe5Nch3wHPChtu1B4DJgBngVuHYR7y0tmbYzMvu51E+TDE5SeF+rdhfwLeAGBiYpAA8nOTnJCndqNIkWHPpV9d+Zf5we4KJ56hdw/ULfTxqHw01SSHKkSQpvCf0km+mOBDjnnHOWtN1anIVeY+DZWy4fckuGzzNypUNwkoKmkaEvzcNJCppWhr40h5MUNM28Rq50MCcpaGoZ+tIcTlLQNHN4R5J6xD19jdw0T4eTJp17+pLUI4a+JPWIoS9JPWLoS1KPGPqS1COGviT1iKEvST1i6EtSj/Tu5KyFnhgkSdPAPX1J6hFDX5J6pHfDO9K0cuhSR8M9fUnqEUNfknrE0JekHjH0JalH/CBXkoZkIR+mj/riQCMP/STrgT8ElgFfrKpbRt0GHZ8m+Ypb9msdL0Ya+kmWAZ8DfhvYCzya5P6qevJYv5bT0zQphtmvwb6tpTXqPf0LgJmqegYgyXbgKmBBfxzShLBfa8FGfQQ76tA/C3h+4Ple4D2DFZJsBja3p/8nydMjaNfpwI9H8D6LZTsXIJ+et3i2jf9wCG9xxH4NY+vbgybp9zJJbYHjsD2H6NezDtmvRx36maes3vKk6g7gjtE0p5NkV1WtHeV7LoTtHJ4ht/GI/RrG07cHTdLvZZLaAv1qz6inbO4Fzh54vhJ4YcRtkIbNfq3jxqhD/1FgTZLVSU4ErgbuH3EbpGGzX+u4MdLhnap6PclHgIfoprZtraonRtmGQxjbIfcxsp3DM7Q2TnC/nmuSfi+T1BboUXtSddDQoyRpSrkMgyT1iKEvST3S69BP8pkkP0iyO8lXkpw8sO3GJDNJnk5yyTjb2dqzvrVlJsmWcbcHIMnZSb6Z5KkkTyT5aCs/NcmOJHva/SkT0NZlSf4iydfa89VJHmlt/FL7AHbqTGIfH3dfnsR+O8r+2evQB3YA76iqdwI/BG4ESHIu3QyM84D1wOfbqfZjMXCa/6XAucCG1sZxex34g6r6TeBC4PrWri3AzqpaA+xsz8fto8BTA88/Ddza2vgycN1YWrX0JqqPT0hfnsR+O7L+2evQr6pvVNXr7enDdPOroTuFfntV/ayqfgTM0J1qPy5vnOZfVa8Bs6f5j1VV7auqx9vjn9J12rPo2nZXq3YX8IHxtLCTZCVwOfDF9jzA+4H7WpWxt3GpTGAfH3tfnrR+O+r+2evQn2MT8PX2eL7T6s8aeYveNGntOUiSVcC7gUeAM6tqH3R/YMAZ42sZAJ8FPg78XXt+GvCTgTCcuJ/nEpmEPj5RfXlC+u1I++fUr6ef5L8BvzrPppuq6qutzk10h3z3zL5snvrjnNs6ae15iyS/BPwJ8HtV9dfdjspkSHIF8FJVPZbkfbPF81SdmJ/nsTrO+vjE/Ownod+Oo39OfehX1W8dbnuSjcAVwEX15kkLk3Za/aS15w1Jfp7uD+eeqvpyK34xyYqq2pdkBfDS+FrIe4Erk1wG/ALwy3R7VicnOaHtTU3Mz3MhjrM+PhF9eYL67ej7Z1X19kb3AdaTwPI55ecB3wVOAlYDzwDLxtjOE1obVgMntradNwE/vwB3A5+dU/4ZYEt7vAX4j+Nua2vL+4Cvtcd/DFzdHn8B+Ffjbt8Sfc8T1ccnoS9Par8dVf8ce6cc543uw6vnge+02xcGtt0E/CXwNHDpBLT1MrrZF39Jd9g+CT+/f0Z32Ll74Gd4Gd2Y5E5gT7s/ddxtbe0d/KP6NeDbrQ/8MXDSuNu3RN/zxPXxcfflSe23o+qfLsMgST3i7B1J6hFDX5J6xNCXpB4x9CWpRwx9SeoRQ1+SesTQl6Qe+f8udtVvekppzgAAAABJRU5ErkJggg==\n",
      "text/plain": [
       "<Figure size 432x288 with 2 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.subplot(121)\n",
    "plt.hist(norm)\n",
    "plt.subplot(122)\n",
    "plt.hist(normal_dag)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.read_csv('GOOG.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Date</th>\n",
       "      <th>Open</th>\n",
       "      <th>High</th>\n",
       "      <th>Low</th>\n",
       "      <th>Close</th>\n",
       "      <th>Adj Close</th>\n",
       "      <th>Volume</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <td>0</td>\n",
       "      <td>2014-12-31</td>\n",
       "      <td>529.795471</td>\n",
       "      <td>531.141724</td>\n",
       "      <td>524.360352</td>\n",
       "      <td>524.958740</td>\n",
       "      <td>524.958740</td>\n",
       "      <td>1368200</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>1</td>\n",
       "      <td>2015-01-02</td>\n",
       "      <td>527.561584</td>\n",
       "      <td>529.815369</td>\n",
       "      <td>522.665039</td>\n",
       "      <td>523.373108</td>\n",
       "      <td>523.373108</td>\n",
       "      <td>1447500</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2</td>\n",
       "      <td>2015-01-05</td>\n",
       "      <td>521.827332</td>\n",
       "      <td>522.894409</td>\n",
       "      <td>511.655243</td>\n",
       "      <td>512.463013</td>\n",
       "      <td>512.463013</td>\n",
       "      <td>2059800</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>3</td>\n",
       "      <td>2015-01-06</td>\n",
       "      <td>513.589966</td>\n",
       "      <td>514.761719</td>\n",
       "      <td>499.678131</td>\n",
       "      <td>500.585632</td>\n",
       "      <td>500.585632</td>\n",
       "      <td>2899900</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>4</td>\n",
       "      <td>2015-01-07</td>\n",
       "      <td>505.611847</td>\n",
       "      <td>505.855164</td>\n",
       "      <td>498.281952</td>\n",
       "      <td>499.727997</td>\n",
       "      <td>499.727997</td>\n",
       "      <td>2065000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "         Date        Open        High         Low       Close   Adj Close  \\\n",
       "0  2014-12-31  529.795471  531.141724  524.360352  524.958740  524.958740   \n",
       "1  2015-01-02  527.561584  529.815369  522.665039  523.373108  523.373108   \n",
       "2  2015-01-05  521.827332  522.894409  511.655243  512.463013  512.463013   \n",
       "3  2015-01-06  513.589966  514.761719  499.678131  500.585632  500.585632   \n",
       "4  2015-01-07  505.611847  505.855164  498.281952  499.727997  499.727997   \n",
       "\n",
       "    Volume  \n",
       "0  1368200  \n",
       "1  1447500  \n",
       "2  2059800  \n",
       "3  2899900  \n",
       "4  2065000  "
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.hist(df.Close, bins = 100)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
