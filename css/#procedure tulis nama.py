#procedure tulis nama
def tulis_nama():
    print('nama saya fathur')
    print('saya tinggal di bandung')

#procedure tulis nama berulang
def tulis_nama_berulang(N):
for i in range(1,N+1):
    print(f'{i} nama saya fathur')

    #program utama
tulis_nama()
tulis_nama_berulang(3)