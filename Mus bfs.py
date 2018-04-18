peta =  {'A':set(['B','F','D']),
         'B':set(['A','C','G']),
         'C':set(['B','D','H','I']),
         'D':set(['A','C','E','J']),
         'E':set(['D','F','K','L']),
         'F':set(['A','E','M']),
         'G':set(['B','H','O','N']),
         'H':set(['C','I','G','O']),
         'I':set(['C','J','H','P']),
         'J':set(['D','I','K','W']),
         'K':set(['E','L','J','Q']),
         'L':set(['E','K','R','M']),
         'M':set(['F','L','R','S']),
         'N':set(['G','O','T']),
         'O':set(['G','N','T','H','U','P']),
         'P':set(['O','I','V','Q']),
         'Q':set(['P','K','R','X']),
         'R':set(['M','S','Z','L','Y','Q']),
         'S':set(['M','R','Z']),
         'T':set(['N','O','U','e']),
         'U':set(['T','O','V','a']),
         'V':set(['U','P','a','W']),
         'W':set(['J','V','b','X']),
         'X':set(['W','Q','Y','d']),
         'Y':set(['d','X','R','Z']),
         'Z':set(['S','Y','R','g']),
         'a':set(['U','V','e','b']),
         'b':set(['W','a','d','h']),
         'd':set(['b','g','X','Y']),
         'e':set(['T','a','h']),
         'g':set(['h','d','Z']),
         'h':set(['e','b','g'])} 
    

def bfs(graf, mulai, tujuan):
    queue = [[mulai]]
    visited = set()
    print("Queue awal\t\t= ", queue, "\n\n")

    while queue:
        # masukkan antrian paling depan ke variabel jalur
        jalur = queue.pop(0)

        # simpan node yang dipilih ke variabel state, misal jalur = C,B maka simpan B ke variabel state
        state = jalur[-1]
        print("State sekarang\t= ", state)

        # cek state apakah sama dengan tujuan, jika ya maka return jalur
        if state == tujuan:
            return jalur
        # jika state tidak sama dengan tujuan, maka cek apakah state tidak ada di visited
        elif state not in visited:
            visited.add(state)
            # jika state tidak ada di visited maka cek cabang
            for cabang in graf.get(state, []): #cek semua cabang dari state
                jalur_baru = list(jalur) #masukkan isi dari variabel jalur ke variabel jalur_baru
                jalur_baru.append(cabang) #update/tambah isi jalur_baru dengan cabang
                queue.append(jalur_baru) #update/tambah queue dengan jalur_baru

            # tandai state yang sudah dikunjungi sebagai visited
            #visited.add(state)

        print("visited\t\t= ", visited)
        print("Queue\t\t= ", queue)
        print("\n")
        

        #cek isi antrian
        isi = len(queue)
        if isi == 0:
            print("Tidak ditemukan")


