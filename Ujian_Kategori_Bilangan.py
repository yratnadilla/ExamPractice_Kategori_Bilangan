num = int(input('Ketik angka Anda : '))

jenisBilangan = ['bulat']

if num >= 0:
    jenisBilangan.append('cacah')
    if num != 0:
        jenisBilangan.append('asli')
        if num % 2 != 0:
            jenisBilangan.append('ganjil')
            for i in range(2, num):
                if num % i != 0:
                    i += 1
                    if i > num - 1:
                        jenisBilangan.append('prima')
                else:
                    jenisBilangan.append('komposit')
                    break
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

print(jenisBilangan)