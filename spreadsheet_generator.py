import os
import openpyxl

input_dir = "/media/matthew/Matt's Backup HDD/Beating_Roulette_Data/Dataset_master/single_spins/"

filename = "spins.xlsx"

wb = openpyxl.Workbook()
sheet = wb.active

row = 2
column = 1

for file in os.listdir(input_dir):
    if file.endswith(".MP4"):
        sheet.cell(row, column).value = file
        row += 1

savepath = "/media/matthew/Matt's Backup HDD/Beating_Roulette_Data/" + filename
# print(savepath)
wb.save(savepath)