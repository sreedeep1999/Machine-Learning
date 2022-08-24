import numpy as np
def create_matrix(mc):
    print("\n ARRAY "+str(mc)+"elements:")
    array_1=map(int,input().split())
    array_1=np.array(list(array_1))
    print("\n array "+str(mc)+",ROWCOLUMN:")
    row,column=map(int,input().split())
    if(len(array_1)!=(row*column)):
        print("\n row and column size not match with total elements!! retry")
        return create_matrix(mc)
    array_1=array_1.reshape(row,column)
    print("\n ARRAY"+str(mc))
    print(array_1)
    print("\n transpose:")
    return (array_1)
print(create_matrix(1).transpose())
