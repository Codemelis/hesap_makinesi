
import tkinter as tk  # 1. Pencere ve butonlar yapmak için gereken araç kutusunu çağırıyoruz.

# ---- RENK PALETİ ----
ZEMIN = "#F9F1F2"  # Pencerenin arka planı 
EKRAN = "#FFFFFF"  # Üstteki sayıların yazdığı beyaz ekran
RAKAM = "#FFFFFF"  # Rakam tuşlarının rengi 
ISLEM = "#E8A3B5"  # + - * / işlem tuşları 
TEMIZLE = "#D96B89"  # C (Temizleme) tuşu
ESIT = "#9E3C56"  # = (Eşittir) tuşu 
YAZI_KOYU = "#4A2E35"  # Rakamların üzerindeki yazı rengi 
YAZI_BEYAZ = "white"  # Renkli tuşların üzerindeki yazı rengi 


# ---- FONKSİYONLAR (Tuşların Arkasında Çalışan Motor) ----
def tikla(deger):  # 10. Bir rakam veya işarete tıklandığında çalışır.
  ekran.insert(tk.END, deger)  # Basılan karakteri ekranın en sonuna ekler.


def temizle():  # 11. "C" tuşuna basıldığında ekranı sıfırlar.
  ekran.delete(0, tk.END)  # Ekrandaki bütün yazıları siler.


def hesapla():  # 12. "=" tuşuna basıldığında matematiksel işlemi çözer.
  try:
    sonuc = eval(ekran.get())  # Ekrandaki metni (örneğin "5+5") matematik gibi çözer.
    temizle()  # Ekranı temizler.
    ekran.insert(0, sonuc)  # Çıkan sonucu ekrana yazar.
  except:
    temizle()
    ekran.insert(
        0, "Hata"
    )  # Yanlış bir işlem yapılırsa ekrana "Hata" yazdırır.


# ---- PENCERE AYARLARI ----
pencere = tk.Tk()  # Boş, yepyeni bir masaüstü penceresi açar.
pencere.title("Aesthetic Pembe Hesap Makinesi")  # Pencerenin başlığı
pencere.configure(
    bg=ZEMIN, padx=15, pady=15
)  # Arka plan rengi ve kenar boşlukları
pencere.resizable(False, False)  # Pencerenin boyutu fareyle değiştirilemesin

# ---- EKRAN (Yazı Kutusu) ----
ekran = tk.Entry(
    pencere,
    font=("Arial", 24, "bold"),
    justify="right",
    bg=EKRAN,
    fg=YAZI_KOYU,
    bd=0,
    insertbackground=YAZI_KOYU,
)
ekran.grid(
    row=0, column=0, columnspan=4, padx=5, pady=(0, 15), ipady=12
)  # En üste yerleştirir.


# ---- RAKAM TUŞLARI ----
# Her bir tuşa basıldığında 'tikla' fonksiyonu çalışır ve üzerindeki sayıyı ekrana yazar.
tk.Button(
    pencere,
    text="7",
    width=5,
    height=2,
    bg=RAKAM,
    fg=YAZI_KOYU,
    bd=0,
    font=("Arial", 14, "bold"),
    command=lambda: tikla("7"),
).grid(row=1, column=0, padx=4, pady=4)
tk.Button(
    pencere,
    text="8",
    width=5,
    height=2,
    bg=RAKAM,
    fg=YAZI_KOYU,
    bd=0,
    font=("Arial", 14, "bold"),
    command=lambda: tikla("8"),
).grid(row=1, column=1, padx=4, pady=4)
tk.Button(
    pencere,
    text="9",
    width=5,
    height=2,
    bg=RAKAM,
    fg=YAZI_KOYU,
    bd=0,
    font=("Arial", 14, "bold"),
    command=lambda: tikla("9"),
).grid(row=1, column=2, padx=4, pady=4)

tk.Button(
    pencere,
    text="4",
    width=5,
    height=2,
    bg=RAKAM,
    fg=YAZI_KOYU,
    bd=0,
    font=("Arial", 14, "bold"),
    command=lambda: tikla("4"),
).grid(row=2, column=0, padx=4, pady=4)
tk.Button(
    pencere,
    text="5",
    width=5,
    height=2,
    bg=RAKAM,
    fg=YAZI_KOYU,
    bd=0,
    font=("Arial", 14, "bold"),
    command=lambda: tikla("5"),
).grid(row=2, column=1, padx=4, pady=4)
tk.Button(
    pencere,
    text="6",
    width=5,
    height=2,
    bg=RAKAM,
    fg=YAZI_KOYU,
    bd=0,
    font=("Arial", 14, "bold"),
    command=lambda: tikla("6"),
).grid(row=2, column=2, padx=4, pady=4)

tk.Button(
    pencere,
    text="1",
    width=5,
    height=2,
    bg=RAKAM,
    fg=YAZI_KOYU,
    bd=0,
    font=("Arial", 14, "bold"),
    command=lambda: tikla("1"),
).grid(row=3, column=0, padx=4, pady=4)
tk.Button(
    pencere,
    text="2",
    width=5,
    height=2,
    bg=RAKAM,
    fg=YAZI_KOYU,
    bd=0,
    font=("Arial", 14, "bold"),
    command=lambda: tikla("2"),
).grid(row=3, column=1, padx=4, pady=4)
tk.Button(
    pencere,
    text="3",
    width=5,
    height=2,
    bg=RAKAM,
    fg=YAZI_KOYU,
    bd=0,
    font=("Arial", 14, "bold"),
    command=lambda: tikla("3"),
).grid(row=3, column=2, padx=4, pady=4)

tk.Button(
    pencere,
    text="0",
    width=5,
    height=2,
    bg=RAKAM,
    fg=YAZI_KOYU,
    bd=0,
    font=("Arial", 14, "bold"),
    command=lambda: tikla("0"),
).grid(row=4, column=0, padx=4, pady=4)
tk.Button(
    pencere,
    text=".",
    width=5,
    height=2,
    bg=RAKAM,
    fg=YAZI_KOYU,
    bd=0,
    font=("Arial", 14, "bold"),
    command=lambda: tikla("."),
).grid(row=4, column=1, padx=4, pady=4)

# ---- İŞLEM TUŞLARI (+, -, *, /) ----
tk.Button(
    pencere,
    text="+",
    width=5,
    height=2,
    bg=ISLEM,
    fg=YAZI_BEYAZ,
    bd=0,
    font=("Arial", 14, "bold"),
    command=lambda: tikla("+"),
).grid(row=1, column=3, padx=4, pady=4)
tk.Button(
    pencere,
    text="-",
    width=5,
    height=2,
    bg=ISLEM,
    fg=YAZI_BEYAZ,
    bd=0,
    font=("Arial", 14, "bold"),
    command=lambda: tikla("-"),
).grid(row=2, column=3, padx=4, pady=4)
tk.Button(
    pencere,
    text="*",
    width=5,
    height=2,
    bg=ISLEM,
    fg=YAZI_BEYAZ,
    bd=0,
    font=("Arial", 14, "bold"),
    command=lambda: tikla("*"),
).grid(row=3, column=3, padx=4, pady=4)
tk.Button(
    pencere,
    text="/",
    width=5,
    height=2,
    bg=ISLEM,
    fg=YAZI_BEYAZ,
    bd=0,
    font=("Arial", 14, "bold"),
    command=lambda: tikla("/"),
).grid(row=4, column=3, padx=4, pady=4)

# ---- ÖZEL TUŞLAR (C ve =) ----
tk.Button(
    pencere,
    text="C",
    width=5,
    height=2,
    bg=TEMIZLE,
    fg=YAZI_BEYAZ,
    bd=0,
    font=("Arial", 14, "bold"),
    command=temizle,
).grid(row=4, column=2, padx=4, pady=4)
tk.Button(
    pencere,
    text="=",
    width=24,
    height=2,
    bg=ESIT,
    fg=YAZI_BEYAZ,
    bd=0,
    font=("Arial", 14, "bold"),
    command=hesapla,
).grid(
    row=5, column=0, columnspan=4, padx=4, pady=4
)  # Tüm alt satırı kaplar

# ---- PROGRAMI ÇALIŞIR TUTAN DÖNGÜ ----
pencere.mainloop()  # Pencerenin açık kalmasını ve tıklamaları dinlemesini sağlar.