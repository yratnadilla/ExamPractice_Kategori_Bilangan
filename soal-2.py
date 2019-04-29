num = input('Ketik angka Anda : ')

jenisBilangan = ['bulat']

if num.isdigit():
    num = int(num)
    if num >= 0:
        jenisBilangan.append('cacah')
        if num != 0:
            jenisBilangan.append('asli')
            if num % 2 != 0:
                jenisBilangan.append('ganjil')
                for i in range (2, num + 1):
                    if num % i == 0:
                        if i != num:
                            jenisBilangan.append('komposit')
                            break
                        else:
                            jenisBilangan.append('prima')
            else:
                jenisBilangan.append('genap')
                if num == 2:
                    jenisBilangan.append('prima')
                else:
                    jenisBilangan.append('komposit')
        else:
            jenisBilangan.append('nol')
    else:
        jenisBilangan.append('negatif')
else:
    print('Harap masukkan bilangan bulat.')

print(jenisBilangan)