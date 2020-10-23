from Helpers.ExcelGenerator import ExcelGenerator


mvfdata = [
    ["NNO", "Story", 1702, 1, 1],
    ["NNO", "Story", 1702, 2, 4],
    ["NNO", "Story", 1702, 2, 3],
    ["NNO", "Story", 1702, 1, 2],
    ["NNO", "Story", 1702, 1, 3],
    ["NNO", "Story", 1702, 1, 7],
    ["NNO", "Story", 1702, 1, 5],
    ["NNO", "Story", 1702, 2, 1],
    ["NNO", "Story", 1702, 2, 5],
    ["NNO", "Story", 1702, 2, 3],
    ["NNO", "Story", 1702, 3, 7],
    ["NNO", "Story", 1702, 2, 2],
    ["NNO", "Story", 1702, 2, 1],
    ["NNO", "Story", 1702, 1, 1],
    ["NNO", "Story", 1702, 1, 2],
    ["NNO", "Task", 1702, 1, 0.25],
    ["NNO", "Task", 1702, 1, 1.25],
    ["ESR", "", 1702, 1, 6],
    ["ESR", "", 1702, 1, 1],
    ["ESR", "", 1702, 2, 7]
]


#startdate = input("Please enter the MVF Start Date? ")
#estimatedenddate = input("Please enter the estimate MVF End Date? ")
#actualenddate = input("Please enter the actual MVF End Date? ")
#noofmembers = input("Please enter the number of people on the team? ")
#unplannedabsences = input("Please enter the number of unplanned absences? ")

#docGenerated = ExcelGenerator.generateExcel(mvfid, startdate, estimatedenddate, actualenddate, noofmembers, unplannedabsences, mvfdata)
docGenerated = ExcelGenerator.generateExcel("MVF-1702", "01-Jan-2020", "24-Jan-2020", "14-Feb-2020", 4, 0, mvfdata)
