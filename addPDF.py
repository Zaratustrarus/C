import PyPDF2

def merge_files(pdf_files):
    # Создаем объект объединения PDF
    pdf_merger = PyPDF2.PdfMerger()

    # Проходим по списку и добавляем каждый PDF в объединение
    for pdf_file in pdf_files:
        pdf_merger.append(pdf_file)

    # Файл для объединенного PDF
    output_pdf = "merged_file.pdf"
    pdf_merger.write(output_pdf)
    pdf_merger.close()

# Список PDF-файлов для объединения
pdf_files = ["Конкурс.pdf","asp.pdf"]

if __name__ == "__main__":
    merge_files(pdf_files)
    print("PDF-файлы успешно объединены.")
