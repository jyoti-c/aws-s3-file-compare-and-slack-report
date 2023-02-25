import difflib
import os
from html2image import Html2Image


def file_compare_and_generate_report(file1, file2, html_report_name) :
    """
    Compares two files, generates HTML report and saves the report to png file
    :param file1: String file 1
    :param file2: String file 2
    :param html_report_name: String report name to be generated
    :return: String absolute file path of png file
    """
    print("Generate HTML diff and save to results image file")
    hti = Html2Image()


    file1Content = open(file1).readlines()
    file2Content = open(file2).readlines()

    diff = difflib.HtmlDiff().make_file(file1Content,file2Content,"Original","Changed")
    with open(html_report_name+".html", 'w') as f:
        f.write(diff)
    hti.screenshot(
        html_file=html_report_name+".html",  save_as=html_report_name+".png"
    )
    return os.path.abspath(html_report_name+".png")