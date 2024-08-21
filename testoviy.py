# import openpyxl
# def export_to_excel(self, response):
#         from openpyxl.styles import Font, PatternFill

#         wb = openpyxl.Workbook()
#         ws = wb.active

#         headers = ["Talaba", "Topshirilgan sanasi", "Deadline", "Holati", "Urinishlar", "Ball"]
#         ws.append(headers)
#         column_widths = [30, 15, 15, 15, 10, 10]
#         for i, column_width in enumerate(column_widths):
#             column_letter = get_column_letter(i + 1)
#             ws.column_dimensions[column_letter].width = column_width

#         for cell in ws[1]:
#             cell.font = Font(bold=True)
#             cell.fill = PatternFill(start_color="0070C0", end_color="0070C0", fill_type="solid")

#         for index, item in enumerate(response):
#             row_data = [
#                 item["student_name"],
#                 item["submitted_at"].strftime("%Y-%m-%d %H:%M") if item["submitted_at"] else "Topshirilmagan",
#                 item["end_date"],
#                 "Topshirilgan" if item["submitted"] else "Topshirilmagan",
#                 item["attempts_count"],
#                 f"{item['ball']:.0f}/{item['max_ball']:.0f}" if item["ball"] else f"0/{item['max_ball']:.0f}",
#             ]
#             ws.append(row_data)

#         for cell in ws["A"]:
#             cell.font = Font(bold=True)

#         excel_file = BytesIO()
#         wb.save(excel_file)

#         response = HttpResponse(content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
#         response["Content-Disposition"] = "attachment; filename=assignments.xlsx"

#         response.write(excel_file.getvalue())
#         return response



# workbook = openpyxl.Workbook()
# sheet = workbook.active

# headers = ["Column1", "Column2", "Column3"]  
# for col, header in enumerate(headers, start=1):
#     sheet.cell(row=1, column=col).value = header
    
# data = ["1","2","3","4"]  
# for row, data_row in enumerate(data, start=2):
#     for col, value in enumerate(data_row, start=1):
#         sheet.cell(row=row, column=col).value = value
        
        
# workbook.save("output.xlsx")