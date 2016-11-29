import numpy as np
import sys
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import PCA
from sklearn.decomposition import TruncatedSVD
from sklearn.cluster import KMeans, MiniBatchKMeans
from sklearn.feature_extraction import text 
from sklearn.preprocessing import Normalizer

path 	= sys.argv[1]
output	= sys.argv[2]

f = open(str(path)+'title_StackOverflow.txt','r')
data = []
for line in f:
	data.append(line.strip())
f.close()


mystop = {'using','file','way','use','application','add','best','code','command','content','create','custom','data','database',
'does','error','files','form','function','list','make','object','page','possible','problem','set','work','table','text','version','vs'}
stop = mystop.union(text.ENGLISH_STOP_WORDS)

TFIDFvectorizer = TfidfVectorizer(stop_words = stop, min_df = 0.0006) #, min_df = 0.01
x = TFIDFvectorizer.fit_transform(data)
print '-----feature size-----'
print TFIDFvectorizer.get_feature_names()
print len(TFIDFvectorizer.get_feature_names())

print '-----feature mapping-----'

print '-----start SVD-----'
svd = TruncatedSVD(n_components=20, n_iter = 30, random_state = 50)
normalizer = Normalizer(copy = False)
U = svd.fit_transform(x)			#fit: create V in SVD #transform: create U*S in SVD, which is need
U = normalizer.fit_transform(U)
print svd.explained_variance_


print '-----start kmeans-----'
minikmeans = MiniBatchKMeans(n_clusters = 22, init = 'k-means++', n_init = 1,init_size = 500)
minikmeans.fit(U)
#print minikmeans.cluster_centers_
print minikmeans.inertia_

label = minikmeans.labels_
'''
print '-----save labels-----'
fout = open('checklabel','w')
for i in label:
	fout.write(' '+str(i)+' \n')
fout.close()
'''
print '-----loading check_index.csv-----'
f = open(str(path)+'check_index.csv','r')
index = []
for line in f:
	index.append(line.strip().split(','))
f.close()

print '-----start write-----'
fout = open(output,'w')
fout.write('ID,Ans\n')
for i in range(5000000):
	fout.write(str(i)+',')
	if label[int(index[i+1][1])] == label[int(index[i+1][2])]:
		fout.write(str(1)+'\n')
	else:
		fout.write(str(0)+'\n')




