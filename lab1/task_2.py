# MegaBytes
disket_space_mb = 1.44
pages = 100
strings = 50
syms_in_string = 25
# Bytes
one_sym = 4
# Bytes in Megabyte
bytes_in_mb = 1024 * 1024

one_book = pages * strings * syms_in_string * one_sym
disket_space_b = disket_space_mb * bytes_in_mb

books_number = round(disket_space_b / one_book)
print("Поместится", books_number, "книг(и)")
