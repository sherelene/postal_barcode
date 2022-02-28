from PrintBarcode import *


# function to remove hyphen from zip code
def remove_hyphen(zip_code):
    zip_code = zip_code.split('-')
    zip_code = ''.join(zip_code)

    return zip_code


# function to create the checksum of zip code
def checksum(zip_code):
    # Loop through zip_code and stores as a list
    zip_list = [int(num) for num in str(zip_code)]
    # Calculates the checksum
    check_digit = 10 - sum(zip_list) % 10
    # Append checksum at last of the zip_code
    zip_code = zip_code + str(check_digit)

    return zip_code


# The main function that calls all functions and generates bar code number
def main():
    # Take user input
    zip_code = input("Enter zip code (in zip + 4 format) : ")

    # call function to remove - from code
    zip_code = remove_hyphen(zip_code)

    # call function to add checksum as last digit
    zip_code = checksum(zip_code)

    # calls function to start drawing the barcode
    zip_encoding(zip_code)
